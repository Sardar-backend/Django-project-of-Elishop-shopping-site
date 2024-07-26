from django import forms
from home.models import contact, newsletter,comment
from captcha.fields import CaptchaField

class contactform(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model =contact
        fields='__all__'

class neeslettertform(forms.ModelForm):

    class Meta:
        model = newsletter
        fields=['email']

class commentform(forms.ModelForm):

    class Meta:
        model=comment
        fields=['name', 'title','content','email','pro']
