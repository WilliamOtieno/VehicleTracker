from rest_framework import viewsets
from .serializers import LocationSerializer
from .models import Location


# Create your views here.


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('time_created')
    serializer_class = LocationSerializer
