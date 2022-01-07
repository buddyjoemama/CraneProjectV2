import piplates.MOTORplate as MOTOR   
from configparser import ConfigParser

##
## Represents an instance of a single motor
##
class CraneMotor(object):
    address = 0
    motor = 1
    
    def __init__(self, address = 0, motor = 1):
        self.address = address
        self.motor = motor

    def forward(self):
        MOTOR.dcCONFIG(self.address, self.motor, 'cw', 100.0, 0)
        MOTOR.dcSTART(self.address, self.motor)

    def reverse(self):
        MOTOR.dcCONFIG(self.address, self.motor, 'ccw', 100.0, 0)
        MOTOR.dcSTART(self.address, self.motor)
    
    def stop(self):
        MOTOR.dcSTOP(self.address, self.motor)

class MagnetController(object):
    magOnOff = None

    def __init__(self):
        cfg = ConfigParser()
        cfg.read('/home/pi/Projects/CraneProjectV2/Server/crane.cfg')
        self.magOnOff = CraneMotor(cfg.getint('ADDRESSES', 'MAG'), cfg.getint('MAG', 'ON_OFF'))

    def off(self):
        self.magOnOff.stop()

    def on(self):
        self.magOnOff.reverse()

    def activate(self, val):
        if(val):
            self.on()
        else:
            self.off()
 

#
# Boom
#
class BoomController(object):
    boomUpDown = None

    def __init__(self):
        cfg = ConfigParser()
        cfg.read('/home/pi/Projects/CraneProjectV2/Server/crane.cfg')
        self.boomUpDown = CraneMotor(cfg.getint('ADDRESSES', 'BOOM'), cfg.getint('BOOM', 'UP_DOWN'))
 
    def up(self):
        self.boomUpDown.forward()
    
    def down(self):
        self.boomUpDown.reverse()

    def stop(self):
        self.boomUpDown.stop()

    def boom(self, up, down):
        self.stop()
        
        if(up):
            self.up()
        elif(down):
            self.down()

#
# Hook
#
class HookController(object):
    boomUpDown = None

    def __init__(self):
        cfg = ConfigParser()
        cfg.read('/home/pi/Projects/CraneProjectV2/Server/crane.cfg')
        self.boomUpDown = CraneMotor(cfg.getint('ADDRESSES', 'HOOK'), cfg.getint('HOOK', 'UP_DOWN'))
 
    def up(self):
        self.boomUpDown.forward()
    
    def down(self):
        self.boomUpDown.reverse()

    def stop(self):
        self.boomUpDown.stop()

    def hook(self, up, down):
        self.stop()
        
        if(up):
            self.up()
        elif(down):
            self.down()

#
# Controls for the platform
#
class DirectionalController(object):
    platEastWest = None
    platNorthSouth = None

    def __init__(self):
        cfg = ConfigParser()
        print (cfg.read('/home/pi/Projects/CraneProjectV2/Server/crane.cfg'))

        self.platEastWest = CraneMotor(cfg.getint('ADDRESSES', 'PLATFORM'), cfg.getint('PLATFORM', 'EAST_WEST'))
        self.platNorthSouth = CraneMotor(cfg.getint('ADDRESSES', 'PLATFORM'), cfg.getint('PLATFORM', 'NORTH_SOUTH'))

    def platform(self, north, south, east, west):
        self.platNorthSouth.stop()
        self.platEastWest.stop()

        if(north):
            self.platNorthSouth.forward()
        elif(south):
            self.platNorthSouth.reverse()
        elif(east):
            self.platEastWest.forward()
        elif(west):
            self.platEastWest.reverse()

    def stop(self):
        self.platNorthSouth.stop()
        self.platEastWest.stop()

class PanAndTiltController(object): 
    camUpDown = None
    camRightLeft = None

    def __init__(self):
        cfg = ConfigParser()
        print (cfg.read('/home/pi/Projects/CraneProjectV2/Server/crane.cfg'))

        self.camUpDown = CraneMotor(cfg.getint('ADDRESSES', 'CAMERA'), cfg.getint('CAMERA', 'UP_DOWN'))
        self.camRightLeft = CraneMotor(cfg.getint('ADDRESSES', 'CAMERA'), cfg.getint('CAMERA', 'LEFT_RIGHT'))
    
    def stop(self):
        self.camRightLeft.stop()
        self.camUpDown.stop()

    def up(self):
        self.camUpDown.forward()
    
    def down(self):
        self.camUpDown.reverse()

    def left(self):
        self.camRightLeft.forward()

    def right(self):
        self.camRightLeft.reverse()
