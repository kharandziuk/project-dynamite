from rest_framework import serializers

from . import models
 
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('password', 'username', 'gender')
        write_only_fields = ('password',)
 
    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Choice
        fields = ('chooser', 'chosen')

    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        choice = super(ChoiceSerializer, self).restore_object(attrs, instance)
        choice.chooser = attrs['chooser']
        choice.chosen = attrs['chosen']
        return choice

