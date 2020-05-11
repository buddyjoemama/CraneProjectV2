from Controls import NorthChip, SouthChip, ExtraChip
import SerialController
import signal
from xbox360controller import Xbox360Controller

sController = SerialController.SerialController('/dev/ttyACM0')

def on_button_pressed(button):
    if (button.name == 'button_a'):
        sController.cameraDown()
    elif (button.name == 'button_y'):
        sController.cameraUp()
    elif (button.name == 'button_b'):
        sController.cameraCW()
    elif (button.name == 'button_x'):
        sController.cameraCCW()

def on_button_released(button):
    sController.cameraOff()
    
try:
    with Xbox360Controller(0, axis_threshold=0.2) as controller:
        # Button A events
        controller.button_a.when_pressed = on_button_pressed
        controller.button_y.when_pressed = on_button_pressed
        controller.button_x.when_pressed = on_button_pressed
        controller.button_b.when_pressed = on_button_pressed
        
        controller.button_a.when_released = on_button_released
        controller.button_y.when_released = on_button_released
        controller.button_x.when_released = on_button_released
        controller.button_b.when_released = on_button_released

        # Left and right axis move event
        #controller.axis_l.when_moved = on_axis_moved
        #controller.axis_r.when_moved = on_axis_moved

        signal.pause()
except KeyboardInterrupt:
    pass
