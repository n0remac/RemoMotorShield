import time
import sys

from adafruit_servokit import ServoKit


command = sys.argv[1]

if command == 'set':
    pin = int(sys.argv[2])
    pos = int(sys.argv[3])
    ServoKit(channels=16).servo[pin].angle = pos
elif command == 'reset':
    print('-------------------------')
    ServoKit(channels=16).servo[4].angle = 180
    ServoKit(channels=16).servo[6].angle = 120
    ServoKit(channels=16).servo[5].angle = 90
    
