from django.urls import path
from .views import HomePage, Pages, ProductsPage, ContactPage, AdminHomePage, AddProductPage

urlpatterns = [
    path('', HomePage.as_view(), name='root'),
    path('our_history', Pages.our_history_page, name='our_history'),
    path('products', ProductsPage.as_view(), name='products'),
    path('contact', ContactPage.as_view(), name='contact'),
    path('administrator/products_list', AdminHomePage.as_view(), name='products_list'),
    path('administrator/add_product', AddProductPage.as_view(), name='add_product'),
]