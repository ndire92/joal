from django.forms import ModelForm
from peche.models import DimPecheFinance
from django import forms

class DPFI(ModelForm):
    codeCommune = forms.CharField(label='Code Commune',widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    nomCommune = forms.CharField(label='Nom Commune',widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))

    OffrServicFinancPech = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    DemandApportPech = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    TypGaranExige = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    LongProcedCredi = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    TauInteret = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    DelaiRemboursMinMax = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    date = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))

    class Meta:
        model = DimPecheFinance
        fields = ['codeCommune' ,'nomCommune' ,'OffrServicFinancPech', 'DemandApportPech', 'TypGaranExige',
                  'LongProcedCredi', 'TauInteret', 'DelaiRemboursMinMax','date','date_modification']
