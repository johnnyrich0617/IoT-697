# Home_Weather_Display.py
#
# Note the dht_sensor_type below may need to be changed depending on which DHT sensor you have:
#  0 - DHT11 - blue one - comes with the GrovePi+ Starter Kit
#  1 - DHT22 - white one, aka DHT Pro or AM2302
#  2 - DHT21 - black one, aka AM2301
#
#

from grovepi import *
from grove_rgb_lcd import *
import time
from math import isnan
from pi_sensors.publishers import HomeWeatherDisplayPublisher as hwdp


def local_on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to Local MQTT Mosquitto Broker....")
        global LOCAL_CONNECTED  # Use global variable
        LOCAL_CONNECTED = True  # Signal connection
    else:
        print("Connection to Local MQTT Mosquitto Broker failed..." + rc)


def public_on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to Public MQTT Mosquitto Broker...")
        global PUBLIC_CONNECTED  # Use global variable
        PUBLIC_CONNECTED = True  # Signal connection
    else:
        print("Connection to Public MQTT Mosquitto Broker failed..." + rc)


def local_on_publish(client, userdata, mid):
    print("LOCAL CLIENT PUBLISHED MESSAGE WITH ID: " + mid)


def public_on_publish(client, userdata, mid):
    print("PUBLIC CLIENT PUBLISHED MESSAGE WITH ID: " + mid)


'''
Setup the sensors
'''
# connect the DHt sensor to port 7
dht_sensor_port = 7
# use 0 for the blue-colored sensor and 1 for the white-colored sensor
dht_sensor_type = 0
# set the default back lighting to BLUE
setRGB(0, 0, 255)
# clear the LED Screen
setText_norefresh(" ")

'''
GLOBALS
'''
# global variables for connection state and other data
LOCAL_CONNECTED = False
PUBLIC_CONNECTED = False

'''
PUBLISHER Metadata
'''
# PUBLISH_TOPIC = "SNHU/IT697/john_richardson3/sensor/data/temphum/"
TOPIC_BASE = "SNHU/IT697/john_richardson3/sensor/data/"
local_broker_address = "localhost"
public_broker_address = "test.mosquitto.org"
port = 1883

'''
CONNECT AND MANAGE CONNECTION
THIS IS THE CODE USING ENCAPSULATED MQTT PUBLISHERS
LOCAL_PUBLISHER
PUBLIC_PUBLISHER
'''
local_publisher = hwdp.HomeWeatherPublisher(local_broker_address, port, "LOCAL_HomeWeatherPublisher", TOPIC_BASE)
public_publisher = hwdp.HomeWeatherPublisher(public_broker_address, port, "PUBLIC_HomeWeatherPublisher", TOPIC_BASE)

local_publisher.set_callbacks(on_connection=local_on_connect, on_publish=local_on_publish)
public_publisher.set_callbacks(on_connection=public_on_connect, on_publish=public_on_connect)

local_publisher.connect()
public_publisher.connect()

local_mqtt_client = local_publisher.get_client()
public_mqtt_client = public_publisher.get_client()

local_mqtt_client.loop_start()
public_mqtt_client.loop_start()
'''
END MQTT CONNECTION MANAGEMENT
'''

# Wait for connections
while not LOCAL_CONNECTED and not PUBLIC_CONNECTED:
    time.sleep(0.1)
    print("Sleeping...Waiting on connection")

while True:
    try:
        # get the temperature and Humidity from the DHT sensor
        [temp, hum] = dht(dht_sensor_port, dht_sensor_type)
        print("temp =", temp, "C\thumidity =", hum, "%")

        # check if we have nans
        # if so, then raise a type error exception
        if isnan(temp) is True or isnan(hum) is True:
            raise TypeError('nan error')

        # Convert the acquired temperature to Fahrenheit
        tempf = (temp * 1.8) + 32

        # Print the converted temperature and humidity
        # to the shell/console
        print('temp =', tempf, 'F\thumidity =', hum, '%')

        # If the temperature in Fahrenheit is greater then 60
        # change the LeD back lighting to RED
        # and print this condition
        if tempf > 68:
            print('Temp is RED........')
            setRGB(255, 0, 0)
        else:
            # If its not greater then 68
            # set the back-lighting to BLUE and
            # print color condition to console
            print('Temp is BLUE.......')
            setRGB(0, 0, 255)

        t = str(temp)
        h = str(hum)
        tf = str(tempf)

        '''
        Publish messages to the broker using publisher objects
        '''
        local_publisher.publish_msg(temp=t, humidity=h)
        public_publisher.publish_msg(temp=t, humidity=h)
        # write to the sensor display LCD
        setText_norefresh("Temp:" + tf + "F\n" + "Humidity:" + h + "%")

    except (IOError, TypeError) as e:
        print(str(e))
        setText_norefresh(" ")
        local_publisher.stop_publishing()
        public_publisher.stop_publishing()

        # and since we got a type error
        # then reset the LCD's text

    except KeyboardInterrupt as e:
        print(str(e))
        setText_norefresh(" ")
        local_publisher.stop_publishing()
        public_publisher.stop_publishing()
        # since we're exiting the program
        # it's better to leave the LCD with a blank text
        break

    # wait some time before re-updating the LCD
    time.sleep(3)
