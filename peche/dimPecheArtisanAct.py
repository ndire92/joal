from django.forms import ModelForm
from peche.models import DimPecheArtisanAct
from django import forms


class PecheArtisanAct(ModelForm):
    CodePostal = forms.IntegerField(
        label='Code Postal', widget=forms.NumberInput(attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }
        )
    )
    NomCommune = forms.CharField( label='Nom Commune',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    ActPech_Artisan= forms.CharField( label='Acteurs Pêche Artisanale',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbrActeur = forms.IntegerField(
    label='Nombre Acteurs de la Pêche artisanale',
    widget=forms.NumberInput(
        attrs={
            'placeholder': '',
            'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
            'class': 'form-control'
        }
    )
)


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
        model = DimPecheArtisanAct
        fields = ['CodePostal',
                        'NomCommune',
                        'ActPech_Artisan',
                        'NbrActeur',  
                        'annee',
                        'annee_modification' ]
