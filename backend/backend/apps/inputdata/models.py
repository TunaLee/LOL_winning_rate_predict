from django.db import models

# Create your models here.

class InputData(models.Model):

    # Basic
    our_top_champ = models.ForeignKey('champs.Champ', blank=True, null=True, verbose_name='우리팀 탑 챔피언', on_delete=models.CASCADE, related_name='our_top_champs')
    our_jungle_champ = models.ForeignKey('champs.Champ', blank=True, null=True, verbose_name='우리팀 정글 챔피언', on_delete=models.CASCADE, related_name='our_jungle_champs')
    our_middle_champ = models.ForeignKey('champs.Champ', blank=True, null=True, verbose_name='우리팀 미드 챔피언', on_delete=models.CASCADE, related_name='our_middle_champs')
    our_carry_champ = models.ForeignKey('champs.Champ', blank=True, null=True, verbose_name='우리팀 원딜 챔피언', on_delete=models.CASCADE, related_name='our_carry_champ')
    our_support_champ = models.ForeignKey('champs.Champ', blank=True, null=True, verbose_name='우리팀 서포터 챔피언', on_delete=models.CASCADE, related_name='our_support_champs')
    our_top_summoner = models.TextField(blank=True, null=True, verbose_name='우리팀 탑 소환사 이름')
    our_jungle_summoner = models.TextField(blank=True, null=True, verbose_name='우리팀 정글 소환사 이름')
    our_middle_summoner = models.TextField(blank=True, null=True, verbose_name='우리팀 미드 소환사 이름')
    our_carry_summoner = models.TextField(blank=True, null=True, verbose_name='우리팀 원딜 소환사 이름')
    our_support_summoner = models.TextField(blank=True, null=True, verbose_name='우리팀 서포터 소환사 이름')
    counter_top_champ = models.ForeignKey('champs.Champ', blank=True, null=True, verbose_name='상대팀 탑 챔피언', on_delete=models.CASCADE, related_name='counter_top_champs')
    counter_jungle_champ = models.ForeignKey('champs.Champ', blank=True, null=True, verbose_name='상대팀 정글 챔피언', on_delete=models.CASCADE, related_name='counter_jungle_champs')
    counter_middle_champ = models.ForeignKey('champs.Champ', blank=True, null=True, verbose_name='상대팀 미드 챔피언', on_delete=models.CASCADE, related_name='counter_middle_champ')
    counter_carry_champ = models.ForeignKey('champs.Champ', blank=True, null=True, verbose_name='상대팀 원딜 챔피언', on_delete=models.CASCADE, related_name='counter_carry_champ')
    counter_support_champ = models.ForeignKey('champs.Champ', blank=True, null=True, verbose_name='상대팀 서포터 챔피언', on_delete=models.CASCADE, related_name='counter_support_champ')
    team_id = models.IntegerField(blank=True, null=True, verbose_name='팀 ID')

class SummonerData(models.Model):

    #Basic
    summoner1 = models.TextField(blank=True, null=True, verbose_name='입력된 소환사 아이디1')
    summoner2 = models.TextField(blank=True, null=True, verbose_name='입력된 소환사 아이디2')
    summoner3 = models.TextField(blank=True, null=True, verbose_name='입력된 소환사 아이디3')
    summoner4 = models.TextField(blank=True, null=True, verbose_name='입력된 소환사 아이디4')
    summoner5 = models.TextField(blank=True, null=True, verbose_name='입력된 소환사 아이디5')


# class CrawlingData(models.Model):
#
#     # Basic
