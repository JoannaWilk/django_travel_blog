from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish_date', 'status')
    list_filter = ('status', 'created_date', 'publish_date', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = "publish_date"
    ordering = ['status', 'publish_date']

# Register your models here.
admin.site.register(Post, PostAdmin)
