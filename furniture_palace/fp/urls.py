from django.conf.urls import url
from .views import login, home

urlpatterns = [
    url(r'^$', home, name='home_view'),
    url(r'^login/$', login, name='login'),
]
