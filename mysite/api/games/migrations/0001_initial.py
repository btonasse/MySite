# Generated by Django 3.2.7 on 2021-09-24 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('typ', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('won', models.BooleanField(default=False)),
                ('level', models.IntegerField(default=1)),
                ('turns_survived', models.IntegerField()),
                ('run_time', models.DurationField()),
                ('seed', models.IntegerField()),
                ('points', models.IntegerField()),
                ('difficulty', models.CharField(choices=[('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard'), ('U', 'Ultraviolence'), ('N', 'Nightmare')], max_length=1)),
                ('total_enemies', models.IntegerField()),
                ('awards', models.ManyToManyField(blank=True, to='games.Award')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.IntegerField()),
                ('rarity', models.CharField(max_length=3)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.character')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('typ', models.CharField(choices=[('W', 'Weapon'), ('B', 'Body'), ('H', 'Head'), ('U', 'Utility'), ('R', 'Relic')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Klass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('code', models.CharField(choices=[('M', 'Marine'), ('S', 'Scout'), ('T', 'Technician')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('short_name', models.CharField(max_length=3)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentPerk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[('I', 'Innate'), ('P', 'Power'), ('B', 'Bulk'), ('A', 'Accuracy'), ('C', 'Calibration')], max_length=1)),
                ('level', models.IntegerField(default=1)),
                ('character_equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.characterequipment')),
                ('perk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.perk')),
            ],
            options={
                'order_with_respect_to': 'character_equipment',
                'unique_together': {('character_equipment', 'perk')},
            },
        ),
        migrations.CreateModel(
            name='CharacterTrait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('order', models.IntegerField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.character')),
                ('trait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.trait')),
            ],
            options={
                'order_with_respect_to': 'character',
                'unique_together': {('character', 'order'), ('character', 'trait', 'level')},
            },
        ),
        migrations.CreateModel(
            name='CharacterLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.character')),
                ('event', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.event')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.location')),
            ],
            options={
                'order_with_respect_to': 'character',
                'unique_together': {('character', 'location'), ('character', 'order')},
            },
        ),
        migrations.CreateModel(
            name='CharacterKill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('howmany', models.IntegerField(default=1)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.character')),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.monster')),
            ],
            options={
                'order_with_respect_to': 'character',
                'unique_together': {('character', 'monster')},
            },
        ),
        migrations.CreateModel(
            name='CharacterInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('howmany', models.IntegerField(default=1)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.character')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.item')),
            ],
            options={
                'order_with_respect_to': 'character',
                'unique_together': {('character', 'item')},
            },
        ),
        migrations.AddField(
            model_name='characterequipment',
            name='equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.equipment'),
        ),
        migrations.AddField(
            model_name='characterequipment',
            name='perks',
            field=models.ManyToManyField(blank=True, through='games.EquipmentPerk', to='games.Perk'),
        ),
        migrations.AddField(
            model_name='character',
            name='equipment',
            field=models.ManyToManyField(blank=True, through='games.CharacterEquipment', to='games.Equipment'),
        ),
        migrations.AddField(
            model_name='character',
            name='inventory',
            field=models.ManyToManyField(blank=True, through='games.CharacterInventory', to='games.Item'),
        ),
        migrations.AddField(
            model_name='character',
            name='kills',
            field=models.ManyToManyField(blank=True, through='games.CharacterKill', to='games.Monster'),
        ),
        migrations.AddField(
            model_name='character',
            name='klass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.klass'),
        ),
        migrations.AddField(
            model_name='character',
            name='traits',
            field=models.ManyToManyField(blank=True, through='games.CharacterTrait', to='games.Trait'),
        ),
        migrations.AddField(
            model_name='character',
            name='visited_locations',
            field=models.ManyToManyField(through='games.CharacterLocation', to='games.Location'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='characterequipment',
            order_with_respect_to='character',
        ),
        migrations.AlterUniqueTogether(
            name='characterequipment',
            unique_together={('character', 'slot')},
        ),
    ]