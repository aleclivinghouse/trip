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
url(r'^dashboard$', views.books),
url(r'^addbook$', views.booksadd),
url(r'^books/(?P<id>\d+)$', views.viewbook),

#these are process ROUTES
url(r'^add$', views.add),

url(r'^add/(?P<id>\d+)$', views.addreviewtobook),
url(r'^user/(?P<id>\d+)$', views.showuser),





url(r'^users$', views.register),

###process the form
url(r'^login$', views.login),
url(r'^logout$', views.logout)
]
