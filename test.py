import sensor
import watertank
import motor
import time
import random

m = motor.MotorController(10)

w = watertank.WaterTank(150)
w.fill(150)

f = sensor.FlowSensor(m, w)

# 모터 회전
m.rotate()

def is_motor_stop():
  rand = random.randint(0, 100)
  return rand < 10

while True:
  if is_motor_stop():
    m.stop()
  else:
    m.rotate()
  print(f"유량 : {f.get_value()}, 탱크 물 잔여량 : {w.get_amount()}")
  w.drain(m.get_power())
  if w.get_amount() == 0:
    w.fill(100)
  time.sleep(0.5)