import paho.mqtt.client as mqtt
import os
import sys
import logging

script_name = os.path.basename(__file__)

FORMAT = '%(asctime)s:%(levelname)s(%(name)s) %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=FORMAT)
log = logging.getLogger(script_name)

MQTT_BROKER_IP = os.environ.get("MQTT_BROKER_IP")
MQTT_BROKER_PORT = int(os.environ.get("MQTT_BROKER_PORT"))
MQTT_USERNAME = os.environ.get("MQTT_USERNAME")
MQTT_PASSWORD = os.environ.get("MQTT_PASSWORD")
CUSTOM_INPUT_TOPIC = os.environ.get("CUSTOM_INPUT_TOPIC", "deye-bridge/output_power")
DEYE_OUTPUT_TOPIC = os.environ.get("DEYE_OUTPUT_TOPIC", "deye/settings/active_power_regulation/command")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        log.info("Connected to MQTT Broker.")
        client.subscribe(CUSTOM_INPUT_TOPIC)
    else:
        log.error("Connection to MQTT Broker failed. Error code: " + str(rc))

def on_message(client, userdata, message):
    if message.topic == CUSTOM_INPUT_TOPIC:
        try:
            value = float(message.payload)
            percentage = value / 800.0 * 100.0
            payload = f"{((percentage / 10)):.1f}"
            log.info(f"Set inverter limit to {percentage:.1f}% / {int(value)}W")  # Log-Ausgabe enthält die Wattzahl
            client.publish(DEYE_OUTPUT_TOPIC, payload)
        except ValueError as e:
            log.error(f"Error processing the message: {e}")
        except Exception as ex:
            log.error(f"An unexpected error occurred: {ex}")

client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(MQTT_BROKER_IP, MQTT_BROKER_PORT)
    client.loop_forever()
except KeyboardInterrupt:
    log.info("Terminated by the user.")
except Exception as e:
    log.error(f"An error occurred: {e}")
