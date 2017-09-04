from django.conf.urls import url
from . import views

#/users sends the register form
#"/login" sends the  login form

#this is the route for the create new list item
#<form action="/main" method="POST">

urlpatterns = [
######THESE ARE FOR RENDERING
#it starts at main
url(r'^$', views.re),
url(r'^main$', views.index),
#it then goes to the dashboard
url(r'^dashboard$', views.dashboard),
url(r'^process/(?P<id>\d+)$', views.process),


url(r'^users$', views.register),

###process the form
url(r'^login$', views.login),
url(r'^logout$', views.logout)
]
