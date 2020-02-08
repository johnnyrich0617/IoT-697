import paho.mqtt.client as mqttClient
import time


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to public MQTT Mosquitto Broker...")
        global CONNECTED
        CONNECTED = True
    else:
        print("Connection to public MQTT Broker failed...")


def on_message(client, userdata, message):
    print "Message received from Public MQTT Broker: " + message.payload


# global variable for the state of the connection
CONNECTED = False
SUBSCRIPTION_TOPIC = "SNHU/IT697/john_richardson3/sensor/data/temphum/"

# Broker address and port
broker_address = "test.mosquitto.org"
port = 1883

# create new instance
client = mqttClient.Client("SUB_PUBLIC")
# attach functions to callbacks
client.on_connect = on_connect
client.on_message = on_message

# connect to broker
client.connect(broker_address, port=port)

# start the loop
client.loop_start()

while not CONNECTED:  # Wait for connection
    time.sleep(0.1)

client.subscribe(topic=SUBSCRIPTION_TOPIC, qos=1)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop()
