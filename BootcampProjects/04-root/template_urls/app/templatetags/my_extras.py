from django import template

register = template.Library()

def snip_it(value,arg):
    """
    snips out arg from the string value
    """
    return value.replace(arg,'')

register.filter('snip_it',snip_it)