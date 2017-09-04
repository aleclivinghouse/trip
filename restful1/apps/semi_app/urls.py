from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^update/(?P<user_id>\d+)$', views.update),
    url(r'^dashboard1$', views.dashboard1),
    url(r'^show/(?P<user_id>\d+)$', views.show),
    url(r'^edit/(?P<user_id>\d+)$', views.edit),
    url(r'^delete/(?P<user_id>\d+)$', views.delete)
]
