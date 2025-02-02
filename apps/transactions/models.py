from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from apps.users.models import User
from apps.wallets.models import Wallet

# Create your models here.
# Transaction Model
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal'), ('Transfer', 'Transfer')])
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Successful', 'Successful'), ('Failed', 'Failed')])
    reference_id = models.CharField(max_length=255, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} for {self.wallet.user.email}"
