from peche.dimPAPiroguImmat import PAPiroguImmat
from peche.dimPAPirogue import PApirogue
from peche.dimPAProdTypeNiv import PAProdTypeNiv
from peche.dimPAProduitPirog import PAProduitPirog
from peche.dimPechArtGpment import Pechegroup
from peche.dimPechComRepartition import REPAT
from peche.dimPecheArtisanAct import PecheArtisanAct

from django.shortcuts import render
import json


from django.core.serializers import serialize
from django.forms.widgets import TextInput
from django.shortcuts import render, redirect
from django.db import models
from django.contrib import messages
from peche.DimPecheInnovat import pecino
from peche.PechTAAssurance import petttassu
from peche.PechTACommerc import pectom
from peche.PechTAFinance import pectafina
from peche.PechTransformArtisan import pectranf
from peche.PecheTAInnovation import pectaino
from django.http import HttpResponseRedirect, JsonResponse
from peche.dimpechear import DPA
from peche.dimpecheas import DPAS
from peche.dimpechecom import DPC
from peche.dimpechefi import DPFI
from django.db.models import Sum
from peche.factPechArtisan import Fact
from peche.models import DimPAPiroguImmat,DimPAProduitPirog,DimPAProdTypeNiv,FactPechArtisan,DimPechComRepartition, DimPechTAAssurance, DimPechTACommerc, DimPechTAFinance, DimPechTransformArtisan, DimPecheArtisan, DimPecheAssure, DimPecheCommerce, DimPecheFinance, DimPecheInnovat, DimPecheTAInnovat, DimPAPirogue, DimPechArtGpment, DimPecheArtisan, DimPecheArtisanAct


# test
from .models import DimPecheCommerce



# def artisan_fishing_chart(request):
#  data = DimPecheArtisan.objects.values('nomCommune').annotate(NbrActeurTotal=Sum('NbrActeur'))
#   return JsonResponse(list(data), safe=False)

# def artisan_fishing_chart(request):
# donnees = DimPecheArtisan.objects.all()  # Extrayez vos données depuis le modèle Django
# return render(request, 'peche/hm.html', {'donnees': donnees})

# views.py


def get_data_for_joal_fadiouth(request):
    # Récupérer les données pour la commune "Joal Fadiouth"

    joal_fadiouth_data = DimPecheArtisan.objects.filter(
        nomCommune="joal").first()

    if joal_fadiouth_data:
        types_acteurs = ["Acteurs", "GIE Pêcheur", "Associations",
                         "Organisations professionnelles", "GIE Mareyeur"]
        valeurs = [
            joal_fadiouth_data.NbrActeur,
            joal_fadiouth_data.NbreGIEPecheur,
            joal_fadiouth_data.Nbr_AssociatPecheur,
            joal_fadiouth_data.NbrOrganiProfessPecheur,
            joal_fadiouth_data.NbreGIEMarey
        ]
        couleurs = ["#FF5733", "#33FF57", "#3357FF", "#57FF33", "#5733FF"]

        data = {
            "types_acteurs": types_acteurs,
            "valeurs": valeurs,
            "couleurs": couleurs,
        }
    else:
        data = None

    # Convertir les données en JSON
    data_json = json.dumps(data)

    return render(request, "peche/hm.html", {"data": data_json})


