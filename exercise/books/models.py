from django.db import models


class Review(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_id = models.IntegerField()
    review = models.CharField(max_length=255, null=False)
    rate = models.IntegerField()
