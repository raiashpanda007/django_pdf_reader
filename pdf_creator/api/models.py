from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)
from time import timezone

class CustomUserManager (BaseUserManager):
    def create_user (self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
    
    
class Pdfs(models.Model):
    class Status(models.IntegerChoices):
        PENDING = 0, 'Pending'
        APPROVED = 1, 'Approved'
        REJECTED = 2, 'Rejected'

    user = models.ForeignKey()
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=Status.choices, default=Status.PENDING)
    path = models.CharField(max_length=1024, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
