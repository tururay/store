from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePage(TemplateView):
    template_name='index.html'

class OurHistoryPage(TemplateView):
    template_name='our_history.html'