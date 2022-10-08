from django.contrib import admin
from .models import ContactModel, ContactLink, Socials, About, ImageAbout

class ImageAboutInLine(admin.StackedInline):
    model = ImageAbout
    extra = 1


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'create_at']
    list_display_links = ['id', 'name']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    list_display_links = ['id', 'text']
    inlines = [ImageAboutInLine]


admin.site.register(ContactLink)
admin.site.register(Socials)