def get_peche_artisan_data(request):

    # Récupérez les données de votre modèle DimPecheArtisan
    data = DimPecheArtisan.objects.all()
    dataObjects = DimPecheArtisan.objects.all()
    da = DimPecheAssure.objects.all()
    # Sérialiser les données en JSON
    data_json = serialize('json', data)
    # Initialisez les totaux pour les champs spécifiés
    total_nbr_acteur = 0
    total_nbre_gie_pecheur = 0
    total_nbr_organi_profess_pecheur = 0
    total_nbr_associat_pecheur = 0
    total_nbre_gie_marey = 0
    total_nbr_organi_profess_marey = 0
    total_nbr_associat_marey = 0
    total_nbre_quai_pech = 0
    total_qteannuel_debarq = 0
    # pirogue
    total_nbre_pirogue_bois = 0
    total_nbre_pirogue_fibre = 0
    total_nbre_pirogue_alum = 0
    total_nbre_pirogue_imma = 0
    # Préparez les données pour le diagramme
    x = [entry.date.year for entry in data]

    y1 = [entry.NbrActeur for entry in data]
    y2 = [entry.NbreGIEPecheur for entry in data]
    y3 = [entry.Nbr_AssociatPecheur for entry in data]
    y4 = [entry.NbreGIEMarey for entry in data]
    y5 = [entry.NbrOrganiProfessPecheur for entry in data]
    y6 = [entry.NbrOrganiProfessMarey for entry in data]
    y7 = [entry.NbreQuaiPech for entry in data]
    y8 = [entry.Qteannuel_debarq for entry in data]

    # Parcourez les enregistrements pour calculer les totaux
    for dataObject in dataObjects:
        total_nbr_acteur += dataObject.NbrActeur
        total_nbre_gie_pecheur += dataObject.NbreGIEPecheur
        total_nbr_organi_profess_pecheur += dataObject.NbrOrganiProfessPecheur
        total_nbr_associat_pecheur += dataObject.Nbr_AssociatPecheur
        total_nbre_gie_marey += dataObject.NbreGIEMarey
        total_nbr_organi_profess_marey += dataObject.NbrOrganiProfessMarey  # Correction ici
        total_nbr_associat_marey += dataObject.Nbr_AssociatMarey  # Correction ici
        total_nbre_quai_pech += dataObject.NbreQuaiPech
        total_qteannuel_debarq += dataObject.Qteannuel_debarq
        # pirogue
        total_nbre_pirogue_bois += dataObject.NbrPirogBois
        total_nbre_pirogue_fibre += dataObject.NbrePirogFibVer
        total_nbre_pirogue_alum += dataObject.NbrPirogAlumin
        total_nbre_pirogue_imma += dataObject.NbrePirogImmatri

        d = [entry.date.year for entry in da]
        total_nbre_SouscripPech = sum(entry.NbreSouscripPech for entry in da)
        total_nbre_PrimePech = sum(entry.NbrePrimePech for entry in da)
        total_nbre_FourniEmblag = sum(entry.NbrFourniEmblag for entry in da)
        total_nbre_ProdLabel = sum(entry.NbrProdLabel for entry in da)
    for entry in da:
        year = entry.date.year
        souscriptions = entry.NbreSouscripPech
        fournitures = entry.NbrFourniEmblag
        labels = entry.NbrProdLabel

    return render(request, "pa/donne.html", {'x': x,

                                             'y1': y1,
                                             'y2': y2,
                                             'y3': y3,
                                             'y4': y4,
                                             'y5': y5,
                                             'y6': y6,
                                             'y7': y7,
                                             'y8': y8,


                                             'total_nbr_acteur': total_nbr_acteur,
                                             'total_nbre_gie_pecheur': total_nbre_gie_pecheur,
                                             'total_nbr_organi_profess_pecheur': total_nbr_organi_profess_pecheur,
                                             'total_nbr_associat_pecheur': total_nbr_associat_pecheur,
                                             'total_nbre_gie_marey': total_nbre_gie_marey,
                                             'total_nbr_organi_profess_marey': total_nbr_organi_profess_marey,
                                             'total_nbr_associat_marey': total_nbr_associat_marey,
                                             'total_nbre_quai_pech': total_nbre_quai_pech,
                                             'total_qteannuel_debarq': total_qteannuel_debarq,
                                             # pirogue
                                             'total_nbre_pirogue_bois': total_nbre_pirogue_bois,
                                             'total_nbre_pirogue_fibre': total_nbre_pirogue_fibre,
                                             'total_nbre_pirogue_alum': total_nbre_pirogue_alum,
                                             'total_nbre_pirogue_imma': total_nbre_pirogue_imma,

                                             'data': data_json,
                                             'd': d,
                                             'total_nbre_SouscripPech': total_nbre_SouscripPech,
                                             'total_nbre_PrimePech': total_nbre_PrimePech,
                                             'total_nbre_FourniEmblag': total_nbre_FourniEmblag,
                                             'total_nbre_ProdLabel': total_nbre_ProdLabel,
                                             'year': year,
                                             'souscriptions': souscriptions,
                                             'fournitures': fournitures,
                                             'labels': labels,
                                             'dataObject': DimPecheArtisan.objects.all()})

# pirogue


# Votre vue Django


def pirogue(request):

    return render(request, 'peche/hm.html')

# get data asure


