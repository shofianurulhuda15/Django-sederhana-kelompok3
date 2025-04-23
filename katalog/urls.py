"""
URL configuration for katalog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from produk import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produk/', views.daftar_produk, name='daftar_produk'),
    path('produk/<int:id>/', views.detail_produk, name='detail_produk'),
    path('kontak/', views.kontak, name='kontak'),
]