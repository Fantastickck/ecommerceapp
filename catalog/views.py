from msilib.schema import ListView
from django.views.generic import DetailView, ListView

from .models import Category, Product, Brand, Product_Feature


class GetCategories(ListView):
    model = Category
    template_name = 'catalog/categories.html'
    context_object_name = 'categories'


class GetProducts(ListView):
    template_name = 'catalog/products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        if self.request.GET.get('brand'):
            return Product.objects.filter(category__slug=self.kwargs['slug'], brand__slug=self.request.GET.get('brand'))
        else:
            return Product.objects.filter(category__slug=self.kwargs['slug'])


class GetOneProduct(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    pk_url_kwarg = "product_id"

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['features'] = Product_Feature.objects.filter(product__id=self.kwargs['product_id'])
        return context
        

class GetBrands(ListView):
    model = Brand
    template_name = 'catalog/brands.html'
    context_object_name = 'brands'


class GetCategoriesByBrand(ListView):
    template_name = 'catalog/categories_by_brand.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(brand__slug=self.kwargs['slug'])
        context['brand'] = Brand.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Category.objects.filter(brand__slug=self.kwargs['slug'])

