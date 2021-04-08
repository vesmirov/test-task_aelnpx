from django.template import Library

register = Library()

@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})
