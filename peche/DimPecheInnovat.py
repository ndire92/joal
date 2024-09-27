from django.forms import ModelForm
from peche.models import DimPecheInnovat
from django import forms

class pecino(ModelForm):
    codeCommune = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    nomCommune = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))

    TechnoIntrod = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    TechnoAdopte = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    CausNoAdoption = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    CausTechnoNoAdop = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    date = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = DimPecheInnovat
        fields = ['codeCommune','nomCommune','TechnoIntrod','TechnoAdopte','CausNoAdoption','CausTechnoNoAdop','date','date_modification']
