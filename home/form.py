from django import forms
from home.models import contact, newsletter,comment,adresses,Order
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
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

class adressform(forms.ModelForm):

    class Meta:
        model=adresses
        fields=['recipient_name','ostan','city','mobile_recver','Postal_code','content','user']

class ordrform(forms.ModelForm):

    class Meta:
        model=Order
        fields="__all__"

class userform(forms.ModelForm):

    class Meta:
        model=User
        fields=['username','email']
