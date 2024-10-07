from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

User = get_user_model()


class Post(models.Model):
    """게시물 모델"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"


class PostImage(models.Model):
    """게시물 이미지 모델"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="insta/")
    image_1080 = ImageSpecField(
        source="image",
        processors=[ResizeToFill(1080, 1080)],
        format="JPEG",
        options={"quality": 90},
    )

    class Meta:
        ordering = ["post"]

    def __str__(self):
        return f"Image for {self.post.user.username}"


class Comment(models.Model):
    """댓글 모델"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.user.username}'s comment on {self.post}"


class Like(models.Model):
    """좋아요 모델"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "post")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} likes {self.post}"
