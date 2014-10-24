from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext

from base_model import BaseModel


class User(AbstractBaseUser, BaseModel):
    username = models.CharField(
        ugettext('Username'), max_length=255,
        db_index=True, unique=True
    )
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'users'
                     
    #email = models.EmailField(
    #    _('Email'), max_length=255, db_index=True,
    #    blank=True, null=True
    #)
