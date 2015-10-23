from django import forms

from things.models import Context, Thing

class TextUpdateForm(forms.ModelForm):
    context = forms.ModelChoiceField(
                Context.objects.all(),
                empty_label='Select Context:',
                required=False)

    class Meta:
        model = Thing
        fields = ['text', 'context']
