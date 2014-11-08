from rest_framework import viewsets
from rest_framework.permissions import AllowAny

import models
import serializers


class UserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
 
    def get_permissions(self):
        if self.request.method == 'POST':
            return (AllowAny(),)
        else:
            return (AllowAny(),)# permissions.IsStaffOrTargetUser(),)


class AttractionView(viewsets.ModelViewSet):
    # serializer_class = serializers.AtSerializer
    queryset = models.Attraction.objects.all()

    def get_permissions(self):
        return AllowAny()


class ChoiceView(viewsets.ModelViewSet):
    serializer_class = serializers.ChoiceSerializer
    queryset = models.Choice.objects.all()

    def get_permissions(self):
        return (AllowAny(),)

    # @staticmethod
    # def choices_page(chooser_id=None):
    #     return models.Choice.objects.all(chooser=chooser_id)