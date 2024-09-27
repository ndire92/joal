from django.forms import ModelForm
from peche.models import DimPechTransformArtisan
from django import forms

class pectranf(ModelForm):
    codeCommune = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    nomCommune = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    ActTransfArtisan = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    GrptTransformtrTA = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    TypServicOffrGIE = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    TypServicOffrAssocia = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    TypServicOffrOrgProf = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    FourniIntranMatTrans = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    SitTransform = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    MatEquipTransExist = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    TypProdTransfPeriod = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    SourcApproIntranMatTA = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    QteProdPeriodTA = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    QteProdTypeTA = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    TauxTransformArtisan = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    date = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;', 'class': 'form-control'}))

    class Meta:
        model = DimPechTransformArtisan
        fields = ['codeCommune','nomCommune','ActTransfArtisan','GrptTransformtrTA','TypServicOffrGIE','TypServicOffrAssocia','TypServicOffrOrgProf','FourniIntranMatTrans','SitTransform','MatEquipTransExist','TypProdTransfPeriod','SourcApproIntranMatTA','QteProdPeriodTA','QteProdTypeTA','TauxTransformArtisan','date','date_modification']
