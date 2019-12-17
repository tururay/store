from django.urls import path
from .views import HomePage, OurHistoryPage, ProductsPage, ContactPage 

urlpatterns = [
    path('', HomePage.as_view(), name='root'),
    path('our_history', OurHistoryPage.as_view(), name='our_history'),
    path('products', ProductsPage.as_view(), name='products'),
    path('contact', ContactPage.as_view(), name='contact'),
]