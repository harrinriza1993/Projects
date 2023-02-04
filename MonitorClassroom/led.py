import time
import RPi.GPIO as GPIO

GREEN_LED = 16
RED_LED = 21
time_delay = 5

def led_init():
    """
    Initializing the pin as output.
    """
    GPIO.setup(GREEN_LED , GPIO.OUT)
    GPIO.setup(RED_LED, GPIO.OUT)

def green_led_blink():
    """
    Making green led on and off
    """
    GPIO.output(GREEN_LED, 1)
    time.sleep(time_delay)
    GPIO.output(GREEN_LED, 0)
    time.sleep(time_delay)

def red_led_blink():
    """
    Making red led on and off
    """
    GPIO.output(RED_LED, 1)
    time.sleep(time_delay)
    GPIO.output(RED_LED, 0)
    time.sleep(time_delay)

