# LEGO type:standard slot:1 autostart
# ^
# |
# +- Autostart Header. The program will autostart in slot one as a standard-typed program

# import all the LEGO APIs. Adjust as you need
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

# connecting to the hub
hub = PrimeHub()

# display a happy face
hub.light_matrix.show_image('HAPPY')
    
# try to run it with the upload button