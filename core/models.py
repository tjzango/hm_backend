from django.db import models
from django.utils import timezone

# Create your models here.
class LandingContent(models.Model):
    landing_image = models.ImageField(upload_to='landing/landing/')
    spoken_Landing = models.ImageField(upload_to='landing/spokenlanding/')
    memorable_quote = models.CharField(max_length=255)

class PressReleaseContent(models.Model):
    landing_image = models.ImageField(upload_to='press/release')
    content = models.CharField(max_length=255)

class SpeechContent(models.Model):
    landing_image = models.ImageField(upload_to='speech/content/')
    content = models.CharField(max_length=255)


class WriteUpContent(models.Model):
    landing_image = models.ImageField(upload_to='speech/writeup')
    content = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

class VideoSection(models.Model):
    landing = models.ForeignKey('LandingContent', on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=100)
    video_path = models.URLField()
    date = models.DateField(default=timezone.now)


class MinistryBrand(models.Model):
    name = models.CharField(max_length=100)
    image_path = models.ImageField(upload_to='brands/')

class PhotoGallery(models.Model):
    landing = models.ForeignKey('LandingContent', on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Publication(models.Model):
    CATEGORY_CHOICES = (
        ('speech', 'Speech'),
        ('release', 'Release'),
        ('news', 'News'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    avg_read_time = models.CharField(max_length=50)
    landing_image = models.ImageField(upload_to='publication/landing/')
    main_image = models.ImageField(upload_to='publication/main/')
    text_title = models.CharField(max_length=255)
    content = models.TextField()
    video_link = models.URLField(blank=True, null=True)
    date = models.DateField()

class SpokenWordsCat(models.Model):  # Former 'write-up group'
    name = models.CharField(max_length=100)
    group_image = models.ImageField(upload_to='knowledge/groups/')

class SpokenWord(models.Model):
    spokenwordscategory = models.ForeignKey(SpokenWordsCat, on_delete=models.CASCADE)
    landing_image = models.ImageField(upload_to='knowledge/landing/')
    main_image = models.ImageField(upload_to='knowledge/main/')
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=255)
    content = models.TextField()


class AboutSection(models.Model):
    image = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=255)
    content = models.TextField()


