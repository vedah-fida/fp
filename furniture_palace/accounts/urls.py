from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^$', views.landing_page, name='index'),
    url(r'^carpenter_login/$', views.login_carpenter, name='login'),
    url(r'^customer_registration/$', views.register_customer_page, name='customer_registration'),
    url(r'^register_customer/$', views.register_customer, name='register_customer'),
    url(r'^logout/$', views.logout_carpenter, name='logout'),
]
