from django.forms import ModelForm
from peche.models import DimPAPirogue
from django import forms

class PApirogue(ModelForm):

    TypePirogu = forms.CharField(label='Type de pirogue', widget=forms.TextInput(
        attrs={
            'placeholder': '',
            'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
            'class': 'form-control'
        }))
    NbrPirogu = forms.IntegerField(label='Nombre de Pirogue', widget=forms.NumberInput(
        attrs={
            'placeholder': '',
            'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
            'class': 'form-control'
        }))
    EspecCible = forms.CharField(label='Espece Ciblé', widget=forms.TextInput(
        attrs={
            'placeholder': '',
            'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
            'class': 'form-control'
        }))
    TypePecheur = forms.CharField(label='Type de Pêcheur', widget=forms.TextInput(
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
        model = DimPAPirogue
        fields = ['TypePirogu',
                  'NbrPirogu',
                  'EspecCible',
                  'TypePecheur',
                  'annee',
                  'annee_modification']



