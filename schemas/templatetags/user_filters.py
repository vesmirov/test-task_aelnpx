from django.template import Library
from django.forms import Select

register = Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def is_select(field):
    return field.field.widget.__class__.__name__ == Select().__class__.__name__
