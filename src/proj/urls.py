"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from references import views as ref_views
from order import views as order_views
from catalog import views as catalog_views
from catalog.views import BookDetail, BookList, BookCreate, BookUpdate, BookDelete

from cart import views as cart_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('references/currency/<int:pk>/', ref_views.currency_detail),
    path('references/currency/list', ref_views.currency_list),
    path('references/currency/create/', ref_views.currency_create),
    path('references/currency/update/<int:pk>/', ref_views.currency_update),
    path ('about_us/', ref_views.AboutUs.as_view()),
    
    path('order/list/', order_views.OrderList.as_view()),
    path('order/create/', order_views.OrderCreate.as_view()),
    path('order/delete/<int:pk>/', order_views.OrderDelete.as_view()),
    path('order/detail/<int:pk>/', order_views.OrderDetail.as_view()),
    path('order/update/<int:pk>/', order_views.OrderUpdate.as_view()),
    path('order/success/', order_views.OrderSuccess.as_view()),
    
    path ('catalog/', BookList.as_view()),
    path ('catalog/create', BookCreate.as_view()),
    path ('catalog/book/<int:pk>/', catalog_views.BookDetail.as_view()),
    path ('catalog/update/<int:pk>/', BookUpdate.as_view()),

    #path ('cart/', Cart)

    



] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #path('', views.home, name='home')
    #path('cart/', cart_views.get_cart),

