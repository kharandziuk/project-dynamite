from django.db import models


class AttractionManager(models.Manager):
    def create_attraction(self, name, description):
        """
        Creates and saves a Attraction with the given username and password.
        """
        attraction = self.create(name=name, description=description)
        attraction.save(using=self._db)
        return attraction


class Attraction(models.Model):
    name = models.TextField()
    description = models.TextField()
    # TODO Implement photo
    # photo = models.ImageField()
    link = models.URLField(blank=True)
    objects = AttractionManager()

    class Meta:
        app_label = 'attractions'