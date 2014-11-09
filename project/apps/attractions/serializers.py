from rest_framework import serializers

from . import models
 

class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attraction
        fields = ('name', 'description', 'link')
        # write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        user = super(AttractionSerializer, self).restore_object(attrs, instance)
        return user
