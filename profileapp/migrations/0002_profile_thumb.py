# Generated by Django 4.0 on 2021-12-16 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='thumb',
            field=models.ImageField(null=True, upload_to='profile/thumnail/'),
        ),
    ]
