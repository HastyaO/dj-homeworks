from django.urls import path

from rest_framework import routers

from .views import SensorView, SingleSensorView, MeasurementView

router = routers.DefaultRouter()

app_name = "measurement"

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SingleSensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]