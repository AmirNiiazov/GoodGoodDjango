from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
