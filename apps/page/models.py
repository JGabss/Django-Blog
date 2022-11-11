from django.db import models
import uuid
# Create your models here.
class Page(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )

    text = models.TextField(

    )

    def __str__(self) -> str:
        return self.title