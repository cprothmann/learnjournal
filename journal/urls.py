from django.urls import path
from journal import views
from journal.views import  ResourceView, ResourceCreateView, ResourceUpdateView, ResourceDeleteView
from . import views
from .views import detail_view

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', ResourceView.as_view(), name="list"),
    path('resources/new/', ResourceCreateView.as_view(), name='resource-add'),
    path('resources/<id>/', detail_view, name='resource-detail'),
    path('resources/<pk>/update', ResourceUpdateView.as_view(), name='resource-update'),
    path('resources/<pk>/delete/', ResourceDeleteView.as_view(), name='resource-delete'),
]