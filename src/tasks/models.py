from django.conf import settings
from django.db import models


class Task(models.Model):
    class Meta:
        db_table = "tasks"

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    attachment = models.FileField(
        null=True,
        blank=True,
        upload_to= "attachments"
    )

    finished = models.BooleanField(
        default= False
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False
    )
