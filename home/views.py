from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView


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

# FBV
# CBV