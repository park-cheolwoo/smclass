# Generated by Django 5.1.3 on 2024-11-25 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_alter_member_mdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mdate',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 25, 18, 18, 54, 220342)),
        ),
    ]
