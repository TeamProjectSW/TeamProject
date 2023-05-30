from django.db import models
from django.contrib.auth.models import (
   BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
   def create_user(self, user_id, password, nick_name, email, phone_num):
       if not email:
           raise ValueError('이메일은 필수입니다.')


       user = self.model(
           user_id = user_id,
           nick_name = nick_name,
           email = email,
           phone_num = phone_num)

       user.set_password(password)
       user.save(using=self._db)
       return user

   def create_superuser(self, user_id, password, nick_name=None, email=None, phone_num=None):
       user = self.create_user(user_id, password, nick_name, email, phone_num)
       user.is_admin = True
       user.save(using=self._db)
       return user

class User(AbstractBaseUser):
   user_id = models.CharField(max_length=18 , verbose_name='아이디', unique=True)
   nick_name = models.CharField(max_length=10, verbose_name='닉네임', null=True)
   email = models.EmailField(verbose_name='이메일', max_length=128, unique=True, null=True)
   phone_num = models.IntegerField(verbose_name='전화번호', null=True)
   is_active = models.BooleanField(default=True)
   is_admin = models.BooleanField(default=False)

   objects = UserManager()

   USERNAME_FIELD = 'user_id'
   REQUIRED_FIELDS = ['email']

   def __str__(self):
       return self.email

   def has_perm(self, perm, obj=None):
       return True

   def has_module_perms(self, app_label):
       return True

   @property
   def is_staff(self):
       return self.is_admin
