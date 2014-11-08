from django.core.urlresolvers import reverse
from django_webtest import WebTest

from .. import models, factories

from mock import call, patch


class UsersEndpointTestCase(WebTest):

    @patch('users.serializers.requests')
    def test_can_sign_up(self, mock_requests):
        data_for_mock = {
            "id": "737522959636397", 
            "first_name": "Max", 
            "gender": "male", 
            "last_name": "Kharandziuk", 
            "link": "https://www.facebook.com/app_scoped_user_id/737522959636397/", 
            "locale": "en_GB", 
            "name": "Max Kharandziuk", 
            "timezone": 2, 
            "updated_time": "2014-04-16T16:18:23+0000", 
            "verified": True
        }

        mock_requests.get.return_value.status_code = 200
        mock_requests.get.return_value.json = lambda: data_for_mock

        response = self.app.post(
            reverse('api-v1:users'),
            params={
                'fb_access_token': '#token',
            },
            xhr=True,
        )
        self.assertEqual(201, response.status_code)
        user = models.User.objects.get(fb_access_token='#token')
        self.assertIsNotNone(user)

    #def test_user_can_get_and_use_token(self):
    #    user = factories.UserFactory()
    #    response = self.app.post(
    #        reverse('api-v1:login'),
    #        params={
    #            'username': user.username,
    #            'password': factories.USER_PASSWORD,
    #        },
    #        xhr=True,
    #    )
    #    token = response.json['token']
    #    response = self.app.get(
    #        reverse('api-v1:users'),
    #        #extra_environ={u'Authorization:': u'JWT {}'.format(token)},
    #        headers={u'Authorization': 'JWT {}'.format(token)},
    #        #user = user.username
    #    )
    #    self.assertEqual(response.status_code, 200)
    #    assert False
