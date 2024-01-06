from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=20, blank=True, null=True)

    def __str__(self):

        return f"{self.name}"

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.name}')
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def get_absolute_url(self):
        return reverse('tag_post', kwargs={'tag_slug': self.slug})

class Post(models.Model):
    post_id = models.PositiveIntegerField(primary_key=True, auto_created=True)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=10000)
    likes = models.IntegerField('lake', default=0, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='tags')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.author} - {self.title} - {self.likes} - {self.post_id}"

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.post_id} - {self.title}')
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)

