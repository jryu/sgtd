from django import forms

from things.models import Thing

class ActionUpdateForm(forms.ModelForm):
    class Meta:
        exclude = ['category']
        model = Thing
