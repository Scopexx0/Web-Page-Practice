from django.shortcuts import render

from pacients.models import Pacient
from pacients.forms import PacientForm
# Create your views here.


def pacient_list(request):
    pacient = Pacient.objects.all()

    context_dict = {
        'pacients': pacient,
    }

    return render(request, 'pacients.html', context_dict)

def create_pacient(request):
    if request.method == 'POST':
        pacient_form = PacientForm(request.POST)
        if pacient_form.is_valid():
            data = pacient_form.cleaned_data
            pacient = Pacient(name=data['name'], surname=data['surname'], dni=data['dni'])
            pacient.save()

            pacient = Pacient.objects.all()
            context_dict = {
                'pacients': pacient,
            }
            return render(request, 'pacients.html', context_dict)
    
    pacient_form = PacientForm(request.POST)
    context_dict = {
        'pacient_form': pacient_form,
    }
    return render(request, 'pacients_form.html', context_dict)