from django.conf.urls import url
from . import views

#/users sends the register form
#"/login" sends the  login form

#this is the route for the create new list item
#<form action="/main" method="POST">

urlpatterns = [
######THESE ARE FOR RENDERING
#it starts at main
url(r'^main$', views.index),
#it then goes to the dashboard
url(r'^dashboard$', views.dashboard),


	
######THESE ARE FOR ROUTES

###this processes the poke button
url(r'^poke/(?P<id>\d+)$', views.poke),
	
url(r'^users$', views.register),

###process the form
url(r'^login$', views.login),
url(r'^logout$', views.logout)
]