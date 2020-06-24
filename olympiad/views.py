from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView

from .forms import UserFormRegister


class BaseMainPage(TemplateView):
    template_name = 'index.html'


class FormRegister(FormView):
    form_class = UserFormRegister
    success_url = '/'
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return super(FormRegister, self).form_valid(form)