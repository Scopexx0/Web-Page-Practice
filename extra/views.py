from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from extra.models import Turns
from extra.forms import TurnsForm
# Create your views here.

class TurnsListView(ListView):
    model = Turns
    template_name = 'turns_list.html'

class TurnsDetailView(DetailView):
    model = Turns
    template_name = 'turns_detail.html'

class TurnsCreateView(CreateView):
    form_class = TurnsForm
    template_name = 'turns_form.html'
    success_url = reverse_lazy('turns-list')

class TurnsUpdateView(UpdateView):
    model = Turns
    template_name = 'turns_form.html'
    success_url = reverse_lazy('turns-list')
    fields = '__all__'

class TurnsDeleteView(DeleteView):
    model = Turns
    template_name = 'turns_confirm_delete.html'
    success_url = reverse_lazy('turns-list')
