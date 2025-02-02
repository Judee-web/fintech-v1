from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from apps.users.models import User

# Create your models here.
# Wallet Model
class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Wallet {self.id} for {self.user.email}"