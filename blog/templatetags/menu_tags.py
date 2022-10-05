
from django import template
from blog.models import Category
#
#
register = template.Library()
#
#
# @register.simple_tag()
# def get_categories():
#     """Вывод всех категорий"""
#     return Category.objects.all()
#
#
@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    category = Category.objects.filter(parent__isnull=False).order_by("name")
    return {"list_category": category}