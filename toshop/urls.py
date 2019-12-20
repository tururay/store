from django.urls import path
from .views import Pages, ContactPage
from .views import CategoriesPage, ProductsPage

urlpatterns = [
    path('', Pages.index, name='root'),
    path('our_history', Pages.our_history_page, name='our_history'),
    path('products', Pages.products, name='products'),
    path('products/<int:product_id>', Pages.product, name='product'),
    path('contact', ContactPage.as_view(), name='contact'),
    path('administrator/categories', CategoriesPage.index, name="categories_list"),
    path('administrator/categories/new', CategoriesPage.new, name="add_category"),
    path('administrator/categories/create', CategoriesPage.create, name="save_category"),
    path('administrator/categories/<int:category_id>/edit', CategoriesPage.edit, name='edit_category'),
    path('administrator/categories/<int:category_id>/update', CategoriesPage.update, name='update_category'),
    path('administrator/categories/<int:category_id>/delete', CategoriesPage.delete, name='delete_category'),

    path('administrator/products', ProductsPage.index, name="products_list"),
    path('administrator/products/new', ProductsPage.new, name="add_product"),
    path('administrator/products/create', ProductsPage.create, name="save_product"),
    # path('administrator/products/<int:product_id>/edit', ProductsPage.edit, name='edit_product'),
    # path('administrator/products/<int:product_id>/update', ProductsPage.update, name='update_product'),
    path('administrator/products/<int:product_id>/delete', ProductsPage.delete, name='delete_product'),
]