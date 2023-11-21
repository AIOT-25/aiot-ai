import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 데이터 준비 (예시 데이터, 실제 데이터로 대체 필요)
# input_flows: 입력 유량, output_flows: 출력 유량
input_flows = np.random.rand(1000) * 100  # 임의의 입력 유량 데이터
output_flows = np.random.rand(1000) * 50  # 임의의 출력 유량 데이터 (실제 데이터로 대체 필요)

# 데이터 전처리
# 데이터 형태를 LSTM에 맞게 조정
def create_dataset(input_data, output_data, time_steps=1):
    Xs, ys = [], []
    for i in range(len(input_data) - time_steps):
        Xs.append(input_data[i:(i + time_steps)])
        ys.append(output_data[i + time_steps])
    return np.array(Xs), np.array(ys)

time_steps = 10  # 과거 몇 개의 시간 단계를 고려할 것인지
X, y = create_dataset(input_flows, output_flows, time_steps)

# 모델 구축
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(time_steps, 1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

# 모델 훈련
model.fit(X, y, epochs=20, batch_size=32, validation_split=0.2)

# 예측 (새로운 데이터에 대한 예측)
new_input_flow = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95])  # 새로운 입력 유량 데이터
new_input_flow = new_input_flow.reshape((1, time_steps, 1))
predicted_output_flow = model.predict(new_input_flow)

print("Predicted Output Flow:", predicted_output_flow[0][0])
