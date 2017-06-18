from django.shortcuts import render
from django.views.generic import TemplateView #ListView ,FormView,
from .models import PersonModel

class Index(TemplateView):
    template_name = 'index.html'

    def get_roots(self):
        return PersonModel.objects.filter(parent=None).first()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['root'] = self.get_roots()
        return context