from django.urls import path
from products import views

app_name = "products"
urlpatterns = [
    path('', views.index, name="index"),
    path('list_view/', views.list_view, name="list"),
    path('<int:product_id>/', views.detail_view, name="detail"),
    path('create/', views.create_view, name="create"),
    path('update/<int:product_id>/', views.update_view, name="update"),
    path('delete/<int:product_id>/', views.delete_view, name="delete"),
]
