from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password = None):
        if(not username):
            raise ValueError('User musst have a username')
        

        user = self.model(username  = username)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, username, password):
        user =  self.ccreate_user(username, password)
        user.is_superuser = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primery_key  =True)
    username = model.CharField('Username', max_lenght = 15, unique = True)
    password = models.CharField('Password', max_lenght = 250)
    name = models.CharField('Name', max_lenght = 30)
    email = models.EmailField('Email', max_lenght = 100)

    def save(self, **kwargs):
        