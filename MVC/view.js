class View {
    constructor(controller, model){
        this.controller = controller;
        this.model = model;
        model.registerObserverBPM(this);
        model.registerObserverBeat(this);
    }

    createView(){
        //TODO
        this.beatBar = {
            setValue: (value)=>{
                console.log(`Beat bar setted value: ${value}`);
            }
        };
        this.inputBpm = {
            value: '100'
        }
        this.bpmOutputLabel = {
            setText: (text)=>{
                console.log(`BpmOutput Label setted text: ${text}`);
            }
        };
    }

    createControls(){
        //TODO
        this.stopMenuItem = {
            setEnabled: (bool)=>{
                console.log(`stopMenuItem: ${bool}`);
            }
        };
        this.startMenuItem = {
            setEnabled: (bool)=>{
                console.log(`startMenuItem: ${bool}`);
            }
        };
        this.btnSubmit = {
            id: 3
        }; //enter
        this.btnIncrease = {
            id: 1
        }; //++
        this.btnDecrease = {
            id: 2
        };//--
    }

    enableStopMenuItem(){
        this.stopMenuItem.setEnabled(true);
    }

    disabledStopMenuItem(){
        this.stopMenuItem.setEnabled(false);
    }

    enableStartMenuItem(){
        this.startMenuItem.setEnabled(true);
    }

    disabledStartMenuItem(){
        this.startMenuItem.setEnabled(false);
    }

    actionPerformed(event){
        //3 btn

        if(event.target.id === this.btnSubmit.id){
            let bpm = +this.inputBpm.value;
            this.controller.setBPM(bpm);
        } else if(event.target.id === this.btnIncrease.id) {
            this.controller.increaseBPM();
        } else if(event.target.id === this.btnDecrease.id){
            this.controller.decreaseBPM();
        }
    }

    updateBPM(){
        let bpm = this.model.getBPM();
        if(bpm === 0) {
            this.bpmOutputLabel.setText('offLine');
        } else {
            this.bpmOutputLabel.setText(`Current BPM: ${this.model.getBPM()}`);
        }
    }

    updateBeat() {
        this.beatBar.setValue(100);
    }
}

export default View