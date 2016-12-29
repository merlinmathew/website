__author__ = 'user'


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'test/', views.test, name='index'),
    url(r'about/', views.about, name='about'),
    url(r'contact/', views.contact, name='contact'),
    url(r'blog/', views.blog, name='blog'),
]


