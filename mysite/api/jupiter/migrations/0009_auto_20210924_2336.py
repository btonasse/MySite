# Generated by Django 3.2.7 on 2021-09-24 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jupiter', '0008_auto_20210924_2327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='award',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='character',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='equipment',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='klass',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='monster',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='perk',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='trait',
            options={'ordering': ['name']},
        ),
    ]
