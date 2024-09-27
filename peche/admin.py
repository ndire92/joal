from django.contrib import admin

from peche.models import DimPecheArtisan,DimPAPirogue,DimPAPiroguImmat,DimPAProduitPirog,DimPAProdTypeNiv,FactPechArtisan,DimPechComRepartition,DimPechTransformArtisan,DimPechTAFinance,DimPechTACommerc, DimPechTAAssurance, DimPecheArtisanAct,DimPecheTAInnovat,DimPecheInnovat,DimPecheAssure,DimPecheCommerce,DimPecheFinance, DimPechArtGpment

# Register your models here.

admin.site.register(DimPecheArtisan)
admin.site.register(DimPecheAssure)
admin.site.register(DimPecheCommerce)
admin.site.register(DimPecheFinance)

admin.site.register(DimPecheInnovat)
admin.site.register(DimPecheTAInnovat)
admin.site.register( DimPechTAAssurance)
admin.site.register(DimPechTACommerc)

admin.site.register(DimPechTAFinance)
admin.site.register(DimPechTransformArtisan)



admin.site.register(DimPecheArtisanAct)

admin.site.register(DimPechArtGpment)
admin.site.register(DimPAPirogue)
admin.site.register( DimPAPiroguImmat)
admin.site.register(DimPAProduitPirog)

admin.site.register(DimPAProdTypeNiv)
admin.site.register(FactPechArtisan)
admin.site.register(DimPechComRepartition)
#admin.site.register(FactPechArtisan)

