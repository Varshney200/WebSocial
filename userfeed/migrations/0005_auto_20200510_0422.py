# Generated by Django 3.1.dev20191223111756 on 2020-05-09 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userfeed', '0004_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='diplayPicture',
        ),
        migrations.AddField(
            model_name='profile',
            name='displayPicture',
            field=models.ImageField(default='default/default-user-icon.jpg', upload_to='Profiles'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='Posts'),
        ),
    ]
