# Generated by Django 5.1.3 on 2024-12-17 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_alter_board_bselect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='bselect',
            field=models.CharField(choices=[('풍경', '풍경🌴'), ('기타', '기타🔍'), ('취미', '취미🎮'), ('감성카페', '감성카페☕'), ('사건사고', '사건사고😈'), ('추천맛집', '추천맛집😋'), ('교통', '교통🚗'), ('실시간공유', '실시간공유🗫'), ('웨이팅', '웨이팅👥'), ('생활/편의', '생활/편의🧼')], max_length=500),
        ),
    ]
