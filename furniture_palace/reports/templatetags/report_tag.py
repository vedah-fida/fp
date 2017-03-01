from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(argument_a, argument_b):
    return argument_a * argument_b
