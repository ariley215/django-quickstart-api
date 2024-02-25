from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # Modify the groups field
    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        related_name="customuser_groups",  # Add a related_name
        related_query_name="group",
    )

    # Modify the user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        related_name="customuser_permissions",  # Add a related_name
        related_query_name="permission",
    )

    def __str__(self):
        return self.username
