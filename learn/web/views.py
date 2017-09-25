# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.shortcuts import render
from django.shortcuts import HttpResponse

from web.models import Country

import reversion
# Create your views here.


def paper_trail_example(request):
    with reversion.create_revision():
        country = Country.objects.first()
        country.name = str(datetime.now())
        country.save()
    return HttpResponse("hello")
