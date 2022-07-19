from rest_framework import serializers

from .models import Review


class ReviewBookSerializer(serializers.Serializer):
    def to_representation(self, value):
        return value.review


class AuthorsSerializer(serializers.Serializer):
    name = serializers.CharField()
    birth_year = serializers.IntegerField()
    death_year = serializers.IntegerField()


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    languages = serializers.ListField(child=serializers.CharField())
    authors = AuthorsSerializer(many=True)
    download_count = serializers.IntegerField()


class BookReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    languages = serializers.ListField(child=serializers.CharField())
    authors = AuthorsSerializer(many=True)
    download_count = serializers.IntegerField()
    rating = serializers.DecimalField(max_digits=2, decimal_places=1)
    reviews = ReviewBookSerializer(many=True)


class ReviewSerializer(serializers.ModelSerializer):
    review = serializers.CharField(allow_blank=False)
    rate = serializers.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = Review
        fields = ["book_id", "review", "rate"]
