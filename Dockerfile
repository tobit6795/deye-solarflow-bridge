FROM python:3.10-alpine

# Create stdconfig directory
WORKDIR /

COPY deye-solarflow-bridge.py /

RUN pip install paho-mqtt
CMD ["python","deye-solarflow-bridge.py"]
