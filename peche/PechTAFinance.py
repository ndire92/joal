from django.forms import ModelForm
from peche.models import DimPechTAFinance
from django import forms


class pectafina(ModelForm):
    codeCommune = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;','class': 'form-control'}))
    nomCommune = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;','class': 'form-control'}))
   

    OffrServicFinancTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;','class': 'form-control'}))
    DemandApportTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;','class': 'form-control'}))
    TypGaranExigeTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;','class': 'form-control'}))
    LongProcedCrditTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;','class': 'form-control'}))
    MontanMoyTA = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;','class': 'form-control'}))
    TauInterTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;','class': 'form-control'}))
    DelaiRemboursMinMaxTA = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;','class': 'form-control'}))
    date = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;','class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;','class': 'form-control'}))
    
    
    class Meta:
        model = DimPechTAFinance
        fields = ['codeCommune','nomCommune','OffrServicFinancTA', 'DemandApportTA', 'TypGaranExigeTA',
                  'LongProcedCrditTA','MontanMoyTA', 'TauInterTA', 'DelaiRemboursMinMaxTA','date','date_modification']
