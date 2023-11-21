import random

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0
        self.previous_error = 0

    def update(self, setpoint, total):
        error = setpoint - total
        self.integral += error
        derivative = error - self.previous_error
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.previous_error = error
        return output

# 예시 파라미터
kp, ki, kd = 2.0, 0.2, 0.05
pid = PIDController(kp, ki, kd)

min_total = 100  # 최소 총량
max_total = 300  # 최대 총량
setpoint = (min_total + max_total) / 2  # 목표 총량을 최소와 최대의 중간값으로 설정

total = 150  # 초기 총량
input_flows = [random.randint(20, 40) for _ in range(10)]  # 입력 유량의 예시 시퀀스

for input_flow in input_flows:
    # 입력 유량에 따라 total 업데이트
    total += input_flow

    # PID 컨트롤러를 이용하여 total 조정
    output_flow = pid.update(setpoint, total)

    # 출력 유량을 이용하여 total 조정
    total -= output_flow

    # total을 최소 및 최대 총량 사이로 제한
    total = max(min_total, min(total, max_total))

    print(f"intput: {input_flow} Total: {total}, Output Flow: {output_flow}")
