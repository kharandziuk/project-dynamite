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
    email = models.EmailField(
        ugettext('Email'), max_length=255, db_index=True,
        blank=True, null=True
    )
    # is_active = models.BooleanField(default=True)
    gender = models.BooleanField(default=True)

    #TODO implement photo
    # photo = models.ImageField()

    lucky = models.BooleanField(default=False)
    group_id = models.IntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('password',)

    class Meta:
        app_label = 'users'


class ChoiceManager(models.Manager):
    def create_choice(self, chooser, chosen):
        """
        Creates and saves a Choice with the given username and password.
        """
        choice = self.create(choser=chooser, chosen=chosen)
        choice.save(using=self._db)
        return choice


class Choice(models.Model):
    chooser = models.ForeignKey(User, default=None)
    chosen = models.ForeignKey(User, default=None)
    objects = ChoiceManager()

    class Meta:
        app_label = 'choice_options'
        db_table = 'choice_options'


class Attraction(BaseModel):
    name = models.TextField()
    description = models.TextField()
    # TODO Implement photo
    # photo = models.ImageField()
    link = models.URLField()

    class Meta:
        app_label = 'attractions'


class Event(BaseModel):
    female = models.ForeignKey(User)
    male = models.ForeignKey(User)
    date = models.DateTimeField()
    attraction = models.ForeignKey(Attraction)

    class Meta:
        app_label = 'events'


class AttractionManager(models.Manager):
    def create_attraction(self, name, description):
        """
        Creates and saves a User with the given username and password.
        """
        attraction = self.create(name=name, description=description)
        attraction.save(using=self._db)
        return attraction