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

    def cameraUp(self):
        self.serConnection.write([0, (1 << 2), (1 << 7), 0])

    def cameraDown(self):
        self.serConnection.write([0, (1 << 3), (1 << 7), 0])

    def cameraCW(self):
        self.serConnection.write([0, (1 << 5), (1 << 7), 0])

    def cameraCCW(self):
        self.serConnection.write([0, (1 << 4), (1 << 7), 0])

    def cameraOff(self):
        self.serConnection.write([0, 0, 0, 0])

    def hookUpDown(self, down, up):
        if (down == 1):
            self.hookDown()
        elif (up == 1):
            self.hookUp()
        else:
            self.off()

    def boomUpDown(self, down, up):
        if down == 1:
            self.boomDown()
        elif up == 1:
            self.boomUp()
        else:
            self.off()

    def hookUp(self):
        self.serConnection.write([(1 << 5), 0, 0, 0])

    def hookDown(self):
        self.serConnection.write([(1 << 6), 0, 0, 0])

    def boomUp(self):
        self.serConnection.write([1, 0, 0, 0])

    def boomDown(self):
        self.serConnection.write([(1 << 7), 0, 0, 0])

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
            val |= 4

        self.serConnection.write([val, 0, 0, 0])
