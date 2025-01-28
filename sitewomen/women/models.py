from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        ordering = ('-created_at',)
        indexes = (models.Index(fields=('-created_at',)),)


class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)