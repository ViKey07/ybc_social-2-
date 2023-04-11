from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login '),
    path('accounts/register/', views.register, name='register'),
    path('', views.post_list, name='post_list'),
    path('blog/<int:post_id>/', views.blog, name='blog'),
]
