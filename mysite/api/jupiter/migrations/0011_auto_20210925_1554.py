# Generated by Django 3.2.7 on 2021-09-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jupiter', '0010_alter_characterkill_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentperk',
            name='source',
        ),
        migrations.AddField(
            model_name='characterequipment',
            name='mod_code',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
