import json
import time
import paho.mqtt.client as mqtt





# MQTT Broker details
broker_address = "test.mosquitto.org"
port = 1883

# MQTT Topics

mqtt_topic_id = "8dacb622-4d1a-4f15-997e-f120f6e46e8f"

input_topic = f"BRE/calculateWinterSupplementInput/{mqtt_topic_id}"
output_topic = f"BRE/calculateWinterSupplementOutput/{mqtt_topic_id}"








# Callback for when the client connects to the broker
def on_connect(client, userdata, flags, rc, properties):
    if rc == 0:
        print(f"Connected to broker with result code {rc}. Subscribing to topic: {input_topic}")
        try:
            client.subscribe("BRE/calculateWinterSupplementInput/#")
            print(f"Subscribed to topic: {input_topic}")
        except:
            print("Subscribing is not working.")
    else:
        print(f"Failed to connect, return code {rc}")

# Callback for when a message is received
def on_message(client, userdata, msg):
    try:
        print("trying.......")
        # Parse the JSON data from the message payload
        coming_data = json.loads(msg.payload.decode())
        print(coming_data)
        # print("Received message:", data)
        print(json.dumps(coming_data, indent=4))
    except json.JSONDecodeError:
        print("Failed to decode JSON:", msg.payload)






# Create the MQTT client
# client = mqtt.Client()
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Assign callbacks
client.on_connect = on_connect
client.on_message = on_message



# client.connect(broker_address, port, 60)

client.connect("test.mosquitto.org", 1883, 60)

# client.loop_forever()
client.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping...")
    client.loop_stop()




# def check_eligibility(data):
#     id = data.get("id")
#     numberOfChildren = data.get("numberOfChildren", 0)
#     familyComposition = data.get("familyComposition", "")
#     familyUnitInPayForDecember = data.get("familyUnitInPayForDecember")


#     if familyUnitInPayForDecember:
#         if familyComposition == "single" and numberOfChildren == 0:
#             baseAmount = 60.0
#             childAmount = 0.0
        
#         elif familyComposition == "couple" and numberOfChildren == 0:
#             baseAmount = 120.0
#             childAmount = 0.0
            
#         # elif familyComposition == "single" and numberOfChildren > 0:
#         #     baseAmount = 120.0
#         #     childAmount = 20.0 * numberOfChildren
        
#         elif (familyComposition == "single" or familyComposition == "couple") and numberOfChildren > 0:
#             baseAmount = 120
#             childAmount = 20.0 * numberOfChildren

#         else:
#             baseAmount = 0.0
#             childAmount = 0.0

#         totalAmount = baseAmount + childAmount
#         data_output = {
#             "id": id,
#             "isEligible": familyUnitInPayForDecember,
#             "baseAmount": baseAmount,
#             "childrenAmount": childAmount,
#             "supplementAmount": totalAmount
#         }
#         json_data = json.dumps(data_output, indent=4)
#         print(json_data)
#         client.publish(output_topic, json_data)
#         # print(f"ID: {id}, Base Amount: {baseAmount}, Child Amount: {childAmount}, Total Amount: {totalAmount}")

#     else:
#         print(f"ID: {id}, Not eligible for payment.")