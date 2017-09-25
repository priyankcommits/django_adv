# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from web.models import Country

from reversion.admin import VersionAdmin


# Register your models here.
@admin.register(Country)
class CountryAdmin(VersionAdmin):
    pass
