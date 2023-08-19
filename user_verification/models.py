from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number field must be set')
        
        user = self.model(phone_number=phone_number, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=20, unique=True)
    my_invite_code = models.ForeignKey('InviteCode', on_delete=models.SET_NULL, related_name='my_invite', null=True, blank=True)
    friend_invite_code = models.ForeignKey('InviteCode', on_delete=models.SET_NULL, related_name='friend_invite', null=True, blank=True)
    is_verified = models.BooleanField(default=False) 

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    # Add related_name arguments to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',  # Added related_name
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',  # Added related_name
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.phone_number
    


class InviteCode(models.Model):
    invite_code = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.invite_code


