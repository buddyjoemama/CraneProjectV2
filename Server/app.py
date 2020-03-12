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

@app.route('/py/control/rotation/cw/<cw>/ccw/<ccw>')
def rotate(cw, ccw):
    return Response("Ok", status=200)

@app.route('/py/control/north/<int:nOp>/south/<int:sOp>/extra/<int:eOp>')
def control(nOp, sOp, eOp):
    
    vNorth = north = NorthChip(nOp - 1)
    vSouth = south = SouthChip(sOp - 1)
    vExtra = extra = ExtraChip(eOp - 1)
     
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
    elif(extra == ExtraChip.CabCCW):
        vExtra = 1 << 7
    elif(extra == ExtraChip.CabCW):
        vExtra = 1 << 6

    #sController.write(vNorth, vSouth, vExtra)
    return Response("Ok", status=200)
    
@app.route('/py/control/magnet/<int:mOp>')
def magnetControl(mOp):
    #sController.writeOne(mOp) 
    return Response("Ok", status=200)

@app.route('/py/control/stop') 
def stop():
    #sController.write(0, 0, 0)
    return Response("Ok", status=200)

@app.route('/py/ping')  
def ping():
    return Response("Ok", status=200)

if __name__ == '__main__':
    app.run(debug=True)