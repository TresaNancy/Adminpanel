from django.urls import path
from .import views


urlpatterns = [
    path('user_index',views.user_index, name="user_index"),
    path('user_login/',views.user_login, name="user_login"),
    path('user_signup',views.user_signup, name="user_signup"),
    path('user_home/',views.user_home, name="user_home"),
    path('user_home/logout',views.user_logout, name="user_logout"),
]
