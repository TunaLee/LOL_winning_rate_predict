# Django
from django.contrib import admin
from django.db import models
from django.forms import Textarea


# Apps
from .models import Champ
#
# @admin.register(ChampRole)
# class ChampRoleAdmin(admin.ModelAdmin):
#     list_display = ('title',)
#     formfield_overrides = {models.TextField: {'widget': Textarea(attrs={'rows': 1, 'style': 'width: 70%;'})}, }


@admin.register(Champ)
class ChampAdmin(admin.ModelAdmin):
    list_display = ('name','blue_WR','red_WR','more_50_WR',)
    formfield_overrides = {models.TextField: {'widget': Textarea(attrs={'rows': 1, 'style': 'width: 70%;'})}, }

