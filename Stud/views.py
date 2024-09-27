
import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,

)
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.contrib.auth.forms import PasswordChangeForm # add this
from django.http import Http404
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseForbidden
from app.models import Video
from app.models import Post, Ressource, UserProfile
from django.contrib.auth import login
from django.contrib import messages
from django.contrib import sessions
from app.forms import SignUpForm, ProfileForm
from app.ressource import Ressou
from app.forms import PostForm,VideoForm
from app.docum import doc
from app.indicateur import indic
from app.atelier import Atel
from app.models import atelier, docum, idcateur
from peche.models import DimPAPiroguImmat, DimPAPirogue, DimPechComRepartition, DimPecheArtisan, DimPechTransformArtisan, DimPechTAFinance, DimPechTACommerc, DimPechTAAssurance, DimPecheArtisanAct, DimPecheTAInnovat, DimPecheArtisan, DimPecheAssure, DimPecheCommerce, DimPecheFinance, DimPecheInnovat, FactPechArtisan
from django.views.generic import TemplateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model

User = get_user_model()


def Base(request):
    return render(request, 'pages/base.html')


def Accueil(request):

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
    # nb_visite = Visiteur.objects.all().count()

    # Vérifie si la clé 'visits' existe dans la session
    if 'visits' not in request.session:
        # Si elle n'existe pas, initialise à 0
        request.session['visits'] = 0

    # Incrémente le nombre de visites
    request.session['visits'] += 1
    total_visits = request.session['visits']
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
        'total_visits': total_visits,

    }

    return render(request, 'pages/accueil.html', context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            role = form.cleaned_data.get('role')

            if role == 'decideur':
                user.is_decideur = True
            elif role == 'gestionnaire':
                user.is_gestionnaire = True

            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            if user and user.is_authenticated:
                # Login successful
                return redirect('login')

    else:
        form = SignUpForm()

    return render(request, 'pages/register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_gestionnaire:
                messages.success(request, 'login succefull !')
                return redirect('home')

            elif user.is_decideur:
                messages.success(request, 'login succefull !')
                return redirect('decideur')

            else:
                messages.success(request, 'login succefull !')
                return redirect('visiteur')
        else:
            messages.error(
                request, 'error!veiller verifier votre login et password')
    return render(request, 'pages/login.html')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'pages/custom_password_reset_form.html'
    form_class = PasswordResetForm

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'pages/custom_password_reset_confirm.html'
    form_class = SetPasswordForm

def custom_password_reset_done(request):
    # Your custom logic for password reset done view
    return render(request, 'pages/custom_password_reset_done.html')

def custom_password_reset_complete(request):
    # Your custom logic for password reset complete view
    return render(request, 'pages/custom_password_reset_complete.html')


def user_logout(request):
    logout(request)
    return redirect('/')


def coord(request):
    return render(request, 'pages/coordonateur.html')

@login_required(login_url='/login/')
def deci(request):

  # Obtenez toutes les années distinctes présentes dans les données
    years = FactPechArtisan.objects.values_list('annee', flat=True).distinct()

    # Créez un dictionnaire pour stocker les données par année
    data_by_year = {}
    for year in years:
        # Filtrer les données pour chaque année
        data_by_year[year] = FactPechArtisan.objects.filter(annee=year)
    # Récupérer également la source pour chaque année

    return render(request, 'pages/decideur.html', {
        'data_by_year': data_by_year, })

@login_required(login_url='/login/')
def visit(request):
    profiles = UserProfile.objects.all()
    
    context = {
        'profiles': profiles
    }
    
    return render(request, 'pages/visiteur.html', context)

# end login

@login_required(login_url='/login/')
def peche(request):

    return render(request, 'pa/peche.html')
# @login_required


@login_required(login_url='/login/')
def ho(request):
    posts = Post.objects.order_by('-id').all()
    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    posts_number = posts.count()
    message = f'{posts_number} posts:'
    if posts_number == 1:
		
        message = f'{posts_number} post:'

    context = {
        'posts': page_object,
        # 'post_number':post_number,
        'message': message
    }

    return render(request, 'pa/index.html', context)


def detail(request, id):
    post = Post.objects.get(id=id)
    recent_posts = Post.objects.exclude(id=id)[:5] 

    context = {
        'post': post,
        'recent_posts': recent_posts
    }
    return render(request, 'pa/detail.html', context)

# @login_required


@login_required(login_url='/login/')
def new_post(request):
    post_form = PostForm(request.POST, request.FILES)
    video_form = VideoForm(request.POST, request.FILES)

    if request.method == 'POST':
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('b')  # Rediriger vers la page de liste des posts après avoir enregistré le post
        elif video_form.is_valid():
            new_video = video_form.save(commit=False)
            new_video.user = request.user  # Assigne l'utilisateur actuel à la vidéo
            new_video.save()
            return redirect('b')  # Rediriger vers l'URL appropriée après avoir enregistré la vidéo

    context = {
        'post_form': post_form,
        'video_form': video_form,
    }
    return render(request, 'pa/new_post.html', context)


@login_required(login_url='/login/')
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Vérifiez si l'utilisateur est l'auteur du post
    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('b')
        else:
            form = PostForm(instance=post)
    else:
        raise Http404

    context = {
        'form': form,
        'post': post
    }
    return render(request, 'pa/update_post.html', context)


@login_required(login_url='/login/')
def delete_post(request, id):
    post = Post.objects.get(id=id)
    if post.user == request.user:
        post.delete()
        return redirect('b')
    else:
        raise Http404

    return render(request, 'pa/delete.html')


@login_required(login_url='/login/')
def search(request):
    search = request.GET.get('search')
    posts = Post.objects.filter(Q(title__icontains=search) |
                                Q(content__icontains=search) |
                                Q(image__icontains=search)
                                )

    posts_number = posts.count()
    message = f'{posts_number} results:'
    if posts_number == 1:
        message = f'{posts_number} results:'

    context = {
        'posts': posts,
        'message': message,
    }
    return render(request, 'pa/search.html', context)

def bl(request):
    pos = Post.objects.order_by('-id').all()
    videos = Video.objects.order_by('-id').all()
    poste = Post.objects.all()
    document = docum.objects.order_by('-id').all()

    # Paginate posts
    post_paginator = Paginator(pos, 2)
    post_page = request.GET.get('post_page')
    try:
        pos = post_paginator.page(post_page)
    except PageNotAnInteger:
        pos = post_paginator.page(1)
    except EmptyPage:
        pos = post_paginator.page(post_paginator.num_pages)

    # Paginate videos
    video_paginator = Paginator(videos, 1)  # Paginate videos by 1 per page
    video_page = request.GET.get('video_page')
    try:
        videos = video_paginator.page(video_page)
    except PageNotAnInteger:
        videos = video_paginator.page(1)
    except EmptyPage:
        videos = video_paginator.page(video_paginator.num_pages)
        
    # Paginate documents
    document_paginator = Paginator(document, 3)
    document_page = request.GET.get('document_page')
    try:
        document = document_paginator.page(document_page)
    except PageNotAnInteger:
        document = document_paginator.page(1)
    except EmptyPage:
        document = document_paginator.page(document_paginator.num_pages)

    context = {
        'pos': pos,
        'videos': videos,
        'poste': poste,
        'document': document
    }

    return render(request, 'pa/bl.html', context)

def update_vid(request,id):
    # Récupérer la vidéo à mettre à jour
    video = get_object_or_404(Video, id=id)
    if request.user == video.user:
        if request.method == 'POST':
            form = VideoForm(request.POST, request.FILES, instance=video)

            if form.is_valid():
                form.save()
                return redirect('b')  # Rediriger vers la page de détail de la vidéo mise à jour
        else:
        # Si la requête n'est pas de type POST, créer une instance du formulaire avec les données de la vidéo actuelle
            form = VideoForm(instance=video)
    else:
        raise Http404
        
    # Afficher le formulaire de mise à jour de la vidéo
    return render(request, 'pa/update_video.html', {'form': form, 'video': video})


def delete_vid(request, id):
    # Récupérer la vidéo à supprimer
    video = get_object_or_404(Video, id=id)
    
    # Vérifier si la requête est de type POST, ce qui signifie que le formulaire de confirmation a été soumis
    if request.method == 'POST':
        # Supprimer la vidéo
        video.delete()
        return redirect('b')  # Rediriger vers la liste des vidéos après la suppression
    
    # Si la requête n'est pas de type POST, afficher le formulaire de confirmation de suppression
    return render(request, 'pa/delete_video.html', {'video': video})



def all(request):

    posts = Post.objects.order_by('-id').all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'posts': posts,
    }
    return render(request, 'pa/blog.html', context)


def ress(request):
    if request.method == 'POST':
        form = Ressou(request.POST, request.FILES)
 

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('/ressource/')


    else:
        form = Ressou()
    

    dataObject = Ressource.objects.order_by('-id').all()


    paginator = Paginator(dataObject, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    return render(request, 'pa/ressource.html', {'form': form,'dataObject': dataObject, 'posts': posts})

def re(request):
    search_query = request.GET.get('q')
    stud = Ressource.objects.all()

    if search_query:
        stud = stud.filter(
            Q(title__icontains=search_query) | Q(
                mot_cle__icontains=search_query)
        )

    stud = stud.order_by('-id')

    paginator = Paginator(stud, 5)
    page_number = request.GET.get('page')
    stud = paginator.get_page(page_number)

    context = {
        'stud': stud,
        'search_query': search_query,
    }

    return render(request, 'pa/r.html', context)


@login_required(login_url='/login/')
def upda_ress(request, id):
    stud = Ressource.objects.get(id=id)

    if request.method == 'POST':
        form = Ressou(request.POST, request.FILES, instance=stud)

        if form.is_valid():
            form.save()
            return redirect('ressource')

    else:
        form = Ressou(instance=stud)

    context = {

        'form': form,


    }

    return render(request, 'pa/update_ress.html', context)


@login_required(login_url='/login/')
def del_ress(request, id):
    stud = Ressource.objects.get(id=id)

    stud.delete()

    return redirect('ressource')




# start profile
@login_required(login_url='/login/')
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('profile_detail')
    else:
        form = ProfileForm()
    return render(request, 'pages/create_profile.html', {'form': form})


def update_profile(request):
    user_profile = request.user.userprofile

    # Form for updating user profile details
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        password_change_form = PasswordChangeForm(request.user, request.POST)

# Inside your views.py


def update_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        password_change_form = StyledPasswordChangeForm(request.user, request.POST)

        # Vérifiez si seul le ProfileForm est valide
        if form.is_valid() and not password_change_form.has_changed():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            messages.success(request, 'Profil mis à jour avec succès.')

            return redirect('profile_detail')

        # Si PasswordChangeForm est soumis, vérifiez sa validité
        elif password_change_form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            password_change_form.save()
            messages.success(request, 'Profil et mot de passe mis à jour avec succès.')

            return redirect('profile_detail')

    else:
        form = ProfileForm(instance=user_profile)
        password_change_form = StyledPasswordChangeForm(request.user)

    return render(request, 'pages/update_profile.html', {'form': form, 'password_change_form': password_change_form})


# Customized PasswordChangeForm with styling
class StyledPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply styling to individual fields
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'style': 'width: 800px;',
                'placeholder': '',
            })
        self.fields['old_password'].required = False
        self.fields['new_password1'].required = False
        self.fields['new_password2'].required = False


