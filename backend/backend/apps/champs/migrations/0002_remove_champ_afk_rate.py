# Generated by Django 3.0.11 on 2020-11-26 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('champs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='champ',
            name='AFK_rate',
        ),
    ]
