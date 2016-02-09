import RPi.GPIO as GPIO
import time

def main():

    try:
        GPIO.setmode(GPIO.BCM)
      
        led_pin = 18
        but_pin = 17
        GPIO.setup(led_pin, GPIO.OUT)
        GPIO.setup(but_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
        GPIO.output(led_pin, GPIO.LOW)

        while True:
            if GPIO.input(but_pin): # button is released
                GPIO.output(led_pin, GPIO.LOW)
            else:
                GPIO.outup(led_pin, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(led_pin, GPIO.LOW)
                time.sleep(1)
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup()

main()
