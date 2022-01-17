import email
from operator import imod
from statistics import mode
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,name, password=None):
        """Created a new user profile"""
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_super_user(self,email,name,passowrd):
        """Create super user"""
        user = self.create_super_user(email,name,passowrd)
        user.is_superuser= True
        user.is_staff = True
        return True

        
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """DB Model for users in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
        """Help Django get full name of user"""
        return self.name
    
    def get_short_name(self):
        """Get Short Name"""
        return self.name

    def __str__(self) -> str:
        return f"{self.name} {self.email}"
