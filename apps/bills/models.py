from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from apps.users.models import User

# Create your models here.
# Bill Model
class Bill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50, choices=[('Airtime', 'Airtime'), ('Electricity', 'Electricity')])
    provider = models.CharField(max_length=100, choices=[('VTPass', 'VTPass'), ('Quickteller', 'Quickteller')])
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Successful', 'Successful'), ('Failed', 'Failed')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bill Payment for {self.user.email}"
