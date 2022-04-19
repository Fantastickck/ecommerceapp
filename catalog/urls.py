from django.urls import path

from .views import GetBrands, GetCategories, GetCategoriesByBrand, GetOneProduct, GetProducts, CreateFeedback


urlpatterns = [
    path('categories/', GetCategories.as_view(), name='get_categories'),
    path('category/<slug:slug>/', GetProducts.as_view(), name='get_products'),
    path('product/<int:product_id>/', GetOneProduct.as_view(), name='get_product'),
    path('brands/', GetBrands.as_view(), name='get_brands'),
    path('brand/<slug:slug>/', GetCategoriesByBrand.as_view(), name='get_brand'),
    path('create_feedback/<int:product_id>/', CreateFeedback.as_view(), name='create_feedback')
]