@login_required(login_url='/login/')
def delete_profile(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        user_profile.delete()
        return redirect('/')  # Replace 'home' with the appropriate URL
    return render(request, 'pages/delete_profile.html', {'user_profile': user_profile})


@login_required(login_url='/login/')
def profile_detail(request):
    user_profile = request.user.userprofile
    return render(request, 'pages/profile_detail.html', {'user_profile': user_profile})


@login_required(login_url='/login/')
def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'pages/profile_list.html', {'profiles': profiles})

# end profile


def commune(request):

    return render(request, 'pa/commune.html')


def co(request):

    return render(request, 'pa/commune_detail.html')


def peche(request):

    return render(request, 'pa/peche.html')


def teste(request):
  # Obtenez toutes les années distinctes présentes dans les données
    years = FactPechArtisan.objects.values_list('annee', flat=True).distinct()

    # Créez un dictionnaire pour stocker les données par année
    data_by_year = {}
    for year in years:
        # Filtrer les données pour chaque année
        data_by_year[year] = FactPechArtisan.objects.filter(annee=year)
    #data = FactPechArtisan.objects.all()
    
    dataOb = DimPecheCommerce.objects.all()
    datassu=DimPecheAssure.objects.all()
    taass=DimPechTAAssurance.objects.all()
    tacom=DimPechTACommerc.objects.all()
    taar=DimPechTransformArtisan.objects.all()
    da = DimPecheArtisanAct.objects.all()
    acts = DimPecheArtisanAct.objects.all()
    pi=DimPAPirogue.objects.all()
    permi=DimPAPiroguImmat.objects.all()
    pirogu_immats = DimPAPiroguImmat.objects.all()
    dataObjects = FactPechArtisan.objects.all()
    paa=DimPAPirogue.objects.all()
    pirogu_immats = DimPAPiroguImmat.objects.all()
    carburant_data = FactPechArtisan.objects.all()
    rnvlle = FactPechArtisan.objects.all()
    carb_data = FactPechArtisan.objects.all()
    acteur_data= FactPechArtisan.objects.all()
    permimt= DimPAPiroguImmat.objects.all()
    unique_years = list(set(item.annee for item in permimt))
    pirogue_data = DimPAPirogue.objects.all()
    CaptAnnuel= FactPechArtisan.objects.all()
    repartition_data = DimPechComRepartition.objects.all()
    Qteannuel=FactPechArtisan.objects.all()

 
    
    selected_data = request.GET.get('selected_data')
    selected_year = request.GET.get('selected_year')

    your_queryset = DimPecheArtisan.objects.all()
    assu=DimPecheAssure.objects.all()

    # Initialisez les totaux pour les champs spécifiés
    total_nbr_acteur = 0
    total_nbr_pirogue=0
    total_nbr_permis=0
    total_nbre_gie_pecheur = 0
    total_nbr_organi_profess_pecheur = 0
    total_nbr_associat_pecheur = 0
    total_nbre_gie_marey = 0
    total_nbr_organi_profess_marey = 0
    total_nbr_associat_marey = 0
    total_nbre_quai_pech = 0
    total_qteannuel_debarq = 0
    total_ProdVendType = 0
    total_nbr_piogue_bois=0
    total_nbr_piogue_verre=0
    total_nbr_piogue_almunium=0
    total_nbr_piogue_immat=0
    total_qt_annuel_debar=0 
    total_q_pr=0
    valeurComCaptAnnuel=0
    volumDebitCarb=0
    valeurCommCarbu=0
    totStatCarbu=0
    nbrTotFabriqGlace=0
    nbrMareyTotDeclare=0
    nbrMareyTotRecensmt =0
    nbrPecheurTotRecensmt=0

    #dimmassurance
    total_nbre_souscrpt=0
    total_nbre_tasouscrpt=0
    total_nbre_tprime=0
    total_nbre_prim=0
    total_nbre_infstck=0
    total_nbre_emb=0
    total_nbre_label=0
    #dimcommerce
    total_ProdVendType=0
    total_ProdVendSais=0
    total_ProdVendhiver =0
    tototal_ProdVendfr =0
    total_ProdVendPrin =0
    total_ProdVendMoy =0
    total_Protamoy=0
    total_qteprtypta=0
    total_txtranf=0
    # Vérifie si la clé 'visits' existe dans la session
    if 'visits' not in request.session:
        # Si elle n'existe pas, initialise à 0
        request.session['visits'] = 0

    # Incrémente le nombre de visites
    request.session['visits'] += 1
    total_visits = request.session['visits']

    # Parcourez les enregistrements pour calculer les totaux
    for dataObject in dataObjects:
        total_qt_annuel_debar +=dataObject.Qteannuel_debarq 
        total_nbr_piogue_bois +=dataObject.NbrPirogBois
        total_nbr_piogue_verre +=dataObject.NbrePirogFibVer
        total_nbr_piogue_almunium+=dataObject.NbrPirogAlumin
        total_nbr_piogue_immat+=dataObject.NbrePirogImmatri
        #total_nbr_acteur += dataObject.NbrActeur
        total_nbre_gie_pecheur += dataObject.NbreGIEPecheur
        total_nbr_organi_profess_pecheur += dataObject.NbrOrganiProfessPecheur
        total_nbr_associat_pecheur += dataObject.Nbr_AssociatPecheur
        total_nbre_gie_marey += dataObject.NbreGIEMarey
        total_nbr_organi_profess_marey += dataObject.NbrOrganiProfessMarey  # Correction ici
        total_nbr_associat_marey += dataObject.Nbr_AssociatMarey  # Correction ici
        total_nbre_quai_pech += dataObject.NbreQuaiPech
        total_qteannuel_debarq += dataObject.Qteannuel_debarq
        valeurComCaptAnnuel+= dataObject.ValeurComCaptAnnuel
        volumDebitCarb += dataObject.VolumDebitCarb
        valeurCommCarbu+= dataObject.ValeurCommCarbu
        totStatCarbu+= dataObject.TotStatCarbu
        nbrTotFabriqGlace+= dataObject.NbrTotFabriqGlace
        nbrMareyTotDeclare+= dataObject.NbrMareyTotDeclare
        nbrMareyTotRecensmt += dataObject.NbrMareyTotRecensmt
        nbrPecheurTotRecensmt+= dataObject.NbrPecheurTotRecensmt
    #taassurance
    for taar in taar:
        total_q_pr +=taar.QteProdPeriodTA
        total_qteprtypta +=taar.QteProdTypeTA
        total_txtranf +=taar.TauxTransformArtisan
    #dimassurance
    for datassu in datassu:
        total_nbre_souscrpt += datassu.NbreSouscripPech
        total_nbre_prim += datassu.NbrePrimePech
        total_nbre_infstck += datassu.NbrInfrastruStokCondition
        total_nbre_emb += datassu.NbrFourniEmblag 
        total_nbre_label += datassu.NbrProdLabel 
    #dimtaassurance
    for taass in taass:
        total_nbre_tasouscrpt +=taass.NbrSouscripTA
        total_nbre_tprime +=taass.NivPrimTA
        
    
    #dimcommerce
    for dataO in dataOb:
        total_ProdVendType += dataO.ProdVendType
        total_ProdVendSais += dataO.ProdVendCampgnInterSais
        total_ProdVendhiver += dataO.ProdVendCampgnHiver
        tototal_ProdVendfr += dataO.ProdVendCampSaisFroid
        total_ProdVendPrin += dataO.ProdVendCampPrintem
        total_ProdVendMoy += dataO.PriVentMoy_Prod
    for tacom in tacom:
        total_Protamoy +=tacom.ProdVenduCampagTA
    for da in da:
        total_nbr_acteur += da.NbrActeur
    for pi in pi:
        total_nbr_pirogue += pi.NbrPirogu
        
    for permi in permi:
        total_nbr_permis += permi.NbrePiroguImmatPermis
        
     
        

    return render(request, 'pa/index.html', {
        #'data':data,
		'data_by_year': data_by_year,
        'da':da,
		'rnvlle':rnvlle,
        'acts':acts,
        'carburant_data': carburant_data,
        'acteur_data': acteur_data,
        'carb_data': carb_data,
        'permimt':permimt,
        'unique_years':unique_years,
        'pirogue_data':pirogue_data,
        'CaptAnnuel':CaptAnnuel,
        'repartition_data':repartition_data,
        'Qteannuel':Qteannuel,
      'paa':paa,
      'pirogu_immats':pirogu_immats,
        'dataObjects': dataObjects,
        'total_qt_annuel_debar':total_qt_annuel_debar,
        'total_nbr_piogue_bois':total_nbr_piogue_bois,
        'total_nbr_piogue_verre':total_nbr_piogue_verre,
        'total_nbr_piogue_almunium':total_nbr_piogue_almunium,
        'total_nbr_piogue_immat' :total_nbr_piogue_immat,
        'total_nbr_acteur': total_nbr_acteur,
        'total_nbre_gie_pecheur': total_nbre_gie_pecheur,
        'total_nbr_organi_profess_pecheur': total_nbr_organi_profess_pecheur,
        'total_nbr_associat_pecheur': total_nbr_associat_pecheur,
        'total_nbre_gie_marey': total_nbre_gie_marey,
        'total_nbr_organi_profess_marey': total_nbr_organi_profess_marey,
        'total_nbr_associat_marey': total_nbr_associat_marey,
        'total_nbre_quai_pech': total_nbre_quai_pech,
        'valeurComCaptAnnuel': valeurComCaptAnnuel,
        'volumDebitCarb':volumDebitCarb,
        'valeurCommCarbu':valeurCommCarbu,
        'totStatCarbu':totStatCarbu,
        'nbrTotFabriqGlace':nbrTotFabriqGlace,
        'nbrMareyTotDeclare':nbrMareyTotDeclare,
        'nbrMareyTotRecensmt':nbrMareyTotRecensmt,
        'nbrPecheurTotRecensmt':nbrPecheurTotRecensmt,
        
        'total_visits': total_visits,
        'total_ProdVendType': total_ProdVendType,
        #dimmassure
        'total_nbre_souscrpt':total_nbre_souscrpt,
        'total_nbre_tasouscrpt':total_nbre_tasouscrpt,
        'total_nbre_tprime':total_nbre_tprime,
        'total_nbre_prim':total_nbre_prim,
        'total_nbre_infstck':total_nbre_infstck,
        'total_nbre_emb':total_nbre_emb,
        'total_nbre_label':total_nbre_label,
        #dimcommerce
        'total_ProdVendType':total_ProdVendType,
        'total_ProdVendSais' :total_ProdVendSais,
        'total_ProdVendhiver':total_ProdVendhiver,
        'tototal_ProdVendfr':tototal_ProdVendfr,
        'total_ProdVendPrin':total_ProdVendPrin,
        'total_ProdVendMoy ':total_ProdVendMoy,
        'total_Protamoy':total_Protamoy,
        #taassurance
        'total_q_pr':total_q_pr,
        'total_qteprtypta':total_qteprtypta,
        'total_txtranf':total_txtranf,
        'your_queryset':your_queryset,
        'assu':assu,
        'selected_data':selected_data,
        'selected_year':selected_year,
        'total_nbr_pirogue':total_nbr_pirogue,
        'total_nbr_permis':total_nbr_permis,
    })
    



