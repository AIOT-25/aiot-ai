import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input, concatenate
from tensorflow.keras.models import Model

# 데이터 준비
np.random.seed(7)  # 재현성을 위한 시드 설정
input_flows = np.random.randint(5, 23, size=10000)

# 시간대 레이블 생성 (22시부터 8시까지를 심야, 그 외를 일반 시간으로 가정)
# 여기서는 간단히 0과 1로 구분 (0: 심야, 1: 일반)
time_labels = np.random.randint(0, 2, 10000)
# 출력 유량 조정
# 심야 시간에는 출력 유량을 크게, 일반 시간에는 작게 설정
# output_flows = np.where(time_labels == 0, output_flows * 70, output_flows * 30)
output_flows = PIDController.run_PID(input_flows)

for flow in range(len(output_flows)):
    if time_labels[flow] == 1:
        output_flows[flow] = output_flows[flow] * 0.2
    if time_labels[flow] == 0:
        output_flows[flow] = output_flows[flow] * 0.8


# 데이터 전처리
def create_dataset(input_data, time_labels, output_data, time_steps=1):
    X1, X2, ys = [], [], []
    for i in range(len(input_data) - time_steps):
        X1.append(input_data[i:(i + time_steps)])
        X2.append(time_labels[i:(i + time_steps)])
        ys.append(output_data[i + time_steps])
    return np.array(X1), np.array(X2), np.array(ys)

time_steps = 10
X1, X2, y = create_dataset(input_flows, time_labels, output_flows, time_steps)

# 모델 구축
input_flow_input = Input(shape=(time_steps, 1))
time_label_input = Input(shape=(time_steps, 1))

lstm1 = LSTM(100, activation='relu')(input_flow_input)
lstm2 = LSTM(100, activation='relu')(time_label_input)
lstm2 = Dense(100, activation='relu')(lstm2)  # 추가 Dense 레이어

# combined = concatenate([lstm1, lstm2])
combined = Add()([lstm1 * 0.2, lstm2 * 1.8])  # lstm2에 더 큰 가중치 부여

output = Dense(1)(combined)

model = Model(inputs=[input_flow_input, time_label_input], outputs=output)
model.compile(optimizer='adam', loss='mean_squared_error')

# 모델 훈련
model.fit([X1, X2], y, epochs=30, batch_size=32, validation_split=0.2)

# 예측 (새로운 데이터에 대한 예측)
new_input_flow = np.random.rand(10) * 100  # 새로운 유량 데이터
new_time_labels = np.random.randint(0, 2, 10)  # 새로운 시간대 데이터
new_input_flow = new_input_flow.reshape((1, time_steps, 1))
new_time_labels = new_time_labels.reshape((1, time_steps, 1))

predicted_output_flow = model.predict([new_input_flow, new_time_labels])
# print(f"input_flow: {new_input_flow}, new_time: {new_time_labels}")
# print(predicted_output_flow)
model.save('./my_model')