from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView, FormView
from .forms import SubscribeForm
from .models import Subscribe, Header, OurCause, OurReach, Event, BannerImage
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


# Create your views here.
class IndexView(FormView):
    template_name = 'core/index.html'
    form_class = SubscribeForm
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['header'] = Header.objects.last()
        context['cause'] = OurCause.objects.all()
        context['reach'] = OurReach.objects.last()
        context['event'] = Event.objects.all()
        context['form'] = SubscribeForm()
        context['banner'] = BannerImage.objects.all()
        return context

    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name', '')
        last_name = form.cleaned_data.get('last_name', '')
        organization = form.cleaned_data.get('organization', '')
        email = form.cleaned_data.get('email', '')
        phone = form.cleaned_data.get('phone', '')
        location = form.cleaned_data.get('location', '')
        Subscribe.objects.create(first_name=first_name, last_name=last_name, organization=organization, email=email,
                                 phone=phone, location=location)
        to_email = 'bodhafoundation@gmail.com'
        mail_subject = 'IT training requested'
        message = render_to_string('core/subscription_email.html', {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'location': location,
            'phone': phone,
            'organization': organization
        })
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return super(IndexView, self).form_valid(form)
    #
    # def post(self, request, *args, **kwargs):
    #     context = self.get_context_data()
    #     if context["form"].is_valid():
    #         first_name = context["form"].cleaned_data.get('first_name', '')
    #         last_name = context["form"].cleaned_data.get('last_name', '')
    #         organization = context["form"].cleaned_data.get('organization', '')
    #         email = context["form"].cleaned_data.get('email', '')
    #         phone = context["form"].cleaned_data.get('phone', '')
    #         location = context["form"].cleaned_data.get('location', '')
    #         Subscribe.objects.create(first_name=first_name, last_name=last_name, organization=organization, email=email,
    #                                  phone=phone, location=location)
    #         to_email = 'bodhafoundation@gmail.com'
    #         mail_subject = 'IT training requested'
    #         message = render_to_string('core/subscription_email.html', {
    #             'email': email,
    #             'first_name': first_name,
    #             'last_name': last_name,
    #             'location': location,
    #             'phone': phone,
    #             'organization': organization
    #         })
    #         email = EmailMessage(
    #             mail_subject, message, to=[to_email]
    #         )
    #         email.send()
    #
    #     return super(TemplateView, self).render_to_response(context)

