# Generated by Django 5.1.4 on 2024-12-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_board_bselect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='bselect',
            field=models.CharField(choices=[('감성카페', '감성카페☕'), ('실시간공유', '실시간공유🗫'), ('취미', '취미🎮'), ('교통', '교통🚗'), ('사건사고', '사건사고😈'), ('웨이팅', '웨이팅👥'), ('추천맛집', '추천맛집😋'), ('기타', '기타🔍'), ('생활/편의', '생활/편의🧼'), ('풍경', '풍경🌴')], max_length=500),
        ),
    ]
