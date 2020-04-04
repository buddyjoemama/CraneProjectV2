from flask import Flask, render_template, send_from_directory, Response
from flask_cors import CORS
from Controls import NorthChip, SouthChip, ExtraChip
import SerialController

app = Flask(__name__)
cors = CORS(app, resources={r"/py/control/*": {"origins": "*"}})
sController = SerialController.SerialController('/dev/ttyACM0')

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
 ,
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

if __name__ == '__main__':
    app.run(debug=True)