from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=255, verbose_name='Title of category')

    def __unicode__(self):
        return self.title


class Portfolio(models.Model):
    class Meta:
        verbose_name = 'porfolio'
        verbose_name_plural = 'portfolio'

    title = models.CharField(max_length=255, verbose_name='Title of portfolio')
    category = models.ManyToManyField(Category, verbose_name='Choose one or more than one category of work')
    main_image = models.ImageField(upload_to='images/main_images', verbose_name='Main image for portfolio')
    image_bg = models.CharField(max_length=255, verbose_name='Background of main image', blank=True, null=True)
    text = RichTextUploadingField(verbose_name='global description of work', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class PortfolioElements(models.Model):
    class Meta:
        verbose_name = 'Element'
        verbose_name_plural = 'Elements'

    image = models.ImageField(upload_to='images/elements', verbose_name='Choose image')
    image_title = models.CharField(max_length=255, verbose_name='Image title', null=True, blank=True)
    text = RichTextUploadingField(verbose_name='Description text', null=True, blank=True)
    portfolio = models.ForeignKey(Portfolio, verbose_name='Portfolio')


