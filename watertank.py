class WaterTank:
  def __init__(self, capacity):
    self.capacity = capacity
    self.amount = 0
  def fill(self, amount):
    if self.amount + amount > self.capacity:
      self.amount = amount
      return
    self.amount += amount
  def drain(self, amount):
    if self.amount - amount <= 0:
      self.amount = 0
      return
    self.amount -= amount
  def get_amount(self):
    return self.amount