def get_peche_assurance_data(request):
    da = DimPecheAssure.objects.all()

    total_nbre_SouscripPech = sum(entry.NbreSouscripPech for entry in da)
    total_nbre_PrimePech = sum(entry.NbrePrimePech for entry in da)
    total_nbre_FourniEmblag = sum(entry.NbrFourniEmblag for entry in da)
    total_nbre_ProdLabel = sum(entry.NbrProdLabel for entry in da)

    return render(request, "peche/hm.html", {
        'data_list': data_list,
        'da': da,
        'total_nbre_SouscripPech': total_nbre_SouscripPech,
        'total_nbre_PrimePech': total_nbre_PrimePech,
        'total_nbre_FourniEmblag': total_nbre_FourniEmblag,
        'total_nbre_ProdLabel': total_nbre_ProdLabel,
        'year': year,
        'souscriptions': souscriptions,
        'fournitures': fournitures,
        'labels': labels,

    })


def mesur(request):
    data = DimPecheAssure.objects.all()
    x = [entry.date.year for entry in data]
    total_nbre_SouscripPech = sum(entry.NbreSouscripPech for entry in data)
    total_nbre_PrimePech = sum(entry.NbrePrimePech for entry in data)
    total_nbre_FourniEmblag = sum(entry.NbrFourniEmblag for entry in data)
    total_nbre_ProdLabel = sum(entry.NbrProdLabel for entry in data)

    data_list = []

    for entry in data:
        year = entry.date.year
        souscriptions = entry.NbreSouscripPech
        fournitures = entry.NbrFourniEmblag
        labels = entry.NbrProdLabel

        # Append data for each entry to the list
        data_list.append({
            'year': year,
            'souscriptions': souscriptions,
            'fournitures': fournitures,
            'labels': labels,
        })

    return render(request, 'peche/mesure.html', {
        'data_list': data_list,

        'total_nbre_SouscripPech': total_nbre_SouscripPech,
        'total_nbre_PrimePech': total_nbre_PrimePech,
        'total_nbre_FourniEmblag': total_nbre_FourniEmblag,
        'total_nbre_ProdLabel': total_nbre_ProdLabel,
        'year': year,
        'souscriptions': souscriptions,
        'fournitures': fournitures,
        'labels': labels,

    })


def total_mesures(request):
    # Récupérez la première (et unique) instance de TotalMesure
    total_mesure = TotalMesure.objects.first()
    return render(request, 'peche/total_mesures.html', {'total_mesure': total_mesure})


