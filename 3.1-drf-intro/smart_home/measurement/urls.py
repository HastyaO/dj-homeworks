from rest_framework import routers

from .views import SensorViewSet, DetailSensorViewSet, MeasurementViewSet

router = routers.DefaultRouter()
router.register('sensors', SensorViewSet)
router.register('sensors', DetailSensorViewSet)
router.register('measurements', MeasurementViewSet)

app_name = "measurement"

urlpatterns = router.urls
