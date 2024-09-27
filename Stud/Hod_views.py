
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# from django.template import engine
# from django.template import Engine, EngineHandler, engines

from django.contrib import messages


from peche.models import DimPecheArtisan, DimPechTransformArtisan, DimPechTAFinance, DimPechTACommerc, DimPechTAAssurance, DimPecheTAInnovat, DimPecheArtisan, DimPecheAssure, DimPecheCommerce, DimPecheFinance, DimPecheInnovat


# @login_required(login_url='/')
def Home(request):

    pfina = DimPecheFinance.objects.all().count()
    peche = DimPecheArtisan.objects.all().count()
    pcom = DimPecheCommerce.objects.all().count()
    peino = DimPecheInnovat.objects.all().count()

    passura = DimPecheAssure.objects.all().count()
    taino = DimPecheTAInnovat.objects.all().count()
    tassur = DimPechTAAssurance.objects.all().count()
    tcom = DimPechTACommerc.objects.all().count()
    tafina = DimPechTAFinance.objects.all().count()
    tart = DimPechTransformArtisan.objects.all().count()
    #nb_visite = Visiteur.objects.all().count()

    context = {
        'peche': peche,
        'pfina': pfina,
        'peino': peino,
        'pcom': pcom,
        'passura': passura,
        'taino': taino,
        'tassur': tassur,
        'tcom': tcom,
        'tafina': tafina,
        'tart': tart,
        #'nb_visite': nb_visite,

    }
    return render(request, 'Hod/home.html', context)
