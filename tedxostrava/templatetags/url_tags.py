from django import template

register = template.Library()

@register.simple_tag
def get_url():
    return request.get_absolute_url()