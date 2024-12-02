import json
import paho.mqtt.client as mqtt
# import paho.mqtt.subscribe as subscribe


# MQTT Broker details
broker_address = "test.mosquitto.org"
port = 1883

# MQTT Topics

mqtt_topic_id = "8dacb622-4d1a-4f15-997e-f120f6e46e8f"

input_topic = f"BRE/calculateWinterSupplementInput/{mqtt_topic_id}"
output_topic = f"BRE/calculateWinterSupplementOutput/{mqtt_topic_id}"


def on_subscribe(client, userdata, mid, reason_code_list, properties):
    # print(f"Subscribed with mid {mid} and QoS {reason_code_list}")
    if reason_code_list[0].is_failure:
        print(f"Broker rejected you subscription: {reason_code_list[0]}")
    else:
        print(f"Broker granted the following QoS: {reason_code_list[0].value}")


def on_message(client, userdata, message):
    print(f"Message received checkinggg")
    print(f"Message received on topic {input_topic}")
    print(f"Message payload: {message.payload}")
    try:
        coming_data = json.loads(message.payload.decode())
        print(f"Received input: {coming_data}")
        print(json.dumps(coming_data, indent=4))
        
        # output_data = {
        #     "id": coming_data.id,
        #     "isEligible": True,
        #     "baseAmount": 300.0,
        #     "childrenAmount": 200.0,
        #     "supplementAmount": 500.0
        #     }

        
        # output_topic = f"BRE/calculateWinterSupplementOutput/{output_topic}"
        
        # client.publish(output_topic, json.dumps(output_data))
        # print(f"Published output: {output_data} to topic {output_topic}")
    except json.JSONDecodeError:
        print("Failed to decode JSON:", message.payload)
        

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(f"Connected with result code {reason_code}")
        try:
            client.subscribe(input_topic)
            print(f"Subscribed to {input_topic}")
        except:
            print(f"Can not subscribed to {input_topic}")
    else:
        print(f"Failed to connect: {reason_code}. loop_forever() will retry connection")
        


try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    print("Connecting as mqtt client")
except:
    print("Can not connect as mqtt client")

# Assign callbacks
client.on_connect = on_connect
try:
    client.on_message = on_message
    print("Connecting to receive messages")
except:
    print("Can not connect and receive messages")

# client.on_subscribe = on_subscribe
try:
    client.connect(broker_address, port, 60)
    print("Connected to 1883")
except:
    print("Can not connect to 1883")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Disconnecting from broker")
    client.disconnect()




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

