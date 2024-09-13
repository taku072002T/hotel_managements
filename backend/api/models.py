from django.db import models
import uuid

# Create your models here.


class Hotel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default=None)
    prefecture = models.CharField(max_length=20, default=None)
    city = models.CharField(max_length=20, default=None)
    postnumber = models.CharField(max_length=12, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
