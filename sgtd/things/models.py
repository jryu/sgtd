from django.db import models


class Project(models.Model):
    text = models.CharField(max_length=128)
    datetime_update = models.DateTimeField(auto_now=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text


class Thing(models.Model):
    STUFF = 's'
    ACTION = 'a'
    WAITING = 'w'
    MAYBE = 'm'

    CATEGORY_CHOICES = (
        (STUFF, 'Stuff'),
        (ACTION, 'Action'),
        (WAITING, 'Waiting for'),
        (MAYBE, 'Maybe / Someday'),
    )

    text = models.CharField(max_length=128)
    datetime_update = models.DateTimeField(auto_now=True)
    datetime_create = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES,
            default=STUFF)
    project = models.ForeignKey(Project, null=True, blank=True)

    def __unicode__(self):
        return self.text
