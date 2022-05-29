""" mel-spectrogram 계산 """
import librosa

import numpy as np
import os
import csv
import warnings
warnings.filterwarnings(action='ignore')


def calc_spec(filename):
    # 계산 parameters
    offset = 0
    n_fft = 512
    hop_length = 513

    speech = f'./{filename}.wav'
    # y : 1차원 numpy float array, 음원 파형 데이터
    # sr : sample rate(초당 샘플링 횟수), default = 22050Hz
    y, sr = librosa.load(speech, mono=True, sr=16000)
    # 파일 앞, 뒤의 무음 제거, yt: 제거 후 신호 / _: (자른 길이, y 길이)
    # top_db: 낮을 수록 덜 민감 -> 작은 noise 도 무음으로 인식 -> 더 많이 제거 (max - top_db 만큼을 무음으로 간주)
    yt, _ = librosa.effects.trim(y, top_db=20)
    y = yt

    spectrogram = librosa.feature.melspectrogram(y, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=23)
    spectrogram_db = librosa.power_to_db(spectrogram)

    filename1 = filename.replace(" ", "")  # 파일명 공백제거
    to_append = {filename1[:-4]}
    # 평균 계산, 입력
    for e in spectrogram_db:
        to_append = np.append(to_append, np.mean(e))
    # 분산 계산, 입력
    for e in spectrogram_db:
        to_append = np.append(to_append, np.var(e))

    input_spec = to_append

    return input_spec



