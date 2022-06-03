import requests

base_url = 'BASE_URL/api/'
sensorId = 2

def postRequest(url, data):
  requests.post(url=url, json=data)

def postSensorData(measurement):
  url = f'{base_url}sensor-data/store'

  data = {
    "sensorId": sensorId,
    "measurement": measurement
  }

  postRequest(url=url, data=data)