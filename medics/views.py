from django.shortcuts import render
from django.db.models import Q
from medics.models import Medic
from medics.forms import MedicForm
from pacients.models import Pacient
from extra.models import Turns

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


class MedicListView(ListView):
    model = Medic
    template_name = 'medics_list.html'

class MedicDetailView(DetailView):
    model = Medic
    template_name = 'medics_detail.html'

class MedicCreateView(CreateView):
    model = Medic
    template_name = 'medics_form.html'
    success_url = reverse_lazy('medics-list')
    fields = '__all__'

class MedicUpdateView(UpdateView):
    model = Medic
    template_name = 'medics_form.html'
    success_url = reverse_lazy('medics-list')
    fields = '__all__'

class MedicDeleteView(DeleteView):
    model = Medic
    template_name = 'medics_confirm_delete.html'
    success_url = reverse_lazy('medics-list')
    fields = '__all__'



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