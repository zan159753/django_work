# views.py
import platform
from multiprocessing.pool import AsyncResult

from rest_framework import viewsets
from .models import City, Room, Host, HostStat
from .serializers import CitySerializer, RoomSerializer, HostSerializer, HostStatSerializer
import subprocess
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.select_related('city').all()
    serializer_class = RoomSerializer


class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.select_related('room__city').all()
    serializer_class = HostSerializer

class HostStatViewSet(viewsets.ModelViewSet):
    queryset = HostStat.objects.all()
    serializer_class = HostStatSerializer


class PingHostAPIView(APIView):
    def post(self, request):
        id = request.data.get('id')

        host = Host.objects.filter(id=id).first()

        if not host:
            return Response({'error': 'Host required'}, status=400)


        # result = ping_host_async(host.ip_address)

        try:
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, "1", host.ip_address]
            print(host.ip_address)
            result = subprocess.run(command, timeout=3, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.TimeoutExpired:
            print(f"Ping {host.ip_address} TimeOut")
            result = False
        except Exception as exc:
            print(f"Ping {host.ip_address} Error: {exc}")
            result = False
        return Response({'result': True if result else False})

