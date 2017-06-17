from django import template
from hierarchy.models import PersonModel
from django.template.loader import render_to_string


register = template.Library()

@register.simple_tag
def myappend(ppk):
    parent = PersonModel.objects.get(pk=int(ppk))
    txt = render_to_string('part.html',{'parent':parent})
    return txt