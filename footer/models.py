from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel
from django.contrib.auth.models import User


class FooterLogoMeta(models.Model):
    image = models.ImageField('Logotip', upload_to='images/FooterLogo/')
    description = models.TextField(' Kompaniya haqida', max_length=300)
    instagram = models.CharField(max_length=100, blank=True)
    telegram = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Logo Meta"
        verbose_name_plural = "Logo Meta"

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    image_tag.short_description = 'Image'


class FooterServicesMeta(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class FooterMenusMeta(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class FooterContactsMeta(models.Model):
    address = models.TextField(max_length=200)
    email = models.TextField(max_length=200)
    phone = models.TextField(max_length=200)

    def __str__(self):
        return self.email
