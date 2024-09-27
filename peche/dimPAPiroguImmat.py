from django.forms import ModelForm, ChoiceField, IntegerField, Select, NumberInput
from peche.models import DimPAPiroguImmat

class PAPiroguImmat(ModelForm):
    TYPE_CHOICES = [
        ('type permis B longueur < à 13', 'type permis B longueur < à 13'),
        ('type permis C longueur > à 13', 'type permis C longueur > à 13'),
        ('A', 'type permis pêche à pied'),
    ]

    TypPermis = ChoiceField(
        label='Type de permis',
        choices=[('', 'Type de permis')] + TYPE_CHOICES,
        widget=Select(attrs={
            'placeholder': '',
            'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
            'class': 'form-control'
        })
    )

    NbrePiroguImmatPermis = IntegerField(
        label='Nombre de Pirogue Immatriculé avec permis',
        widget=NumberInput(attrs={
            'placeholder': '',
            'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
            'class': 'form-control'
        })
    )

    ANNEE_CHOICES = [
        ('2024', '2024'),
        ('2023', '2023'),
        ('2022', '2022'),
        ('2021', '2021'),
        ('2020', '2020'),
        ('2019', '2019'),
    ]

    annee = ChoiceField(
        label='Année enregistrée',
        choices=[('', 'Année')] + ANNEE_CHOICES,
        widget=Select(attrs={'class': 'form-select'})
    )

    annee_modification = ChoiceField(
        label='Année de modification',
        choices=[('', 'Année')] + ANNEE_CHOICES,
        widget=Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = DimPAPiroguImmat
        fields = ['TypPermis', 'NbrePiroguImmatPermis', 'annee', 'annee_modification']
