from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=str, **extra_fields):
        """Creates and saves a new user"""

        email = self.normalize_email(email)
        password = make_password(password)

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        user = self.model(email=email, password=password, **extra_fields)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=str, **extra_fields):
        """Creates and saves a superuser"""

        email = self.normalize_email(email)
        password = make_password(password)

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.model(email=email, password=password, **extra_fields)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'users'


    email = models.EmailField(max_length=255, unique=True, null=False,blank=False)
    name = models.CharField(max_length=255, null=False,blank=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    # last_login = models.DateTimeField(auto_now=True)


    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

# User.objects.create_user('<EMAIL>', '<PASSWORD>')
