# Generated by Django 3.2.5 on 2021-07-06 08:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_boardgame_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]