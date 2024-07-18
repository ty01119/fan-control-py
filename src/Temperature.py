import board
import adafruit_dht

class Temperature:
  def __init__(self):
    self.dhtDevice = adafruit_dht.DHT22(board.D17, use_pulseio=False)

  def getTemperature(self):
    try:
      temperature_c = self.dhtDevice.temperature
      return temperature_c
    except RuntimeError as error:
      print(error.args[0])
      return 0

  def getHumidity(self):
    try:
      humidity = self.dhtDevice.humidity
      return humidity
    except RuntimeError as error:
      print(error.args[0])
      return 0

  def getTemperatureAndHumidity(self):
    try:
      temperature_c = self.dhtDevice.temperature
      humidity = self.dhtDevice.humidity
      return temperature_c, humidity
    except RuntimeError as error:
      print(error.args[0])
      return 0, 0
