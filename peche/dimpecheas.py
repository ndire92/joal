from django.forms import ModelForm
from peche.models import DimPecheAssure
from django import forms

class DPAS(ModelForm):
    codeCommune = forms.CharField(
        label='code postal commune',
        widget=forms.NumberInput(
            attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }
        )
    )
    
    nomCommune = forms.CharField(
        label='Nom Commune',
        widget=forms.TextInput(
            attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }
        )
    )

    OffreAssureExistPech = forms.CharField(label='Offreurs d’assurance Existant ou Non existant',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    TypeAssurancPech = forms.CharField(label='Type d’assurance ',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbreSouscripPech  = forms.CharField(label='Nombre de souscription',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbrePrimePech  = forms.CharField(label='Niveau des primes (cout de la souscription)',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    BesoinFormatPech = forms.CharField(label='Besoins en formation ',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    ActeurSensibilisePech = forms.CharField(label='Acteurs à la sensibilisation',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    ActeurFormatPech = forms.CharField(label='Acteurs à la formation',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    BesoinSensibilisePech = forms.CharField(label='Besoin en sensibilisation',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    ContraintGlobPech = forms.CharField(label='Contraintes globales sur la pêche',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    ContrainMajFilier = forms.CharField(label='Contraintes majeures par filière',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbrInfrastruStokCondition = forms.CharField(label='Nombre d’Infrastructures de stockage et de conditionnement (aires) ',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbrFourniEmblag = forms.CharField(label='Nombre de Fournisseurs d’emballage',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbrProdLabel = forms.CharField(label='Nombre de Label (produits labellisés)',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    date = forms.CharField(label='Date entrant',widget=forms.DateInput(
        attrs={'type': 'date', 'style':'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    date_modification = forms.CharField(label='Date de modification',widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'border: 2px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'}))
    
    class Meta:
        model = DimPecheAssure
        fields = ['codeCommune',
                    'nomCommune',
                    'OffreAssureExistPech',
                    'TypeAssurancPech',
                    'NbreSouscripPech',
                    'NbrePrimePech',
                    'BesoinFormatPech',
                    'ActeurSensibilisePech',
                    'ActeurFormatPech',
                    'BesoinSensibilisePech',
                    'ContraintGlobPech',
                    'ContrainMajFilier',
                    'NbrInfrastruStokCondition',
                    'NbrFourniEmblag',
                    'NbrProdLabel',
                    'annee','annee_modification']
