from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from tensorflow.python.keras.models import load_model
from .wav import m4a_to_wav
from .spec import calc_spec
import numpy as np
import os
from pickle import load
import warnings

import os

warnings.filterwarnings(action='ignore')

@api_view(['GET'])
def HelloAPI(request):
    filename = 'cha (1)'
    m4a_to_wav(filename)

    input_spec = calc_spec(filename)
    # (1, 46)으로 변형 (transform input type: 2D array)
    X = input_spec[1:].reshape(1, len(input_spec) - 1)
    # scaler load
    scaler = load(open('./standard_scaler.pkl', 'rb'))
    X = scaler.transform(X)

    # 모델 load
    model = load_model('./Capstone_220507.h5')

    y_preds = model.predict(X)
    prediction = np.argmax(model.predict(X), axis=-1)

    if max(y_preds[0]) >= 0.97:  # 확률이 97% 이상이면 open
        print("Prediction Accuracy: {}".format(max(y_preds[0])))
        print("Result: {}".format(np.array(prediction)))
    else:
        print("Prediction Accuracy is too low")


    return Response(str(y_preds[0]))
@api_view(['POST'])
def upload_file(request):
        form = UserSongForm(request.body)
        print(request)

        def handle_uploaded_file(f):
                destination = open('./a.m4a', 'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
        try:
            handle_uploaded_file(request.FILES['file'])
            print(form)
            print(handle_uploaded_file)

            temp=test()
            if os.path.isfile('./a.m4a'):
                os.remove('./a.m4a')
            if os.path.isfile('./a.wav'):
                os.remove('./a.wav')
            return Response(temp)

        except:
            return Response('x')


def test():
    filename = 'a'
    m4a_to_wav(filename)

    input_spec = calc_spec(filename)
    # (1, 46)으로 변형 (transform input type: 2D array)
    X = input_spec[1:].reshape(1, len(input_spec) - 1)
    # scaler load
    scaler = load(open('./standard_scaler.pkl', 'rb'))
    X = scaler.transform(X)

    # 모델 load
    model = load_model('./Capstone_220507.h5')

    y_preds = model.predict(X)
    prediction = np.argmax(model.predict(X), axis=-1)
    print(y_preds)
    if max(y_preds[0]) >= 0.97:  # 확률이 97% 이상이면 open

        print("Prediction Accuracy: {}".format(max(y_preds[0])))
        print("Result: {}".format(np.array(prediction)))
        return 1
    else:
        print("Prediction Accuracy is too low")
        return 0

