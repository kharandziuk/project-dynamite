from django.core.urlresolvers import reverse
from django_webtest import WebTest

from .. import models, factories


class ViewsTestCase(WebTest):

    def test_can_sign_up(self):
        _user = factories.UserFactory.build()
        assert _user.pk == None
        response = self.app.post(
            reverse('api-v1:users'),
            params={
                'username': _user.username,
                'password': factories.USER_PASSWORD,
            },
            xhr=True,
        )
        self.assertEqual(201, response.status_code)
        user = models.User.objects.get(username=_user.username)
        self.assertIsNotNone(user)

    def test_user_can_get_and_use_token(self):
        user = factories.UserFactory()
        response = self.app.post(
            reverse('api-v1:login'),
            params={
                'username': user.username,
                'password': factories.USER_PASSWORD,
            },
            xhr=True,
        )
        token = response.json['token']
        response = self.app.get(
            reverse('api-v1:users'),
            #extra_environ={u'Authorization:': u'JWT {}'.format(token)},
            headers={u'Authorization': 'JWT {}'.format(token)},
            #user = user.username
        )
        self.assertEqual(response.status_code, 200)

