from django import forms
from accounts.models import Customers, Revenue

class customerforms(forms.ModelForm):
    class Meta:
        model=Customers
        fields='__all__'

class revenueforms(forms.ModelForm):
    class Meta:
        model = Revenue
        fields='__all__'