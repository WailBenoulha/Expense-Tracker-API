from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profile_pics/',blank=True,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = CustomUserManager()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email
    
class Expenses(models.Model):
    CATEGORIES_CHOICES = [
        ('Groceries','Groceries'),
        ('Leisure','Leisure'),
        ('Electronics','Electronics'),
        ('Utilities','Utilities'),
        ('Clothing','Clothing'),
        ('Health','Health'),
        ('Others','Others'),
    ]
    name = models.CharField(max_length=100,null=True)
    coast = models.FloatField()
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100,choices=CATEGORIES_CHOICES,default='O')
    user = models.ForeignKey('CustomUser',on_delete=models.CASCADE,editable=False)

    def __str__(self):
        return f'{self.user}-{self.coast}-{self.date}'

class Incomes(models.Model):  
    name = models.CharField(max_length=100,null=True)
    coast = models.FloatField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey('CustomUser',on_delete=models.CASCADE,editable=False)
    
    def __str__(self):
        return f'{self.user}-{self.coast}-{self.date}'