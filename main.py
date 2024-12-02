from mqtt_connection import setup_mqtt, input_topic, output_topic
from eligibility_check import check_eligibility
import json

def on_message(client, userdata, message):
    print(f"Message received on topic {message.topic}")
    try:
        data = json.loads(message.payload.decode())
        print(f"Received input: {json.dumps(data, indent=4)}")

        result = check_eligibility(data)
        print(f"Calculated output: {json.dumps(result, indent=4)}")

        client.publish(output_topic, json.dumps(result))
        print(f"Published output to topic {output_topic}")
    except json.JSONDecodeError:
        print("Failed to decode JSON:", message.payload)
    except Exception as e:
        print(f"Error processing message: {e}")

if __name__ == "__main__":
    client = setup_mqtt(on_message)
    if client:
        try:
            client.loop_forever()
        except KeyboardInterrupt:
            print("Disconnecting from broker")
            client.disconnect()
