from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class DimPecheArtisan(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    ActPech_Artisan = models.CharField(max_length=250)
    NbrActeur = models.IntegerField()
    GroupPecheur = models.CharField(max_length=250)
    NbreGIEPecheur = models.IntegerField()
    NbrOrganiProfessPecheur = models.IntegerField()
    Nbr_AssociatPecheur = models.IntegerField()
    GroupMareyeur = models.CharField(max_length=250)
    NbreGIEMarey = models.IntegerField()
    NbrOrganiProfessMarey = models.IntegerField()
    Nbr_AssociatMarey = models.IntegerField()
    NbreQuaiPech = models.IntegerField()
    TypePirogu = models.CharField(max_length=250)
    NbrPirogBois = models.IntegerField(default=0)
    NbrePirogFibVer = models.IntegerField(default=0)
    NbrPirogAlumin = models.IntegerField(default=0)
    NbrePirogImmatri = models.IntegerField(default=0)
    TypProdPechPirogBois = models.CharField(max_length=250)
    TypProdPechPirogFibr = models.CharField(max_length=250)
    TypProdPechPirogAlumin = models.CharField(max_length=250)
    TypeProdHalieuHiver = models.CharField(max_length=250)

    TypeProdHalieuInterSaison = models.CharField(max_length=250)
    TypeProdHalieuSaisFroid = models.CharField(max_length=250)
    TypeProdHalieuPrimptem = models.CharField(max_length=250)
    IntrantPech = models.CharField(max_length=250)
    MatUtilisePech = models.CharField(max_length=250)
    SourcApprovis_Intran = models.CharField(max_length=250)
    SourcApprovis_Materiel = models.CharField(max_length=250)
    Qteannuel_debarq = models.IntegerField()
    NivCaptMoyenHiver = models.CharField(max_length=250)
    NivCaptMoyenInterSaison = models.CharField(max_length=250)
    NivCaptMoyenSaisFroid = models.CharField(max_length=250)
    NivCaptMoyenPrintem = models.CharField(max_length=250)
    NivCaptMoyenSortTypProd = models.CharField(max_length=250)
    NivPertPostCaptHiver = models.CharField(max_length=250)
    NivPertPostCaptInterSaison = models.CharField(max_length=250)
    NivPertPostCaptSaisFroid = models.CharField(max_length=250)
    NivPertPostCaptPrintem = models.CharField(max_length=250)
    NivPertPostCaptTypProd = models.CharField(max_length=250)

    annee = models.IntegerField()
    annee_modification = models.IntegerField()

    def sum_of_selected_fields(self):
        # Remplacez les champs que vous souhaitez additionner ici
        fields_to_sum = [
            self.NbrActeur,
            self.NbreGIEPecheur,
            self.NbrOrganiProfessPecheur,
            self.Nbr_AssociatPecheur,
            self.NbreGIEMarey,
            self.NbrOrganiProfessMarey,
            self.Nbr_AssociatMarey,
            self.NbreQuaiPech,
            self.NbrPirogBois,
            # Ajoutez d'autres champs à additionner si nécessaire
        ]

        # Utilisez une boucle pour additionner les champs
        total_sum = sum(fields_to_sum)

        return total_sum

class DimPecheArtisanAct(models.Model):
    CodePostal = models.IntegerField()
    NomCommune = models.CharField(max_length=300)
    ActPech_Artisan = models.CharField(max_length=250)
    NbrActeur = models.IntegerField()
    annee = models.IntegerField()
    annee_modification = models.IntegerField()
    
    
    def sum_of_selected_fields(self):
            # Remplacez les champs que vous souhaitez additionner ici
        fields_to_sum = [
            self.NbrActeur,
        ]

        total_sum = sum(fields_to_sum)

        return total_sum


class DimPechArtGpment(models.Model):
    # for
    ActPech_Artisan = models.CharField(max_length=250)
    GroupmentActeur = models.CharField(max_length=250)  
    annee = models.IntegerField()
    annee_modification = models.IntegerField()
    
    def __str__(self):
        return str(self.ActPech_Artisan)
    

class DimPAPirogue(models.Model):
    TypePirogu = models.CharField(max_length=250)
    NbrPirogu = models.IntegerField()
    EspecCible = models.CharField(max_length=250)
    TypePecheur = models.CharField(max_length=250)
    annee = models.IntegerField()
    annee_modification = models.IntegerField()

    def __str__(self):
        return str(self.NbrPirogu)

    
class DimPAPiroguImmat(models.Model):
    TYPE_CHOICES = (
        ('type permis B longueur < à 13', 'type permis B longueur < à 13'),
        ('type permis C longueur > à 13', 'type permis C longueur > à 13'),
        ('A', 'Type A: pêche à pied = 0'),
    )

    TypPermis = models.CharField(max_length=250, choices=TYPE_CHOICES, verbose_name='Type de Permis')
    NbrePiroguImmatPermis = models.IntegerField(verbose_name='Nombre de Pirogues Immatriculées')
    annee = models.IntegerField(verbose_name='Année')
    annee_modification  = models.IntegerField(verbose_name='Année de Modification')

    def __str__(self):
        return f"{self.get_TypPermis_display()} - {self.Annee}"

    class Meta:
        verbose_name = 'Pirogue Immatriculée'
        verbose_name_plural = 'Pirogues Immatriculées'
        unique_together = ('TypPermis', 'annee')

    def save(self, *args, **kwargs):
        # Ajoutez des vérifications ou des opérations supplémentaires avant de sauvegarder si nécessaire
        super().save(*args, **kwargs)
    

class DimPAProduitPirog(models.Model):
    TypePirogu = models.CharField(max_length=250)
    TypeProdPechPirog = models.CharField(max_length=250)
    IntrantPech = models.CharField(max_length=250)
    MatUtilisePech = models.CharField(max_length=250)
    SourcApprovis_Intran = models.CharField(max_length=250)
    SourcApprovis_Materiel = models.CharField(max_length=250)
    annee = models.IntegerField()
    annee_modification = models.IntegerField()
    
    def __str__(self):
        return str(self.TypeProdPechPirog)

class DimPAProdTypeNiv(models.Model):
    TypeProdHalieuPeriod = models.CharField(max_length=250)
    TypeProdHalieuHiver = models.CharField(max_length=250)
    NivCaptMoyenSortTypProd = models.CharField(max_length=250)
    NivPertPostCaptTypProd = models.CharField(max_length=250)
    annee = models.IntegerField()
    annee_modification = models.IntegerField()
    
    def __str__(self):
        return str(self.TypeProdHalieuPeriod)
    

class FactPechArtisan(models.Model):
    CodePostal = models.IntegerField()
    NomCommune = models.CharField(max_length=300)
    annee = models.IntegerField()

    NbreGIEPecheur = models.IntegerField()
    NbrOrganiProfessPecheur = models.IntegerField()
    Nbr_AssociatPecheur = models.IntegerField()
    NbreGIEMarey = models.IntegerField()
    NbrOrganiProfessMarey = models.IntegerField()
    Nbr_AssociatMarey = models.IntegerField()
    NbreQuaiPech = models.IntegerField()
    NbrPirogBois = models.IntegerField()
    NbrePirogFibVer = models.IntegerField()
    NbrPirogAlumin = models.IntegerField()
    NbrePirogImmatri = models.BigIntegerField()
    Qteannuel_debarq = models.BigIntegerField()
    ValeurComCaptAnnuel = models.BigIntegerField()
    VolumDebitCarb = models.BigIntegerField()
    ValeurCommCarbu = models.BigIntegerField()
    TotStatCarbu = models.BigIntegerField()
    NbrTotFabriqGlace = models.BigIntegerField()
    NbrMareyTotDeclare = models.BigIntegerField()
    NbrMareyTotRecensmt = models.BigIntegerField()
    NbrPecheurTotRecensmt = models.BigIntegerField()
    NbrPirogRenouvll = models.IntegerField()
    QteApprovisPoisson = models.IntegerField()
    QteTotProdTA = models.IntegerField()
    ValeurComProdTA = models.CharField(max_length=500)
    NbreTotTypPirog = models.IntegerField()

    annee_modification = models.IntegerField()
    
    def __str__(self):
        return str(self.NomCommune)

 
    
 

class DimPecheAssure(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)

    OffreAssureExistPech = models.CharField(max_length=25)
    TypeAssurancPech = models.CharField(max_length=25)
    NbreSouscripPech = models.IntegerField()
    NbrePrimePech = models.IntegerField()
    BesoinFormatPech = models.CharField(max_length=250)
    ActeurSensibilisePech = models.CharField(max_length=250)
    ActeurFormatPech = models.CharField(max_length=250)
    BesoinSensibilisePech = models.CharField(max_length=250)
    ContraintGlobPech = models.CharField(max_length=250)
    ContrainMajFilier = models.CharField(max_length=250)
    NbrInfrastruStokCondition = models.IntegerField()
    NbrFourniEmblag = models.IntegerField()
    NbrProdLabel = models.IntegerField()

    annee = models.IntegerField()
    annee_modification = models.IntegerField()

    def sum_of_selected_fields(self):
        # Remplacez les champs que vous souhaitez additionner ici
        fields_to_sum = [
            self.NbreSouscripPech,

            # Ajoutez d'autres champs à additionner si nécessaire
        ]

        # Utilisez une boucle pour additionner les champs
        total_sum = sum(fields_to_sum)

        return total_sum
    
class DimPechComRepartition(models.Model):
    TypRepartiProd = models.CharField(max_length=250)
    QteRepAnnuel = models.IntegerField()
    
    annee = models.IntegerField()
    annee_modification = models.IntegerField()
    
    def __str__(self):
        return str(self.TypRepartiProd)
    
    

class DimPecheCommerce(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    ProdVendType = models.DecimalField(max_digits=10, decimal_places=5)
    PeriodProdVend = models.DecimalField(max_digits=10, decimal_places=5)
    QteProdVendCampgn = models.DecimalField(max_digits=10, decimal_places=5)
    Type_VentPech = models.CharField(max_length=250)
    PriVentMoy_Prod = models.IntegerField()
    Mod_ecoulement = models.CharField(max_length=250)
    ClientPech = models.CharField(max_length=250)
    annee = models.IntegerField()
    annee_modification = models.IntegerField()

    def sum_of_selected_fields(self):
        # Remplacez les champs que vous souhaitez additionner ici
        fields_to_sum = [
            self.ProdVendType,

            # Ajoutez d'autres champs à additionner si nécessaire
        ]

        # Utilisez une boucle pour additionner les champs
        total_sum = sum(fields_to_sum)

        return total_sum


class DimPecheFinance(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    OffrServicFinancPech = models.CharField(max_length=25)
    DemandApportPech = models.CharField(max_length=25)
    TypGaranExige = models.CharField(max_length=250)
    LongProcedCredi = models.CharField(max_length=250)
    TauInteret = models.CharField(max_length=250)
    DelaiRemboursMinMax = models.CharField(max_length=250)
    annee = models.IntegerField()
    annee_modification = models.IntegerField()

    def __str__(self):
        return self.OffrServicFinancPech


class DimPecheInnovat(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    TechnoIntrod = models.CharField(max_length=250)
    TechnoAdopte = models.CharField(max_length=25)
    CausNoAdoption = models.CharField(max_length=250)
    CausTechnoNoAdop = models.CharField(max_length=250)
    annee = models.IntegerField()
    annee_modification = models.IntegerField()

    def __str__(self):
        return self.TechnoIntrod


class DimPecheTAInnovat(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    TechnoIntroTA = models.CharField(max_length=250)
    TechnoAdoptTA = models.CharField(max_length=25)
    CausNoAdoptTA = models.CharField(max_length=250)
    CausTechnoNoAdopTA = models.CharField(max_length=250)
    annee = models.IntegerField()
    annee_modification = models.IntegerField()

    def __str__(self):
        return self.TechnoIntroTA


class DimPechTAAssurance(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    OffreAssurTA = models.CharField(max_length=250)
    TypAssurTA = models.CharField(max_length=250)
    NbrSouscripTA = models.IntegerField()
    NivPrimTA = models.IntegerField()
    BesoinformTA = models.CharField(max_length=250)
    ContraintGlobTA = models.CharField(max_length=250)
    ContrainMajFilierTA = models.CharField(max_length=250)

    annee = models.IntegerField()
    annee_modification = models.IntegerField()

    def __str__(self):

        return self.OffreAssurTA


class DimPechTACommerc(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    ProdVenduCampagTA = models.CharField(max_length=300)
    TypVentTA = models.CharField(max_length=300)
    PrixVentMoyProdTA = models.DecimalField(max_digits=10, decimal_places=5)

    ModEcoulmtTA = models.CharField(max_length=300)
    ClientTA = models.CharField(max_length=300)
    annee = models.IntegerField()
    annee_modification = models.IntegerField()

    def __str__(self):

        return self.ProdVenduCampagTA


class DimPechTAFinance(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    OffrServicFinancTA = models.CharField(max_length=25)
    DemandApportTA = models.CharField(max_length=25)
    TypGaranExigeTA = models.CharField(max_length=250)
    LongProcedCrditTA = models.CharField(max_length=250)
    MontanMoyTA = models.DecimalField(max_digits=10, decimal_places=5)
    TauInterTA = models.CharField(max_length=250)
    DelaiRemboursMinMaxTA = models.CharField(max_length=250)

    annee = models.IntegerField()
    annee_modification = models.IntegerField()

    def __str__(self):
        return self.OffrServicFinancTA


class DimPechTransformArtisan(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    ActTransfArtisan = models.CharField(max_length=25)
    GrptTransformtrTA = models.CharField(max_length=25)
    TypServicOffrGIE = models.CharField(max_length=250)
    TypServicOffrAssocia = models.CharField(max_length=250)
    TypServicOffrOrgProf = models.CharField(max_length=250)
    FourniIntranMatTrans = models.CharField(max_length=250)
    SitTransform = models.CharField(max_length=250)
    MatEquipTransExist = models.CharField(max_length=250)

    TypProdTransfPeriod = models.CharField(max_length=250)
    SourcApproIntranMatTA = models.CharField(max_length=250)
    QteProdPeriodTA = models.DecimalField(max_digits=10, decimal_places=5)
    QteProdTypeTA = models.DecimalField(max_digits=10, decimal_places=5)
    TauxTransformArtisan = models.DecimalField(max_digits=10, decimal_places=5)
    annee = models.IntegerField()
    annee_modification = models.IntegerField()

    def __str__(self):
        return str(self.TauxTransformArtisan)



