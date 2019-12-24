from django.shortcuts import render
from dbsettings.models import Setting

def getValue(key):
    try:
        return Setting.objects.get(key=key).value
    except:
        raise KeyError("No such setting: %s" % key)

def setValue(key, value):
    obj = Setting.objects.get_or_create(key=key)[0] # pylint: disable=E1101
    obj.value = value
    obj.save()
    return True