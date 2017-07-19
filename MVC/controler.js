import View from './view';

class BeatControler {
    constructor(model){
        this.model = model;
        this.view = new View(this, this.model);
        this.view.createView();
        this.view.createControls();
        this.view.disabledStopMenuItem();
        this.view.enableStartMenuItem();
        this.model.initialize();
    }

    start(){
        this.model.on();
        this.view.disabledStartMenuItem();
        this.view.enableStopMenuItem();
    }

    stop(){
        this.model.off();
        this.view.enableStartMenuItem();
        this.view.disabledStopMenuItem();
    }

    increaseBPM(){
        let bpm = this.model.getBPM();
        this.model.setBPM(bpm+1);
    }

    decreaseBPM(){
        let bpm = this.model.getBPM();
        this.model.setBPM(bpm-1);
    }

    setBPM(bpm) {
        model.setBPM(bpm);
    }
}


export default BeatControler;