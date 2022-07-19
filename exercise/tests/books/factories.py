import factory
from books.models import Review


class ReviewFactory(factory.django.DjangoModelFactory):
    review = factory.Faker("paragraphs")
    rate = factory.Iterator(range(5))

    class Meta:
        model = Review
