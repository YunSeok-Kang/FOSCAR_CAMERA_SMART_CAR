#!/usr/bin/env python
import RPi.GPIO as GPIO
import car_dir
import motor
import time

#from time import ctime          # Import necessary modules

frequency = 60
period = 1 / frequency

busnum = 1

def setup():
    car_dir.setup(busnum=busnum)
    motor.setup(busnum=busnum)
    car_dir.calibrate(0)

    motor.setSpeed(50)

if __name__ == "__main__":
    #try:
            #setup()
            #loop()
    #except KeyboardInterrupt:
     #       tcpSerSock.close()
    setup()
    car_dir.turn(0);
    time.sleep(2);
    car_dir.turn(45);
    time.sleep(2);
    car_dir.turn(90);
    time.sleep(2);

    while (True):
        time_before = time.time()

        motor.forward()

        # To do
        #motor.ctrl(1)
        #time.sleep(3)
        #motor.ctrl(1, -1)
        #time.sleep(3)
        #motor.ctrl(0)

        while (time.time() - time_before) < period:
            time.sleep(0.001)  # precision here



