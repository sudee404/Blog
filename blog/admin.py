from django.contrib import admin
from .models import Post,Author,Tags,Team
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','publish_date')

class PostInline(admin.TabularInline):
    '''Tabular Inline View for Post'''

    model = Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [PostInline,]
    
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name',)