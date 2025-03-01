from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class RoleModel(models.Model):
    id = models.AutoField(primary_key=True)

    ROLE_NAME_CHOICES = (
        ('ADMIN', 'ADMIN'),
        ('USER', 'USER'),
    )

    name = models.CharField(
        choices=ROLE_NAME_CHOICES,
        default='USER',
        max_length=10
    )

    class Meta:
        db_table = 'roles'

class UserModel(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.ForeignKey(
        RoleModel,
        on_delete=models.CASCADE,
        related_name='users',
        db_column='role_id'
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'