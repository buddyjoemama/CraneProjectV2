from flask import Flask, render_template, send_from_directory, Response
from flask_cors import CORS
from Controls import NorthChip, SouthChip, ExtraChip
import SerialController
import signal

import sys
from MotorControls import DirectionalController, BoomController, HookController, PanAndTiltController, MagnetController

app = Flask(__name__)
cors = CORS(app, resources={r"/py/control/*": {"origins": "*"}})

plat = DirectionalController()
bm = BoomController()
hk = HookController()
cam = PanAndTiltController()
mag = MagnetController()

@app.route('/py/control/platform/north/<int:north>/south/<int:south>/east/<int:east>/west/<int:west>')
def platform(north, east, south, west):    
    plat.platform(north, south, east, west)
    return Response(status=200)

@app.route('/py/control/hook/up/<int:up>/down/<int:down>')
def hook(up, down):
    hk.hook(up, down)
    return Response(status=200)

@app.route('/py/control/boom/up/<int:up>/down/<int:down>')
def boom(up, down):
    bm.boom(up, down)
    return Response(status=200)

@app.route('/py/control/rotation/cw/<int:cw>/ccw/<int:ccw>/speed/<int:speed>')
def rotate(cw, ccw, speed):
    sController.rotation(cw, ccw, speed)
    return Response(status=200)

@app.route('/py/control/magnet/<int:val>')
def magnet(val):
    mag.activate(val)
    return Response(status=200)

@app.route('/py/control/ping')
def ping():
    return Response(status=200)

@app.route('/py/control/cam/up')
def camUp():
    cam.up()
    return Response(status=200)

@app.route('/py/control/cam/down')
def camDown():
    cam.down()
    return Response(status=200)

@app.route('/py/control/cam/cw')
def cameraCW():
    cam.right()
    return Response(status=200)

@app.route('/py/control/cam/ccw')
def cameraCCW():
    cam.left()
    return Response(status=200)

@app.route('/py/control/cam/stop')
def cameraStop():
    cam.stop()
    return Response(status=200)

@app.route('/py/control/off')
def off():
    sController.off()
    return Response(sController.readResult(), status=200)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
