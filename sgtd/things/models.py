from django.db import models

class Thing(models.Model):
    STUFF = 's'
    ACTION = 'a'
    MAYBE = 'm'

    CATEGORY_CHOICES = (
        (STUFF, 'Stuff'),
        (ACTION, 'Action'),
        (MAYBE, 'Maybe / Someday'),
    )

    text = models.CharField(max_length=128)
    datetime_update = models.DateTimeField(auto_now=True)
    datetime_create = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES,
            default=STUFF)

    def __unicode__(self):
        return self.text
