# Generated by Django 5.1.3 on 2024-12-17 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodBoard', '0007_alter_fboard_btime'),
        ('member', '0003_remove_member_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='star',
            name='fboard',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='star_fboard', to='foodBoard.fboard'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='star',
            name='star',
        ),
        migrations.AddField(
            model_name='star',
            name='star',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='star_member', to='member.member'),
            preserve_default=False,
        ),
    ]
