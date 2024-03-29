import factory
import models


class AttractionsFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.Attraction

    username = factory.Sequence(lambda i: "attraction{}".format(i))
    description = factory.Sequence(lambda i: "description{}".format(i))


    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)


class AttractionFactory(factory.DjangoModelFactory):

    FACTORY_FOR = models.Attraction

    name = factory.Sequence(lambda i: "attraction{}".format(i))
    description = factory.Sequence(lambda i: "description{}".format(i))

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_attraction(*args, **kwargs)
