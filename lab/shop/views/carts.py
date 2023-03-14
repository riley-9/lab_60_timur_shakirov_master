from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import RedirectView, DeleteView, ListView

from shop.forms.orders import OrderForm
from shop.models import Cart, Product


class AddProductToCart(RedirectView):
    def get(self, *args, **kwargs):
        cart_products = Cart.objects.all()
        pk = self.kwargs['pk']
        main_product = get_object_or_404(Product, pk=kwargs['pk'])
        Cart.add_to_cart(cart_products, main_product)
        return redirect('main')


class CartView(ListView):
    template_name = 'carts/cart_products.html'
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        cart = Cart.objects.all()
        context['cart'] = cart
        context['form'] = OrderForm()
        context['total'] = Cart.get_total(cart)
        return context


class CartProductDeleteView(DeleteView):
    template_name = 'carts/cart_product_delete.html'
    model = Cart
    context_object_name = 'product'
    success_url = reverse_lazy('cart')
