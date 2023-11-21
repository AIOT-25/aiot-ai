import random
import sensor

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
        # 출력 유량을 0과 50 사이로 제한
        if output < 0:
            output = output * - 1
        output = max(0, min(output, 50))
        return int(output)

    @staticmethod
    def run_PID(input_flows):
        # 예시 파라미터
        kp, ki, kd = 2.0, 0.2, 0.05
        setpoint = 150  # 목표 총량을 150으로 설정
        total = 150  # 초기 총량
        min_total = 100

        pid = PIDController(kp, ki, kd)
        output_flows = []
        # for i in range(50):
        #     input_flows.append(sensor.FlowSensor().get_value())
        print(input_flows)
        for input_flow in input_flows:
            # 입력 유량에 따라 total 업데이트
            total += int(input_flow)

            # PID 컨트롤러를 이용하여 total 조정
            output_flow = pid.update(setpoint, total)

            if total - output_flow <= min_total:
                output_flow = 0
            # 출력 유량을 이용하여 total 조정
            total -= output_flow

            print(f"Input: {input_flow}, Current Total: {total}, Output Flow: {output_flow}")
            output_flows.append(output_flow)

        print(input_flows)
        print(output_flows)
        return output_flows







