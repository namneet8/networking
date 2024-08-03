"""
Group 5 - MQTT Publisher

Members:
- Namneet Kaur
- Salih, Zeinelabdin
- Ngo, Huu Duc
- Kaushik, Sachin
- Vohra, Muhammad Shahzaib

"""

import time
import json
import paho.mqtt.client as mqtt
import paho.mqtt.properties as Properties
import paho.mqtt.packettypes as PacketTypes
from group5_util import Util

# Create a single instance of Util
util = Util()


# MQTT settings
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "group5/lab11/data"
MESSAGE_COUNT = 10  # Number of messages to publish

def on_connect(client, userdata, flags, reason, properties):
    """Handles the event of connecting to the MQTT broker."""
    print("Connected successfully to the broker.")

def on_publish(client, userdata, mid, reason, properties):
    """Handles the event of publishing a message."""
    print(f'Publish message {mid} -- code {reason}')

def on_disconnect(client, userdata, reason, properties):
    """Handles the event of disconnecting from the MQTT broker."""
    print(f'Disconnected with reason: {reason}')
    client.loop_stop()

def publish_data(topic, message_count):
    """
    Connects to the MQTT broker and publishes data messages.
    """
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,
                         client_id='pub_demo',
                         protocol=mqtt.MQTTv5)
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_disconnect = on_disconnect

    try:
        client.connect(BROKER, PORT, 60)
        client.loop_start()  # Start the network loop in a separate thread

        for _ in range(message_count):
            data = util.get_json_data()
            message = json.dumps(data)
            client.publish(topic, message)
            print("Published message:", message)
            time.sleep(3)
        
        client.loop_stop()  # Stop the network loop
        client.disconnect()
    except Exception as e:
        print(f"An error occurred: {e}")
        client.loop_stop()  # Ensure the loop is stopped
        client.disconnect()

if __name__ == "__main__":
    publish_data(TOPIC, MESSAGE_COUNT)

