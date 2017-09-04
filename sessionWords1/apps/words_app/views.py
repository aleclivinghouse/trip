# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import gmtime, strftime
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "words_app/index.html")

def process(request):
    # first you have to test the session
    try:
        request.session['words']
    except:
        request.session['words'] = []

    if request.method == "POST":
        if request.POST['font'] == 'yes':
            fontsize = "Big"
        else:
            fontsize = "Small"

        #this is where we add everything to the context dictionary
        context = {
            'word': request.POST['word'],
            'color': request.POST['color'],
            'date': strftime("%B %d %Y", gmtime()),
            'time': strftime("%X %p", gmtime()),
            'font': fontsize
        }
        #at the front of request.session['words']
        #insert the context created above
        request.session['words'].insert(0, context)
        request.session.modified = True
        return redirect('/')
    else:
        return redirect("/")


#this is the route tp clear all the words
def clear(request):
    request.session['words'] = []
    return redirect('/')
