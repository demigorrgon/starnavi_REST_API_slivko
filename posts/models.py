from django.db import models
from users.models import BaseUser


class Post(models.Model):
    title = models.CharField(max_length=128)
    creator = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        BaseUser, related_name="likes", blank=True, through="Like"
    )

    def __str__(self) -> str:
        return f"id: {self.pk}, title: {self.title} created by: {self.creator.username}"


class Like(models.Model):
    liked_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [["liked_post", "liked_by"]]

    def __str__(self) -> str:
        return f"id: {self.pk}, liked post: {self.liked_post.title} by {self.liked_by.username}"
