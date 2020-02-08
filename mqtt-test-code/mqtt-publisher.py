import paho.mqtt.client as mqttClient
import time


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


# global variables for connection state and other data
LOCAL_CONNECTED = False
PUBLIC_CONNECTED = False
PUBLISH_TOPIC = "SNHU/IT697/john_richardson3/sensor/data/temphum/"

local_broker_address = "localhost"
public_broker_address = "test.mosquitto.org"
public_broker_port = 1883
# user = "yourUser"
# password = "yourPassword"

# create the MQTT Clients
local_client = mqttClient.Client("LOCAL")  # create new instance
public_client = mqttClient.Client("PUBLIC")

# local_client.username_pw_set(user, password=password)  # set username and password

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

# Wait for connections
while not LOCAL_CONNECTED and not PUBLIC_CONNECTED:
   	print('SLEEPING...WATING FOR CONNECTION')
	time.sleep(0.1)

try:
    while True:
        value = raw_input('Enter a message to send:')
        local_client.publish(topic=PUBLISH_TOPIC, payload=value, qos=1)
        public_client.publish(topic=PUBLISH_TOPIC, payload=value, qos=1)
except KeyboardInterrupt:
    local_client.disconnect()
    public_client.disconnect()
    public_client.loop_stop()
    local_client.loop_stop()
