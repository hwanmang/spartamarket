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
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(author=request.user)
            return redirect("products:detail", product.id)
    else:
        form = ProductForm()

    context = {"form": form}
    return render(request, "products/create.html", context)


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


# @require_POST
# def like(request, pk):
#     print(product.pk)
#     if request.user.is_authenticated:
#         product = get_object_or_404(Product, pk=pk)
#         if product.like_users.filter(pk=request.user.pk).exists():
#             product.like_users.remove(request.user)
#         else:
#             product.like_users.add(request.user)
#     else:
#         return redirect("accounts:login")

#     return redirect("products:detail", product.pk)


@require_POST
def like(request, pk):
    print(pk)
    if request.user.is_authenticated:
        article = get_object_or_404(Product, pk=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
    else:
        return redirect("accounts:login")

    return redirect("products:detail", pk)
