from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from journal.forms import ResourcelistForm
from django.views import generic
from django.template import loader
from journal.models import Resourcelist
# Create your views here.

def home_view(request):
    context ={}

    return render(request, "welcome.html", context)

def index(request):
    rlist = Resourcelist.objects.all()
    template =loader.get_template('home.html')
    #resource_list = ",".join([r.name for r in Resources_list])

    context = {
        'rlist': rlist,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'list.html', context)

def detail_view(request, id):


    context = {}

    context["data"] = Resourcelist.objects.get(id = id)

    return render(request, "detail_view.html", context)

def updateview(request, id):

    context = {}

    obj = get_object_or_404(Resourcelist, id = id)

    form = ResourcelistForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    context["form"] = form

    return render(request, "update_view.html")

class ResourceView(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'rlist'

    def get_queryset(self):
        """Return Resources"""
        return Resourcelist.objects.order_by('name')

class ResourceDetailView(DetailView):
    model = Resourcelist
    fields = ['name', 'url', 'resource_description']
    template_name = 'detail_view.html'

class ResourceCreateView(CreateView):
    model = Resourcelist
    fields = ['name', 'url', 'resource_description']
    template_name = 'resource_form.html'
    success_url = reverse_lazy('list')

class ResourceUpdateView(UpdateView):
    model = Resourcelist
    fields = ['name', 'url', 'resource_description']
    template_name = 'resource_form.html'
    success_url = "/journal/resources/"

class ResourceDeleteView(DeleteView):
    model = Resourcelist
    #fields = ['name', 'url', 'resource_description']
    context_object_name = 'resources'
    success_url = "/journal/resources/"
    template_name = 'delete.html'