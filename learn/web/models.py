# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import signals
from django.core import serializers


import papertrail
import reversion
# Create your models here.


def update_count(sender, instance, *args, **kwargs):
    count = Count.objects.first()
    count.count = count.count+1
    count.save()


@reversion.register()
class Country(models.Model):
    name = models.CharField(max_length=10000, default="")
    population = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        papertrail.log(
            "Country",
            serializers.serialize("json", [self, ]),
            data=serializers.serialize("json", [self, ])
        )
        super(Country, self).save(*args, **kwargs)


class Count(models.Model):
    count = models.IntegerField(default=0)


signals.post_save.connect(update_count, sender=Country)
