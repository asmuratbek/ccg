from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Contacts(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    text = models.TextField(verbose_name='Text on the contact page')
    address = models.CharField(max_length=255, verbose_name='Address')
    email = models.CharField(max_length=255, verbose_name='Email')
    phone = models.CharField(max_length=255, verbose_name='Phone')
    facebook = models.CharField(max_length=255, verbose_name='Facebook page link', null=True, blank=True)
    instagram = models.CharField(max_length=255, verbose_name='Instagram page link', null=True, blank=True)
    behance = models.CharField(max_length=255, verbose_name='Behance page link', null=True, blank=True)
    all_rights_reserved = models.CharField(max_length=255, verbose_name='All rights text, can change', null=True, blank=True)

