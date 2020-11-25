from django.contrib import admin
from django.db import models
from django.forms import Textarea

# Apps
from .models import InputData, SummonerData

@admin.register(InputData)
class ChampRoleAdmin(admin.ModelAdmin):
    list_display = ('our_top_champ','our_jungle_champ','our_middle_champ','our_carry_champ','our_support_champ','our_top_summoner','our_jungle_summoner','our_middle_summoner','our_carry_summoner','our_support_summoner','counter_top_champ','counter_jungle_champ','counter_middle_champ','counter_carry_champ','counter_support_champ',)
    formfield_overrides = {models.TextField: {'widget': Textarea(attrs={'rows': 1, 'style': 'width: 70%;'})}, }


@admin.register(SummonerData)
class SummonerAdmin(admin.ModelAdmin):
    list_display = ('summoner1',)
    formfield_overrides = {models.TextField: {'widget': Textarea(attrs={'rows': 1, 'style': 'width: 70%;'})}, }
