# Generated by Django 5.1.3 on 2024-12-02 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodBoard', '0002_alter_board_f_bhit_alter_board_f_blike'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Board_f',
            new_name='fBoard',
        ),
    ]