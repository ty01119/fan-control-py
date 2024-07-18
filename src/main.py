import time
from Display import Display
# from NASTemperature import NASTemperature
from Temperature import Temperature
from PWM import PWM
# from PWM1 import pi5RC as PWM1

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
    displayInstance = Display()
    displayInstance.clear()
    TemperatureInstance = Temperature()
    pwm = PWM()

    try:
      while True:
        dateTime = time.localtime()
        day, month, year, hour, minute = dateTime.tm_mday, dateTime.tm_mon, dateTime.tm_year, dateTime.tm_hour, dateTime.tm_min 
        dateTimeStr = '{:02d}/{:02d}/{:04d} {:02d}:{:02d}'.format(day, month, year, hour, minute)

        temperature = TemperatureInstance.getTemperature()
        cycle = 0

        if(temperature > 35):
          cycle = 100
        elif(temperature > 33):
          cycle = 65
        elif(temperature > 31):
          cycle = 50
        else:
          cycle = 0

        displayInstance.drawText(f"Temp: {temperature} °C", f"Cycle: {cycle}%", f"{dateTimeStr}" )
        displayInstance.show()
        pwm.setSpeed(cycle)

        time.sleep(2)

    except KeyboardInterrupt:
      displayInstance.clear()
      pwm.stop()
      print("Exiting...")
      exit(0)

main()