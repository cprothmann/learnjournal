from django.urls import path
from journal import views
from journal.views import ResourceView, ResourceCreateView, ResourceUpdateView, ResourceDeleteView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', ResourceView.as_view(), name="list"),
    path('resources/new/', ResourceCreateView.as_view(), name='resource-add'),
    path('resources/<int:pk>/', ResourceUpdateView.as_view(), name='resource-update'),
    path('resources/<int:pk>/delete/', ResourceDeleteView.as_view(), name='resource-delete'),
]