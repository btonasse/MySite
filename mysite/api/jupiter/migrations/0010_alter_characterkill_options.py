# Generated by Django 3.2.7 on 2021-09-24 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jupiter', '0009_auto_20210924_2336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characterkill',
            options={'ordering': ['character', 'monster']},
        ),
    ]
