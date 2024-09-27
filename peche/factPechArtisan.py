from django.forms import ModelForm
from peche.models import FactPechArtisan
from django import forms


class Fact(ModelForm):
    CodePostal = forms.IntegerField(
        label='Code Postal', widget=forms.NumberInput(attrs={
            'placeholder': '',
            'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
            'class': 'form-control'
        })
    )
    NomCommune = forms.CharField(label='Nom Commune', widget=forms.TextInput(
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
        choices=[('', 'Année')] + ANNEE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    NbreGIEPecheur = forms.IntegerField(label='Nbr GIE Pecheur',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbrOrganiProfessPecheur = forms.IntegerField(label='Nbr Organisation Profess Pecheur',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    Nbr_AssociatPecheur = forms.IntegerField(label='Nbr Association Pecheur',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbreGIEMarey = forms.IntegerField(label='Nbre GIE Mareyeur ',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbrOrganiProfessMarey = forms.IntegerField(label='Nbr Organisation Profess Mareyeur',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))



    Nbr_AssociatMarey = forms.IntegerField(label='Nbr Association Mareyeur',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbreQuaiPech = forms.IntegerField(label='Nbre Quai Pecheur',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbrPirogBois = forms.IntegerField(label='Nbre de Pirogue en bois ',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbrePirogFibVer=forms.IntegerField(label='Nbre de Pirogue en Fibre ',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            })) 
    NbrPirogAlumin = forms.IntegerField(label='Nbre de Pirogue en Amlumiume ',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))  # Vous pouvez utiliser la valeur par défaut que vous préférez

    NbrePirogImmatri=forms.IntegerField(label='Nbre de Pirogue Immatriculée',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    Qteannuel_debarq = forms.IntegerField(label='Quantité annuel debarquée',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))

    ValeurComCaptAnnuel=forms.IntegerField(label='Valeure commerciale de la capture annuelle',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    VolumDebitCarb=forms.IntegerField(label='Volume débité en carburant (litre)',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    ValeurCommCarbu=forms.IntegerField(label='Valeur commerciale du carburant vendu (fcfa)',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    TotStatCarbu=forms.IntegerField(label='TotStatCarbu',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbrTotFabriqGlace=forms.IntegerField(label='Nombre total de fabriques de glace',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbrMareyTotDeclare=forms.IntegerField(label='Nombre total de mareyeurs déclarés',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbrMareyTotRecensmt=forms.IntegerField(label='Nombre de Mareyeurs total recensé',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbrPecheurTotRecensmt=forms.IntegerField(label='Nombre de pêcheurs total recensé',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbrPirogRenouvll=forms.IntegerField(label='Nombre de pirogue ayant renouvelé leur permisBC',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    QteApprovisPoisson=forms.IntegerField(label='Approvisionnement en poisson frais pour la transformation(kg)',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    QteTotProdTA=forms.IntegerField(label='Quantité totale de produits par la transformation artisanale (kg)',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    ValeurComProdTA=forms.IntegerField(label='Valeur commerciale de la production totale',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))
    NbreTotTypPirog=forms.IntegerField(label='Nombre total de type de pirogue ',widget=forms.NumberInput(
        attrs={
                'placeholder': '',
                'style': 'border: 1px solid #1da8dd; border-radius: 10px;',
                'class': 'form-control'
            }))


    annee_modification = forms.ChoiceField(
        label='Année de modification',
        choices=[('', 'Année')] + ANNEE_CHOICES,  # Option vide pour le libellé par défaut
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = FactPechArtisan
        fields = ['CodePostal','NomCommune','annee',
                     'NbreGIEPecheur',
                        'NbrOrganiProfessPecheur',
                        'Nbr_AssociatPecheur',
                        'NbreGIEMarey',
                         'NbrOrganiProfessMarey',
                         'Nbr_AssociatMarey',
                        'NbreQuaiPech',
                        'NbrPirogBois',
                        'NbrePirogFibVer',
                        'NbrPirogAlumin',
                        'NbrePirogImmatri',
                        'Qteannuel_debarq',
                        'ValeurComCaptAnnuel',
                        'VolumDebitCarb',
                        'ValeurCommCarbu',
                        'TotStatCarbu',
                        'NbrTotFabriqGlace',
                        'NbrMareyTotDeclare',
                        'NbrMareyTotRecensmt',
                        'NbrPecheurTotRecensmt',
				  'NbrPirogRenouvll',
				  'QteApprovisPoisson',
				  'QteTotProdTA',
				  'ValeurComProdTA',
				  'NbreTotTypPirog',
				  'annee_modification' ]

