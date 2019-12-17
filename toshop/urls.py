from django.urls import path
from .views import HomePage, OurHistoryPage

urlpatterns = [
    path('', HomePage.as_view(), name='root'),
    path('our_history', OurHistoryPage.as_view(), name='our_history'),
]