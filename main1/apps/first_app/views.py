# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render,  HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    context = {
     "random_string": get_random_string(length=14),
     "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
    }
    return render(request, "first_app/index.html", context)



# def create(request):
#     if request.method == "POST":
#         request.session['name'] = request.POST['name']
#         request.session['desc'] = request.POST['desc']
