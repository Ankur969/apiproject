
# Register your models here.
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'rated', 'genre')
    search_fields = ('title', 'genre', 'director', 'actors')
