
from django.conf import settings
from django.core.mail import EmailMessage
from django.urls import reverse
from django.views.generic.edit import FormView

from .forms import ContactForm


class LandingPageView(FormView):

    template_name = "landing_page/index.html"
    form_class = ContactForm

    def form_valid(self, form):
        info = form.cleaned_data
        email = EmailMessage(
            "Formulario de contacto Ilana",
            "Hola, {} con el email {} y el celular {}, ha solicitado que lo contactes por medio de la landing page de IlanaLab".format(info['name'], info['email'], info['celular']),
            settings.EMAIL_USER,
            ["czuniga@ilanalab.com"],
        )
        try:
            email.send()
        except e:
            print(e)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("index") + "?ok"
