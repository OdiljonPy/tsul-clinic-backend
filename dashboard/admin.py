from django.contrib import admin
from .models import CustomerUser
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomerUser)
class CustomerUserAdmin(admin.ModelAdmin):
    pass
