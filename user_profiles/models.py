from django.db import models
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=255,
        default='',
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=255,
        default='',
        null=True,
        blank=True
    )
    profile_image = models.ImageField(
        upload_to='profiles/',
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=255,
        default='',
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=255,
        default='',
        null=True,
        blank=True
    )
    city = models.CharField(
        max_length=255,
        default='',
        null=True,
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )

    def __str__(self) -> str:
        return self.first_name
