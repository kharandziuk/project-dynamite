from django.core.urlresolvers import reverse
from django_webtest import WebTest

from .. import models, factories


class AttractionsEndpointTestCase(WebTest):
    def create_attraction(self, name='DefaultName'):
        attraction = factories.AttractionFactory.build()
        attraction.name = name
        assert attraction.pk is None
        response = self.app.post(
            reverse('api-v2:attractions'),
            params={
                'name': attraction.name,
                'description': attraction.description,
            },
            xhr=True,
        )
        self.assertEqual(201, response.status_code)
        return attraction

    def test_create_attractions(self):
        attraction = self.create_attraction("Hello")
        attraction = models.Attraction.objects.get(name=attraction.name)
        self.assertIsNotNone(attraction)
        self.assertEqual(attraction.name, "Hello")




