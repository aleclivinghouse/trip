# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render,  HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from .models import Course

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    context = {
    "all_courses": Course.objects.all()
    }
    return render(request, "courses_app/index.html", context)

#this is where we process the form
def add(request):
    Course.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect("/")

def deletepage(request, course_id):
    context = {
    "course": Course.objects.get(id=course_id)
    }
    return render(request, "courses_app/deletepage.html", context)

def delete(request, course_id):
    Course.objects.get(id=course_id).delete()

    return redirect("/")


# def create(request):
#     if request.method == "POST":
#         request.session['name'] = request.POST['name']
#         request.session['desc'] = request.POST['desc']
