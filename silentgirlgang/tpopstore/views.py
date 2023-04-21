from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

import sellers.models as sellers_models
import buyers.models as buyers_models
# Create your views here.

def store(request):
    return HttpResponse("Coming Soon",)
