# Generated by Django 3.2.7 on 2021-09-24 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_alter_characterequipment_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterequipment',
            name='rarity',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
