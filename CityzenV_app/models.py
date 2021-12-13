from django.core.validators import RegexValidator
from django.db import models


# Create your models here.

class cong_dan(models.Model):
    id = models.AutoField(primary_key=True)
    identity_id = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    name = models.CharField(max_length=255)
    birth_date = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    home_town = models.TextField()
    permanent_address = models.TextField()
    temporary_address = models.TextField()
    religion = models.CharField(max_length=255)
    educational_level = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    objects = models.Manager()
