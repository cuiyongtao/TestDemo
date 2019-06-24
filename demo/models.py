from django.db import models


# Create your models here.

class UserInfo(models.Model):
    usrename = models.CharField(max_length=32, verbose_name="用户名")
    password = models.CharField(max_length=32, verbose_name="密码")
