import json
import paho.mqtt.client as mqtt

broker_address = "test.mosquitto.org"
port = 1883
mqtt_topic_id = "88350c79-59a7-4b86-90ce-f4023b1210bc"

input_topic = f"BRE/calculateWinterSupplementInput/{mqtt_topic_id}"
output_topic = f"BRE/calculateWinterSupplementOutput/{mqtt_topic_id}"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(f"Connected with result code {reason_code}")
        try:
            client.subscribe(input_topic)
            print(f"Subscribed to {input_topic}")
        except:
            print(f"Cannot subscribe to {input_topic}")
    else:
        print(f"Failed to connect: {reason_code}")

def setup_mqtt(on_message_callback):
    try:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        print("Connecting as MQTT client")
    except Exception as e:
        print(f"Cannot create MQTT client: {e}")
        return None

    client.on_connect = on_connect
    client.on_message = on_message_callback

    try:
        client.connect(broker_address, port, 60)
        print("Connected to broker")
    except Exception as e:
        print(f"Cannot connect to broker: {e}")
        return None

    return client
