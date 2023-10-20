from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
from . import views


def default(req):
    return HttpResponseRedirect('/accounts/login')


def login(req):
    return HttpResponse("login")


def register(req):
    return HttpResponse("reg")