def come(request):

    return render(request, 'pa/com.html')


def donne(request):
  # Obtenez toutes les années distinctes présentes dans les données
    years = FactPechArtisan.objects.values_list('annee', flat=True).distinct()

    # Créez un dictionnaire pour stocker les données par année
    data_by_year = {}
    for year in years:
        # Filtrer les données pour chaque année
        data_by_year[year] = FactPechArtisan.objects.filter(annee=year)
    #data = FactPechArtisan.objects.all()
    dataOb = DimPecheCommerce.objects.all()
    datassu=DimPecheAssure.objects.all()
    taass=DimPechTAAssurance.objects.all()
    tacom=DimPechTACommerc.objects.all()
    taar=DimPechTransformArtisan.objects.all()
    da = DimPecheArtisanAct.objects.all()
    acts = DimPecheArtisanAct.objects.all()
    pi=DimPAPirogue.objects.all()
    permi=DimPAPiroguImmat.objects.all()
    pirogu_immats = DimPAPiroguImmat.objects.all()
    dataObjects = FactPechArtisan.objects.all()
    paa=DimPAPirogue.objects.all()
    pirogu_immats = DimPAPiroguImmat.objects.all()
    carburant_data = FactPechArtisan.objects.all()
    rnvlle = FactPechArtisan.objects.all()
    carb_data = FactPechArtisan.objects.all()
    acteur_data= FactPechArtisan.objects.all()
    permimt= DimPAPiroguImmat.objects.all()
    unique_years = list(set(item.annee for item in permimt))
    pirogue_data = DimPAPirogue.objects.all()
    CaptAnnuel= FactPechArtisan.objects.all()
    repartition_data = DimPechComRepartition.objects.all()
    Qteannuel=FactPechArtisan.objects.all()

 
    
    selected_data = request.GET.get('selected_data')
    selected_year = request.GET.get('selected_year')

    your_queryset = DimPecheArtisan.objects.all()
    assu=DimPecheAssure.objects.all()

    # Initialisez les totaux pour les champs spécifiés
    total_nbr_acteur = 0
    total_nbr_pirogue=0
    total_nbr_permis=0
    total_nbre_gie_pecheur = 0
    total_nbr_organi_profess_pecheur = 0
    total_nbr_associat_pecheur = 0
    total_nbre_gie_marey = 0
    total_nbr_organi_profess_marey = 0
    total_nbr_associat_marey = 0
    total_nbre_quai_pech = 0
    total_qteannuel_debarq = 0
    total_ProdVendType = 0
    total_nbr_piogue_bois=0
    total_nbr_piogue_verre=0
    total_nbr_piogue_almunium=0
    total_nbr_piogue_immat=0
    total_qt_annuel_debar=0 
    total_q_pr=0
    valeurComCaptAnnuel=0
    volumDebitCarb=0
    valeurCommCarbu=0
    totStatCarbu=0
    nbrTotFabriqGlace=0
    nbrMareyTotDeclare=0
    nbrMareyTotRecensmt =0
    nbrPecheurTotRecensmt=0

    #dimmassurance
    total_nbre_souscrpt=0
    total_nbre_tasouscrpt=0
    total_nbre_tprime=0
    total_nbre_prim=0
    total_nbre_infstck=0
    total_nbre_emb=0
    total_nbre_label=0
    #dimcommerce
    total_ProdVendType=0
    total_ProdVendSais=0
    total_ProdVendhiver =0
    tototal_ProdVendfr =0
    total_ProdVendPrin =0
    total_ProdVendMoy =0
    total_Protamoy=0
    total_qteprtypta=0
    total_txtranf=0
    # Vérifie si la clé 'visits' existe dans la session
    if 'visits' not in request.session:
        # Si elle n'existe pas, initialise à 0
        request.session['visits'] = 0

    # Incrémente le nombre de visites
    request.session['visits'] += 1
    total_visits = request.session['visits']

    # Parcourez les enregistrements pour calculer les totaux
    for dataObject in dataObjects:
        total_qt_annuel_debar +=dataObject.Qteannuel_debarq 
        total_nbr_piogue_bois +=dataObject.NbrPirogBois
        total_nbr_piogue_verre +=dataObject.NbrePirogFibVer
        total_nbr_piogue_almunium+=dataObject.NbrPirogAlumin
        total_nbr_piogue_immat+=dataObject.NbrePirogImmatri
        #total_nbr_acteur += dataObject.NbrActeur
        total_nbre_gie_pecheur += dataObject.NbreGIEPecheur
        total_nbr_organi_profess_pecheur += dataObject.NbrOrganiProfessPecheur
        total_nbr_associat_pecheur += dataObject.Nbr_AssociatPecheur
        total_nbre_gie_marey += dataObject.NbreGIEMarey
        total_nbr_organi_profess_marey += dataObject.NbrOrganiProfessMarey  # Correction ici
        total_nbr_associat_marey += dataObject.Nbr_AssociatMarey  # Correction ici
        total_nbre_quai_pech += dataObject.NbreQuaiPech
        total_qteannuel_debarq += dataObject.Qteannuel_debarq
        valeurComCaptAnnuel+= dataObject.ValeurComCaptAnnuel
        volumDebitCarb += dataObject.VolumDebitCarb
        valeurCommCarbu+= dataObject.ValeurCommCarbu
        totStatCarbu+= dataObject.TotStatCarbu
        nbrTotFabriqGlace+= dataObject.NbrTotFabriqGlace
        nbrMareyTotDeclare+= dataObject.NbrMareyTotDeclare
        nbrMareyTotRecensmt += dataObject.NbrMareyTotRecensmt
        nbrPecheurTotRecensmt+= dataObject.NbrPecheurTotRecensmt
    #taassurance
    for taar in taar:
        total_q_pr +=taar.QteProdPeriodTA
        total_qteprtypta +=taar.QteProdTypeTA
        total_txtranf +=taar.TauxTransformArtisan
    #dimassurance
    for datassu in datassu:
        total_nbre_souscrpt += datassu.NbreSouscripPech
        total_nbre_prim += datassu.NbrePrimePech
        total_nbre_infstck += datassu.NbrInfrastruStokCondition
        total_nbre_emb += datassu.NbrFourniEmblag 
        total_nbre_label += datassu.NbrProdLabel 
    #dimtaassurance
    for taass in taass:
        total_nbre_tasouscrpt +=taass.NbrSouscripTA
        total_nbre_tprime +=taass.NivPrimTA
        
    
    #dimcommerce
    for dataO in dataOb:
        total_ProdVendType += dataO.ProdVendType
        total_ProdVendSais += dataO.ProdVendCampgnInterSais
        total_ProdVendhiver += dataO.ProdVendCampgnHiver
        tototal_ProdVendfr += dataO.ProdVendCampSaisFroid
        total_ProdVendPrin += dataO.ProdVendCampPrintem
        total_ProdVendMoy += dataO.PriVentMoy_Prod
    for tacom in tacom:
        total_Protamoy +=tacom.ProdVenduCampagTA
    for da in da:
        total_nbr_acteur += da.NbrActeur
    for pi in pi:
        total_nbr_pirogue += pi.NbrPirogu
        
    for permi in permi:
        total_nbr_permis += permi.NbrePiroguImmatPermis
        
 
    return render(request, 'pa/donne.html', {
	     #'data':data,
		'data_by_year': data_by_year,
        'da':da,
		'rnvlle':rnvlle,
        'acts':acts,
        'carburant_data': carburant_data,
        'acteur_data': acteur_data,
        'carb_data': carb_data,
        'permimt':permimt,
        'unique_years':unique_years,
        'pirogue_data':pirogue_data,
        'CaptAnnuel':CaptAnnuel,
        'repartition_data':repartition_data,
        'Qteannuel':Qteannuel,
      'paa':paa,
      'pirogu_immats':pirogu_immats,
        'dataObjects': dataObjects,
        'total_qt_annuel_debar':total_qt_annuel_debar,
        'total_nbr_piogue_bois':total_nbr_piogue_bois,
        'total_nbr_piogue_verre':total_nbr_piogue_verre,
        'total_nbr_piogue_almunium':total_nbr_piogue_almunium,
        'total_nbr_piogue_immat' :total_nbr_piogue_immat,
        'total_nbr_acteur': total_nbr_acteur,
        'total_nbre_gie_pecheur': total_nbre_gie_pecheur,
        'total_nbr_organi_profess_pecheur': total_nbr_organi_profess_pecheur,
        'total_nbr_associat_pecheur': total_nbr_associat_pecheur,
        'total_nbre_gie_marey': total_nbre_gie_marey,
        'total_nbr_organi_profess_marey': total_nbr_organi_profess_marey,
        'total_nbr_associat_marey': total_nbr_associat_marey,
        'total_nbre_quai_pech': total_nbre_quai_pech,
        'valeurComCaptAnnuel': valeurComCaptAnnuel,
        'volumDebitCarb':volumDebitCarb,
        'valeurCommCarbu':valeurCommCarbu,
        'totStatCarbu':totStatCarbu,
        'nbrTotFabriqGlace':nbrTotFabriqGlace,
        'nbrMareyTotDeclare':nbrMareyTotDeclare,
        'nbrMareyTotRecensmt':nbrMareyTotRecensmt,
        'nbrPecheurTotRecensmt':nbrPecheurTotRecensmt,
        
        'total_visits': total_visits,
        'total_ProdVendType': total_ProdVendType,
        #dimmassure
        'total_nbre_souscrpt':total_nbre_souscrpt,
        'total_nbre_tasouscrpt':total_nbre_tasouscrpt,
        'total_nbre_tprime':total_nbre_tprime,
        'total_nbre_prim':total_nbre_prim,
        'total_nbre_infstck':total_nbre_infstck,
        'total_nbre_emb':total_nbre_emb,
        'total_nbre_label':total_nbre_label,
        #dimcommerce
        'total_ProdVendType':total_ProdVendType,
        'total_ProdVendSais' :total_ProdVendSais,
        'total_ProdVendhiver':total_ProdVendhiver,
        'tototal_ProdVendfr':tototal_ProdVendfr,
        'total_ProdVendPrin':total_ProdVendPrin,
        'total_ProdVendMoy ':total_ProdVendMoy,
        'total_Protamoy':total_Protamoy,
        #taassurance
        'total_q_pr':total_q_pr,
        'total_qteprtypta':total_qteprtypta,
        'total_txtranf':total_txtranf,
        'your_queryset':your_queryset,
        'assu':assu,
        'selected_data':selected_data,
        'selected_year':selected_year,
        'total_nbr_pirogue':total_nbr_pirogue,
        'total_nbr_permis':total_nbr_permis,
    })


