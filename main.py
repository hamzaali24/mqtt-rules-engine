# Import the setup function and topics
from mqtt_connection import setup_mqtt, input_topic, output_topic

# Import the eligibility check function
from eligibility_check import check_eligibility

# Import the JSON module for handling JSON data
import json

def on_message(client, userdata, message):
    """
    Function that gets triggered when a message is received on the subscribed topic and publish data.
    """
    print(f"Message received on topic {message.topic}")
    try:
        # Decode JSON format data
        data = json.loads(message.payload.decode())
        print(f"Received input: {json.dumps(data, indent=4)}")
        
        # Call the check eligibility function
        result = check_eligibility(data)
        print(f"Calculated output: {json.dumps(result, indent=4)}")
        
        # Publish the resulting data to the output topic
        client.publish(output_topic, json.dumps(result))
        print(f"Published output to topic {output_topic}")
    except json.JSONDecodeError:
        # Handle errors if the message is not valid
        print("Failed to decode JSON:", message.payload)
    except Exception as e:
        # Catch any other exceptions and print the error
        print(f"Error processing message: {e}")

if __name__ == "__main__":
    """
    Main entry point for the script. 
    Sets up the MQTT client and starts the event loop to listen for incoming messages.
    """
    
    # Setup the MQTT client with the on_message callback
    client = setup_mqtt(on_message)
    if client:
        try:
            # Start the client loop to listen for messages
            client.loop_forever()
        except KeyboardInterrupt:
            # Handle a manual interruption (Ctrl+C)
            print("Disconnecting from broker")
            client.disconnect()
