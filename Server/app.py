from flask import Flask, render_template, send_from_directory, Response
from Controls import NorthChip, SouthChip
import SerialController

app = Flask(__name__)

sController = SerialController.SerialController('/dev/tty')

@app.route('/py/control/north/<int:nOp>/south/<int:sOp>')
def control(nOp, sOp):
    north = NorthChip(nOp)
    south = SouthChip(sOp)    
    
    sController.write(1 << north, 1 << south)
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