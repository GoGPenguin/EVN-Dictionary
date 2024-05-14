from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime

class UserManager(BaseUserManager):
    def create_user(self, username, fullname, password=None, **extra_fields):
        if not username:
            raise ValueError('The username must be set')
        user = self.model(
            username=username,
            fullname=fullname,
            registered_at=datetime.now(),
            image=None,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(username, None, password, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    fullname = models.CharField(max_length=100, null=True)
    registered_at = models.DateTimeField(auto_now_add=True, null=False)  # Changed to registered_at
    image = models.TextField(null=True)
    is_admin = models.BooleanField(default=False)

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'
