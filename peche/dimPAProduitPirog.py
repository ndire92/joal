from django.forms import ModelForm
from peche.models import DimPAProduitPirog
from django import forms


class PAProduitPirog (ModelForm):


    TypePirogu= forms.CharField( label='Nature de la pirogue',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    TypeProdPechPirog= forms.CharField( label='Type de produits pêchés par pirogue',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    IntrantPech = forms.CharField( label='Intrants ',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    MatUtilisePech= forms.CharField( label='Matériels utilisés',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    SourcApprovis_Intran= forms.CharField( label='Sources d’approvisionnement en intrants (essence ou gazoil)',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    SourcApprovis_Materiel= forms.CharField( label='Sources d’approvisionnement en matériels ',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    ANNEE_CHOICES = [
    ('2024', '2024'),
    ('2023', '2023'),
    ('2022', '2022'),
    ('2021', '2021'),
    ('2020', '2020'),
    ('2019', '2019'),
]

    annee = forms.ChoiceField(
    label='Année enregistrée',
    choices=[('', 'Année')] + ANNEE_CHOICES,  # Option vide pour le libellé par défaut
    widget=forms.Select(attrs={'class': 'form-select'})
)

    annee_modification = forms.ChoiceField(
    label='Année de modification',
    choices=[('', 'Année')] + ANNEE_CHOICES,  # Option vide pour le libellé par défaut
    widget=forms.Select(attrs={'class': 'form-select'})
)
    
    

    class Meta:
        model = DimPAProduitPirog
        fields = ['TypePirogu',
                  'TypeProdPechPirog',
                        'IntrantPech',
                        'MatUtilisePech',
                        'SourcApprovis_Intran',
                        'SourcApprovis_Materiel',
                        'annee',
                        'annee_modification']


