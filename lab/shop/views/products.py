from urllib.parse import urlencode

from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from shop.forms.product import ProductForm, SearchForm
from shop.models.products import Product, CategoryChoices


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})


class ProductsView(ListView):
    template_name = 'products/main.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5
    extra_context = {'categories': CategoryChoices.choices}

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_queryset(self):
        queryset = Product.objects.exclude(rest=0).order_by('category', 'product')
        if self.search_value:
            query = Q(product__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context


class ProductView(DetailView):
    template_name = 'products/product.html'
    model = Product

    def get_object(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        product = get_object_or_404(Product, pk=pk)

        if product.rest <= 0:
            raise Http404('Product not found')
        return product


class ProductAddView(SuccessDetailUrlMixin, CreateView):
    template_name = 'products/add_product.html'
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        project = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)


class ProductEditView(SuccessDetailUrlMixin, UpdateView):
    template_name = 'products/edit_product.html'
    model = Product
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    template_name = 'products/delete_product.html'
    model = Product
    success_url = reverse_lazy('main')


class ProductsByCategoryView(ListView):
    template_name = 'products/main.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5
    extra_context = {'categories': CategoryChoices.choices}

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        self.key = self.kwargs.get('key')
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_queryset(self):
        queryset = Product.objects.exclude(rest=0).order_by('category', 'product').filter(category=
                                                                                          self.kwargs['key'])
        if self.search_value:
            query = Q(product__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context
