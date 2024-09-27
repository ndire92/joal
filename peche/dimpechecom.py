from django.forms import ModelForm
from peche.models import DimPecheCommerce
from django import forms


class DPC(ModelForm):

    codeCommune   = forms.CharField(label='Code Commune',widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    nomCommune  = forms.CharField(label='Nom Commune ',widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    ProdVendType   = forms.DecimalField( label='Production vendue (en tonne) par type de produit: ',widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    ProdVendCampgnInterSais   = forms.DecimalField(label='Production vendue (en tonne) par campagne Inter-saison (Looly)',widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    ProdVendCampgnHiver   = forms.DecimalField(label='Production vendue (en tonne) par campagne Hivernage (saison chaude):',widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    ProdVendCampSaisFroid   = forms.DecimalField(label='Production vendue (en tonne) par campagne Saison froide (Nör):',widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    ProdVendCampPrintem   = forms.DecimalField(label='Production vendue (en tonne) par campagne Printemps (Thiorone-inter-saison):',widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    Type_VentPech  = forms.CharField(label='Type de vente',widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    PriVentMoy_Prod  = forms.CharField(label='Prix Vendre Moyenne Pro',widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    Mod_ecoulement  = forms.CharField(label='Mode d’écoulement',widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    ClientPech  = forms.CharField(label='Client Peche',widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    
    date = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))  


    class Meta:
        model = DimPecheCommerce
        fields = ['codeCommune',
                    'nomCommune',
                    'ProdVendType',
                    'ProdVendCampgnInterSais',
                    'ProdVendCampgnHiver',
                    'ProdVendCampSaisFroid',
                    'ProdVendCampPrintem',
                    'Type_VentPech',
                    'PriVentMoy_Prod',
                    'Mod_ecoulement',
                    'ClientPech','date','date_modification']
