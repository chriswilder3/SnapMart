from django import template

register = template.Library()

@register.filter(name='times')
def times(number):
    # Changed later to serve 10 option in select tag.
    return range(1, 10 + 1)