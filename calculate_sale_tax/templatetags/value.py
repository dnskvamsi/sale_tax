from django import template

register = template.Library()


@register.filter(name="value")
def value(dictonary, key):
    return dictonary[key]
