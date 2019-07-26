from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView


def home(request):
    #import pdb; pdb.set_trace()
    a = 10
    b = 20
    c = a * b
    return render(request, 'home.html', {'result':c})


def my_logout(request):
    logout(request)
    return redirect('home')


class HomePageView(TemplateView):
    template_name = 'home2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_variable'] = 'Hello, welcome!'
        return context


class MyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home3.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')





# FBV
# CBV