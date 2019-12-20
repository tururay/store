from django import forms
from .models import Category, Product
from .models import product_directory_path
from djmoney.forms.fields import MoneyField
from djmoney.forms.widgets import MoneyWidget

class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}))
    parent = forms.ModelChoiceField(
            queryset=Category.objects.all(),
            required=False,
            empty_label="(Sem Pai)",
            widget=forms.Select(attrs={'class':'form-control'})
        )

    class Meta:
        model = Category
        fields = ('name', 'parent')

class ProductImageForm(forms.ModelForm):
    image = forms.ImageField()

class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}))
    price = forms.DecimalField(max_digits=7, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '24.99'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'cols': None, 'rows': None}))
    category = forms.ModelChoiceField(
            queryset=Category.objects.all(),
            required=True,
            widget=forms.Select(attrs={'class':'form-control'})
        )

    active_choices = [('t', 'Sim'), ('f', 'Não')]
    active = forms.ChoiceField(choices=active_choices, widget=forms.RadioSelect(), required=True)

    discount = forms.BooleanField(initial=False, label="Pode aplicar descont?", required=False)

    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'category', 'active', 'discount')