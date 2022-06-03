import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Connect to ADS1015 and get its value
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads, ADS.P0)

# Sensitivity of the ACS712 sensor in mV/A.
# For the 30A module, sensitivity = 66 mV/A
SENSITIVITY = 66

# Default voltage of teh ACS712 when no current is used
# The value should be half of the input voltage of the ADS712
DEFAULT_VOLTAGE = 2.606

def getCurrentCurrent():
  measured_voltage = chan.voltage
  voltage_diff_mv = (DEFAULT_VOLTAGE - measured_voltage) * 1000

  current = voltage_diff_mv / SENSITIVITY

  return current