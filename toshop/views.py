from django.views.generic.base import TemplateView
from django.shortcuts import render
from .models import StaticPages

class HomePage(TemplateView):
    template_name='index.html'

class Pages(TemplateView):
    def our_history_page(request):
        page = StaticPages.objects.filter(page_id='our_history').first()
        context = {
            'title': page.title,
            'content': page.content
        }
        return render(request, 'our_history.html', context)

class ProductsPage(TemplateView):
    template_name='products.html'

class ContactPage(TemplateView):
    template_name='contact.html'

class AdminHomePage(TemplateView):
    template_name='administrator/index.html'

class AddProductPage(TemplateView):
    template_name='administrator/add-product.html'