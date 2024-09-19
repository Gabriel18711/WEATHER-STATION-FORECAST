from django.urls import path
from .views import TemperatureReadingList, TemperatureReadingDetail, TemperatureCreateAPIView, LatestTemperatureAPIView, temperature_monitor, relay_control_view, get_relay_status

urlpatterns = [
    path('temperatures/', TemperatureReadingList.as_view(), name='temperature-list'),
    path('temperatures/<int:pk>/', TemperatureReadingDetail.as_view(), name='temperature-detail'),
    path('temperatures/create/', TemperatureCreateAPIView.as_view(), name='temperature-create'),
    path('latest-temperature/', LatestTemperatureAPIView.as_view(), name='latest-temperature'),
    path('', temperature_monitor, name='temperature-monitor'),
    path('relay-control/<str:action>/', relay_control_view, name='relay_control'),
    path('getrelaystatus/', get_relay_status, name='get_relay_status'),
]
