
# Create your views here.
from __future__ import unicode_literals

from django.shortcuts import render,  HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    items = [{"name": "farm", "earns": "10 through 20", {"name": "cave", "earns": "5 through 10")},
    {"name": "house", "earns": "2 through 5"}, {"name": "casino", "earns": "0-50"}]

    context = {
    'item_list' : items
    }

    return render(request, "ninja_app/index.html", context )
