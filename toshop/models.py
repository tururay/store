from django.db import models
from djmoney.models.fields import MoneyField

def product_directory_path(instance, filename):
    return 'product_{0}/{1}-%Y-%m-%d'.format(instance.product.id, filename)

class StaticPages(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Título")
    content = models.TextField(null=False, blank=False, verbose_name="Conteúdo")
    page_id = models.CharField(max_length=15, unique=True, null=False, blank=False, verbose_name="Identificador")

class Category(models.Model):
    name = models.CharField(max_length=15, null=False, unique=True, verbose_name='Categoria')
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, verbose_name="Categoria Pai")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nome do Produto")
    price = MoneyField(max_digits=7, decimal_places=2, default_currency='BRL', null=False, blank=False)
    description = models.TextField(verbose_name='Descrição', null=False, blank=False)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=False, verbose_name="Categoria")
    active = models.BooleanField(verbose_name="Ativo", default=False)
    discount = models.BooleanField(verbose_name="Desconto", default=False)
    discount_value = MoneyField(max_digits=7, decimal_places=2, default_currency='BRL', null=True)

    def cover(self):
        return self.productimage_set.first()

    def images(self):
        return self.productimage_set.all()

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=False, verbose_name="Produto")
    image = models.FileField(upload_to=product_directory_path, verbose_name='Imagem')
    cover = models.BooleanField(default=False, verbose_name="Capa")
