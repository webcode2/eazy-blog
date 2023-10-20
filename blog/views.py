from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(req):
    return HttpResponse("home")


def all_articles(req):
    return HttpResponse('all_post')


def single_article(req):
    return HttpResponse('post')
