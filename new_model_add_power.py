import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Concatenate, Input, concatenate
from tensorflow.keras.models import Model

# 데이터 준비
np.random.seed(0)  # 재현성을 위한 시드 설정
input_flows = np.random.rand(1000) * 100  # 임의의 유량 데이터
power_usage = np.random.rand(1000) * 100  # 임의의 전력 사용량 데이터

# 낮(높은 전력 사용량)과 밤(낮은 전력 사용량)을 시뮬레이션
output_flows = np.where(power_usage > 50, np.random.rand(1000) * 30, np.random.rand(1000) * 70)

# 데이터 전처리
def create_dataset(input_data, power_data, output_data, time_steps=1):
    X1, X2, ys = [], [], []
    for i in range(len(input_data) - time_steps):
        X1.append(input_data[i:(i + time_steps)])
        X2.append(power_data[i:(i + time_steps)])
        ys.append(output_data[i + time_steps])
    return np.array(X1), np.array(X2), np.array(ys)

time_steps = 10
X1, X2, y = create_dataset(input_flows, power_usage, output_flows, time_steps)

# 모델 구축
# 두 입력을 위한 LSTM 레이어
input_flow_input = Input(shape=(time_steps, 1))
power_usage_input = Input(shape=(time_steps, 1))

# 두 LSTM 레이어
lstm1 = LSTM(50, activation='relu')(input_flow_input)
lstm2 = LSTM(50, activation='relu')(power_usage_input)

# 연결
combined = concatenate([lstm1, lstm2])

# 출력 레이어
output = Dense(1)(combined)

# 최종 모델
model = Model(inputs=[input_flow_input, power_usage_input], outputs=output)
model.compile(optimizer='adam', loss='mean_squared_error')

# 모델 훈련
model.fit([X1, X2], y, epochs=20, batch_size=32, validation_split=0.2)

# 예측
new_input_flow = np.random.rand(10) * 100  # 새로운 유량 데이터
new_power_usage = np.random.rand(10) * 100  # 새로운 전력 사용량 데이터
new_input_flow = new_input_flow.reshape((1, time_steps, 1))
new_power_usage = new_power_usage.reshape((1, time_steps, 1))

predicted_output_flow = model.predict([new_input_flow, new_power_usage])
print(f"input_flow: {new_input_flow}, new_power: {new_power_usage}")
print(predicted_output_flow)
