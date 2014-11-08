from django.contrib.auth import get_user_model


class FbBackend( object):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """

    def authenticate(self, fb_access_token):
        assert False
        UserModel = get_user_model()
        try:
            user, _ = UserModel._default_manager.get_or_create(username=username)
            return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            user = UserModel._default_manager.get(pk=user_id)
            return user
        except UserModel.DoesNotExist:
            return None
~

class JSONWebTokenSerializer(serializers.Serializer):
    """
    Serializer class used to validate a username and password.

    'username' is identified by the custom UserModel.USERNAME_FIELD.

    Returns a JSON Web Token that can be used to authenticate later calls.
    """

    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        """Dynamically add the USERNAME_FIELD to self.fields."""
        super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField()

    @property
    def username_field(self):
        User = utils.get_user_model()

        try:
            return User.USERNAME_FIELD
        except AttributeError:
            return 'username'

    def validate(self, attrs):
        credentials = {self.username_field: attrs.get(self.username_field),
                       'password': attrs.get('password')}
        if all(credentials.values()):
            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)

                # Include original issued at time for a brand new token,
                # to allow token refresh
                if api_settings.JWT_ALLOW_REFRESH:
                    payload['orig_iat'] = timegm(
                        datetime.utcnow().utctimetuple()
                    )

                return {
                    'token': jwt_encode_handler(payload)
                }
            else:
                msg = 'Unable to login with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "username" and "password"'
            raise serializers.ValidationError(msg)
