from django import template
from dbsettings.models import Setting

register = template.Library()

@register.simple_tag
def dbsetting(key):
    return Setting.objects.get(key=key).value # pylint: disable=no-member