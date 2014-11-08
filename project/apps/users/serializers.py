from django.contrib.auth.models import User

from rest_framework import serializers

import requests

from . import models
 
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('fb_access_token',)
        write_only_fields = ('fb_access_token',)
 
    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).restore_object(attrs, instance)
        #user.set_password(attrs['password'])
        return user
    
    # I receive a token
    # I make a request to facebook api
    # if user is defined then get a user id
    def validate(self, attrs):#*args, **kwargs):
        return data


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('title', 'body')
