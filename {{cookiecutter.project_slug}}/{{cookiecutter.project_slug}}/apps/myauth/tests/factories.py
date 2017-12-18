import factory
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailAddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmailAddress

    email = factory.Faker('email')


class VerifiedEmailAddressFactory(EmailAddressFactory):
    verified = True


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Faker('user_name')
    email = factory.Faker('email')

    # generate allauth EmailAddress entry that matches the User.email field
    emailaddress_set = factory.RelatedFactory(EmailAddressFactory, 'user',
                                              primary=True,
                                              email=factory.SelfAttribute('..email'))

    @factory.post_generation
    def extra_emails(self, create, count: int):
        if not create:
            # not persisted to db
            return

        if count:
            EmailAddressFactory.create_batch(size=count, user=self)

    @factory.post_generation
    def extra_verified_emails(self, create, count: int):
        if not create:
            # not persisted to db
            return

        if count:
           VerifiedEmailAddressFactory.create_batch(size=count, user=self)


class VerifiedUserFactory(UserFactory):

    # TODO - how can we avoid this duplicated definition?

    # generate allauth EmailAddress entry that matches the User.email field
    emailaddress_set = factory.RelatedFactory(VerifiedEmailAddressFactory, 'user',
                                              primary=True,
                                              email=factory.SelfAttribute('..email'))