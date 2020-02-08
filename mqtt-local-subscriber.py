import paho.mqtt.client as mqttClient
import time


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to Local MQTT Mosquiitto Broker...")
        global CONNECTED  # Use global variable
        CONNECTED = True  # Signal connection
    else:
        print("Connection failed")


def on_message(client, userdata, message):
    print "Message received: " + message.payload


# global variable
CONNECTED = False
SUBSCRIPTION_TOPIC = "SNHU/IT697/john_richardson3/sensor/data/temphum/"

# Broker address and Port
broker_address = "localhost"
port = 1883

# create new instance
client = mqttClient.Client("SUB_LOCAL")

# attach functions to callbacks

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port=port)  # connect to broker

client.loop_start()  # start the loop

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