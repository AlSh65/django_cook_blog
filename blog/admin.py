from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *


class RecipeInLine(admin.StackedInline):
    model = Recipe
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'create_ad']
    list_display_links = ['id', 'title']
    inlines = [RecipeInLine]
    save_as = True
    save_on_top = True



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'website','create_at', 'post']
    list_display_links = ['id', 'name']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'serves', 'prep_time', 'cook_time', 'post']


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Tag)
