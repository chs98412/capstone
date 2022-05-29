"""m4a를 wav 로 변환"""
from pydub import AudioSegment
import warnings
warnings.filterwarnings(action='ignore')


def m4a_to_wav(filename):
    speech = AudioSegment.from_file(f'./{filename}.m4a')
    speech.export(f'./{filename}.wav', format="wav")

# import librosa
# import numpy as np
# import matplotlib.pyplot as plt
#
# filename = "non0 (6)"
# speech = AudioSegment.from_file(f'./{filename}.m4a')
# speech.export(f'./{filename}.wav', format="wav")
#
# speech = f'./{filename}.wav'
#
# y, sr = librosa.load(speech, sr=16000)
# # 파일 앞, 뒤의 무음 제거, yt: 제거 후 신호 / _: (자른 길이, y 길이)
# # top_db: 낮을 수록 덜 민감 -> 작은 noise 도 무음으로 인식 -> 더 많이 제거 (max - top_db 만큼을 무음으로 간주)
# yt, _ = librosa.effects.trim(y, top_db=30)
#
# time1 = np.linspace(0, len(y) / sr, len(y))  # time axis
# time2 = np.linspace(0, len(yt) / sr, len(yt))
#
# fig, axes = plt.subplots(2, 1)  # 여러개 plt
# axes[0].plot(time1, y, color='b')
# axes[1].plot(time2, yt, color='b')
# axes[1].set_ylabel("Amplitude")  # y 축
# axes[1].set_xlabel("Time [s]")  # x 축
# axes[0].set_title(filename)
# plt.subplots_adjust(wspace=0, hspace=0.2)   # width, height 간격 조정
# plt.show()