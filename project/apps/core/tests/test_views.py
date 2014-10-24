from django.core.urlresolvers import reverse
from django_webtest import WebTest

from .. import models


class ViewsTestCase(WebTest):

    def test_can_sign_up(self):
        USERNAME = 'super-duper-user'
        response = self.app.post_json(
            reverse('api-v1:sign-up')
            params={
                'username': USERNAME
                'password': '123456'
            }
        )
        self.assertEqual(200, response.status_code)
        user = models.User.get(username=USERNAME)
        self.assertIsNotNone(user)
