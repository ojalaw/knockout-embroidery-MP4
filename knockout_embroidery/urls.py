"""
URL configuration for knockout_embroidery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from home.views import home
from product.views import products, product_detail, review
from users.views import profile
from basket.views import add_to_basket, view_basket, adjust_basket, remove_from_basket
from checkout.views import checkout
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('users/', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('products', products, name='products'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('reviews/', review, name='review'),
    path('profile/', profile, name='profile'),
    path('basket/', view_basket, name='view_basket'),
    path('add/<item_id>/', add_to_basket, name='add_to_basket'),
    path('adjust/<item_id>/', adjust_basket, name='adjust_basket'),
    path('basket/remove/<item_id>/', remove_from_basket, name='remove_from_basket'),
    path('checkout/', checkout, name='checkout')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)