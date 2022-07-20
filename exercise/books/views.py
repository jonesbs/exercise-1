from datetime import datetime

from django.db.models import Avg
from rest_framework import status, viewsets
from rest_framework.response import Response

from .client import GutendexClient
from .exceptions import RequestFail
from .models import Review
from .serializers import BookReviewSerializer, BookSerializer, ReviewSerializer


class BookViewset(viewsets.ViewSet):

    serializer_class = BookSerializer
    http_method_names = ["get"]

    def list(self, request):
        try:
            book_list = GutendexClient.search(request.query_params)
            serializer = BookSerializer(book_list["results"], many=True)
            return Response(serializer.data)
        except RequestFail as e:
            return Response(e.content, e.status_code)

    def retrieve(self, request, pk=None):
        try:
            book = GutendexClient.retrieve(pk)
            book["reviews"] = []
            book["rating"] = Review.objects.filter(book_id=book["id"]).aggregate(
                Avg("rate")
            )["rate__avg"]
            reviews = Review.objects.filter(book_id=book["id"]).all()
            if reviews:
                book["reviews"] = reviews

            serializer = BookReviewSerializer(book)
            return Response(serializer.data)
        except RequestFail as e:
            return Response(e.content, e.status_code)


class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ["post"]
