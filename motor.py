class MotorController:
  def __init__(self, power):
    self.power = power
    self._is_rotate = False
  def rotate(self):
    print("Motor Rotating")
    self._is_rotate = True
  def stop(self):
    print("Motor Stopped")
    self._is_rotate = False
  def is_rotate(self):
    return self._is_rotate
  def get_power(self):
    return self.power