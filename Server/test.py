import time                                  #import the time module
import piplates.MOTORplate as MOTOR          #import the MOTORplate module
from MotorControls import CraneMotor, DirectionalController, BoomController, PanAndTiltController

# m1 = CraneMotor(0, 1)
# m1.forward()
# time.sleep(5)
# m1.stop()
# m1.reverse()
# time.sleep(5)
# m1.stop()

# m2 = CraneMotor(0, 2)
# m2.forward()
# time.sleep(5)
# m2.stop()
# m2.reverse()
# time.sleep(5)
# m2.stop()

# m3 = DirectionalController()
# m3.platform(1, 0, 0, 0)
# time.sleep(5)
# m3.platform(0, 1, 0, 0)
# time.sleep(5)
# m3.platform(0,0, 1, 0)
# time.sleep(5)
# m3.platform(0,0,0,1)
# time.sleep(5)
# m3.platform(0,0,0,0)

#m4 = BoomController()
#m4.up()
#m4.down()
#m4.stop()

# MOTOR.dcCONFIG(0,1,'ccw',100.0,0)           #configure dc motor 2 on the MOTORplate at address 0 being configured for clockwise 
# MOTOR.dcCONFIG(0,2,'ccw',100.0,0)   
#                                              #motion at a 50% duty cycle and 2.5 seconds of acceleration 
# MOTOR.dcSTART(0,2)                           #Start DC motor
# MOTOR.dcSTART(0,1)  
# time.sleep(5.0)                              #delay 5 seconds
# MOTOR.dcSPEED(0,2,100.0)                     #increase speed to 100%
# MOTOR.dcSPEED(0,1,100.0)  
# time.sleep(10)                               #wait 10 seconds
# MOTOR.dcSTOP(0,2)                            #stop the motor                            #wait for deceleration
# #print "DC Motor demo completed"              #print notice#
# MOTOR.dcSTOP(0, 1)

#MOTOR.dcCONFIG(1, 4, 'ccw', 100.0, 0)
#MOTOR.dcSTART(1,4)  
#time.sleep(6.0)  
#MOTOR.dcSTOP(1, 4)

#MOTOR.dcCONFIG(0, 3, 'ccw', 100.0, 0)
#MOTOR.dcSTART(0,3)  
#time.sleep(5.0)  
#MOTOR.dcSTOP(0, 3)

m1 = PanAndTiltController()
#m1.down()
#time.sleep(5)
#m1.stop()
#m1.up()
#time.sleep(5)
#m1.stop()
m1.left()
time.sleep(5)
m1.stop()
m1.right()
time.sleep(5)
m1.stop()