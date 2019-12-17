from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePage(TemplateView):
    template_name='index.html'

class OurHistoryPage(TemplateView):
    template_name='our_history.html'

class ProductsPage(TemplateView):
    template_name='products.html'

class ContactPage(TemplateView):
    template_name='contact.html'

class AdminHomePage(TemplateView):
    template_name='administrator/index.html'

class AddProductPage(TemplateView):
    template_name='administrator/add-product.html'