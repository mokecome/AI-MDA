document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('riveCanvas');
    let currentAnimation = 'idle';

    const idleRiveInstance = new rive.Rive({
        src: 'static/Idle_nurse.riv',
        canvas: canvas,
        autoplay: true,
        stateMachines: ['State Machine_Idle'],
        onLoad: () => {
            console.log('Idle animation loaded');
            idleRiveInstance.resizeDrawingSurfaceToCanvas();
        }
    });
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }

    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();
    const actionARiveInstance = new rive.Rive({
        src: 'static/actionA_nurse.riv',
        canvas: canvas,
        autoplay: false,
        stateMachines: ['State Machine_Action_A'],
        onLoad: () => {
            console.log('Action A animation loaded');
            actionARiveInstance.resizeDrawingSurfaceToCanvas();
        }
    });

    const actionBRiveInstance = new rive.Rive({
        src: 'static/actionB_nurse.riv',
        canvas: canvas,
        autoplay: false,
        stateMachines: ['State Machine_Action_B'],
        onLoad: () => {
            console.log('Action B animation loaded');
            actionBRiveInstance.resizeDrawingSurfaceToCanvas();
        }
    });


    document.getElementById('switchButton').addEventListener('click', () => {
        if (currentAnimation === 'idle') {
            console.log('Switching to action A animation');
            idleRiveInstance.pause('State Machine_Idle');
            actionARiveInstance.play('State Machine_Action_A');
            actionBRiveInstance.pause('State Machine_Action_B');
            currentAnimation = 'actionA';

            return;
        } 
        
        if (currentAnimation === 'actionA') {
            console.log('Switching to action B animation');
            idleRiveInstance.pause('State Machine_Idle');
            actionARiveInstance.pause('State Machine_Action_A');
            actionBRiveInstance.play('State Machine_Action_B');
            currentAnimation = 'actionB';

            return;
        }

        if (currentAnimation === 'actionB') {
            console.log('Switching to idle animation');
            idleRiveInstance.play('State Machine_Idle');
            actionARiveInstance.pause('State Machine_Action_A');
            actionBRiveInstance.pause('State Machine_Action_B');
            currentAnimation = 'idle';

            return;
        }
    });

});
