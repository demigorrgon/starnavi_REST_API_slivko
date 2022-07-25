from django.contrib import admin
from posts.models import Post

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # explicit column specification redundant in this case,
    # but comes in handy if we have a lot of columns that could slow down admin site
    list_display = ("id", "title", "creator", "content", "created_at", "updated_at")
