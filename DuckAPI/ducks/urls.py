from django.conf.urls import url
from ducks.views import *

app_name = 'ducks'

urlpatterns = [
    url(r'^ducks/$', DuckList.as_view(), name='ducks')
]
