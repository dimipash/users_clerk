from django.db import models
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def create_user(self, clerk_user_id, **extra_fields):
        if not clerk_user_id:
            raise ValueError("Clerk ID is required")

        user = self.model(clerk_user_id=clerk_user_id, **extra_fields)
        user.is_active = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    clerk_user_id = models.CharField(max_length=255, unique=True, db_index=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "clerk_user_id"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
