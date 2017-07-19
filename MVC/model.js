class BeatModel {
    constructor(){
        this.beatObservers = [];
        this.bpmObservers = [];
        this.bpm = 90;
        this.sequencer = new Sequencer();
    }

    setUp(){
        console.log('setup..')
    }

    buildTrackAndStart(){
        console.log('Build track and start..')
    }

    initialize() {
        this.setUp();
        this.buildTrackAndStart();
    }

    on() {
        this.setBPM(90);
        this.sequencer.start();
    }

    off(){
        this.setBPM(0);
        this.sequencer.stop();
    }

    setBPM(bpm){
        this.bpm = bpm;
        this.sequencer.setTempoInBPM(this.getBPM());
        this.notifyBPMObservers();
    }

    getBPM(){
        return this.bpm;
    }

    beatEvent(){
        this.notifyBeatObservers()
    }

    registerObserverBeat(obj){
        this.beatObservers.push(obj);
    }

    notifyBeatObservers(){
        for(let i = 0; i< this.beatObservers.length; i++) {
            this.beatObservers[i].updateBeat();
        }
    }

    registerObserverBPM(obj){
        this.bpmObservers.push(obj);
    }

    notifyBPMObservers(){
        for(let i=0; i< this.bpmObservers.length; i++) {
            this.bpmObservers[i].updateBPM();
        }
    }

    removeObserverBeat(obj){
        let i = this.beatObservers.indexOf(obj);
        if(i>=0){
            this.beatObservers.splice(i, 1);
        }
    }

    removeObserverBPM(obj) {
        let i = this.bpmObservers.indexOf(obj);
        if(i>=0) {
            this.bpmObservers.splice(i, 1);
        }
    }
}


class Sequencer {
    constructor(){
        this.bpm=null;
        this._timerId = null
    }

    start(){
        this.__core();
    }

    stop(){
        clearInterval(this._timerId);
        this._timerId=null;
    }

    __core(){
        this._timerId = setInterval(()=>{
            console.log(`Boom.. ${this.bpm}`)
        }, this.bpm*100);
    }

    setTempoInBPM(temp){
        this.bpm=temp;
        if(this._timerId !== null) {
            this.stop();
            this.start();
        }
    }
}


export default BeatModel