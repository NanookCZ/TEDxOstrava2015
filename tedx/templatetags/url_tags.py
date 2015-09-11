from django import template
from django.core.urlresolvers import request 

register = template.Library()

@register.simple_tag
def get_url():
    return request.get_absolute_url()