from django import forms
from .models import Rapper,Audience
#Forms start from here

class RapperForm(forms.ModelForm):
    class Meta:
        model = Rapper
        fields = ['name','stage_name','email','mobile_number','instagram',] 

class AudienceForm(forms.ModelForm):
    class Meta:
        model = Audience
        fields = ['name','email','mobile_number','instagram','three_rappers','three_songs','three_rap_songs']