from django.db import models
from django.core.validators import RegexValidator


class EmailMessage(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, db_index=True)
    email = models.EmailField(max_length=300,
                              validators=[RegexValidator(regex="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.["r"a-zA-Z0-9-.]+$",
                                                         message='please enter the correct format')])
    subject = models.CharField(max_length=100)
    message = models.TextField(null=True)