from django.contrib import admin
from .models import Post,Team,Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','publish_date')

class PostInline(admin.TabularInline):
    '''Tabular Inline View for Post'''

    model = Post


    
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','created_at')