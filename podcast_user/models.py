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

class PodcastUser(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30,unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True, unique=True, default='+')
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_join = models.DateField(blank=True, null=True,default=date.today)
    address = models.CharField(max_length=100,blank=True, null=True)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    city_name = models.CharField(max_length=30, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    postal_code = models.CharField(max_length=10,blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(max_length=30,
                              validators=[RegexValidator(regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.["r"a-zA-Z0-9-.]+$",
                                                         message='please enter the correct format')],unique=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','username','country']

    def create_superuser(self, email, password, **extra_fields):
        if self.filter(is_superuser=True).exists():
            raise ValueError('Superuser already exists')
        # set some default values for the superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # create the superuser with the provided email and password
        return self._create_user(email=email, password=password, **extra_fields)

    def __str__(self):
        return f"{self.username} ({self.user_id})"

class UserInfo(models.Model):
    user = models.ForeignKey(PodcastUser, on_delete=models.CASCADE,blank=False, null=False)
    bio = models.TextField()
    language = models.CharField(max_length=25, null=True,blank=True)
    education = models.CharField(max_length=100, null=True,blank=True)
    skills = models.CharField(max_length=25, null=True,blank=True)

    def __str__(self):
        return f"{self.user})"



