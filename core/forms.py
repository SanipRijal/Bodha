from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email', '')

        if validate_email(email) is False:
            raise ValidationError('Enter a valid Email address')
        else:
            return email
