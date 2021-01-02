from django.db import models
from django.contrib.auth.models import AbstractUser


class Userinfo(models.Model):
    age = models.PositiveIntegerField(null=False, default=20)


class User(AbstractUser):
    userinfo = models.OneToOneField('orm_test.Userinfo', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username

