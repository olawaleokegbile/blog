from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('post/<str:pk>', views.post, name='post'),
    path('contact', views.contact, name='contact'),
]
