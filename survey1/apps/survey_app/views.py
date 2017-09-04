# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "survey_app/index.html")

def process(request):

        if request.method =="POST":
            request.session['name'] = request.POST['name']
            request.session['location'] = request.POST['location']
            request.session['language'] = request.POST['language']
            request.session['comment'] = request.POST['comment']
            request.session['count'] += 1;

            context = {
            "name": request.session['name'],
            'location': request.session['location'],
            'language': request.session['language'],
            'comment': request.session['comment'],
            'count': request.session['count'],
            }
            return render(request, "survey_app/show.html", context)
        else:
            return redirect("/")
