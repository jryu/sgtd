from django.db import models

class Thing(models.Model):
    text = models.CharField(max_length=128)
    datetime_update = models.DateTimeField(auto_now=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text
