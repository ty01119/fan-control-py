import RPi.GPIO as GPIO
import time

class PWM:
  def __init__(self):
    self.pwmPin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.pwmPin, GPIO.OUT)

    self.pwm = GPIO.PWM(self.pwmPin, 60)
    self.pwm.start(0)

  def setSpeed(self, speed):
    dutyCycle = float(speed) / 100.0 * 100
    self.pwm.ChangeDutyCycle(dutyCycle)

  def stop(self):
    self.pwm.stop()
    GPIO.cleanup()