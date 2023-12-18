# forms.py
from django import forms

class UserInputForm(forms.Form):
    domain_specific_keyword = forms.CharField()
    #specific_alert_keyword = forms.CharField()
    start_date = forms.DateField()
    end_date = forms.DateField()
    country = forms.CharField()
    language = forms.CharField()