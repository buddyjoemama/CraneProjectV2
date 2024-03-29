import serial
import threading

class SerialController(object):
    port = '/dev/ttyACM'
    serConnection = None

    def __init__(self):
        self.lock = threading.Lock()
        id = 0
        while id < 10:
            try:
                self.port = '/dev/ttyACM' + str(id)
                self.serConnection = serial.Serial(self.port)
                break
            except:
                id += 1

    def write(self, north, south, extra):
        self.lock.acquire()
        try:
            self.serConnection.write([north, south, extra])
        finally:
            self.lock.release()

    def writeOne(self, magnet):
        self.serConnection.write([magnet])

    def off(self):
        self.serConnection.write([0, 0, 0, 0])

    def camera_Ccw(self):
        self.serConnection.write([0, (1 << 6), (1 << 7), 0])

    def camera_Cw(self):
        self.serConnection.write([0, (1 << 7), (1 << 7), 0])

    def camera_Up(self):
        self.serConnection.write([0, (1 << 4), (1 << 7), 0])

    def camera_Down(self):
        self.serConnection.write([0, (1 << 5), (1 << 7), 0])

    def cameraOff(self):
        self.serConnection.write([0, 0, 0, 0])

    def platformCW(self, speed):
        self.serConnection.write([0, (1 << 1), speed, 0])

    def platformCCW(self, speed):
        self.serConnection.write([0, 1, speed, 0])

    def rotation(self, cw, ccw, speed):
        if(cw == 1):
            self.platformCW(speed)
        elif(ccw == 1):
            self.platformCCW(speed)
        else:
            self.off()

    def hookUpDown(self, up, down):
        if (up == 1):
            self.hookUp()
        elif (down == 1):
            self.hookDown()
        else:
            self.off()

    def boomUpDown(self, up, down):
        if up == 1:
            self.boomUp()
        elif down == 1:
            self.boomDown()
        else:
            self.off()

    def hookUp(self):
        self.serConnection.write([(1 << 6), 0, 0, 0])

    def hookDown(self):
        self.serConnection.write([(1 << 5), 0, 0, 0])

    def boomUp(self):
        self.serConnection.write([(1 << 7), 0, 0, 0])

    def boomDown(self):
        self.serConnection.write([1, 0, 0, 0])

    def magnet(self, val):
        self.serConnection.write([0, 0, 0, val])

    def platform(self, north, south, east, west):
        val = 0

        if (north):
            val |= (1 << 1)
        if (south):
            val |= (1 << 2)
        if (east):
            val |= (1 << 3)
        if (west):
            val |= (1 << 4)

        self.serConnection.write([val, 0, 0, 0])

    def readResult(self):
        return self.serConnection.read_all()