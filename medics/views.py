from django.shortcuts import render
from django.db.models import Q
from medics.models import Medic
from medics.forms import MedicForm
from pacients.models import Pacient
from extra.models import Turns
# Create your views here.


def medic_list(request):
    medic = Medic.objects.all()

    context_dict = {
        'medics': medic,
    }

    return render(request, 'medics.html', context_dict)

def create_medic(request):
    if request.method == 'POST':
        medic_form = MedicForm(request.POST)
        if medic_form.is_valid():
            data = medic_form.cleaned_data
            medic = Medic(name=data['name'], surname=data['surname'], medic_type=data['medic_type'])
            medic.save()

            medics = Medic.objects.all()
            context_dict = {
                'medics': medics,
            }
            return render(request, 'medics.html', context_dict)
    
    medic_form = MedicForm(request.POST)
    context_dict = {
        'medic_form': medic_form,
    }
    return render(request, 'medics_form.html', context_dict)


def search(request):
    context_dict = dict()
    if request.GET['medic_search']:
        search_param = request.GET['medic_search']
        query = Q(name__contains=search_param)
        query.add(Q(surname__contains=search_param), Q.OR)
        query.add(Q(medic_type__contains=search_param), Q.OR)
        medics = Medic.objects.filter(query)
        context_dict = {
            'medics': medics
        }
    elif request.GET['pacient_search']:
        search_param = request.GET['pacient_search']
        query = Q(name__contains=search_param)
        query.add(Q(surname__contains=search_param), Q.OR)
        query.add(Q(dni__contains=search_param), Q.OR)
        pacient = Pacient.objects.filter(query)
        context_dict = {
            'pacients': pacient
        }
    elif request.GET['turn_search']:
        search_param = request.GET['turn_search']
        turn = Turns.objects.filter(day__contains=search_param)
        context_dict = {
            'turn': turn
        }

    return render(request, 'home.html', context_dict)