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
    val = sController.platform(north, east, south, west)
    return Response(val, status=200)


@app.route('/py/control/hook/up/<int:up>/down/<int:down>')
def hook(up, down):
    sController.hookUpDown(up, down)
    return Response("Ok", status=200)


@app.route('/py/control/boom/up/<int:up>/down/<int:down>')
def boom(up, down):
    sController.boomUpDown(up, down)
    return Response("Ok", status=200)


@app.route('/py/control/rotation/cw/<int:cw>/ccw/<int:ccw>/speed/<int:speed>')
def rotate(cw, ccw, speed):
    sController.rotation(cw, ccw, speed)
    return Response("Ok", status=200)


@app.route('/py/control/magnet/<int:val>')
def magnet(val):
    sController.magnet(val)
    return Response("Ok", status=200)


@app.route('/py/control/off')
def off():
    sController.off()
    return Response("Ok", status=200)


@app.route('/py/control/ping')
def ping():
    return Response("Ok", status=200)

@app.route('/py/control/cam/up')
def camUp():
    #sController.cameraUp()
    return Response("Ok", status=200)

@app.route('/py/control/cam/down')
def camDown():
    #sController.cameraDown()
    return Response("Ok", status=200)

@app.route('/py/control/cam/cw')
def cameraCW():
    sController.cameraDown()
    return Response("Ok", status=200)

@app.route('/py/control/cam/ccw')
def cameraCCW():
    sController.cameraUp()
    return Response("Ok", status=200)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
