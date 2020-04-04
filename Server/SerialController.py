import serial

class SerialController(object):
    
    port = '/dev/ttyACM0'
    serConnection = None

    def __init__(self, p):
        self.port = p
        self.serConnection = serial.Serial(self.port)
    
    def write(self, north, south, extra):
        self.serConnection.write([north, south, extra])
    
    def writeOne(self, magnet):
        self.serConnection.write([magnet])

    def off(self):
        self.serConnection.write([0, 0, 0, 0])

    def platform(self, north, south, east, west):
        val = 0

        if(north):
            val |= (1 << 3)
        if(south):
            val |= (1 << 2)
        if(east):
            val |= (1 << 1)
        if(west):
            val |= 1
        
        self.serConnection.write([val, 0, 0, 0])

        line = []

        while True:
            for c in self.serConnection.read():
                line.append(c)
                if c == '\n':
                    return line