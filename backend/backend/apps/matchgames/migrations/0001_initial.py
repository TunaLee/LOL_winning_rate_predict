# Generated by Django 3.0.11 on 2020-11-23 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlueMatchGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.IntegerField(blank=True, null=True, verbose_name='게임ID(블루팀)')),
                ('team_id', models.IntegerField(default=100, verbose_name='팀ID(블루팀)')),
                ('champ_WR_dif', models.FloatField(blank=True, null=True, verbose_name='상대팀과의 챔피언 승률 차이')),
                ('user_champ_WR', models.FloatField(blank=True, null=True, verbose_name='유저들의 챔피언 승률 평균')),
                ('tier', models.FloatField(blank=True, null=True, verbose_name='팀 라인 티어 평균')),
                ('our_top', models.IntegerField(blank=True, null=True, verbose_name='우리팀 탑')),
                ('our_jungle', models.IntegerField(blank=True, null=True, verbose_name='우리팀 정글')),
                ('our_middle', models.IntegerField(blank=True, null=True, verbose_name='우리팀 미드')),
                ('our_carry', models.IntegerField(blank=True, null=True, verbose_name='우리팀 원딜')),
                ('our_support', models.IntegerField(blank=True, null=True, verbose_name='우리팀 서포터')),
                ('counter_top', models.IntegerField(blank=True, null=True, verbose_name='상대팀 탑')),
                ('counter_jungle', models.IntegerField(blank=True, null=True, verbose_name='상대팀 정글')),
                ('counter_middle', models.IntegerField(blank=True, null=True, verbose_name='상대팀 미드')),
                ('counter_carry', models.IntegerField(blank=True, null=True, verbose_name='상대팀 원딜')),
                ('counter_support', models.IntegerField(blank=True, null=True, verbose_name='상대팀 서포터')),
                ('win', models.BooleanField(blank=True, null=True, verbose_name='승부 여푸(블루팀)')),
            ],
        ),
        migrations.CreateModel(
            name='RedMatchGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.IntegerField(blank=True, null=True, verbose_name='게임ID(레드팀)')),
                ('team_id', models.IntegerField(default=100, verbose_name='팀ID(레드팀)')),
                ('champ_WR_dif', models.FloatField(blank=True, null=True, verbose_name='상대팀과의 챔피언 승률 차이')),
                ('user_champ_WR', models.FloatField(blank=True, null=True, verbose_name='유저들의 챔피언 승률 평균')),
                ('tier', models.FloatField(blank=True, null=True, verbose_name='팀 라인 티어 평균')),
                ('our_top', models.IntegerField(blank=True, null=True, verbose_name='우리팀 탑')),
                ('our_jungle', models.IntegerField(blank=True, null=True, verbose_name='우리팀 정글')),
                ('our_middle', models.IntegerField(blank=True, null=True, verbose_name='우리팀 미드')),
                ('our_carry', models.IntegerField(blank=True, null=True, verbose_name='우리팀 원딜')),
                ('our_support', models.IntegerField(blank=True, null=True, verbose_name='우리팀 서포터')),
                ('counter_top', models.IntegerField(blank=True, null=True, verbose_name='상대팀 탑')),
                ('counter_jungle', models.IntegerField(blank=True, null=True, verbose_name='상대팀 정글')),
                ('counter_middle', models.IntegerField(blank=True, null=True, verbose_name='상대팀 미드')),
                ('counter_carry', models.IntegerField(blank=True, null=True, verbose_name='상대팀 원딜')),
                ('counter_support', models.IntegerField(blank=True, null=True, verbose_name='상대팀 서포터')),
                ('win', models.BooleanField(blank=True, null=True, verbose_name='승부 여푸(레드팀)')),
            ],
        ),
    ]