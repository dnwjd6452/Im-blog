from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list,name='post_list'),
    path('', views.create, name='create'),
    path('im_blog/<int:blog_id>', views.detail, name='detail'),
]