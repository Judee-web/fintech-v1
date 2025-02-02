from django.contrib import admin

from apps.bills.models import Bill
from apps.transactions.models import Transaction
from apps.wallets.models import Wallet

# Register your models here.
from .models import User

# # Register your models here
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'email', 'phone_number', 'kyc_status', 'created_at', 'updated_at')
#     search_fields = ('email', 'phone_number')
#     list_filter = ('kyc_status',)
#     ordering = ('created_at',)

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'balance', 'currency', 'created_at', 'updated_at')
    search_fields = ('user__email',)
    list_filter = ('currency',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'wallet', 'type', 'amount', 'status', 'timestamp')
    search_fields = ('wallet__user__email',)
    list_filter = ('type', 'status')

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service_type', 'provider', 'amount', 'status', 'created_at')
    search_fields = ('user__email',)
    list_filter = ('service_type', 'status')

admin.site.register(User)
