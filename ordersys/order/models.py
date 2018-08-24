# -*-coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
# from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserProfile(AbstractUser):
    # user = models.OneToOneField(User)
    id = models.AutoField(primary_key=True) 
    user_name=models.CharField(max_length=45,verbose_name='用户名',unique=True)
    user_phone=models.CharField(max_length=20,verbose_name='电话')
    # password = models.CharField(max_length=100,verbose_name='密码')
    user_birthday = models.DateField(max_length=40,verbose_name='生日')
    user_height = models.CharField(max_length=20,verbose_name='身高')
    user_weight = models.CharField(max_length=20,verbose_name='体重')
    user_idcard = models.CharField(max_length=20,verbose_name='身份证')
    # user_age=models.CharField(max_length=3,verbose_name='年龄',default="")
    user_sex = models.CharField(max_length = 6,choices=(("male",u"男"),("female",u"女")),verbose_name='性别')
    user_nation = models.CharField(max_length=4,verbose_name='国家')
    user_is_area = models.CharField(max_length=1,verbose_name='地区')
    user_community = models.CharField(max_length=12,verbose_name='社区')
    user_type = models.CharField(max_length=20,verbose_name='类型')
    user_isFirstTabooCheck = models.CharField(max_length=1,verbose_name='')
    user_not_managed = models.CharField(max_length=1,verbose_name='是否为非管理对象')
    user_fill_time = models.DateField(default=datetime.now,verbose_name="注册时间")
    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name 
    def  __unicode__(self):
        return self.username 