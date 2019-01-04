from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import  Marks, Students

# Create your views here.
def index(request):
    context = {
        "students": Marks.objects.all()
    }
    return render(request, "login/index.html", context)
