import serial

class SerialController(object):
    
    port = '/dev/ttyACM0'
    serConnection = None

    def __init__(self, p):
        self.port = p
        self.serConnection = serial.Serial(self.port)
    
    def write(self, north, south):
        self.serConnection.write([north, south])