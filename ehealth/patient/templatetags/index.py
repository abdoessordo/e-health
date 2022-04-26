from django import template
register = template.Library()

@register.filter(name="index")
def index(l, i):
    return l[i]