def log(request):

    return render(request, 'pa/log.html')


# @login_required
class MapView(TemplateView):
    template_name = 'pa/index.html'


def carte(request):
    da = DimPecheArtisanAct.objects.all()

    dataObjects = DimPecheArtisan.objects.all()
    dataOb = DimPecheCommerce.objects.all()
    datassu=DimPecheAssure.objects.all()
    taass=DimPechTAAssurance.objects.all()
    tacom=DimPechTACommerc.objects.all()
    taar=DimPechTransformArtisan.objects.all()
    
    selected_data = request.GET.get('selected_data')
    selected_year = request.GET.get('selected_year')

    your_queryset = DimPecheArtisan.objects.all()
    assu=DimPecheAssure.objects.all()

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
    total_ProdVendType = 0
    total_nbr_piogue_bois=0
    total_nbr_piogue_verre=0
    total_nbr_piogue_almunium=0
    total_nbr_piogue_immat=0
    total_qt_annuel_debar=0 
    total_q_pr=0
    #dimmassurance
    total_nbre_souscrpt=0
    total_nbre_tasouscrpt=0
    total_nbre_tprime=0
    total_nbre_prim=0
    total_nbre_infstck=0
    total_nbre_emb=0
    total_nbre_label=0
    #dimcommerce
    total_ProdVendType=0
    total_ProdVendSais=0
    total_ProdVendhiver =0
    tototal_ProdVendfr =0
    total_ProdVendPrin =0
    total_ProdVendMoy =0
    total_Protamoy=0
    total_qteprtypta=0
    total_txtranf=0
    # Vérifie si la clé 'visits' existe dans la session
    if 'visits' not in request.session:
        # Si elle n'existe pas, initialise à 0
        request.session['visits'] = 0

    # Incrémente le nombre de visites
    request.session['visits'] += 1
    total_visits = request.session['visits']

    # Parcourez les enregistrements pour calculer les totaux
    for dataObject in dataObjects:
        total_qt_annuel_debar +=dataObject.Qteannuel_debarq 
        total_nbr_piogue_bois +=dataObject.NbrPirogBois
        total_nbr_piogue_verre +=dataObject.NbrePirogFibVer
        total_nbr_piogue_almunium+=dataObject.NbrPirogAlumin
        total_nbr_piogue_immat+=dataObject.NbrePirogImmatri
        total_nbr_acteur += dataObject.NbrActeur
        total_nbre_gie_pecheur += dataObject.NbreGIEPecheur
        total_nbr_organi_profess_pecheur += dataObject.NbrOrganiProfessPecheur
        total_nbr_associat_pecheur += dataObject.Nbr_AssociatPecheur
        total_nbre_gie_marey += dataObject.NbreGIEMarey
        total_nbr_organi_profess_marey += dataObject.NbrOrganiProfessMarey  # Correction ici
        total_nbr_associat_marey += dataObject.Nbr_AssociatMarey  # Correction ici
        total_nbre_quai_pech += dataObject.NbreQuaiPech
        total_qteannuel_debarq += dataObject.Qteannuel_debarq
    #taassurance
    for taar in taar:
        total_q_pr +=taar.QteProdPeriodTA
        total_qteprtypta +=taar.QteProdTypeTA
        total_txtranf +=taar.TauxTransformArtisan
    #dimassurance
    for datassu in datassu:
        total_nbre_souscrpt += datassu.NbreSouscripPech
        total_nbre_prim += datassu.NbrePrimePech
        total_nbre_infstck += datassu.NbrInfrastruStokCondition
        total_nbre_emb += datassu.NbrFourniEmblag 
        total_nbre_label += datassu.NbrProdLabel 
    #dimtaassurance
    for taass in taass:
        total_nbre_tasouscrpt +=taass.NbrSouscripTA
        total_nbre_tprime +=taass.NivPrimTA
        
    
    #dimcommerce
    for dataO in dataOb:
        total_ProdVendType += dataO.ProdVendType
        total_ProdVendSais += dataO.ProdVendCampgnInterSais
        total_ProdVendhiver += dataO.ProdVendCampgnHiver
        tototal_ProdVendfr += dataO.ProdVendCampSaisFroid
        total_ProdVendPrin += dataO.ProdVendCampPrintem
        total_ProdVendMoy += dataO.PriVentMoy_Prod
    for tacom in tacom:
        total_Protamoy +=tacom.ProdVenduCampagTA
    for da in dataObjects:
        total_nbr_acteur += dataObject.NbrActeur
        
     
        

    return render(request, 'pa/carte.html', {
        'da':da,
        'dataObjects': dataObjects,
        'total_qt_annuel_debar':total_qt_annuel_debar,
        'total_nbr_piogue_bois':total_nbr_piogue_bois,
        'total_nbr_piogue_verre':total_nbr_piogue_verre,
        'total_nbr_piogue_almunium':total_nbr_piogue_almunium,
        'total_nbr_piogue_immat' :total_nbr_piogue_immat,
        'total_nbr_acteur': total_nbr_acteur,
        'total_nbre_gie_pecheur': total_nbre_gie_pecheur,
        'total_nbr_organi_profess_pecheur': total_nbr_organi_profess_pecheur,
        'total_nbr_associat_pecheur': total_nbr_associat_pecheur,
        'total_nbre_gie_marey': total_nbre_gie_marey,
        'total_nbr_organi_profess_marey': total_nbr_organi_profess_marey,
        'total_nbr_associat_marey': total_nbr_associat_marey,
        'total_nbre_quai_pech': total_nbre_quai_pech,
        'total_qteannuel_debarq': total_qteannuel_debarq,
        'total_visits': total_visits,
        'total_ProdVendType': total_ProdVendType,
        #dimmassure
        'total_nbre_souscrpt':total_nbre_souscrpt,
        'total_nbre_tasouscrpt':total_nbre_tasouscrpt,
        'total_nbre_tprime':total_nbre_tprime,
        'total_nbre_prim':total_nbre_prim,
        'total_nbre_infstck':total_nbre_infstck,
        'total_nbre_emb':total_nbre_emb,
        'total_nbre_label':total_nbre_label,
        #dimcommerce
        'total_ProdVendType':total_ProdVendType,
        'total_ProdVendSais' :total_ProdVendSais,
        'total_ProdVendhiver':total_ProdVendhiver,
        'tototal_ProdVendfr':tototal_ProdVendfr,
        'total_ProdVendPrin':total_ProdVendPrin,
        'total_ProdVendMoy ':total_ProdVendMoy,
        'total_Protamoy':total_Protamoy,
        #taassurance
        'total_q_pr':total_q_pr,
        'total_qteprtypta':total_qteprtypta,
        'total_txtranf':total_txtranf,
        'your_queryset':your_queryset,
        'assu':assu,
        'selected_data':selected_data,
        'selected_year':selected_year,
    })