def pec_art(request):
    if request.method == 'POST':
        form = DPA(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Successfully Added!")
            return redirect('/peche/dimpecart/')
    else:
        form = DPA()

    dataObjects = DimPecheArtisan.objects.all()

    # Initialisez les totaux pour les champs spécifiés
    total_nbr_acteur = 0
    total_nbre_gie_pecheur = 0
    total_nbr_organi_profess_pecheur = 0
    total_nbr_associat_pecheur = 0
    total_nbre_gie_marey = 0
    total_nbr_organi_profess_marey = 0
    total_nbr_associat_marey = 0
    total_nbre_quai_pech = 0
    total_qteannuel_debarq = 0

    # Parcourez les enregistrements pour calculer les totaux
    for dataObject in dataObjects:
        total_nbr_acteur += dataObject.NbrActeur
        total_nbre_gie_pecheur += dataObject.NbreGIEPecheur
        total_nbr_organi_profess_pecheur += dataObject.NbrOrganiProfessPecheur
        total_nbr_associat_pecheur += dataObject.Nbr_AssociatPecheur
        total_nbre_gie_marey += dataObject.NbreGIEMarey
        total_nbr_organi_profess_marey += dataObject.NbrOrganiProfessMarey  # Correction ici
        total_nbr_associat_marey += dataObject.Nbr_AssociatMarey  # Correction ici
        total_nbre_quai_pech += dataObject.NbreQuaiPech
        total_qteannuel_debarq += dataObject.Qteannuel_debarq

    return render(request, 'peche/dimpecheart.html', {
        'form': form,
        'total_nbr_acteur': total_nbr_acteur,
        'total_nbre_gie_pecheur': total_nbre_gie_pecheur,
        'total_nbr_organi_profess_pecheur': total_nbr_organi_profess_pecheur,
        'total_nbr_associat_pecheur': total_nbr_associat_pecheur,
        'total_nbre_gie_marey': total_nbre_gie_marey,
        'total_nbr_organi_profess_marey': total_nbr_organi_profess_marey,
        'total_nbr_associat_marey': total_nbr_associat_marey,
        'total_nbre_quai_pech': total_nbre_quai_pech,
        'total_qteannuel_debarq': total_qteannuel_debarq,
        'dataObject': DimPecheArtisan.objects.all()
    })

# update art


def update_ar(request, id):
    dataObject = DimPecheArtisan.objects.get(id=id)
    form = DPA(instance=dataObject)
    if request.method == 'POST':
        form = DPA(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpecart/')

    context = {

        'form': form

    }
    return render(request, 'peche/dimpecheart.html', context)


def delete_ar(request, id):
    dataObject = DimPecheArtisan.objects.get(id=id)
    if request.method == 'POST':
        dataObject.delete()
        return redirect('/peche/dimpecart/')
    context = {

        'item': dataObject, }
    return render(request, 'peche/delete_ar.html', context)
#mise a jours

def pec_artact(request):
    if request.method == 'POST':
        form = PecheArtisanAct(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Successfully Added!")
            return redirect('/peche/dimact/')
    else:
        form = PecheArtisanAct()

    dataObjects = DimPecheArtisanAct.objects.all()

    # Initialisez les totaux pour les champs spécifiés
    total_nbr_acteur = 0
    total_nbre_gie_pecheur = 0
    total_nbr_organi_profess_pecheur = 0
    total_nbr_associat_pecheur = 0
    total_nbre_gie_marey = 0
    total_nbr_organi_profess_marey = 0
    total_nbr_associat_marey = 0
    total_nbre_quai_pech = 0
    total_qteannuel_debarq = 0

    # Parcourez les enregistrements pour calculer les totaux
    for dataObject in dataObjects:
        total_nbr_acteur += dataObject.NbrActeur
       #  total_nbre_gie_pecheur += dataObject.NbreGIEPecheur
       #  total_nbr_organi_profess_pecheur += dataObject.NbrOrganiProfessPecheur
        # total_nbr_associat_pecheur += dataObject.Nbr_AssociatPecheur
       #  total_nbre_gie_marey += dataObject.NbreGIEMarey
       #  total_nbr_organi_profess_marey += dataObject.NbrOrganiProfessMarey  # Correction ici
       #  total_nbr_associat_marey += dataObject.Nbr_AssociatMarey  # Correction ici
        # total_nbre_quai_pech += dataObject.NbreQuaiPech
        # total_qteannuel_debarq += dataObject.Qteannuel_debarq

    return render(request, 'peche/dimPecheArtisanAct.html', {
        'form': form,
        'total_nbr_acteur': total_nbr_acteur,
        # 'total_nbre_gie_pecheur': total_nbre_gie_pecheur,
        # 'total_nbr_organi_profess_pecheur': total_nbr_organi_profess_pecheur,
        # 'total_nbr_associat_pecheur': total_nbr_associat_pecheur,
        # 'total_nbre_gie_marey': total_nbre_gie_marey,
        # 'total_nbr_organi_profess_marey': total_nbr_organi_profess_marey,
        # 'total_nbr_associat_marey': total_nbr_associat_marey,
        # 'total_nbre_quai_pech': total_nbre_quai_pech,
        # 'total_qteannuel_debarq': total_qteannuel_debarq,
        'dataObject': DimPecheArtisanAct.objects.all()
    })

# update art


def update_act(request, id):
    dataObject = DimPecheArtisanAct.objects.get(id=id)
    form = PecheArtisanAct(instance=dataObject)
    if request.method == 'POST':
        form = PecheArtisanAct(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimact/')

    context = {

        'form': form

    }
    return render(request, 'peche/dimPecheArtisanAct.html', context)


def delete_act(request, id):
    dataObject = DimPecheArtisanAct.objects.get(id=id)
    if request.method == 'POST':
        dataObject.delete()
        return redirect('/peche/dimact/')
    context = {

        'item': dataObject, }
    return render(request, 'peche/delete_act.html', context)

def pech_goupe(request):
    if request.method == 'POST':
        form = Pechegroup(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Successfully Added!")
            return redirect('/peche/dimpechgpt/')
    else:
        form = Pechegroup()

    # Whether it's a GET request or the form is not valid, always return a response
    return render(request, 'peche/dimPechArtGpment.html', {'form': form, 'dataObject': DimPechArtGpment.objects.all()})


   
# update group
def update_grpt(request, id):
    dataOf = DimPechArtGpment.objects.get(id=id)
    form =Pechegroup(instance=dataOf)
    if request.method == 'POST':
        form = Pechegroup(request.POST, instance=dataOf)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpechgpt/')

    context = {

        'form': form,

    }
    
    return render(request, 'peche/dimPechArtGpment.html', context)


def delete_grpt(request, id):
    dataOf = DimPechArtGpment.objects.get(id=id)
    if request.method == 'POST':
        dataOf.delete()
        return redirect('/peche/dimpechgpt/')
    context = {

        'item': dataOf, }
    return render(request, 'peche/delete_grpt.html', context)

#end groupement pêche

#PApIROGUE
def pech_pirogue(request):
    if request.method == 'POST':
        form =PApirogue(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpechpirogue/')
    else:
        form =PApirogue()

        return render(request, 'peche/dimPAPirogue.html', {'form': form, 'dataObject': DimPAPirogue.objects.all()})


# update pirogue
def update_piro(request, id):
    dataOf = DimPAPirogue.objects.get(id=id)
    form = PApirogue(instance=dataOf)  # Use PApirogue consistently here
    if request.method == 'POST':
        form = PApirogue(request.POST, instance=dataOf)  # Use PApirogue consistently here
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Updated!")
            return redirect('/peche/dimpechpirogue/')

    context = {
        'form': form,
    }
    return render(request, 'peche/dimPAPirogue.html', context)


def delete_piro(request, id):
    dataOf = DimPAPirogue.objects.get(id=id)
    if request.method == 'POST':
        dataOf.delete()
        return redirect('/peche/dimpechpirogue/')
    context = {

        'item': dataOf, }
    return render(request, 'peche/delete_piro.html', context)

#end pirogue

#PApirogueimat
def pech_immat(request):
    if request.method == 'POST':
        form = PAPiroguImmat(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpechimmat/')
    else:
        form =PAPiroguImmat()

        return render(request, 'peche/dimPAPiroguImmat.html', {'form': form, 'dataObject':DimPAPiroguImmat.objects.all()})


# update immat
def update_imat(request, id):
    dataOf = DimPAPiroguImmat.objects.get(id=id)
    form = PAPiroguImmat(instance=dataOf)
    if request.method == 'POST':
        form = PAPiroguImmat(request.POST, instance=dataOf)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpechimmat/')

    context = {

        'form': form,

    }
    return render(request, 'peche/dimPAPiroguImmat.html', context)


def delete_imat(request, id):
    dataOf = DimPAPiroguImmat.objects.get(id=id)
    if request.method == 'POST':
        dataOf.delete()
        return redirect('/peche/dimpechimmat/')
    context = {

        'item': dataOf, }
    return render(request, 'peche/delete_imat.html', context)

#end pirogueimmtri

#produitpirogue
def pech_propirogue(request):
    if request.method == 'POST':
        form = PAProduitPirog(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpechprod/')
    else:
        form =PAProduitPirog()

        return render(request, 'peche/dimPAProduitPirog.html', {'form': form, 'dataObject': DimPAProduitPirog.objects.all()})


# update produit pirog
def update_prodp(request, id):
    dataOf = DimPAProduitPirog.objects.get(id=id)
    form = PAProduitPirog(instance=dataOf)
    if request.method == 'POST':
        form = PAProduitPirog(request.POST, instance=dataOf)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpechprod/')

    context = {

        'form': form,

    }
    return render(request, 'peche/dimPAProduitPirog.html', context)


def delete_prodp(request, id):
    dataOf = DimPAProduitPirog.objects.get(id=id)
    if request.method == 'POST':
        dataOf.delete()
        return redirect('/peche/dimpechprod/')
    context = {

        'item': dataOf, }
    return render(request, 'peche/delete_prodp.html', context)

#end produit pirogue

#protypeniv
def pech_typeniv(request):
    if request.method == 'POST':
        form = PAProdTypeNiv(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpechniv/')
    else:
        form =PAProdTypeNiv()

        return render(request, 'peche/dimPAProdTypeNiv.html', {'form': form, 'dataObject': DimPAProdTypeNiv.objects.all()})


# update niv
def update_niv(request, id):
    dataOf = DimPAProdTypeNiv.objects.get(id=id)
    form = PAProdTypeNiv(instance=dataOf)
    if request.method == 'POST':
        form = PAProdTypeNiv(request.POST, instance=dataOf)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpechniv/')

    context = {

        'form': form,

    }
    return render(request, 'peche/dimPAProdTypeNiv.html', context)


def delete_niv(request, id):
    dataOf = DimPAProdTypeNiv.objects.get(id=id)
    if request.method == 'POST':
        dataOf.delete()
        return redirect('/peche/dimpechniv/')
    context = {

        'item': dataOf, }
    return render(request, 'peche/delete_niv.html', context)

#endprotypeniv


#fact
#fact
def pech_fact(request):
    if request.method == 'POST':
        form = Fact(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Successfully Added!")
            return redirect('/peche/dimfact/')
        else:
            # Handle the case when the form is not valid
            messages.error(request, "Form is not valid. Please check the data.")
    else:
        form = Fact()

    return render(request, 'peche/FactPechArtisan.html', {'form': form, 'dataObject': FactPechArtisan.objects.all()})

# update fact
def update_fact(request, id):
    dataOf = FactPechArtisan.objects.get(id=id)
    form = Fact(instance=dataOf)
    if request.method == 'POST':
        form = Fact(request.POST, instance=dataOf)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimfact/')

    context = {

        'form': form,

    }
    return render(request, 'peche/FactPechArtisan.html', context)


def delete_fact(request, id):
    dataOf = FactPechArtisan.objects.get(id=id)
    if request.method == 'POST':
        dataOf.delete()
        return redirect('/peche/dimfact/')
    context = {

        'item': dataOf, }
    return render(request, 'peche/delete_fact.html', context)

#end fac
#DimPechComRepartition
def pech_ComRepartition(request):
    if request.method == 'POST':
        form = REPAT(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimrepart/')
    else:
        form =REPAT()

        return render(request, 'peche/dimPechComRepartition.html', {'form': form, 'dataObject': DimPechComRepartition.objects.all()})


# update repart
def update_repart(request, id):
    dataOf = DimPechComRepartition.objects.get(id=id)
    form = REPAT(instance=dataOf)
    if request.method == 'POST':
        form = REPAT(request.POST, instance=dataOf)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimrepart/')

    context = {

        'form': form,

    }
    return render(request, 'peche/dimPechComRepartition.html', context)


def delete_repart(request, id):
    dataOf = DimPechComRepartition.objects.get(id=id)
    if request.method == 'POST':
        dataOf.delete()
        return redirect('/peche/dimrepart/')
    context = {

        'item': dataOf, }
    return render(request, 'peche/delete_repart.html', context)

#end DimPechComRepartition

#end mise jours

def pech_assu(request):
    if request.method == 'POST':
        form = DPAS(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Successfully Added!")
            return redirect('/peche/dimpecass/')
    else:
        form = DPAS()

    dataObjects = DimPecheAssure.objects.all()
    # Initialisez les totaux pour les champs spécifiés
    total_nbre_souscrip_Pech = 0

    # Parcourez les enregistrements pour calculer les totaux

    for dataObject in dataObjects:
        total_nbre_souscrip_Pech += dataObject.NbreSouscripPech

    return render(request, 'peche/dimpecheass.html', {'form': form, 'total_nbre_souscrip_Pech': total_nbre_souscrip_Pech, 'dataObject': DimPecheAssure.objects.all()})

# update ass


def update_ass(request, id):
    dataOd = DimPecheAssure.objects.get(id=id)
    form = DPAS(instance=dataOd)
    if request.method == 'POST':
        form = DPAS(request.POST, instance=dataOd)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpecass/')

    context = {

        'form': form,

    }
    return render(request, 'peche/dimpecheass.html', context)


def delete_ass(request, id):
    dataOd = DimPecheAssure.objects.get(id=id)
    if request.method == 'POST':
        dataOd.delete()
        return redirect('/peche/dimpecass/')
    context = {

        'item': dataOd, }
    return render(request, 'peche/delete_ass.html', context)


def pech_fin(request):
    if request.method == 'POST':
        form = DPFI(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpecfin/')
    else:
        form = DPFI()

        return render(request, 'peche/dimpechefin.html', {'form': form, 'dataObject': DimPecheFinance.objects.all()})


# update finace
def update_fin(request, id):
    dataOf = DimPecheFinance.objects.get(id=id)
    form = DPFI(instance=dataOf)
    if request.method == 'POST':
        form = DPFI(request.POST, instance=dataOf)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpecfin/')

    context = {

        'form': form,

    }
    return render(request, 'peche/dimpechefin.html', context)


def delete_fin(request, id):
    dataOf = DimPecheFinance.objects.get(id=id)
    if request.method == 'POST':
        dataOf.delete()
        return redirect('/peche/dimpecfin/')
    context = {

        'item': dataOf, }
    return render(request, 'peche/delete_fin.html', context)


def pech_ec(request):
    if request.method == 'POST':
        form = DPC(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/dimpecec/')
    else:
        form = DPC()

    dataObjects = DimPecheCommerce.objects.all()
    # Initialisez les totaux pour les champs spécifiés
    priventmoy_prod = 0

    # Parcourez les enregistrements pour calculer les totaux
    for dataObject in dataObjects:
        priventmoy_prod += dataObject.PriVentMoy_Prod

    return render(request, 'peche/dimpechecomm.html', {'form': form, 'priventmoy_prod': priventmoy_prod, 'dataObject': DimPecheCommerce.objects.all()})


# update commm
def update_com(request, id):
    dataOC = DimPecheCommerce.objects.get(id=id)
    form = DPC(instance=dataOC)
    if request.method == 'POST':
        form = DPC(request.POST, instance=dataOC)
        if form.is_valid():
            messages.success(request, " Are Successfully Added !")
            form.save()
            return redirect('/peche/dimpecec/')

    context = {

        'form': form,

    }
    return render(request, 'peche/dimpechecomm.html', context)


def delete_com(request, id):
    dataOC = DimPecheCommerce.objects.get(id=id)
    if request.method == 'POST':
        dataOC.delete()
        return redirect('/peche/dimpecec/')
    context = {

        'item': dataOC, }
    return render(request, 'peche/delete_com.html', context)


def pech_inov(request):
    if request.method == 'POST':
        form = pecino(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_ino/')
    else:
        form = pecino()
        return render(request, 'peche/peche_ino.html', {'form': form, 'dataObject': DimPecheInnovat.objects.all()})


# update commm
def update_ino(request, id):
    dataOC = DimPecheInnovat.objects.get(id=id)
    form = pecino(instance=dataOC)
    if request.method == 'POST':
        form = pecino(request.POST, instance=dataOC)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_ino/')

    context = {

        'form': form,

    }
    return render(request, 'peche/peche_ino.html', context)


def delete_ino(request, id):
    dataOC = DimPecheInnovat.objects.get(id=id)
    if request.method == 'POST':
        dataOC.delete()
        return redirect('/peche/pech_ino/')
    context = {

        'item': dataOC, }
    return render(request, 'peche/delete_ino.html', context)


# peche trans

def pechtrans(request):
    if request.method == 'POST':
        form = pectranf(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_trans/')
    else:
        form = pectranf()
        return render(request, 'peche/peche_transf.html', {'form': form, 'dataObject': DimPechTransformArtisan.objects.all()})


# update commm
def update_trs(request, id):
    dataOC = DimPechTransformArtisan.objects.get(id=id)
    form = pectranf(instance=dataOC)
    if request.method == 'POST':
        form = pectranf(request.POST, instance=dataOC)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_trans/')

    context = {

        'form': form,

    }
    return render(request, 'peche/peche_transf.html', context)


def delete_trs(request, id):
    dataOC = DimPechTransformArtisan.objects.get(id=id)
    if request.method == 'POST':
        dataOC.delete()
        return redirect('/peche/pech_trans/')
    context = {

        'item': dataOC, }
    return render(request, 'peche/delete_trans.html', context)


# pechetaassu
def pechtassu(request):
    if request.method == 'POST':
        form = petttassu(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Are Successfully Added !")
            return redirect('/peche/pech_taassu/')
    else:
        form = petttassu()

    dataObjects = DimPechTAAssurance.objects.all()
    # Initialisez les totaux pour les champs spécifiés
    total_nbr_souscrt_ta = 0

    # Parcourez les enregistrements pour calculer les totaux
    for dataObject in dataObjects:
        total_nbr_souscrt_ta += dataObject.NbrSouscripTA

    return render(request, 'peche/peche_tass.html', {'form': form, 'total_nbr_souscrt_ta': total_nbr_souscrt_ta, 'dataObject': DimPechTAAssurance.objects.all()})



# update commm
def update_tassu(request, id):
    dataOC = DimPechTAAssurance.objects.get(id=id)
    form = petttassu(instance=dataOC)
    if request.method == 'POST':
        form = petttassu(request.POST, instance=dataOC)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_taassu/')

    context = {

        'form': form,

    }
    return render(request, 'peche/peche_tass.html', context)


def delete_tasuu(request, id):
    dataOC = DimPechTAAssurance.objects.get(id=id)
    if request.method == 'POST':
        dataOC.delete()
        return redirect('/peche/pech_taassu/')
    context = {

        'item': dataOC, }
    return render(request, 'peche/delete_taassu.html', context)


# pechet

def petacom(request):
    if request.method == 'POST':

        form = pectom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_tacom/')
    else:
        form = pectom()

    dataObjects = DimPechTACommerc.objects.all()
    # Initialisez les totaux pour les champs spécifiés
    priventmoy_prod_ta = 0

    # Parcourez les enregistrements pour calculer les totaux
    for dataObject in dataObjects:

        priventmoy_prod_ta += dataObject.PrixVentMoyProdTA
    return render(request, 'peche/peche_tacom.html', {'form': form, 'priventmoy_prod_ta': priventmoy_prod_ta, 'dataObject': DimPechTACommerc.objects.all()})


# update commm
def update_tacom(request, id):
    dataObject = DimPechTACommerc.objects.get(id=id)
    form = pectom(instance=dataObject)
    if request.method == 'POST':
        form = pectom(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_tacom/')

    context = {

        'form': form,

    }
    return render(request, 'peche/peche_tacom.html', context)


def delete_tacom(request, id):
    dataObject = DimPechTACommerc.objects.get(id=id)
    if request.method == 'POST':
        dataObject.delete()
        return redirect('/peche/pech_tacom/')
    context = {

        'item': dataObject, }
    return render(request, 'peche/delete_tacom.html', context)


# pechetpech_tainov

def pech_tainov(request):
    if request.method == 'POST':
        form = pectaino(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_taino/')
    else:
        form = pectaino()
        return render(request, 'peche/peche_taino.html', {'form': form, 'dataObject': DimPecheTAInnovat.objects.all()})


# update commm
def up_taino(request, id):
    dataOC = DimPecheTAInnovat.objects.get(id=id)
    form = pectaino(instance=dataOC)
    if request.method == 'POST':
        form = pectaino(request.POST, instance=dataOC)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_taino/')

    context = {

        'form': form,

    }
    return render(request, 'peche/peche_taino.html', context)


def de_taino(request, id):
    dataOC = DimPecheTAInnovat.objects.get(id=id)
    if request.method == 'POST':
        dataOC.delete()
        return redirect('/peche/pech_taino/')
    context = {

        'item': dataOC, }
    return render(request, 'peche/delete_taino.html', context)


# pechetpech_tainov

def pechtafina(request):
    if request.method == 'POST':
        form = pectafina(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_tafina/')
    else:
        form = pectafina()
        return render(request, 'peche/peche_fina.html', {'form': form, 'dataObject': DimPechTAFinance.objects.all()})


# update commm
def up_fina(request, id):
    dataOC = DimPechTAFinance.objects.get(id=id)
    form = pectafina(instance=dataOC)
    if request.method == 'POST':
        form = pectafina(request.POST, instance=dataOC)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/peche/pech_tafina/')

    context = {

        'form': form,

    }
    return render(request, 'peche/peche_fina.html', context)


def de_fina(request, id):
    dataOC = DimPechTAFinance.objects.get(id=id)
    if request.method == 'POST':
        dataOC.delete()
        return redirect('/peche/pech_tafina/')
    context = {

        'item': dataOC, }
    return render(request, 'peche/delete_tafina.html', context)


# pechetpech_fac
def pcount(request):

    pfina = DimPecheFinance.objects.all().count()
    peche = DimPecheArtisan.objects.all().count()
    pcom = DimPecheCommerce.objects.all().count()
    peino = DimPecheInnovat.objects.all().count()

    context = {
        'peche': peche,
        'pfina': pfina,
        'peino': peino,
        'pcom': pcom,

    }
    return render(request, 'peche/hm.html', context)
