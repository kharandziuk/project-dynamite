from django.core.urlresolvers import reverse
from django_webtest import WebTest

from .. import models, factories


class UsersEndpointTestCase(WebTest):

    setup_auth = False

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


class PostsEndpointTestCase(WebTest):

    setup_auth = False

    def test_user_creates_post(self):
        user = factories.UserFactory()
        assert user.posts.count() == 0

        response = self.app.post(
            reverse('api-v1:login'),
            params={
                'username': user.username,
                'password': factories.USER_PASSWORD,
            },
            xhr=True,
        )
        token = response.json['token']

        TEXT = 'some text'
        TITLE = 'title'
        response = self.app.post(
            reverse('api-v1:posts'),
            params={
                'title': TITLE,
                'body': TEXT,
            },
            user=user.username,
            headers={u'Authorization': 'JWT {}'.format(token)},
        )
        self.assertEqual(user.posts.count(), 1)

    def test__anonymous__list_of_post(self):
        posts = [factories.PostFactory() for _ in xrange(5)]

        response = self.app.get(
            reverse('api-v1:posts'),
        )
        actual = response.json
        self.assertEqual(len(actual), 5)
        
    

