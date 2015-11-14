# from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import *

from .forms import EventForm

def index(request):
  event_list = Event.objects.order_by('date')
  roomie_list = Roomie.objects.order_by('name')
  chore_list = Chore.objects.order_by('description')
  if hasattr(event_list.filter(chore__description='Bathroom').last(), 'date'):
    last_bath = event_list.filter(chore__description='Bathroom').last().date
  if hasattr(event_list.filter(chore__description='Trash').last(), 'date'):
    last_trash = event_list.filter(chore__description='Trash').last().date
  if hasattr(event_list.filter(chore__description='Kitchen').last(), 'date'):
    last_kitchen = event_list.filter(chore__description='Kitchen').last().date
  if hasattr(event_list.filter(chore__description='Floors').last(), 'date'):
    last_floor = event_list.filter(chore__description='Floors').last().date

  chore_count = {}
  for chore in chore_list:
    for roomie in roomie_list:
      if chore.description in chore_count.keys():
        chore_events = chore_count[chore.description]
        chore_events.append(event_list.filter(chore__description=chore.description).filter(roomie__name=roomie.name).count())
        chore_count[chore.description] = chore_events
      else:
        chore_count[chore.description] = [event_list.filter(chore__description=chore.description).filter(roomie__name=roomie.name).count()]

  roomie_chores = {}
  for roomie in roomie_list:
    roomie_chores[roomie.name] = event_list.filter(roomie__name=roomie.name).count()

  context = {
    'event_list': event_list,
    'roomie_list': roomie_list,
    'chore_list': chore_list,
    'chore_count': chore_count,
    'roomie_chores': roomie_chores,
    'last_bath': datetime.utcfromtimestamp(last_bath),
    'last_trash': last_trash,
    'last_kitchen': last_kitchen,
    'last_floor': last_floor,
  }
  return render(request, 'chores/index.html', context)

def roomie(request):
  roomie_list = Roomie.objects.order_by('name')
  context = {'roomie_list': roomie_list}
  return render(request, 'chores/roomie.html', context)

def chore(request):
  chore_list = Chore.objects.order_by('description')
  context = {'chore_list': chore_list}
  return render(request, 'chores/chore.html', context)

def detail(request, event_id):
  event = get_object_or_404(Event, pk=event_id)
  return render(request, 'chores/detail.html', {'event': roomie})

def results(request, chore_id):
  response = "You're looking at the results of chore %s."
  return HttpResponse(response % chore_id)

def event_new(request):
  if request.method == 'POST':
    form = EventForm(request.POST)
    if form.is_valid():
      event = form.save(commit=False)
      event.save()
      return redirect('/')
  else:
    form = EventForm()
  return render(request, 'chores/event_new.html', {'form': form})
