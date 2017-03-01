from django.conf.urls import url
from reports import views

urlpatterns = [
    url(r'^carpenter_payroll_summary/$', views.show_carpenter_summary, name='carpenter_payroll'),
    # url(r'^monthly_summary/$',),
]
