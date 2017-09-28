from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import DetailRoomsView
# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        print(context)
        return context

class AboutView(TemplateView):
    template_name = "about.html"
class ContactView(TemplateView):
    template_name = "contact.html"

class RoomsListView(ListView):
    template_name = 'rooms/rooms_list.html'
    queryset = DetailRoomsView.objects.all()
class SingleroomsListView(ListView):
    template_name = 'rooms/rooms_list.html'
    queryset = DetailRoomsView.objects.filter(rooms_type__iexact= "Double bad room")

