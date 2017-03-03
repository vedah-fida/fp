from django.conf.urls import url
from catalog import views

urlpatterns = [
    url('^catalog/get_furniture_price/$', views.get_furniture, name='furniture'),
    url('^catalog/fP/lent_tools/$', views.show_lent_tools, name='lent_tools'),
    url('^catalog/fP/lent_tools_record/$', views.show_tools_record, name='lent_tool_record'),
    url('^catalog/fP/lent_tools_page/$', views.lend_tool_page, name='lend_tool_page'),
    url('^catalog/fP/lend_tool_to_carpenter/$', views.lend_to_carpenter, name='lend_tool_to_carpenter'),
    url('^catalog/fP/lent_tools_return_page/$', views.update_lent_tool_page, name='lent_tool_return_page'),
    url('^catalog/fP/update_lent_tool/$', views.update_lent_tool, name='update_lent_tool'),
]
