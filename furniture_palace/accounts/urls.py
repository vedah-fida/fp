from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^$', views.landing_page, name='index'),
    url(r'^carpenter_login/$', views.login_carpenter, name='login'),
    url(r'^customer_registration/$', views.register_customer_page, name='customer_registration'),
    url(r'^register_customer/$', views.register_customer, name='register_customer'),
    url(r'^view/customers/$', views.view_customers, name='view_customer'),
    url(r'^get/customer/$', views.get_customer, name='get_customer'),
    url(r'^update/customer/$', views.update_customer, name='update_customer'),
    url(r'^search/customer/$', views.search_customer, name='search_customer'),
    url(r'^logout/$', views.logout_carpenter, name='logout'),
]
