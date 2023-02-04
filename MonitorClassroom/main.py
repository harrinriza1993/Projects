from publish_sensor_data import *
from file import *
from led import *
from pmsensordata import *

def send_sensor_data(data):
    """
    Sending the sensor data to the webpage. If not then save the data
    in a file.
    """
    try :
        send_data(data)
        green_led_blink()
    except :
        print("Failed to publish the sensor data, Please check the internet connection\n")
        append(data)
        red_led_blink()    

def main():

    # Initializing red and green led 
    led_init()
    # Initializing the scd sensor
    scd = scd_sensor_init()
    # Initializing the pm sensor
    pm25 = pm_sensor_init()

    while(True):
        # Send the sensor data to the webpage if it is available in the file
        if(is_file_exist()):
            lines = read_file()
            for line in lines:
                send_sensor_data(line)      

        # Read the pm sensor data
        pm_sensor_data = read_pm_sensor(pm25)

        if not pm_sensor_data :
            print("PM sensor data not received\n")
            continue

        string_of_pm_sensor_data = "".join("/"+str(data) for data in pm_sensor_data)
        
        # Read the scd sensor data
        scd_sensor_data = read_scd_sensor(scd)

        if not scd_sensor_data:
            print("Scd data not received\n")
            continue

        string_of_scd_sensor_data = "".join("/" + str(data) for data in scd_sensor_data)        
        # Concatenate two strings
        string_of_sensor_data = string_of_pm_sensor_data + string_of_scd_sensor_data

        # Publish the sensor data to webpage
        send_sensor_data(string_of_sensor_data)

if __name__ == "__main__":
    main()