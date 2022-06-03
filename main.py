from current_measurement import getCurrentCurrent
from api import postSensorData
import time

try:
  while True:
    postSensorData(getCurrentCurrent())

    time.sleep(0.5)

except KeyboardInterrupt:
  pass