from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.all_products, name="all_products"),
    path("<slug:c_slug>/", views.all_products, name="category_products"),
    path("product/new/", views.add_product, name="add_product"),
    path("product/<slug:p_slug>/", views.product_detail, name="product_detail"),
]
