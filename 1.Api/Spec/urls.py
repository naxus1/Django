from django.conf.urls import url 
from Spec import views 
 
urlpatterns = [
    url(r'^company/$', views.info_company_list, name='company'),
    url(r'^company/(?P<pk>[0-9]+)$', views.info_company_detail, name='company_detail'),
    url(r'^company_ss/(?P<pk>[0-9]+)$', views.seguridad_social_detail, name='company_ss'),
]