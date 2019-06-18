from django.shortcuts import render
from django.urls import reverse

from .models import Category, Product
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from . import forms


# Create your views here.

def all_products(request, c_slug=None):
    print(f"Request !!!!{dir(request)}")
    if c_slug:
        category = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    
    return render(request, 'shop/all_products.html', {"products": products, "categories": categories})


def product_detail(request, p_slug=None):
    product = get_object_or_404(Product, slug=p_slug)
    categories = Category.objects.all()
    return render(request, 'shop/product_detail.html', {"product": product, "categories": categories})


def add_product(request):
    if request.method == "POST":
        form = forms.ProductForm(request.user, request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            print(request.FILES)
            product.image = request.FILES['image']
            product.save()
            url = product.get_url()
            return HttpResponseRedirect(url)
    else:
        form = forms.ProductForm()
    return render(request, 'shop/add_product.html', {"form": form})
