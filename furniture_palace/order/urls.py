from django.conf.urls import url
from order import views

urlpatterns = [
    url('^order/$', views.make_order_page, name='order_page'),
    url('^my_active_orders/$', views.view_carpenter_orders, name='active_orders'),
    url(r'^make_order/$', views.make_order, name='make_order'),
    url(r'^order_info/(?P<order_id>[-\w]+)/$', views.order_info, name='order_info'),
    url(r'^all_orders/$', views.view_all_orders, name='all_orders'),
    url(r'^customer_orders/$', views.view_orders_for_customer, name='customer_orders'),
    url(r'^carpenter_orders/$', views.carpenter_orders, name='carpenter_orders'),
    url(r'^order_complete_status/$', views.view_complete_status_orders, name='order_status'),
    url(r'^change_complete_status/$', views.change_complete_status, name='change_complete_status'),
    url(r'^assign_order_page/$', views.assign_order_page, name='assign_order_page'),
    url(r'^assign_order/$', views.take_order, name='take_order'),
    url(r'^assign_order_to_carpenter/$', views.assign_order, name='assign_order'),
    url(r'^search_orders/$', views.search_order, name='search_order'),
    url(r'^order_payments/$', views.show_payment_list, name='payment_list'),
    url(r'^order_update_page/$', views.show_order_payment, name='order_update_page'),
    url(r'^order_update/$', views.update_order, name='order_update'),
    url(r'^order_edit/$', views.edit_order, name="edit_order"),
]
