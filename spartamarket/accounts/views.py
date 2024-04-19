from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    update_session_auth_hash
)
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.shortcuts import render, get_object_or_404
from .models import User
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.contrib.auth import get_user_model


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("/")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("/")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            auth_login(request, form.instance)
            return redirect("/")
        else:
            messages.error(request, '회원가입에 실패하였습니다. 올바른 정보를 입력해주세요.')
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


@login_required
def profile(request, user_id):
    profile_user = get_object_or_404(get_user_model(), pk=user_id)
    products = Product.objects.filter(author=profile_user)
    return render(request, 'accounts/profile.html', {'profile_user': profile_user, 'products': products})


@require_POST
def delete_user(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect("/")


@login_required
@require_http_methods(["GET", "POST"])
def update_user(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update_user.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("/")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/change_password.html", context)


def good(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user: User = request.user
    user.good_products.add(product)
    return redirect("products:list")


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_pk)
        if request.user != member:
            if request.user in member.followers.all():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("accounts:profile", member.pk)
    return redirect("accounts:login")
