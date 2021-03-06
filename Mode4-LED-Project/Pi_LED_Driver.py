import time
import grovepi
import jsonpickle
from pi_sensors.subscribers import MQTTSubscriber as ms

# Connect the blue LED to digital port D5
BLUE_LED = 5
RED_LED = 4
GREEN_LED = 6

# Set the blue LED pin to output mode
grovepi.pinMode(BLUE_LED, "OUTPUT")
time.sleep(1)  # give the hardware time to initialize


def on_connect(client, userdata, flags, rc):
    """
     Called each time the client connects to the message broker
     :param client: The client object making the connection
     :param userdata: Arbitrary context specified by the user program
     :param flags: Response flags sent by the message broker
     :param rc: the connection result
     :return: None
     """
    # subscribe to the LEDs topics when connected
    topics = [("SNHU/IT697/leds/red", 2), ("SNHU/IT697/leds/green", 2), ("SNHU/IT697/leds/blue", 2)]
    print("Connected to MQTT Broker........")
    # client.subscribe("SNHU/IT697/leds")
    client.subscribe(topics)
    print("Subscribed to ...", topics)


def on_message(client, userdata, msg):
    """
     Called for each message received
     :param client
     :param userdata:
     :param msg:
     :return: none
     """
    print("Received message from MQTT Broker.....")
    print(msg.topic, msg.payload)
    _topic = msg.topic
    led_payload = jsonpickle.decode(msg.payload)
    if _topic == 'SNHU/IT697/leds/red':
        print("Processing " + _topic + " with msg " + msg.payload)
        # write discrete for RED LED
        grovepi.analogWrite(RED_LED, led_payload['red'])
    elif _topic == 'SNHU/IT697/leds/green':
        print("Processing " + _topic + " with msg " + msg.payload)
        # write discrete for GREEN LED
        grovepi.analogWrite(GREEN_LED, led_payload['green'])
    elif _topic == 'SNHU/IT697/leds/blue':
        print("Processing " + _topic + " with msg " + msg.payload)
        # write discrete for BLUE LED
        grovepi.analogWrite(BLUE_LED, led_payload['blue'])
    else:
        print("No Registered Topic......")


subscriber = ms.MQTTSubscriber(mqtt_host="localhost", mqtt_client_id="LOCAL_SUBSCRIBER", port=1883)
subscriber.register_callbacks(on_connect=on_connect, on_message=on_message)
subscriber.connect()
local_client = subscriber.get_client()
local_client.loop_forever()
