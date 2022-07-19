from django.urls import include, path
from rest_framework import routers

from .views import BookViewset, ReviewViewset

router = routers.DefaultRouter()
router.register(r"review", ReviewViewset, basename="review")
router.register(r"books", BookViewset, basename="book")

app_name = "books"
urlpatterns = [
    path("", include(router.urls)),
]
