import numpy as np
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('./my_model')

new_input_flow = np.array([20, 15, 20, 17, 27, 7, 38, 45, 29, 32])  # 새로운 입력 유량 데이터
time_label2 = np.array([1,1,1,1,1,1,1,1,1,1])
time_label2 = time_label2.reshape((1, 10, 1))
time_label = np.array([0,0,0,0,0,0,0,0,0,0])
time_label = time_label.reshape((1, 10, 1))
new_input_flow = new_input_flow.reshape((1, 10, 1))
predicted_output_flow = model.predict([new_input_flow,time_label2])

print("Predicted Output Flow:", predicted_output_flow[0][0])

predicted_output_flow = model.predict([new_input_flow,time_label])

print("Predicted Output Flow:", predicted_output_flow[0][0])