# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import signals
from django.dispatch import receiver


# Create your models here.
def update_count(sender, instance, *args, **kwargs):
    print("========EASY=========")
    print(sender)
    print(instance)
    print(args)
    print(kwargs)
    print("========EASY AGAIN=======")
    count = Count.objects.first()
    count.count = count.count+1
    count.save()


class Country(models.Model):
    name = models.CharField(max_length=10000, default="")
    population = models.IntegerField(default=0)


class Count(models.Model):
    count = models.IntegerField(default=0)


signals.post_save.connect(update_count, sender=Country)
