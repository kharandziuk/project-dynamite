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


class LoginView(APIView):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    throttle_classes = ()
    permission_classes = ()
    authentication_classes = ()
    parser_classes = (parsers.FormParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = serializers.JSONWebTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            return Response({'token': serializer.object['token']})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

