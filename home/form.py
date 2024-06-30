from django import forms
from home.models import contact, newsletter
class contactform(forms.ModelForm):

    class Meta:
        model =contact
        fields='__all__'
class neeslettertform(forms.ModelForm):

    class Meta:
        model = newsletter
        fields=['email']
