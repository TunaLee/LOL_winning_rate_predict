# Generated by Django 3.1.3 on 2020-12-02 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('champs', '0002_remove_champ_afk_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champ',
            name='champ_role',
        ),
        migrations.DeleteModel(
            name='ChampRole',
        ),
    ]
