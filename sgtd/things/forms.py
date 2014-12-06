from django import forms

from things.models import Thing

class TextUpdateForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['text']
