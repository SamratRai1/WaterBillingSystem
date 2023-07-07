from django import forms
from accounts.models import Revenue, Users,Customers,Rates

class userforms(forms.ModelForm):
    class Meta:
        model=Users
        fields='__all__'

class customerforms(forms.ModelForm):
    class Meta:
        model=Customers
        fields='__all__'

class ratesforms(forms.ModelForm):
    class Meta:
        model=Rates
        fields='__all__'

