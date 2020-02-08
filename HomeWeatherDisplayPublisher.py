import paho.mqtt.client as mqttClient
import weather_display_message as wdm

CONNECTED = False

'''
def on_connect(userdata, flags, rc):
    if rc == 0:
        print("Connected to " + userdata + " MQTT Mosquitto Broker...")
        global CONNECTED  # Use global variable
        CONNECTED = True  # Signal connection
    else:
        print("Connection to" + userdata + " MQTT Mosquitto Broker failed..." + rc)
'''


class HomeWeatherPublisher:

    def __init__(self, mqtt_host, port, mqtt_client_id, topic):
        self.mqtt_host = mqtt_host
        self.mqtt_client_id = mqtt_client_id
        self.port = port
        self.topic = topic
        # self.CONNECTED = False
        self.mqtt_client = mqttClient.Client(self.mqtt_client_id)
        # self.mqtt_client.on_connect = self.on_connect

    def connect(self):
        print("HomeWeatherPublisher::Connecting to client with id = ", self.mqtt_client_id)
        print("HomeWeatherPublisher::Connecting to host " + self.mqtt_host)
        self.mqtt_client.connect(host=self.mqtt_host, port=self.port)

    def stop_publishing(self):
        self.mqtt_client.disconnect()
        self.mqtt_client.loop_stop()

    def publish_msg(self, temp, humidity):
        mqtt_msg = wdm.WeatherDisplayMessage(temp=temp, humidity=humidity)
        print("Created new MQTT Message with the following:")
        mqtt_msg.print_raw_content()
        print("")
        print("Serialized MQTT Message is as follows:")
        mqtt_msg.print_serialized_obj()
        print("")
        print("")
        self.mqtt_client.publish(topic=self.topic, payload=mqtt_msg.serialize(), qos=1)

    def is_connect(self):
        global CONNECTED
        return CONNECTED

    def get_client(self):
        return self.mqtt_client

    def get_topic(self):
        return self.topic
