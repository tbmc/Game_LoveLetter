# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-02 23:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.IntegerField(choices=[(0, {'name': 'Garde'}), (1, {'name': 'Prêtre'}), (2, {'name': 'Baron'}), (3, {'name': 'Servante'}), (4, {'name': 'Prince'}), (5, {'name': 'Roi'}), (6, {'name': 'Comtesse'}), (7, {'name': 'Princesse'})], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CardPacket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_packet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameLoveLetter.CardPacket')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerInGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameLoveLetter.Game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameLoveLetter.Player')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='card_packet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameLoveLetter.CardPacket'),
        ),
    ]
