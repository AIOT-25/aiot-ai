import random

class FlowSensor:
  def __init__(self):
    self.value = 0
    self.step = 0
  def get_value(self):
    # 스텝 5번이 지나기 전에는 기존 value 출력
    if not self.step % 5 == 0:
      self.step += 1;
      # 유량이 없는 경우 그대로 출력
      if self.value == 0:
        return self.value
      offset = random.randint(-1, 1)
      return self.value + offset
    else:
      rand = random.randint(0, 100)
      # 25% 확률로 유량 X
      if rand < 30:
        self.value = 0
      else:
        self.value = random.randint(0, 50)
      
      self.step += 1;
      return self.value
