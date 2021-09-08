from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
from django.template import loader
from journal.models import Resourcelist
# Create your views here.

def index(request):
    rlist = Resourcelist.objects.all()
    template =loader.get_template('home.html')
    #resource_list = ",".join([r.name for r in Resources_list])

    context = {
        'rlist': rlist,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'list.html', context)

class ResourceView(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'rlist'

    def get_queryset(self):
        """Return Resources"""
        return Resourcelist.objects.order_by('name')

class ResourceCreateView(CreateView):
    model = Resourcelist
    fields = ['name', 'url', 'resource_description']
    template_name = 'resource_form.html'
    success_url = reverse_lazy('list')

class ResourceUpdateView(UpdateView):
    model = Resourcelist
    fields = ['name', 'url', 'resource_description']

class ResourceDeleteView(DeleteView):
    model = Resourcelist
    success_url = reverse_lazy('allresources')