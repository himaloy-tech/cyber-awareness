# Register your models here.
from django.contrib import admin
from .models import Contact, Article, Comment, Video

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'datetime')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('time', )

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', )

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(Contact, ContactAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Comment, CommentAdmin)