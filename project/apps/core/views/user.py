from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core import permissions, models, serializers


class UserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    model = models.User
 
    def get_permissions(self):
        # allow non-authenticated user to create via POST
        if self.request.method == 'POST':
            return (AllowAny(),)
        else:
            return permissions.IsStaffOrTargetUser()

