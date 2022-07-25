from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils.translation import gettext_lazy as _


class BaseUserManager(BaseUserManager):
    def create_user(
        self, email, username, password, first_name, last_name, **other_fields
    ):
        if not email:
            raise ValueError(_("Please provide an email"))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            **other_fields,
        )
        user.set_password(password)
        user.first_name = first_name.capitalize()
        user.last_name = last_name.capitalize()
        user.save(using=self._db)  # saving to 'default' db
        return user

    def create_superuser(
        self, email, username, password, first_name, last_name, **other_fields
    ):
        user = self.create_user(email, username, password, first_name, last_name)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class BaseUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    posts = models.ManyToManyField("posts.Post")  # avoiding circular import
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    objects = BaseUserManager()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Id: {self.pk} - user: {self.username}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
