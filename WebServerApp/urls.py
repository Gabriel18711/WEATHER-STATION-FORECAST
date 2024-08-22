from django.urls import path
from .views import TemperatureReadingList, TemperatureReadingDetail, TemperatureCreateAPIView, LatestTemperatureAPIView, temperature_monitor

urlpatterns = [
    path('temperatures/', TemperatureReadingList.as_view(), name='temperature-list'),
    path('temperatures/<int:pk>/', TemperatureReadingDetail.as_view(), name='temperature-detail'),
    path('temperatures/create/', TemperatureCreateAPIView.as_view(), name='temperature-create'),
    path('latest-temperature/', LatestTemperatureAPIView.as_view(), name='latest-temperature'),
    path('', temperature_monitor, name='temperature-monitor'),
]
