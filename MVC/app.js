import BeatModel from './model';
import BeatControler from './controler';


function main(){
    var model = new BeatModel();
    var ctrl = new BeatControler(model);
    ctrl.start();
}


main();