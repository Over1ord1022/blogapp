from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('preferences/', views.preferences, name='preferences'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]