# Generated by Django 5.1.3 on 2024-12-17 09:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodBoard', '0008_alter_fboard_btime'),
        ('member', '0004_delete_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fboard',
            name='bTime',
            field=models.CharField(choices=[(30, '30분 이내'), (10, '10분 이내'), (120, '2시간 이상'), (60, '1시간 이상'), (0, '바로 입장'), (45, '30분~1시간')], max_length=200),
        ),
        migrations.CreateModel(
            name='fTime',
            fields=[
                ('fNo', models.AutoField(primary_key=True, serialize=False)),
                ('fPeople', models.IntegerField(default=0)),
                ('fTime', models.IntegerField(choices=[(30, '30분 이내'), (10, '10분 이내'), (120, '2시간 이상'), (60, '1시간 이상'), (0, '바로 입장'), (45, '30분~1시간')])),
                ('fDate', models.TimeField()),
                ('fboard', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='fTime_fBoard', to='foodBoard.fboard')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='fTime_member', to='member.member')),
            ],
        ),
    ]
