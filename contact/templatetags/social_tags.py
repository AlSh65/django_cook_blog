from django import template
from contact.models import Socials, About


register = template.Library()


@register.simple_tag()
def get_social_links():
    return Socials.objects.all()


@register.simple_tag()
def get_about():
    return About.objects.last()