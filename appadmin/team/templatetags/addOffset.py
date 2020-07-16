from django import template
import ast
from django.conf import settings
from datetime import datetime, timedelta

register = template.Library()

@register.filter('addOffset')
def addOffset(qs,arg):
    offset = settings.OFFSET
    date = qs.created_at + \
           timedelta(hours=int(offset[:2]), minutes=int(offset[2:]))
    return date.strftime("%d %b %Y") + '; ' + date.strftime("%-I:%M %p")