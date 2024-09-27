from django.forms import ModelForm
from peche.models import DimPechComRepartition
from django import forms


class REPAT(ModelForm):


    TypRepartiProd= forms.CharField( label=' Type de Répartition par produit: ',widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 400px;', 'class': 'form-control'}))
    QteRepAnnuel  = forms.IntegerField(label='Quanntité Répartition Annuel',widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width:400px;', 'class': 'form-control'}))
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
        model = DimPechComRepartition
        fields = [
                    'TypRepartiProd',
                    'QteRepAnnuel',
                 
                 'annee',
                 'annee_modification']
