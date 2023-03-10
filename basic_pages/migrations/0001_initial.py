# Generated by Django 4.1.7 on 2023-02-22 12:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmailMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=50)),
                (
                    "email",
                    models.EmailField(
                        max_length=300,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="please enter the correct format",
                                regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$",
                            )
                        ],
                    ),
                ),
                ("subject", models.CharField(max_length=100)),
                ("message", models.TextField(null=True)),
            ],
        ),
    ]
