# Generated by Django 5.1.4 on 2024-12-13 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FoodCafe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='delMember',
            fields=[
                ('dNo', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=50)),
                ('dDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('birth', models.DateField(null=True)),
                ('email', models.EmailField(max_length=100)),
                ('tel', models.CharField(max_length=20)),
                ('addr', models.CharField(max_length=200)),
                ('mDate', models.DateTimeField(auto_now_add=True)),
                ('point', models.IntegerField(default=0)),
                ('agree1', models.DateTimeField(auto_now_add=True)),
                ('agree2', models.DateTimeField(auto_now_add=True)),
                ('verification_email', models.EmailField(max_length=254)),
                ('verification_code', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('rNo', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('rDate', models.DateTimeField(auto_now=True)),
                ('cafe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='FoodCafe.cafe')),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='FoodCafe.food')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('rNo', models.AutoField(primary_key=True, serialize=False)),
                ('resPeople', models.IntegerField(default=0)),
                ('resMemo', models.TextField(default='', max_length=2000)),
                ('rDate', models.DateTimeField(auto_now=True)),
                ('res', models.ManyToManyField(default='', related_name='res_members', to='member.member')),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('sNo', models.AutoField(primary_key=True, serialize=False)),
                ('sDate', models.DateTimeField(auto_now=True)),
                ('star', models.ManyToManyField(default='', related_name='star_members', to='member.member')),
            ],
        ),
    ]