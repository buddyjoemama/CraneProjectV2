from flask import Flask, render_template, send_from_directory, Response
from flask_cors import CORS
from Controls import NorthChip, SouthChip, ExtraChip
import SerialController
import signal
from xbox360controller import Xbox360Controller

app = Flask(__name__)
cors = CORS(app, resources={r"/py/control/*": {"origins": "*"}})

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

@app.route('/py/control/platform/north/<int:north>/south/<int:south>/east/<int:east>/west/<int:west>')
def platform(north, east, south, west):
    val = sController.platform(north, east, south, west)
    return Response(val, status=200)

@app.route('/py/control/hook/up/<up>/down/<down>')
def hook(up, down):
    return Response("Ok", status=200)

@app.route('/py/control/boom/up/<up>/down/<down>')
def boom(up, down):
    return Response("Ok", status=200)
 
@app.route('/py/control/rotation/cw/<cw>/ccw/<ccw>')
def rotate(cw, ccw):
    return Response("Ok", status=200)

@app.route('/py/control/off')
def off():
    sController.off()
    return Response("Ok", status=200)

@app.route('/py/control/ping')  
def ping():
    return Response("Ok", status=200)

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

        #signal.pause()
except KeyboardInterrupt:
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')