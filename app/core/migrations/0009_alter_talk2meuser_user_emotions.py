# Generated by Django 3.2.13 on 2022-05-24 03:08

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20220524_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk2meuser',
            name='user_emotions',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Hopeful'), (2, 'Excited'), (3, 'Sad'), (4, 'Anxious'), (5, 'Frustrated'), (6, 'Withdrawn'), (7, 'Stressed'), (8, 'Scared'), (9, 'Lonely'), (10, 'Happy'), (11, 'Indifferent'), (12, 'Angry'), (13, 'No feelings')], default=13, max_length=29),
        ),
    ]
