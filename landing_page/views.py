from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.


class LandingPageView(FormView):

    template_name = "landing_page/index.html"
    form_class = ContactForm

    def form_valid(self, form):
        #send mail
        info = form.cleaned_data
        print(info)
        email = EmailMessage(
            "Formulario de contacto Ilana",
            "Hola, {} con el email {} y el celular {}, ha solicitado que lo contactes por medio de la landing page de IlanaLab".format(info['name'], info['email'], info['celular']),
            settings.EMAIL_USER,#el que envía
            ["jsanz@apptitud.com.co"],#el que recibe xd
        )
        try:
            email.send()  
        except e:
            print(e)     
        return super().form_valid(form)


    def get_success_url(self):
        return reverse("index") + "?ok"