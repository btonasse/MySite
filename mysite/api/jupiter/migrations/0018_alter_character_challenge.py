# Generated by Django 3.2.7 on 2021-10-07 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jupiter', '0017_auto_20211007_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='challenge',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='jupiter.challenge'),
        ),
    ]
