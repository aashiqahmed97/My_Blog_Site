from django.shortcuts import render, HttpResponse,redirect
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect


def index(request):
    return redirect('app_blog:blog_list')