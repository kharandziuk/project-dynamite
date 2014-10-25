import factory

import models

USER_PASSWORD = 'super-duper'


class UserFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.User

    username = factory.Sequence(lambda i: "username{}".format(i))
    password = USER_PASSWORD

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)
