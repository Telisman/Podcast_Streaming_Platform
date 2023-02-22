# Generated by Django 4.1.7 on 2023-02-22 13:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("podcast_blog", "0003_blogcomment"),
    ]

    operations = [
        migrations.AddField(
            model_name="podcast_blog",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="liked_blogs", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]