import uuid
from django.utils.text import slugify
from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

class Diary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now=True)
    cover_image = CloudinaryField('image', folder=settings.MEDIA_ROOT + 'diary_cover_images/', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)[:50] + self.created_at.strftime('%Y-%m-%d')
        super(Diary, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['slug', 'user'], name='unique_slug'),
        ]

class DiaryEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('created at', auto_now=True)
    entry = models.TextField()
    diary = models.ForeignKey('Diary', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.created_at)