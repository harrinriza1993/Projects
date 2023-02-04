import requests

from urllib.request import urlopen

def send_data(sensor_data):
    """
    Send the sensor data to webpage
    """

    WEB_PAGE = "https://molnteknik.se/sfhallproj/node/27"

    # Append sensor data to the link 
    LINK = WEB_PAGE + sensor_data
    print(LINK)

    try :
        myobj = {'somekey': 'somevalue'}
        # Send the sensor data to webpage
        respone = requests.post(LINK, json = myobj)
        print("Response from url: " + response.text)
    except :
        raise Exception("Error occured while sending the sensor data")
