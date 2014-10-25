from rest_framework import viewsets
from rest_framework.permissions import AllowAny

import models
import permissions
import serializers


class UserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
 
    def get_permissions(self):
        if self.request.method == 'POST':
            return (AllowAny(),)
        else:
            return (AllowAny(),)# permissions.IsStaffOrTargetUser(),)

