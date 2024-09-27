from django.forms import ModelForm
from peche.models import DimPAProdTypeNiv
from django import forms


class PAProdTypeNiv (ModelForm):


    TypeProdHalieuPeriod= forms.CharField( label='Types de production halieutique par période',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    TypeProdHalieuHiver= forms.CharField( label='type de production halieutique pendant la saison hivernale',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NivCaptMoyenSortTypProd = forms.CharField( label='Niveau moyen de capture par type de production',widget=forms.TextInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NivPertPostCaptTypProd= forms.CharField( label='Niveau de perte post-capture par type de production',widget=forms.TextInput(
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
        model = DimPAProdTypeNiv
        fields = ['TypeProdHalieuPeriod',
                        'TypeProdHalieuHiver',  
                        'NivCaptMoyenSortTypProd',
                        'NivPertPostCaptTypProd',
                        'annee',
                        'annee_modification']


