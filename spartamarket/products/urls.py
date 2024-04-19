from django.urls import path
from products import views

app_name = "products"
urlpatterns = [
    path('', views.index, name="index"),
    path('list_view/', views.list, name="list"),
    path('<int:product_id>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('update/<int:product_id>/', views.update, name="update"),
    path('delete/<int:product_id>/', views.delete, name="delete"),
    path("<int:pk>/like/", views.like, name="like"),
]
