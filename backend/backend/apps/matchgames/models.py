from django.db import models

# Create your models here.


class BlueMatchGame(models.Model):

    # Basic
    game_id = models.IntegerField(blank=True, null=True, verbose_name='게임ID(블루팀)')
    team_id = models.IntegerField(default=100, verbose_name='팀ID(블루팀)')
    champ_WR_dif = models.FloatField(blank=True, null=True, verbose_name='상대팀과의 챔피언 승률 차이')
    user_champ_WR = models.FloatField(blank=True, null=True, verbose_name='유저들의 챔피언 승률 평균')
    tier = models.FloatField(blank=True, null=True, verbose_name='팀 라인 티어 평균')
    our_top = models.IntegerField(blank=True, null=True, verbose_name='우리팀 탑')
    our_jungle = models.IntegerField(blank=True, null=True, verbose_name='우리팀 정글')
    our_middle = models.IntegerField(blank=True, null=True, verbose_name='우리팀 미드')
    our_carry = models.IntegerField(blank=True, null=True, verbose_name='우리팀 원딜')
    our_support = models.IntegerField(blank=True, null=True, verbose_name='우리팀 서포터')
    counter_top = models.IntegerField(blank=True, null=True, verbose_name='상대팀 탑')
    counter_jungle = models.IntegerField(blank=True, null=True, verbose_name='상대팀 정글')
    counter_middle = models.IntegerField(blank=True, null=True, verbose_name='상대팀 미드')
    counter_carry = models.IntegerField(blank=True, null=True, verbose_name='상대팀 원딜')
    counter_support = models.IntegerField(blank=True, null=True, verbose_name='상대팀 서포터')
    win = models.BooleanField(blank=True, null=True, verbose_name='승부 여푸(블루팀)')
    def __str__(self):
        return '%s' % (self.game_id,)

class RedMatchGame(models.Model):

    # Basic
    game_id = models.IntegerField(blank=True, null=True, verbose_name='게임ID(레드팀)')
    team_id = models.IntegerField(default=100, verbose_name='팀ID(레드팀)')
    champ_WR_dif = models.FloatField(blank=True, null=True, verbose_name='상대팀과의 챔피언 승률 차이')
    user_champ_WR = models.FloatField(blank=True, null=True, verbose_name='유저들의 챔피언 승률 평균')
    tier = models.FloatField(blank=True, null=True, verbose_name='팀 라인 티어 평균')
    our_top = models.IntegerField(blank=True, null=True, verbose_name='우리팀 탑')
    our_jungle = models.IntegerField(blank=True, null=True, verbose_name='우리팀 정글')
    our_middle = models.IntegerField(blank=True, null=True, verbose_name='우리팀 미드')
    our_carry = models.IntegerField(blank=True, null=True, verbose_name='우리팀 원딜')
    our_support = models.IntegerField(blank=True, null=True, verbose_name='우리팀 서포터')
    counter_top = models.IntegerField(blank=True, null=True, verbose_name='상대팀 탑')
    counter_jungle = models.IntegerField(blank=True, null=True, verbose_name='상대팀 정글')
    counter_middle = models.IntegerField(blank=True, null=True, verbose_name='상대팀 미드')
    counter_carry = models.IntegerField(blank=True, null=True, verbose_name='상대팀 원딜')
    counter_support = models.IntegerField(blank=True, null=True, verbose_name='상대팀 서포터')
    win = models.BooleanField(blank=True, null=True, verbose_name='승부 여푸(레드팀)')
    def __str__(self):
        return '%s' % (self.game_id,)
