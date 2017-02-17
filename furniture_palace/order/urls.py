from django.conf.urls import url
from order import views

urlpatterns = [
    url('^order/$', views.order_page, name='order_page'),
    url(r'make_order/$', views.make_order, name='make_order'),
]
