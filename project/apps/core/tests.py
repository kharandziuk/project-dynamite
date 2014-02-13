from django.core.urlresolvers import reverse
from django_webtest import WebTest


class SmokeTest(WebTest):

    def test_can_see_hello(self):
        response = self.app.get(reverse('index'))
        self.assertTemplateUsed(response, 'test.html')
