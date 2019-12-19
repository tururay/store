from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import StaticPages, Category
from .forms import CategoryForm

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

class CategoriesPage(TemplateView):
    def index(request):
        query = request.GET.get('query')

        if query:
            categories = Category.objects.filter(name__icontains=query).order_by('name')
        else:
            categories = Category.objects.all().order_by('name')
            
        paginator = Paginator(categories, 10)

        try:
            page_number = int(request.GET.get('page', '1'))
        except ValueError:
            page_number = 1
        
        try:
            categories = paginator.page(page_number)
        except (EmptyPage, InvalidPage):
            categories = paginator.page(paginator.num_pages)

        return render(request, 'administrator/category/index.html', { 'categories': categories, 'paginator': paginator })

    def new(request):
        form = CategoryForm(request.POST)
        return render(request, 'administrator/category/new.html', { 'form': form })

    def create(request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            parent = None

            print("Parent: " + str(form.cleaned_data['parent']))

            if form.cleaned_data['parent']:
                parent = Category.objects.filter(id=form.cleaned_data['parent'].id)[0]

            category = Category(name=name, parent=parent)
            category.save()
            return redirect('categories_list')
        else:
            return redirect('add_category')
    
    def edit(request, category_id):
        category = Category.objects.get(id=category_id)
        form = CategoryForm(instance=category)
        return render(request, 'administrator/category/edit.html', { 'form': form, 'category': category })

    def update(request, category_id):
        form = CategoryForm(request.POST)
        category = Category.objects.get(id=category_id)

        if form.is_valid():
            category.name = form.cleaned_data['name']
            
            if form.cleaned_data['parent']:
                category.parent = Category.objects.get(id=form.cleaned_data['parent'].id)
            
            category.save()
            return redirect('categories_list')
        else:
            return render(request, 'administrator/category/edit.html', { 'form': form, 'category': category })
        
    def delete(request, category_id):
        category = Category.objects.get(id=category_id)
        
        if category:
            category.delete()
        
        return redirect('categories_list')
