# Generated by Django 3.1 on 2020-08-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200807_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='default_picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
