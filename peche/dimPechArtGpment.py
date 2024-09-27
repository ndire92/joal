from django.forms import ModelForm
from peche.models import DimPechArtGpment
from django import forms


class Pechegroup (ModelForm):
    ActPech_Artisan= forms.CharField( label='Acteurs Pêche Artisanale',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    GroupmentActeur = forms.CharField( label='Groupements de pêcheurs',widget=forms.TextInput(
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
        model = DimPechArtGpment
        fields = ['ActPech_Artisan',
                        'GroupmentActeur', 
                        'annee',
                        'annee_modification']


