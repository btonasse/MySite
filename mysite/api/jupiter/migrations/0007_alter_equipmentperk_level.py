# Generated by Django 3.2.7 on 2021-09-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jupiter', '0006_alter_characterequipment_rarity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentperk',
            name='level',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]