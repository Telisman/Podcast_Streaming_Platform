# Generated by Django 4.1.7 on 2023-02-19 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("podcast_user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PodcastUser",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("username", models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
