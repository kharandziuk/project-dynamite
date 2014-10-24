from django.core.urlresolvers import reverse
from django_webtest import WebTest

from .. import models


class ViewsTestCase(WebTest):

    def test_can_sign_up(self):
        USERNAME = 'super-duper-user'
        response = self.app.post(
            reverse('api-v1:users'),
            params={
                'username': USERNAME,
                'password': '123456',
            },
            xhr=True,
        )
        self.assertEqual(201, response.status_code)
        user = models.User.objects.get(username=USERNAME)
        self.assertIsNotNone(user)
