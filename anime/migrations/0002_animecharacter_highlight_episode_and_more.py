# Generated by Django 5.0.7 on 2024-08-20 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animecharacter',
            name='highlight_episode',
            field=models.CharField(default='https://www.youtube.com/watch?v=KfznTm8mJA4', max_length=150),
        ),
        migrations.AddField(
            model_name='animecharacter',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
