from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('insert', views.insert, name='insert'),
    path('update/<id>', views.update, name='update'),
    path('delete/<id>', views.delete, name='delete'),
    # path("admin/register/", views.admin_register, name="admin_register"),
    path("admin_login", views.admin_login, name="admin_login"),
    # path("admin/logout/", views.admin_logout, name="admin_logout"),
    path("index", views.index, name="index"), #Admin page
    path('search/', views.search_students, name="search_students"),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    
]