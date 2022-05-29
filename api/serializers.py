from rest_framework import serializers
from .models import Calc
from .models import UserSong

class CalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calc
        fields = ('title', 'body', 'rate', 'count')


class UserSongForm(serializers.ModelSerializer):
    class Meta:
        model = UserSong
        fields = ('title','audio_file')
