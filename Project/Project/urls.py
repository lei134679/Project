"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Users.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^user/', include('Users.urls', namespace='user')),
    url(r'^address/', include('Address.urls', namespace='address')),
    url(r'^store/', include('Store.urls', namespace='store')),
    url(r'^goodstype/', include('GoodsType.urls', namespace='goodstype')),
    url(r'^goods/', include('Goods.urls', namespace='goods')),
    url(r'^goodsimage/', include('GoodsImage.urls', namespace='goodsimage')),
    url(r'^shopcart/', include('Shopcart.urls', namespace='shopcart')),
    url(r'^order/', include('Order.urls', namespace='order')),
]
