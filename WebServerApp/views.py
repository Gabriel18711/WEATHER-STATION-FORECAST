from django.shortcuts import render
from rest_framework import generics
from .models import TemperatureReading
from .serializer import TemperatureReadingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class TemperatureReadingList(generics.ListAPIView):
    queryset = TemperatureReading.objects.all()
    serializer_class = TemperatureReadingSerializer

class TemperatureReadingDetail(generics.RetrieveAPIView):
    queryset = TemperatureReading.objects.all()
    serializer_class = TemperatureReadingSerializer

class TemperatureCreateAPIView(generics.CreateAPIView):
    queryset = TemperatureReading.objects.all()
    serializer_class = TemperatureReadingSerializer

class LatestTemperatureAPIView(APIView):
    def get(self, request):
        latest_temperature = TemperatureReading.objects.latest('id')
        serializer = TemperatureReadingSerializer(latest_temperature)
        return Response(serializer.data)

# Function-based view for handling both GET and POST requests
@api_view(['POST', 'GET'])
def record_data(request):
    if request.method == 'POST':
        serializer = TemperatureReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        data = TemperatureReading.objects.all().order_by('-timestamp')[:10]
        response_data = [
            {
                "temperature": entry.temperature,
                "humidity": entry.humidity,
                "timestamp": entry.timestamp,
            }
            for entry in data
        ]
        return Response({"data": response_data}, status=status.HTTP_200_OK)
    
def temperature_monitor(request):
    return render(request, 'home.html')
