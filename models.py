from django.db import models

# Create your models here.

class Setting(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.key
