from django.shortcuts import render

from extra.models import Turns
from extra.forms import TurnsForm
# Create your views here.

def turns_list(request):
    turn = Turns.objects.all()

    context_dict = {
        'turn': turn,
    }
    return render(request, 'turns.html', context_dict)

def create_turns(request):
    if request.method == 'POST':
        turn_form = TurnsForm(request.POST)
        if turn_form.is_valid():
            data = turn_form.cleaned_data
            turn = Turns(day=data['day'])
            turn.save()

            turns = Turns.objects.all()
            context_dict= {
                'turn': turns
            }
            return render(request, 'turns.html', context_dict)
    
    turn_form = TurnsForm(request.POST)
    context_dict = {
        'turn_form': turn_form,
    }
    return render(request, 'turns_form.html', context_dict)

