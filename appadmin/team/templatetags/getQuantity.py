from django import template
import ast

register = template.Library()

@register.filter('getQuantity')
def getQuantity(set,id):
    return set.get(branch_id=id).stock