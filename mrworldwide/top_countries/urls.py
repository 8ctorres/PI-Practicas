from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.top, name='top_index'),
]