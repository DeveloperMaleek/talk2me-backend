# Generated by Django 3.2.13 on 2022-05-24 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220523_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk2meuser',
            name='user_emotions',
            field=models.ManyToManyField(default='', to='core.UserEmotions'),
        ),
    ]
