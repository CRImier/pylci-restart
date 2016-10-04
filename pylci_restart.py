#!/usr/bin/env python
from RPi import GPIO
from time import sleep
from subprocess import call

#configuration variables
pin = 12
restart_state = GPIO.HIGH
command = ['systemctl', 'restart', 'pylci.service']

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

while True:
    if GPIO.input(pin) == restart_state:
        call(command)
        while GPIO.input(pin) == restart_state:
            sleep(0.1)
    sleep(1)


