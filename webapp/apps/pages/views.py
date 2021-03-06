from django.http import Http404
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.generic import TemplateView, DetailView

from webapp.apps.register.forms import SubscribeForm

from django.core.context_processors import csrf

from django.conf import settings

def settings_context_processor(request):
    return {'BLOG_URL': settings.BLOG_URL}

def subscribeform(request):
    if request.method == 'POST':
        subscribeform = SubscribeForm(request.POST)
        if subscribeform.is_valid():
            subscribeform.save()
    else:
        subscribeform = SubscribeForm()
    return subscribeform

def homepage(request):
    csrf_token = csrf(request)
    test = render(request, 'pages/home_content.html', {
        'csrv_token': csrf(request)['csrf_token'],
        'email_form': subscribeform(request),
        'section': {
            'active_nav': 'home',
            'title': 'Welcome to the Open Source Policy Center',
        }
    })

    return test

def aboutpage(request):
    test_1 = render(request, 'pages/about.html', {
        'csrv_token': csrf(request)['csrf_token'],
        'email_form': subscribeform(request),
        'section': {
            'active_nav': 'about',
            'title': 'About',
        }
    })
    return test_1

def newspage(request):
    return redirect(BLOG_URL)

def newsdetailpage(request):
    return redirect(BLOG_URL)
