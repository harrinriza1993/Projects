import os


FILE_NAME = "store_sensor_data.txt"

def is_file_exist():
    """
    Return true if the file exists otherwise false
    """

    return os.path.isfile(FILE_NAME)

def read_file():
    """
    Returns the stored sensor data
    """

    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
        f.close()
        os.remove(FILE_NAME)
        return lines

def append(sensor_data):
    """
    Store the sensor data in a file
    to send to webpage latter.
    """
    f = open(FILE_NAME, "a")
    f.write(sensor_data)
    f.close()