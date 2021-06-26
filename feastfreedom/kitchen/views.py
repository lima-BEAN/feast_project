import random
from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse, reverse_lazy

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#TODO: Require login to create App in LimaBeanLab Apps section
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required

from kitchen.models import Kitchen

def home(request):
    return HttpResponse("It works")

#class HomePageView(TemplateView):
#    template_name = "apps/home.html"

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['number'] = random.randrange(1, 100)
#        context['latest_kitchen'] = Kitchen.objects.all()[:3]
#        return context

class KitchenListView(ListView):
    model = Kitchen
    context_object_name = 'kitchen'

class KitchenDetailView(DetailView):
    model = Kitchen

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kitchen_list'] = Kitchen.objects.all()
        return context

class KitchenCreateView(CreateView):
    model = Kitchen
    fields = ['name', 'open_time', 'close_time']
    template_name = 'kitchen/kitchen_create.html'
    success_url = reverse_lazy('kitchen:home')
    #TODO: # login_url = '/login/'

class KitchenUpdateView(UpdateView):
    model = Kitchen
    fields = ['name',  'open_time', 'close_time']
    template_name = 'kitchen/kitchen_update.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('kitchen:home')
    #TODO # login_url = '/login/'

class KitchenDeleteView(DeleteView):
    model = Kitchen
    template_name = 'kitchen/kitchen_confirm_delete.html'
    success_url = reverse_lazy('kitchen:home')
    #TODO: # login_url = '/login/'


def check():
    pass

def error_500(request):
    return render(request, '500.html')
