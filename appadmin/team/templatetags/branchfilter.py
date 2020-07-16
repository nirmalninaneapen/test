from django import template
import ast

register = template.Library()

@register.filter('branchfilter')
def branchfilter(list,branchid):
    if list is not None:
        if str(branchid) in list:
            return True
    return False

