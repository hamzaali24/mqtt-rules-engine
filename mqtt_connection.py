import json

# Importing Paho MQTT library for handling MQTT connections
import paho.mqtt.client as mqtt

# Define the MQTT broker address and port
broker_address = "test.mosquitto.org"
port = 1883

# Add MQTT topic ID here
mqtt_topic_id = "6c2e15da-eacd-4c48-9ab3-d30ff6c413b0"

# Assessment input and output topics for MQTT communication (not working)
# input_topic = f"BRE/calculateWinterSupplementInput/{mqtt_topic_id}"
# output_topic = f"BRE/calculateWinterSupplementOutput/{mqtt_topic_id}"


# Custom topics for testing
input_topic = f"hamza/test/mqtt/input"
output_topic = f"hamza/test/mqtt/output"

def on_connect(client, userdata, flags, reason_code, properties):
    """
    Function triggered when the client connects to the MQTT broker.
    """
    if reason_code == 0:
        # Successful connection
        print(f"Connected with result code {reason_code}")
        try:
            # Subscribing to the input topic
            client.subscribe(input_topic)
            print(f"Subscribed to {input_topic}")
        except:
            # Print errors
            print(f"Can not subscribe to {input_topic}: {e}")
    else:
        # Connection failed
        print(f"Failed to connect: {reason_code}")

def setup_mqtt(on_message_callback):
    """
    Sets up and connects a MQTT client.
    """
    try:
        # Create a MQTT client
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        print("Connected as MQTT client")
    except Exception as e:
        # Connection failed
        print(f"Can not create MQTT client: {e}")
        return None
    
    # Connection and message handling callbacks
    client.on_connect = on_connect
    client.on_message = on_message_callback

    try:
        # Connect client to the broker
        client.connect(broker_address, port, 60)
        print("Connected to the broker")
    except Exception as e:
        # Print errors while connecting to the broker
        print(f"Can not connect to broker: {e}")
        return None
    
    # Return the connected MQTT client
    return client
