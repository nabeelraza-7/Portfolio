from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    """
    TheTemplateViewalreadycontainsallthelogic needed to display our template,
    we just need to specify the template’s name
    """
    template_name = 'home.html'

class AboutPageView(TemplateView):
    """
    TheTemplateViewalreadycontainsallthelogic needed to display our template,
    we just need to specify the template’s name
    """
    template_name = 'about.html'
