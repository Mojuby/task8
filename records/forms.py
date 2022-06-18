from django import forms
from .models import Cust_Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Cust_Info
        fields = '__all__'