from rest_framework import viewsets
from rest_framework.permissions import AllowAny

import models
import serializers


class AttractionView(viewsets.ModelViewSet):
    serializer_class = serializers.AttractionSerializer
    queryset = models.Attraction.objects.all()

    def get_permissions(self):
        return AllowAny(),