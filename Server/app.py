from flask import Flask, render_template, send_from_directory, Response
from Controls import NorthChip, SouthChip, ExtraChip
import SerialController

app = Flask(__name__)

sController = SerialController.SerialController('/dev/ttyACM1')

@app.route('/py/control/north/<int:nOp>/south/<int:sOp>/extra/<int:eOp>')
def control(nOp, sOp, eOp):
    vNorth = north = NorthChip(nOp)
    vSouth = south = SouthChip(sOp)
    vExtra = extra = ExtraChip(eOp)
    
    if(north == NorthChip.Nothing):
        vNorth = 0
    else:
        vNorth = 1 << north
    if(south == SouthChip.Nothing):
        vSouth = 0
    else:
        vSouth = 1 << south
    if(extra == ExtraChip.Nothing):
        vExtra = 0
    else:
        vExtra = 1 << extra

    sController.write(vNorth, vSouth, vExtra)
    return Response("Ok", status=200)

@app.route('/py/control/stop')
def stop():
    sController.write(0, 0)
    return Response("Ok", status=200)

@app.route('/py/ping')
def ping():
    return Response("Ok", status=200)

if __name__ == '__main__':
    app.run(debug=True)