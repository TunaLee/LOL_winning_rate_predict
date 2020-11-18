from django.db import models

# Create your models here.
class ChampRole(models.Model):

    #Basic
    title = models.TextField(blank=True, bull=True, verbose_name='챔피언 군 이름')
    def __str__(self):
        return '%s' % (self.title,)

class Champ(models.Model):

    #Basic
    name = models.TextField(blank=True, null=True, verbose_name='챔피언 이름')
    number = models.IntegerField(blank=True, null=True, verbose_name='챔피언 번호')
    blue_WR = models.FloatField(blank=True, null=True, verbose_name='블루팀 승률')
    red_WR = models.FloatField(blank=True, null=True, verbose_name='레드팀 승률')
    more_50_WR = models.FloatField(blank=True, null=True, verbose_name='50판 이상 승률')
    AFK_rate = models.FloatField(blank=True, null=True, verbose_name='탈주자 정도')
    champ_role = models.ForeignKey(ChampRole, blank=True, null=True, verbose_name='챔피언 군 이름',on_delete=models.CASCADE, related_name='champ_role')
    def __str__(self):
        return '%s' % (self.name,)

