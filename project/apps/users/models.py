from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils.translation import ugettext


class BaseModel(models.Model):
    # all models should be inheritted from this model
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):

    def create_user(self, username, password):
        """
        Creates and saves a User with the given username and password.
        """
        user = self.create(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, BaseModel):
    username = models.CharField(
        ugettext('Username'), max_length=255,
        db_index=True, unique=True
    )
    fb_id = models.TextField()
    fb_access_token = models.TextField()
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('fb_access_token',)

    class Meta:
        app_label = 'users'


class Post(BaseModel):
    user = models.ForeignKey(User, related_name='posts')
    title = models.CharField(
        ugettext('Username'), max_length=255,
        db_index=True
    )
    body = models.TextField()
    

    class Meta:
        app_label = 'users'
                     
