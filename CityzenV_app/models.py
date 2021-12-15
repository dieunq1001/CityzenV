from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class CongDan(models.Model):
    id = models.AutoField(primary_key=True)
    identity_id = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{1,10}$')])
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


class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (2, "A1"), (3, "A2"), (4, "A3"), (5, "B1"), (6, "B2"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)


class A1(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    home_town = models.TextField()
    objects = models.Manager()


class A2(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    a1_control_id = models.ForeignKey(A1, on_delete=models.DO_NOTHING)
    home_town = models.TextField()
    objects = models.Manager()


class A3(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    a2_control_id = models.ForeignKey(A2, on_delete=models.DO_NOTHING)
    home_town = models.TextField()
    objects = models.Manager()


class B1(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    a3_control_id = models.ForeignKey(A3, on_delete=models.DO_NOTHING)
    home_town = models.TextField()
    objects = models.Manager()


class B2(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    b1_control_id = models.ForeignKey(B1, on_delete=models.DO_NOTHING)
    home_town = models.TextField()
    objects = models.Manager()


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Admin.objects.create(admin=instance)
        if instance.user_type == 2:
            A1.objects.create(admin=instance)
        if instance.user_type == 3:
            A2.objects.create(admin=instance)
        if instance.user_type == 4:
            A3.objects.create(admin=instance)
        if instance.user_type == 5:
            B1.objects.create(admin=instance)
        if instance.user_type == 6:
            B2.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.a1.save()
    if instance.user_type == 3:
        instance.a2.save()
    if instance.user_type == 4:
        instance.a3.save()
    if instance.user_type == 5:
        instance.b1.save()
    if instance.user_type == 6:
        instance.b2.save()
