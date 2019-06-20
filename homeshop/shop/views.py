from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from . import forms
from .models import Category, Product


# Create your views here.

def all_products(request, c_slug=None):
    print(f"Request !!!!{dir(request)}")
    if c_slug:
        category = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    print(f"Request-{request.GET}, Page-{page}")
    products = paginator.get_page(page)

    return render(request, 'shop/all_products.html', {"products": products, "categories": categories})


def product_detail(request, p_slug=None):
    product = get_object_or_404(Product, slug=p_slug)
    categories = Category.objects.all()
    return render(request, 'shop/product_detail.html', {"product": product, "categories": categories})


@login_required
def add_product(request):
    if request.method == "POST":
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.image = request.FILES.get('image')
            product.save()
            url = product.get_url()
            return HttpResponseRedirect(url)
    else:
        form = forms.ProductForm()
    return render(request, 'shop/add_product.html', {"form": form})


def update_product(request, p_slug):
    product = get_object_or_404(Product, slug=p_slug)
    if request.method == "POST":
        form = forms.ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.image = request.FILES.get('image')
            product.save()
            url = product.get_url()
            return HttpResponseRedirect(url)
    else:
        form = forms.ProductForm()
    return render(request, 'shop/edit_product.html', {"form": form})


def remove_product(request, p_slug):
    try:
        product = get_object_or_404(Product, slug=p_slug)
        product.delete()
        return HttpResponseRedirect(reverse("shop:all_products"))
    except:
        return HttpResponseNotFound()
