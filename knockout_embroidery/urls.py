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

from home.views import home, about_us
from product.views import (
    products,
    product_detail,
    reviews,
    add_review,
    add_product,
    edit_product,
    delete_product,
    delete_review,
    update_review
)
from users.views import (
    profile,
    order_history,
    CustomLoginView,
    CustomLogoutView
)
from basket.views import (
    add_to_basket,
    view_basket,
    adjust_basket,
    remove_from_basket
)
from checkout.views import checkout, checkout_success
from checkout.webhook import webhook

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about-us/', about_us, name='about_us'),
    path('users/', include('users.urls')),
    path('login/', CustomLoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('products/', products, name='products'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('reviews/', reviews, name='reviews'),
    path('review/add/', add_review, name='add_review'),
    path('review/update/<int:review_id>/', update_review,
         name='update_review'),
    path('delete_review/<int:review_id>/', delete_review,
         name='delete_review'),
    path('profile/', profile, name='profile'),
    path('basket/', view_basket, name='view_basket'),
    path('add/<item_id>/', add_to_basket, name='add_to_basket'),
    path('adjust/<str:unique_key>/', adjust_basket, name='adjust_basket'),
    path('basket/remove/<str:unique_key>/', remove_from_basket,
         name='remove_from_basket'),
    path('checkout/', checkout, name='checkout'),
    path('checkout_success/<order_number>', checkout_success,
         name='checkout_success'),
    path('wh/', webhook, name='webhook'),
    path('order_history/<order_number>/', order_history, name='order_history'),
    path('add_product/', add_product, name='add_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
