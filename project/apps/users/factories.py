import factory

import models

PASSWORD = 'super-duper'


class UserFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.User

    username = factory.Sequence(lambda i: "username{}".format(i))
    password = PASSWORD
