from django.contrib import admin
from .models import CustomUser, InviteCode

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(InviteCode)
