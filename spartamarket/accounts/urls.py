from django.urls import path
from . import views
from .views import good

app_name = "accounts"
urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("delete_user/", views.delete_user, name="delete_user"),
    path("update_user/", views.update_user, name="update_user"),
    path("password/", views.change_password, name="change_password"),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('good/<int:user_id>/', good, name="good")
]
