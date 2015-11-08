from django import forms

from .models import Event

class EventForm(forms.ModelForm):
    comment = forms.CharField(required=False)

    class Meta:
        model = Event
        fields = ('roomie', 'chore', 'comment')
