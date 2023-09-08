# deye-solarflow-bridge

Enables you to set inverter limit on your broker from this

```bash
deye/settings/active_power_regulation 2.9
```

to this format

```bash
deye-bridge/output_power 300
```


### Dependencies
https://github.com/kbialek/deye-inverter-mqtt


### Configuration

```bash
MQTT_BROKER_IP=
MQTT_BROKER_PORT=1883
MQTT_USERNAME=
MQTT_PASSWORD=
```

### Setup

```bash
docker run -d --restart=always --env-file .env --name deye-solarflow-bridge tobit6795/deye-solarflow-bridge:latest
```


### Limitations
Unfortunately we can only send one digit values, means depending on your inverter MAX you can only increase/decrease the limit by 1% which would be 8w for an 800w inverter
