from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def depan(request):
    template = loader.get_template('depan.html')
    return HttpResponse(template.render())
def biodata(request):
    template = loader.get_template('biodata.html')
    return HttpResponse(template.render())
def History(request):
    template = loader.get_template('History.html')
    return HttpResponse(template.render())



