
from rest_framework import serializers
from .models import City, Room, Host, HostStat


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'

class HostStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostStat
        fields = '__all__'