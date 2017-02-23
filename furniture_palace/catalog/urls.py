from django.conf.urls import url
from catalog import views

urlpatterns = [
    url('^catalog/get_furniture/$', views.get_furniture, name='furniture'),
]
