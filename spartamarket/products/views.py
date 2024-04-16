from django.shortcuts import get_object_or_404, redirect, render

from products.form import ProductForm
from products.models import Product
from django.views.decorators.http import require_POST


def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {"products": products})


def list_view(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'products/list.html', {"products": products})


def create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products:list")
    return render(request, 'products/create.html', {"form": form})


def detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {"product": product})


def update_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products:list")
    return render(request, 'products/create.html', {"form": form})


@require_POST
def delete_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect("products:list")
