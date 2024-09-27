
from django.urls import path

from peche import views


app_name = 'peche'


urlpatterns = [
    path('pch/', views.pcount, name='pch'),
    path('dimpecart/', views.pec_art, name='dimpecart'),
    path('dimact/', views.pec_artact, name='dimact'),
    path('dimpechgpt/', views.pech_goupe, name='dimpechgpt'),
    #path('dimpechgpt/', views.Pech_goupeCreateView.as_view(), name='dimpechgpt'),

    path('dimpechpirogue/', views.pech_pirogue, name='dimpechpirogue'),
    path('dimpechniv/', views.pech_typeniv, name='dimpechniv'),
    
    path('dimpechimmat/', views.pech_immat, name='dimpechimmat'),
    path('dimrepart/', views.pech_ComRepartition, name='dimrepart'),
    path('dimpechprod/', views.pech_propirogue, name='dimpechprod'),
    path('dimfact/', views.pech_fact, name='dimfact'),
    
    path('dimpecass/', views.pech_assu, name='dimpecass'),
    path('dimpecec/', views.pech_ec, name='dimpecec'),
    path('dimpecfin/', views.pech_fin, name='dimpecfin'),
    path('up_ar<int:id>/', views.update_ar, name='up_ar'),
    path('de_ar<int:id>/', views.delete_ar, name='de_ar'),
    #mise jours
    path('up_act<int:id>/', views.update_act, name='up_act'),
    path('de_act<int:id>/', views.delete_act, name='de_act'),
    path('up_grpt<int:id>/', views.update_grpt, name='up_grpt'),
    path('de_grpt<int:id>/', views.delete_grpt, name='de_grpt'),
    path('up_piro<int:id>/', views.update_piro, name='up_piro'),
    path('de_piro<int:id>/', views.delete_piro, name='de_piro'),
    path('up_imat<int:id>/', views.update_imat, name='up_imat'),
    path('de_imat<int:id>/', views.delete_imat, name='de_imat'),
    path('up_prodp<int:id>/', views.update_prodp, name='up_prodp'),
    path('de_prodp<int:id>/', views.delete_prodp, name='de_prodp'),
    path('up_niv<int:id>/', views.update_niv, name='up_niv'),
    path('de_niv<int:id>/', views.delete_niv, name='de_niv'),
    path('up_fact<int:id>/', views.update_fact, name='up_fact'),
    path('de_fact<int:id>/', views.delete_fact, name='de_fact'),
    path('up_repart<int:id>/', views.update_repart, name='up_repart'),
    path('de_repart<int:id>/', views.delete_repart, name='de_repart'),
    #end mise 
    path('up_ass<int:id>/', views.update_ass, name='up_ass'),
    path('de_ass<int:id>/', views.delete_ass, name='de_ass'),
    path('up_fin<int:id>/', views.update_fin, name='up_fin'),
    path('de_fin<int:id>/', views.delete_fin, name='de_fin'),
    path('up_com<int:id>/', views.update_com, name='up_com'),
    path('de_com<int:id>/', views.delete_com, name='de_com'),
    # ath('dimagroog/',views.dimagroorg_form,name='dimagroorg'),
    path('pech_ino/', views.pech_inov, name='pech_ino'),
    path('up_ino<int:id>/', views.update_ino, name='up_ino'),
    path('de_ino<int:id>/', views.delete_ino, name='de_ino'),
    path('pech_trans/', views.pechtrans, name='pech_trans'),
    path('update_trs<int:id>/', views.update_trs, name='update_trs'),
    path('delete_trs<int:id>/', views.delete_trs, name='delete_trs'),
    path('pech_taassu/', views.pechtassu, name='pech_taassu'),
    path('up_tassu<int:id>/', views.update_tassu, name='up_tassu'),
    path('de_tassu<int:id>/', views.delete_tasuu, name='de_tassu'),
    path('pech_tacom/', views.petacom, name='pech_tacom'),
    path('up_tc<int:id>/', views.update_tacom, name='up_tc'),
    path('de_tc<int:id>/', views.delete_tacom, name='de_tc'),
    path('pech_taino/', views.pech_tainov, name='pech_taino'),
    path('up_taino<int:id>/', views.up_taino, name='up_taino'),
    path('de_taino<int:id>/', views.de_taino, name='de_taino'),
    path('pech_tafina/', views.pechtafina, name='pech_tafina'),
    path('up_fi<int:id>/', views.up_fina, name='up_fi'),
    path('de_fi<int:id>/', views.de_fina, name='de_fi'),
    path('interactive-chart/', views.get_peche_artisan_data,
         name='interactive_chart'),
    path('interactive-chart/', views.get_peche_assurance_data,
         name='interactive_chart'),
    path('pirogue-chart/', views.pirogue,
         name='pirogue-chart'),

    path('mesure/', views.mesur, name='mesure'),
    path('total-mesures/', views.total_mesures, name='total_mesures'),


]
