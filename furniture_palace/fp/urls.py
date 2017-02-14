from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name='home_view'),
    url(r'^furniture_palace/$', carpenter_login_page, name='carpenter_login_page'),
    url(r'^furniture_palace/carpenter_login/$', carpenter_login, name='carpenter_login'),
    url(r'^furniture_palace/lend_tool/$', lend_tool, name='lend_tool'),
    url(r'^furniture_palace/register_customer/$', register_customer, name='register_customer'),
    url(r'^furniture_palace/payment_summary/$', payment_summary, name='payment_summary'),
    url(r'^furniture_palace/make_order/$', make_order, name='make_order'),
    url(r'^furniture_palace/logout/$', logout, name='logout'),
]