def at(request):
    # Récupérer le paramètre de recherche
    search_query = request.GET.get('q')

    # Récupérer tous les ateliers
    stud = atelier.objects.all()
    stud = stud.order_by('-id')

    # Filtrer les ateliers en fonction de la recherche s'il y en a une
    if search_query:
        stud = stud.filter(
            Q(title__icontains=search_query) | Q(
                mot_cle__icontains=search_query)
        )

    # Pagination
    paginator = Paginator(stud, 5)
    page_number = request.GET.get('page')
    try:
        stud = paginator.page(page_number)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, renvoyer la première page
        stud = paginator.page(1)
    except EmptyPage:
        # Si la page est hors limite (par exemple, 9999), renvoyer la dernière page de résultats
        stud = paginator.page(paginator.num_pages)

    # Gestion de l'ajout d'un nouvel atelier
    if request.method == 'POST':
        form = Atel(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('/atelier/')
    else:
        form = Atel()

    # Passer le contexte à votre modèle
    context = {
        'stud': stud,
        'search_query': search_query,
        'form': form,
    }

    return render(request, 'pa/atelier.html', context)


@login_required
def upda_atl(request, id):
    stud = get_object_or_404(atelier, id=id)

    if request.method == 'POST':
        form = Atel(request.POST, request.FILES, instance=stud)
        if form.is_valid():
            form.save()
            return redirect('atelier')  # Redirection vers l'URL 'atelier'
    else:
        form = Atel(instance=stud)

    context = {
        'form': form,
    }

    return render(request, 'pa/update_atl.html', context)


def del_atl(request, id):
    # Récupérer l'instance de l'atelier
    stud = get_object_or_404(atelier, id=id)

    # Supprimer l'atelier
    stud.delete()

    # Rediriger vers l'URL nommée 'atelier'
    return redirect('atelier')
# documentaire


def documt(request):
    # Récupérer le paramètre de recherche
    search_query = request.GET.get('q')

    # Récupérer tous les ateliers
    stud = docum.objects.all()
    stud = stud.order_by('-id')

    # Filtrer les ateliers en fonction de la recherche s'il y en a une
    if search_query:
        stud = stud.filter(
            Q(title__icontains=search_query) | Q(
                mot_cle__icontains=search_query)
        )

    # Pagination
    paginator = Paginator(stud, 5)
    page_number = request.GET.get('page')
    try:
        stud = paginator.page(page_number)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, renvoyer la première page
        stud = paginator.page(1)
    except EmptyPage:
        # Si la page est hors limite (par exemple, 9999), renvoyer la dernière page de résultats
        stud = paginator.page(paginator.num_pages)

    # Gestion de l'ajout d'un nouvel atelier
    if request.method == 'POST':
        form = doc(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('/documt/')
    else:
        form = doc()

    # Passer le contexte à votre modèle
    context = {
        'stud': stud,
        'search_query': search_query,
        'form': form,
    }

    return render(request, 'pa/doc.html', context)


@login_required
def upda_doc(request, id):
    stud = get_object_or_404(docum, id=id)

    if request.method == 'POST':
        form = doc(request.POST, request.FILES, instance=stud)
        if form.is_valid():
            form.save()
            return redirect('documt')  # Redirection vers l'URL 'atelier'
    else:
        form = doc(instance=stud)

    context = {
        'form': form,
    }

    return render(request, 'pa/update_doc.html', context)


def del_doc(request, id):
    # Récupérer l'instance de l'atelier
    stud = get_object_or_404(docum, id=id)

    # Supprimer l'atelier
    stud.delete()

    # Rediriger vers l'URL nommée 'atelier'
    return redirect('documt')
# fin document

# idicateur


def indict(request):
    # Récupérer le paramètre de recherche
    search_query = request.GET.get('q')

    # Récupérer tous les ateliers
    stud = idcateur.objects.all()
    stud = stud.order_by('-id')

    # Filtrer les ateliers en fonction de la recherche s'il y en a une
    if search_query:
        stud = stud.filter(
            Q(title__icontains=search_query) | Q(
                mot_cle__icontains=search_query)
        )

    # Pagination
    paginator = Paginator(stud, 5)
    page_number = request.GET.get('page')
    try:
        stud = paginator.page(page_number)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, renvoyer la première page
        stud = paginator.page(1)
    except EmptyPage:
        # Si la page est hors limite (par exemple, 9999), renvoyer la dernière page de résultats
        stud = paginator.page(paginator.num_pages)

    # Gestion de l'ajout d'un nouvel atelier
    if request.method == 'POST':
        form = indic(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('/indi/')
    else:
        form = indic()

    # Passer le contexte à votre modèle
    context = {
        'stud': stud,
        'search_query': search_query,
        'form': form,
    }

    return render(request, 'pa/indicateur.html', context)


@login_required
def upda_i(request, id):
    stud = get_object_or_404(idcateur, id=id)

    if request.method == 'POST':
        form = indic(request.POST, request.FILES, instance=stud)
        if form.is_valid():
            form.save()
            return redirect('indi')  # Redirection vers l'URL 'atelier'
    else:
        form = indic(instance=stud)

    context = {
        'form': form,
    }

    return render(request, 'pa/update_indi.html', context)


def del_i(request, id):
    # Récupérer l'instance de l'atelier
    stud = get_object_or_404(idcateur, id=id)

    # Supprimer l'atelier
    stud.delete()

    # Rediriger vers l'URL nommée 'atelier'
    return redirect('indi')
# fin indicateur

