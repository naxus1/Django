from tasks import views
from django.conf.urls import url


urlpatterns = [
    url(r'^user/$', views.user_list),
    url(r'^user/(?P<pk>[0-9]+)$', views.user_detail),
    url(r'^task/$', views.task_list),
    url(r'^task_view/(?P<pk>[0-9]+)$', views.task_view),
    url(r'^task_user/(?P<pk>[0-9]+)$', views.task_user)
]