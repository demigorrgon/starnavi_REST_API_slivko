from django.contrib import admin
from users.models import BaseUser


@admin.register(BaseUser)
class UserAdmin(admin.ModelAdmin):
    # explicit column specification redundant in this case,
    # but comes in handy if we have a lot of columns that could slow down admin site
    list_display = ("id", "username", "email", "first_name", "last_name")
