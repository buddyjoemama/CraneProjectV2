from flask import Flask, render_template, send_from_directory, Response
from flask_cors import CORS
from Controls import NorthChip, SouthChip, ExtraChip
import SerialController
import signal

import sys
from MotorControls import DirectionalController, BoomController

app = Flask(__name__)
cors = CORS(app, resources={r"/py/control/*": {"origins": "*"}})

#sController = SerialController.SerialController()

plat = DirectionalController()
bm = BoomController()

@app.route('/py/control/platform/north/<int:north>/south/<int:south>/east/<int:east>/west/<int:west>')
def platform(north, east, south, west):    
    plat.platform(north, south, east, west)
    return Response(status=200)

@app.route('/py/control/hook/up/<int:up>/down/<int:down>')
def hook(up, down):
    return Response(status=200)

@app.route('/py/control/boom/up/<int:up>/down/<int:down>')
def boom(up, down):
    bm.boom(up, down)
    return Response(status=200)

@app.route('/py/control/rotation/cw/<int:cw>/ccw/<int:ccw>/speed/<int:speed>')
def rotate(cw, ccw, speed):
    sController.rotation(cw, ccw, speed)
    return Response(sController.readResult(), status=200)

@app.route('/py/control/magnet/<int:val>')
def magnet(val):
    sController.magnet(val)
    return Response(sController.readResult(), status=200)

@app.route('/py/control/ping')
def ping():
    return Response(sController.readResult(), status=200)

@app.route('/py/control/cam/up')
def camUp():
    sController.camera_Up()
    return Response(sController.readResult(), status=200)

@app.route('/py/control/cam/down')
def camDown():
    sController.camera_Down()
    return Response(sController.readResult(), status=200)

@app.route('/py/control/cam/cw')
def cameraCW():
    sController.camera_Cw()
    return Response(sController.readResult(), status=200)

@app.route('/py/control/cam/ccw')
def cameraCCW():
    sController.camera_Ccw()
    return Response(sController.readResult(), status=200)

@app.route('/py/control/cam/stop')
def cameraStop():
    sController.cameraOff()
    return Response(sController.readResult(), status=200)

@app.route('/py/control/off')
def off():
    sController.off()
    return Response(sController.readResult(), status=200)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
