
# Home_Weather_Display.py
#
# This is an project for using the Grove RGB LCD Display and the Grove DHT Sensor from the GrovePi starter kit
#
# In this project, the Temperature and humidity from the DHT sensor is printed on the RGB-LCD Display
#
#
# Note the dht_sensor_type below may need to be changed depending on which DHT sensor you have:
#  0 - DHT11 - blue one - comes with the GrovePi+ Starter Kit
#  1 - DHT22 - white one, aka DHT Pro or AM2302
#  2 - DHT21 - black one, aka AM2301
#
# For more info please see: http://www.dexterindustries.com/topic/537-6c-displayed-in-home-weather-project/
#
'''
The MIT License (MIT)
GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

from grovepi import *
from grove_rgb_lcd import *
import time
from math import isnan
import paho.mqtt.client as mqttClient
import HomeWeatherDisplayPublisher as hwdp
import weather_display_message as wdm

'''
# USE WITH OUT PUBLISHER
def local_on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to Local MQTT Mosquitto Broker....")
        global LOCAL_CONNECTED  # Use global variable
        LOCAL_CONNECTED = True  # Signal connection
    else:
        print("Connection to Local MQTT Mosquitto Broker failed..." +rc)


def public_on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to Public MQTT Mosquitto Broker...")
        global PUBLIC_CONNECTED  # Use global variable
        PUBLIC_CONNECTED = True  # Signal connection
    else:
        print("Connection to Public MQTT Mosquitto Broker failed..." +rc)


def local_on_publish(client, userdata, mid):
    print("LOCAL CLIENT PUBLISHED MESSAGE WITH ID: " + mid)


def public_on_publish(client, userdata, mid):
    print("PUBLIC CLIENT PUBLISHED MESSAGE WITH ID: " + mid)
    mqtt_client.publish(topic=self.topic, payload=mqtt_msg.serialize(), qos=1)
'''
        

# connect the DHt sensor to port 7
dht_sensor_port = 7
# use 0 for the blue-colored sensor and 1 for the white-colored sensor
dht_sensor_type = 0
# set the default back lighting to BLUE
setRGB(0, 0, 255)
# clear the LED Screen
setText_norefresh(" ")


# global variables for connection state and other data
'''
# USE WITH OUT PUBLISHER
LOCAL_CONNECTED = False
PUBLIC_CONNECTED = False
'''

PUBLISH_TOPIC = "SNHU/IT697/john_richardson3/sensor/data/temphum/"
local_broker_address = "localhost"
public_broker_address = "test.mosquitto.org"
# public_broker_port = 1883
port = 1883

local_publisher = hwdp.HomeWeatherPublisher(local_broker_address, port, "LOCALCLIENT", PUBLISH_TOPIC)
public_publisher = hwdp.HomeWeatherPublisher(public_broker_address, port, "PUBLICCLIENT", PUBLISH_TOPIC)

local_publisher.connect_and_loop()
public_publisher.connect_and_loop()

'''
# USE WITH OUT PUBLISHER
# create the MQTT Clients
local_client = mqttClient.Client("LOCAL")  # create new instance
public_client = mqttClient.Client("PUBLIC")

# attach functions to callbacks
local_client.on_connect = local_on_connect
local_client.on_publish = local_on_publish
public_client.on_connect = public_on_connect
public_client.on_publish = public_on_publish

local_client.connect(local_broker_address)  # connect to broker
public_client.connect(public_broker_address, port=public_broker_port)

# start the connection loops
local_client.loop_start()
public_client.loop_start()
'''

# Wait for connections
while not local_publisher.is_connect() and not public_publisher.is_connect():
    time.sleep(0.1)
    print("Sleeping..........")

while True:
    try:
        # get the temperature and Humidity from the DHT sensor
        [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
        print("temp =", temp, "C\thumidity =", hum,"%")

        # check if we have nans
        # if so, then raise a type error exception
        if isnan(temp) is True or isnan(hum) is True:
            raise TypeError('nan error')
        
    # Convert the aquired temperature to Fahrenheit
        tempf = (temp * 1.8) + 32

    # Print the converted temperature and humidity
    # to the shell/console
        print('temp =', tempf, 'F\thumidity =', hum, '%')
        
    # If the temperature in Fahrenheit is greater then 60
    # change the LeD back lighting to RED
    # and print this condition
        if tempf > 68:
            print('Temp is RED........')
            setRGB(255,0,0)
            pass
        else:
        # If its not greater then 68
        # set the backlighting to BLUE and 
        # print color condition to console
            print('Temp is BLUE')
            setRGB(0,0,255)

        t = str(temp)
        h = str(hum)
        tf = str(tempf)

        '''
        # USE WITH OUT PUBLISHER
        mqtt_msg = wdm.WeatherDisplayMessage(temp=t, humidity=h)
        print("Created new MQTT Message with the following:")
        mqtt_msg.print_raw_content()
        print("")
        print("Serialized MQTT Message is as follows:")
        mqtt_msg.print_serialized_obj()
        print("")
        print("")

        local_client.publish(topic=PUBLISH_TOPIC, payload=mqtt_msg.serialize(), qos=1)
        public_client.publish(topic=PUBLISH_TOPIC, payload=mqtt_msg.serialize(), qos=1)
        '''
        local_publisher.publish_msg(temp=t, humidity=h)
        public_publisher.publish_msg(temp=t, humidity=h)


    # allowing the screen to refresh on writes
        setText("Temp:" + tf + "F\n" + "Humidity:" + h + "%")

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
    time.sleep(2)
