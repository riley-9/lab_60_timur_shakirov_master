from django.urls import path

from shop.views.carts import AddProductToCart, CartView, CartProductDeleteView
from shop.views.orders import OrderAddView
from shop.views.products import ProductsView, ProductView, ProductAddView, ProductEditView, ProductDeleteView, \
    ProductsByCategoryView

urlpatterns = [
    path('', ProductsView.as_view(), name='main'),
    path('products/add/', ProductAddView.as_view(), name='add_product'),
    path('products/<pk>/', ProductView.as_view(), name='product'),
    path('products/productsedit/<pk>/', ProductEditView.as_view(), name='edit_product'),
    path('products/delete/<pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('products/confirm-delete-product/<pk>/', ProductDeleteView.as_view(), name='confirm_delete_product'),
    path('products/category/<key>/', ProductsByCategoryView.as_view(), name='by_category'),

    path('cart/add/<pk>/', AddProductToCart.as_view(), name='add_to_cart'),
    path('cart/delete/<pk>/', CartProductDeleteView.as_view(), name='delete_cart_product'),
    path('cart/confirm-delete-cart-product/<pk>/', CartProductDeleteView.as_view(), name='confirm_delete_cart_product'),
    path('cart/', CartView.as_view(), name='cart'),

    path('order/add/', OrderAddView.as_view(), name='add_order'),
]
