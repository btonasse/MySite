# Generated by Django 3.2.7 on 2021-10-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jupiter', '0016_auto_20211003_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='character',
            name='effects',
            field=models.ManyToManyField(blank=True, to='jupiter.Effect'),
        ),
    ]