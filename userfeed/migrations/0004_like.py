# Generated by Django 3.1.dev20191223111756 on 2020-05-09 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userfeed', '0003_auto_20200509_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userfeed.Post')),
                ('user', models.ManyToManyField(related_name='likingUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
