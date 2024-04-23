from django.contrib import admin

from apps.blog.models import Post, Author


admin.site.register(Post)
admin.site.register(Author)
