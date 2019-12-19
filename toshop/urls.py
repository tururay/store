from django.urls import path
from .views import HomePage, Pages, ProductsPage, ContactPage, AdminHomePage, AddProductPage
from .views import CategoriesPage

urlpatterns = [
    path('', HomePage.as_view(), name='root'),
    path('our_history', Pages.our_history_page, name='our_history'),
    path('products', ProductsPage.as_view(), name='products'),
    path('contact', ContactPage.as_view(), name='contact'),
    path('administrator/products_list', AdminHomePage.as_view(), name='products_list'),
    path('administrator/add_product', AddProductPage.as_view(), name='add_product'),
    path('administrator/categories', CategoriesPage.index, name="categories_list"),
    path('administrator/categories/new', CategoriesPage.new, name="add_category"),
    path('administrator/categories/create', CategoriesPage.create, name="save_category"),
    path('administrator/categories/<int:category_id>/edit', CategoriesPage.edit, name='edit_category'),
    path('administrator/categories/<int:category_id>/update', CategoriesPage.update, name='update_category'),
    path('administrator/categories/<int:category_id>/delete', CategoriesPage.delete, name='delete_category'),
]