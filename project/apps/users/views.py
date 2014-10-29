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


class PostView(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = models.User.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(),)
        else:
            return super(PostView, self).get_permissions()
        

    def pre_save(self, obj):
        obj.user = self.request.user
