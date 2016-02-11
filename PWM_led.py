
import RPi.GPIO as GPIO
import time

def main():
    led = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    pwm = GPIO.PWM(led, 1000)
    while True:
        for i in range(0, 100):
            pwm.ChangeDutyCycle(i)
            pwm.start(i)
            time.sleep(.05)

main()

