from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AboutUs(models.Model):
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    logo = models.ImageField(upload_to='images/logo', verbose_name='Upload logo')
    slogan = models.CharField(max_length=255, verbose_name='Slogan on about us page')
    about_text = models.TextField(verbose_name='Text about us')
    development_icon = models.ImageField(upload_to='images/icons', verbose_name='Icon for development')
    development_text = models.TextField(verbose_name='Development text')
    branding_icon = models.ImageField(upload_to='images/icons', verbose_name='Icon for branding')
    branding_text = models.TextField(verbose_name='Branding text')
    art_icon = models.ImageField(upload_to='images/icons', verbose_name='Icon for art direction')
    art_text = models.TextField(verbose_name='Text for art direction')