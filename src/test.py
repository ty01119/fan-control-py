import time
from Display import Display
from NASTemperature import NASTemperature
# from PWM import PWM

def setSpeedByTemp(pwm, maxTemp):
  if maxTemp > 60:
    pwm.setSpeed(100)
  elif maxTemp > 50:
    pwm.setSpeed(75)
  elif maxTemp > 40:
    pwm.setSpeed(50)
  else:
    pwm.setSpeed(25)


def main():
  try:
    displayInstance = Display()
    # pwm = PWM()
    displayInstance.clear()
    # for loop to display each line of text and sleep for 2 second

    try:
      while True:
        dateTime = time.localtime()
        day, month, year, hour, minute = dateTime.tm_mday, dateTime.tm_mon, dateTime.tm_year, dateTime.tm_hour, dateTime.tm_min 
        dateTimeStr = '{:02d}/{:02d}/{:04d} {:02d}:{:02d}'.format(day, month, year, hour, minute)

        maxTemp = NASTemperature.get_temperature()

        displayInstance.drawText(f"Temp: {maxTemp} °C", f"Humi: 50%", f"{dateTimeStr}" )
        displayInstance.show()

        # setSpeedByTemp(pwm, maxTemp)

        time.sleep(60)

    except KeyboardInterrupt:
      displayInstance.clear()
      # pwm.stop()
      print("Exiting...")
      exit(0)

  except Exception as e:
    print(e)
    exit(1)

main()