from django.contrib.auth import get_user_model

UserModel = get_user_model()

class FbBackend( object):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """

    def authenticate(self, fb_access_token):
        assert 'fb_access_token' in attrs
        values = dict(access_token=attrs['fb_access_token'])#social_user.tokens)
        url = 'https://graph.facebook.com/me'
        request = requests.get(url, params=values)
        json = request.json()
        if 'error' in json:
            return None
        fb_id = json[id]
        user = UserModel.get_or_create(
            fb_id=fb_id
        )
        return user
