import schedule
import os
import RPi.GPIO as GPIO
import PiMotor
import time

#Name of Individual MOTORS 
m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)



#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2)

#Names for Individual Arrows
ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3) 
ar = PiMotor.Arrow(4)

os.system('python3 /home/pi/remotv/hardware/servo_controller.py reset')

class Servo:
    def __init__(self, pin=0):
        self.pin = pin
        self.pos = 0
        
    def up(self):
        self.pos += 5
        print('pppppppppppppp: ')
        print(self.pos)
        command = 'python3 /home/pi/remotv/hardware/servo_controller.py set ' + str(self.pin) +' '+ str(self.pos)
        print('ccccccccc')
        print(command)
        os.system(command)
        
    def down(self):
        self.pos -= 5
        #print('pppppppppppppp: '+self.pin)
        command = 'python3 /home/pi/remotv/hardware/servo_controller.py set ' + str(self.pin) +' '+ str(self.pos)
        print('ccccccccc')
        print(command)
        os.system(command)
        
    def open(self):
        self.pos = 0
        #print('pppppppppppppp: '+self.pin)
        command = 'python3 /home/pi/remotv/hardware/servo_controller.py set ' + str(self.pin) +' '+ str(self.pos)
        print('ccccccccc')
        print(command)
        os.system(command)
        
    def close(self):
        self.pos = 180
        #print('pppppppppppppp: '+self.pin)
        command = 'python3 /home/pi/remotv/hardware/servo_controller.py set ' + str(self.pin) +' '+ str(self.pos)
        print('ccccccccc')
        print(command)
        os.system(command)
        
# Servors
OC = Servo(4) # open close
UD = Servo(6) # up down
LR = Servo(5) # left right
        
OC.pos = 180
UD.pos = 120
LR.pos = 90


def setup(robot_config):
  # your hardware setup code goes here
  return

def move(args):
  global prev_f
  global prev_b
  global prev_l
  global prev_r
  m1Speed = 99
  m2Speed = 99
  command=args['button']['command']
  wait_time = .25

  if command == 'F':
    print("Robot Moving Forward")
    af.on()
    prev_f = float(round(time.time() * 1000))
    m1.forward(m1Speed)
    m2.reverse(m2Speed)
    schedule.single_task(wait_time, stop_f)
  elif command == 'B':
    print("Robot Moving Backward ")
    ab.on()
    m1.reverse(m1Speed)
    m2.forward(m2Speed)
    prev_b = float(round(time.time() * 1000))
    schedule.single_task(wait_time, stop_b)
    return
  elif command == 'L':
    print("Robot Moving Left ")
    al.on()
    m1.forward(m1Speed)
    m2.forward(m2Speed)
    prev_l = float(round(time.time() * 1000))
    schedule.single_task(wait_time, stop_l)
    return
  elif command == 'R':
    print("Robot Moving Right ")
    ar.on()
    m1.reverse(m1Speed)
    m2.reverse(m2Speed)
    prev_r = float(round(time.time() * 1000))
    schedule.single_task(wait_time, stop_r)
    return
  elif command == 'Q':
    print("Robot Moving Left ")
    al.on()
    m1.forward(50)
    m2.reverse(99)
    prev_l = float(round(time.time() * 1000))
    schedule.single_task(wait_time, stop_l)
    return
  elif command == 'E':
    print("Robot Moving Left ")
    al.on()
    m1.forward(99)
    m2.reverse(50)
    prev_l = float(round(time.time() * 1000))
    schedule.single_task(wait_time, stop_l)
    return
  elif command == 'open':
    print("Claw Open ")
    OC.open()
    return
  elif command == 'close':
    print("Claw Close ")
    OC.close()
    return
  elif command == 'up':
    print("Claw Up ")
    UD.up()
    return
  elif command == 'down':
    print("Claw Down ")
    UD.down()
    return
  elif command == 'clockwise':
    print("Rotate Claw Right ")
    LR.up()
    return
  elif command == 'counterclockwise':
    print("Servo Left ")
    LR.down()
    return

def stop_f():
  cur_time = float(round(time.time() * 1000))
  time_elapsed = cur_time - prev_f
  if time_elapsed > 250.0:
    af.off()
    motorAll.stop()

def stop_b():
  cur_time = float(round(time.time() * 1000))
  time_elapsed = cur_time - prev_b
  if time_elapsed > 250.0:
    ab.off()
    motorAll.stop()

def stop_l():
  cur_time = float(round(time.time() * 1000))
  time_elapsed = cur_time - prev_l
  if time_elapsed > 250.0:
    al.off()
    motorAll.stop()

def stop_r():
  cur_time = float(round(time.time() * 1000))
  time_elapsed = cur_time - prev_r
  if time_elapsed > 250.0:
    ar.off()
    motorAll.stop()

        