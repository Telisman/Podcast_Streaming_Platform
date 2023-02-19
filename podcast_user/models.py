from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,AbstractUser
from django.core.validators import RegexValidator
from datetime import date


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3)

    def __str__(self):
        return self.country_name
