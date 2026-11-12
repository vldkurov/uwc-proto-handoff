import re
from django import template

register = template.Library()

@register.filter
def is_email(value):
    return bool(re.match(r"^[\w.+-]+@[\w-]+\.[\w.-]+$", value))