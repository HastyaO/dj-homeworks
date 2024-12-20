from rest_framework import viewsets, mixins
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class DetailSensorViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Sensor.objects.prefetch_related('measurements')
    serializer_class = SensorDetailSerializer


class MeasurementViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
