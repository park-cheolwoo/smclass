# Generated by Django 5.1.4 on 2025-01-01 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0006_remove_rating_cafe_remove_rating_food_rating_fboard_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminUser',
            fields=[
                ('aNo', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=50)),
                ('pw', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('authority', models.IntegerField()),
                ('mDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('sNo', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.CharField(max_length=200)),
                ('where', models.CharField(max_length=200)),
                ('sDate', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
        ),
    ]