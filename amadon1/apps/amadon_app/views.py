# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,  HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    #first you make a list of items with dictionaries of each item

    items = [{"name": "Dojo tshirt", "price": 19.99}, {"name": "Dojo Sweater",
    "price": 29.99}, {"name": "Dojo Cup", "price": 4.99}, {"name": "Algorithm Book", "price": 49.99}]
    #this is where we create the session for the number of items bough

    context = {
        'product_list': items
    }
    try:
        request.session['allItems']
    except:
        request.session['allItems'] = 0
    try:
        request.session['total']
    except:
        request.session['total'] = 0
    try:
         request.session['gTotal']
    except:
         request.session['gTotal'] = 0

    return render(request, "amadon_app/index.html", context)

def process(request):

    request.session['allItems'] += float(request.POST['quantity'])
    request.session['gTotal'] += float(request.POST['price'])
    request.session['total'] += float(request.POST['price']) * float(request.POST['quantity'])


    return render(request, "amadon_app/checkout.html")
