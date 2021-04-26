from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#用户信息
class User(AbstractUser):

    #手机号
    #unique 唯一验证
    mobile = models.CharField(max_length=20,unique=True,blank=True)
    #头像信息
    #upload_to  保存到相应的子目录中
    avatar = models.ImageField(upload_to='avatar/%Y%m%d',blank=True)
    #简介信息
    user_desc = models.TextField(max_length=500,blank=True)

    #修改认证的字段为手机号
    USERNAME_FIELD = 'mobile'

    #创建超级管理员必须输入的字段(不包括欧手机号和密码)
    REQUIRED_FIELDS = ['username','email']

    #内部类为class Meta 用于给model定义元数组
    class Meta:
        db_table = 'tb_users' #修改表名
        verbose_name = '用户管理'   #admin 后台显示
        verbose_name_plural = verbose_name  #admin 后台显示

    def __str__(self):
        return self.mobile
