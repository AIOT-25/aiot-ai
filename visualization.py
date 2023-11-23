import matplotlib.pyplot as plt
from PID_test import PIDController
import numpy as np

# 데이터 필요
input_flows = []

output_flows = PIDController.run_PID(input_flows)
# 그래프 하나에 두가지 표현
# 첫 번째 데이터 세트 그리기
plt.plot(input_flows[100:200], color='blue', label='input_flows')
# 두 번째 데이터 세트 그리기
plt.plot(output_flows[100:200], color='red', label='output_flows')
# 그래프 제목과 축 레이블 추가
plt.title("PID")
plt.xlabel("time")
plt.ylabel("flow rate")
# 범례 추가
plt.legend()
# 그래프 보여주기
plt.show()



# 그래프 각각 데이터 표현
# 첫 번째 데이터 세트 그리기, 파란색 선과 'Data 1' 라벨 사용
plt.plot(input_flows[100:200], color='blue')
plt.xlabel("time")
plt.ylabel("flow rate")
plt.ylim(-2, 30)
plt.legend()
plt.title("Inlet Flow")
plt.show()
# 두 번째 데이터 세트 그리기, 빨간색 선과 'Data 2' 라벨 사용
plt.plot(output_flows[100:200], color='red')
plt.xlabel("time")
plt.ylabel("flow rate")
plt.legend()
plt.title("Outlet Flow")
plt.ylim(-2, 30)
plt.show()


# 모델 결과 값 확인
time_steps = 10
time_label = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
time_label = time_label.reshape((1, time_steps, 1))
start = 100
result_list = []
for i in range(110, 210, 10):
    new_input_flow = np.array(output_flows[start:i])
    # print(new_input_flow)
    new_input_flow = new_input_flow.reshape((1, time_steps, 1))

    # 모델 추가 필수
    #result = model.predict([new_input_flow, time_label])
    # print(result)
    result = np.repeat(result, 10)
    result_list.append(result)
    start = i
plt.plot(result_list, color='red')
plt.xlabel("time")
plt.ylabel("flow rate")
plt.legend()
plt.title("Outlet Flow")
plt.ylim(-2, 30)
plt.show()
print(result_list)


# 시간별 모델 결과 값 비교
time_label2 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
time_label2 = time_label2.reshape((1, time_steps, 1))
start = 100
result_list2 = []
for i in range(110, 210, 10):
    new_input_flow2 = np.array(output_flows[start:i])

    # print(new_input_flow)
    new_input_flow2 = new_input_flow2.reshape((1, time_steps, 1))
    # 모델 필수
    #result2 = model.predict([new_input_flow2, time_label2])
    # print(result)
    result2 = np.repeat(result2, 10)
    result_list2.append(result2)
    start = i
plt.plot(result_list, color='red')
plt.plot(result_list2, color='blue')
plt.xlabel("time")
plt.ylabel("flow rate")
plt.legend()
plt.title("Outlet Flow")
plt.ylim(-2, 30)
plt.show()
print(result_list2)
print(result_list)
