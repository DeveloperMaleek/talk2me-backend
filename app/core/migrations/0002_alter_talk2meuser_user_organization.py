# Generated by Django 3.2.13 on 2022-06-04 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk2meuser',
            name='user_organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.organization'),
        ),
    ]