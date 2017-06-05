# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from polls.models import Question
from polls.models import Choice

from django.contrib import admin

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)