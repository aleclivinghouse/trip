from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^deletepage/(?P<course_id>\d+)$', views.deletepage),
    url(r'^delete/(?P<course_id>\d+)$', views.delete),
]
