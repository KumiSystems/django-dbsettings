# django-dbsettings

dbsettings is a simple reusable Django app allowing you to store key-value
pairs in your database, so you can store configuation in your database easily.

## Quick start

1. Add "dbsettings" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Run ``python manage.py makemigrations`` and ``python manage.py migrate`` to
   create the polls models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to add configuration values or use dbsettings.functions.setValue(key, value)
   in your code.

4. To retrieve a configuration value from the database, use
   dbsettings.functions.getValue(key) in your code.