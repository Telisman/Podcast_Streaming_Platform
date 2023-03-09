# Generated by Django 4.1.7 on 2023-02-28 17:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("podcast_user", "0002_podcastuser_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="podcastuser",
            name="followers",
            field=models.ManyToManyField(
                blank=True, related_name="following", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
