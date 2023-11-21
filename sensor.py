import random
import motor
import watertank

class FlowSensor:
  def __init__(self, motor, watertank):
    self.motor = motor
    self.watertank = watertank

  def get_value(self):
    if not self.motor.is_rotate():
      return 0
    if self.watertank.get_amount() == 0:
      return 0

    power = self.motor.get_power()
    amount = self.watertank.get_amount()

    if amount < power:
      return power - amount;

    return power
