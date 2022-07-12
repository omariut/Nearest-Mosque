from django import forms
from mosque.models import Mosque



class MosqueForm(forms.ModelForm):
    longitude = forms.FloatField()
    latitude = forms.FloatField()

    class Meta:
        model = Mosque
        exclude = ['location']
        