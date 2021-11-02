from flask import Flask, render_template, send_from_directory, Response
from flask_cors import CORS
from Controls import NorthChip, SouthChip, ExtraChip
import SerialController
import signal

app = Flask(__name__)
cors = CORS(app, resources={r"/py/control/*": {"origins": "*"}})

sController = SerialController.SerialController()

@app.route('/py/control/platform/north/<int:north>/south/<int:south>/east/<int:east>/west/<int:west>')
def platform(north, east, south, west):    
    sController.platform(north, east, south, west)
    result = sController.readResult()

    if(north == 0 and south == 0 
        and east == 0 and west == 0):
        sController.platform(north, east, south, west)
        sController.platform(north, east, south, west)

    return Response(result, status=200)

@app.route('/py/control/hook/up/<int:up>/down/<int:down>')
def hook(up, down):
    sController.hookUpDown(up, down)
    result = sController.readResult()
    
    if(up == 0 and down == 0): 
        sController.hookUpDown(up, down)
        sController.hookUpDown(up, down)

    return Response(result, status=200)

@app.route('/py/control/boom/up/<int:up>/down/<int:down>')
def boom(up, down):
    sController.boomUpDown(up, down)
    result = sController.readResult()

    if(up == 0 and down == 0):
        sController.boomUpDown(up, down)
        sController.boomUpDown(up, down)

    return Response(result, status=200)

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
