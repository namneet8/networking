"""
Group 5 - MQTT Subscriber

Members:
- Namneet Kaur
- Salih, Zeinelabdin
- Ngo, Huu Duc
- Kaushik, Sachin
- Vohra, Muhammad Shahzaib

"""

import json
import paho.mqtt.client as mqtt
import paho.mqtt.properties as Properties
import paho.mqtt.packettypes as PacketTypes
from group5_util import Util, print_data


# MQTT settings
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "group5/lab11/data"

def on_connect(client, userdata, flags, reason, properties):
    """Handles the event of connecting to the MQTT broker."""
    print("Connected successfully to the broker.")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    """Handles incoming MQTT messages."""
    try:
        data = json.loads(msg.payload.decode())
        print_data(data)
    except Exception as e:
        print(f"Error processing message: {e}")

def on_disconnect(client, userdata, reason, properties):
    """Handles the event of disconnecting from the MQTT broker."""
    print(f"Disconnected with reason: {reason}")

def subscribe(broker, port, topic):
    """
    Connects to the MQTT broker, subscribes to a topic, and processes incoming messages.
    """
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,
                         client_id='sub_demo',
                         protocol=mqtt.MQTTv5)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    try:
        client.connect(broker, port, 60)
        print(f"Connecting to broker {broker} on port {port}...")
        client.loop_forever()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    subscribe(BROKER, PORT, TOPIC)


