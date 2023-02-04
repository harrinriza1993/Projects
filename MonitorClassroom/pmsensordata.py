import board
import busio
import adafruit_scd30
import time

from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C

def pm_sensor_init():
    """
    Intializing the pm sensor
    """
    # Create library object, use 'slow' 100KHz frequency!
    i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
    # Connect to a PM2.5 sensor over I2C
    pm25 = PM25_I2C(i2c, None)

    return pm25

def read_pm_sensor(pm25):
    """
    Read the pmsensor data
    """
    try:
        aqdata = pm25.read()
        # print(aqdata)
        # print(aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
        return [ str(aqdata["pm10 standard"]) , str(aqdata["pm25 standard"]) , str(aqdata["pm100 standard"])]
    
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        return []
        
