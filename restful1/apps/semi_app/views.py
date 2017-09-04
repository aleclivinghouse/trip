# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render,  HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect
from .models import User


#these are the render routes
def index(request):

    return render(request, "semi_app/index.html")

def dashboard1(request):
    context = {
    "all_users": User.objects.all()
    }
    return render(request, "semi_app/dashboard.html", context)

def edit(request, user_id):
    #use get to retireve
    the_user = User.objects.get(id=user_id)
    context = {
    "user": the_user
    }
    return render(request, "semi_app/edit.html", context)

def show(request, user_id):
    context = {
    "user": User.objects.get(id=user_id)
    }
    return render(request, "semi_app/show.html", context)

# these are the process routes
def process(request):
    ##here we will create a new user
    User.objects.create(firstname = request.POST['firstname'], lastname = request.POST['lastname'], email = request.POST['email'])
    return redirect("/dashboard1")

def update(request, user_id):
    ##use filter to update
    the_user = User.objects.filter(id=user_id)
    the_user.update(firstname = request.POST['firstname'], lastname = request.POST['lastname'], email = request.POST['email'])

    return redirect("/dashboard1")

def delete(request, user_id):
    User.objects.get(id=user_id).delete()

    return redirect('/dashboard1')
