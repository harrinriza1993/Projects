import time
import board
import busio
import adafruit_scd30

from urllib.request import urlopen

def scd_sensor_init():
    """
    Intializing the Scd sensor
    """
    i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
    scd = adafruit_scd30.SCD30(i2c)
    return scd

def read_scd_sensor(scd):
    """
    Read the scd sensor data
    """
    try :
        if scd.data_available:
            return [str(round(scd.CO2, 2)) , str(round(scd.temperature, 2)), str(round(scd.relative_humidity, 2))]
    except :
        print("Unable to read from sensor, retrying...")
        return []
        

        

