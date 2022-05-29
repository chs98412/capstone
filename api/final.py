from tensorflow.python.keras.models import load_model
import wav
import spec
import numpy as np

from pickle import load
import warnings

warnings.filterwarnings(action='ignore')

filename = 'cha (1)'
wav.m4a_to_wav(filename)

input_spec = spec.calc_spec(filename)
# (1, 46)으로 변형 (transform input type: 2D array)
X = input_spec[1:].reshape(1, len(input_spec)-1)
# scaler load
scaler = load(open('../standard_scaler.pkl', 'rb'))
X = scaler.transform(X)


# 모델 load
model = load_model('../Capstone_220507.h5')

y_preds = model.predict(X)
prediction = np.argmax(model.predict(X), axis=-1)

if max(y_preds[0]) >= 0.97:  # 확률이 97% 이상이면 open
    print("Prediction Accuracy: {}".format(max(y_preds[0])))
    print("Result: {}".format(np.array(prediction)))
else:
    print("Prediction Accuracy is too low")
