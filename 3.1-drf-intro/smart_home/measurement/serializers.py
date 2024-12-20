from rest_framework import serializers
from measurement.models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'image', 'sensors']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
