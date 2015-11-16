from django import forms

from .models import Event, Roomie, Chore

class EventForm(forms.Form):
  roomie = forms.ModelChoiceField(queryset=Roomie.objects.all(), empty_label='Please Select')
  chore = forms.ModelChoiceField(queryset=Chore.objects.all(), empty_label='Please Select')
  comment = forms.CharField(required=False)

  def save(self):
    data = self.cleaned_data
    event = Event(
      roomie=Roomie.objects.all().filter(name=data['roomie']).first(),
      chore=Chore.objects.all().filter(description=data['chore']).first(),
      comment=data['comment']
    )
    event.save()
