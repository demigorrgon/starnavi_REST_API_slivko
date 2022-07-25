from django.db import models
from users.models import BaseUser


class Post(models.Model):
    title = models.CharField(max_length=128)
    creator = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"id: {self.pk}, title: {self.title} created by: {self.creator.username}"
