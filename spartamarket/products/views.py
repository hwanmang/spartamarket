from django.shortcuts import get_object_or_404, redirect, render
from products.form import ProductForm
from products.models import Product
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {"products": products})


@login_required
def list(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'products/list.html', {"products": products})


@login_required
def create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save(author=request.user)
            return redirect("products:list")
    return render(request, 'products/create.html', {"form": form})


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {"product": product})


@login_required
@require_http_methods(["GET", "POST"])
def update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.author != request.user:
        messages.warning(request, '작성자 본인만 수정이 가능합니다.')
        return redirect("products:detail", product_id=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products:list")
    return render(request, 'products/create.html', {"form": form})


@login_required
@require_POST
def delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.author == request.user:
        product.delete()
        messages.add_message(request, messages.ERROR, '게시글이 삭제되었습니다.')
    else:
        messages.add_message(request, messages.ERROR, '작성자가 아니라면 삭제할 수 없습니다.')
    return redirect("products:list")


@login_required
@require_POST
def good_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    user.good_products.add(product)
    return redirect("products:list")
