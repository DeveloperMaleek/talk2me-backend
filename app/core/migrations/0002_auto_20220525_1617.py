# Generated by Django 3.2.13 on 2022-05-25 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talk2meuser',
            name='anonymous_profile_image_url',
        ),
        migrations.DeleteModel(
            name='UserAnonymousDisplayImage',
        ),
    ]
