from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=128)
    datetime_update = models.DateTimeField(auto_now=True)
    datetime_create = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text

    class Meta:
        ordering = ['text']


class Log(models.Model):
    datetime_create = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    todo = models.ForeignKey(Todo)

    def __unicode__(self):
        return ' - '.join([
                self.todo.text,
                self.date.strftime("%d/%m/%y"),
                self.datetime_create.isoformat(' ')])
