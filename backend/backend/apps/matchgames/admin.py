from django.contrib import admin
from django.db import models
from django.forms import Textarea

# Register your models here.

# Apps
from .models import RedMatchGame, BlueMatchGame

@admin.register(RedMatchGame)
class ChampRoleAdmin(admin.ModelAdmin):
    list_display = ('game_id','team_id','champ_WR_dif','user_champ_WR','tier','our_top','our_jungle','our_middle','our_carry','our_support','counter_top','counter_jungle','counter_middle','counter_carry','counter_support','win')
    formfield_overrides = {models.TextField: {'widget': Textarea(attrs={'rows': 1, 'style': 'width: 70%;'})}, }


@admin.register(BlueMatchGame)
class ChampAdmin(admin.ModelAdmin):
    list_display = ('game_id','team_id','champ_WR_dif','user_champ_WR','tier','our_top','our_jungle','our_middle','our_carry','our_support','counter_top','counter_jungle','counter_middle','counter_carry','counter_support','win')
    formfield_overrides = {models.TextField: {'widget': Textarea(attrs={'rows': 1, 'style': 'width: 70%;'})}, }
