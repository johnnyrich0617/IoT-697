"""
The MQTTSubcriber Class
@author jrichardson
"""

import paho.mqtt.client as mqttClient


class MQTTSubscriber:

    def __init__(self, mqtt_host, mqtt_client_id, port):
        self.mqtt_host = mqtt_host
        self.mqtt_client_id = mqtt_client_id
        self.port = port
        self.mqtt_client = mqttClient.Client(self.mqtt_client_id)

    def connect(self):
        print("MQTTSubscriber::Connecting to client with id = ", self.mqtt_client_id)
        print("MQTTSubscriber::Connecting to host " + self.mqtt_host)
        self.mqtt_client.connect(host=self.mqtt_host, port=self.port)

    def register_callbacks(self, on_connect, on_message):
        self.mqtt_client.on_connect = on_connect
        self.mqtt_client.on_message = on_message
        print("Registered all Callbacks.....")

    def get_client(self):
        return self.mqtt_client

    def get_topic(self):
        return self.topic
