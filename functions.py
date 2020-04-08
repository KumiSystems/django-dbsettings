from dbsettings.models import Setting

def getValue(key, default=None):
    try:
        return Setting.objects.get(key=key).value
    except:
        if default is None:
            raise KeyError("No such setting: %s" % key)
        else:
            return default

def setValue(key, value):
    obj = Setting.objects.get_or_create(key=key)[0] # pylint: disable=E1101
    obj.value = value
    obj.save()
    return True

