from django import template
register = template.Library()
@register.simple_tag
def alias(obj):
    """
    Alias Tag
    """
    return obj