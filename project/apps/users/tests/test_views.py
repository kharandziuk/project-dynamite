from django.core.urlresolvers import reverse
from django_webtest import WebTest

from .. import models, factories
from apps.users.models import Choice


class UsersEndpointTestCase(WebTest):

    def create_user(self, gender=True):
        _user = factories.UserFactory.build()
        assert _user.pk == None
        response = self.app.post(
            reverse('api-v1:users'),
            params={
                'username': _user.username,
                'password': factories.USER_PASSWORD,
                'gender': gender
            },
            xhr=True,
        )
        self.assertEqual(201, response.status_code)
        return _user

    def test_can_sign_up(self):
        gender = False

        _user = self.create_user(gender)
        user = models.User.objects.get(username=_user.username)
        self.assertIsNotNone(user)
        self.assertEqual(user.gender, gender)

    def test_get_choise_options(self):
        _user_1 = self.create_user(True)
        _user_2 = self.create_user(False)

        _user_one = models.User.objects.get(username=_user_1.username)
        _user_two = models.User.objects.get(username=_user_2.username)

        Choice(chooser=_user_one, chosen=_user_two)
        self.app.post(
            reverse('api-v1:choice_options'),
            params={
                'chooser': _user_one.pk,
                'chosen': _user_two.pk
            }
        )

        choise = models.Choice.objects.get(chooser=_user_one.pk, choosen=_user_two.pk)
        self.assertIsNotNone(choise)
        #
        # Choice(chooser=_user_one.pk, chosen=_user_two.pk)
        # get_result = self.app.get(reverse('api-v1:choiceOptions'), chooser=_user_one.pk)
        # print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")
        # print(get_result)
        # print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")
        #
        # self.assertIsNotNone(get_result)
