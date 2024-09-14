from django import forms
from home.models import contact, newsletter,comment,adresses,Order
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Invisible
# from django_recaptcha.fields import ReCaptchaField

class captcha (forms.Form):
    captcha = ReCaptchaField()
        # captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)

class contactform(forms.ModelForm):
    # captcha = CaptchaField()
    class Meta:
        model =contact
        fields=['name','content']
        #fields=['name','content']

class neeslettertform(forms.ModelForm):

    class Meta:
        model = newsletter
        fields=['email']

class commentform(forms.ModelForm):

    class Meta:
        model=comment
        fields=['name','cost','quality','Innovation','beauty','Services','Longevity', 'title','content','pro']

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
