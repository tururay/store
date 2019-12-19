from django import forms
from .models import Category

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