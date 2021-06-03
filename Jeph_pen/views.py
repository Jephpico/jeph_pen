from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = 'homepage.html'