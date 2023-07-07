from django import forms
from accounts.models import Customers

class customerforms(forms.ModelForm):
    class Meta:
        model=Customers
        fields='__all__'