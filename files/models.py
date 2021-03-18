from django.db import models


class ControlFile(models.Model):

    registry_type = models.IntegerField(default=1)
    NIT = models.IntegerField()
    name = models.CharField(max_length=20, blank=True)
    partnership_code = models.IntegerField()
    tranmission_date = models.DateField()
    shipping_code = models.CharField(max_length=1)
    expiry_date = models.DateField()
    registry_count = models.IntegerField()
    transactions_total = models.FloatField()
    details = models.CharField(max_length=79, blank=True)

    def __str__(self):
        return f"{self.name} {self.tranmission_date}"


class DetailFile(models.Model):

    BANCOLOMBIA = 5600078
    DAVIVIENDA = 5895142
    BANCO_AGRARIO = 1040
    BANCO_BOGOTA = 5600010
    BANCO_POPULAR = 5600023
    ITAU_CORPBANCA = 5600065
    CITIBANK = 5600094
    BANCO_SUDAMERIS = 5600120
    BANCO_BBVA = 5600133
    ITAU = 5600146
    SCOTTIA_BANK_COLPATRIA = 5600191
    BANCO_OCCIDENTE = 5600230
    BANCO_CAJA_SOCIAL = 5600230
    BANCO_AV_VILLAS = 6013677
    CONFIAR = 1292
    BANCO_PROCREDIT_COLOMBIA = 1058
    BANCO_COOPERATIVA_COOPCENTRAL = 1066
    RAPPIPAY = 1151
    BANCO_SERFINANZA = 1342
    NEQUI = 1507
    DAVIPLATA = 1551

    BANK_CHOICES = [
        (BANCOLOMBIA, "Bancolombia"),
        (DAVIVIENDA, "Davivienda"),
        (BANCO_AGRARIO, "Banco Agrario"),
        (BANCO_BOGOTA, "Banco de Bogota"),
        (ITAU_CORPBANCA, "Itau Corpbanca"),
        (CITIBANK, "Citibank"),
        (BANCO_SUDAMERIS, "Banco Sudameris"),
        (BANCO_BBVA, "Banco BBVA"),
        (ITAU, "Itau"),
        (SCOTTIA_BANK_COLPATRIA, "Scottia Bank Colpatria"),
        (BANCO_OCCIDENTE, "Banco de Occidente"),
        (BANCO_CAJA_SOCIAL, "Banco Caja Social"),
        (BANCO_AV_VILLAS, "Banco AV Villas"),
        (CONFIAR, "Confiar"),
        (BANCO_PROCREDIT_COLOMBIA, "Banco Procredit Colombia"),
        (BANCO_COOPERATIVA_COOPCENTRAL, "Banco Cooperativa Coopcentral"),
        (RAPPIPAY, "Rappipay"),
        (BANCO_SERFINANZA, "Banco Serfinanza"),
        (NEQUI, "Nequi"),
        (DAVIPLATA, "Daviplata"),
    ]

    CORRIENTE = 57
    AHORRO = 67
    TC_VISA = 77
    TC_MASTER = 87
    AMEX = 97

    TRANSACTION_CHOICES = [
        (CORRIENTE, "Cuenta Corriente"),
        (AHORRO, "Cuenta de Ahorros"),
        (TC_VISA, "TC Visa"),
        (TC_MASTER, "TC Master"),
        (AMEX, "Amex"),
    ]

    SI = "S"
    NO = "N"

    INDICATOR_CHOICES = [(SI, "Si"), (NO, "No")]

    control_file = models.ForeignKey(
        ControlFile, related_name="detail_files", on_delete=models.CASCADE
    )
    registry_type = models.IntegerField(default=6)
    NIT = models.CharField(max_length=13, blank=True)
    name = models.CharField(max_length=20, blank=True)
    bank_account = models.CharField(choices=BANK_CHOICES, max_length=9, blank=True)
    account_number = models.CharField(max_length=17, blank=True)
    transaction_type = models.CharField(
        choices=TRANSACTION_CHOICES, max_length=2, blank=True
    )
    transaction_amount = models.FloatField()
    validation_indicator = models.CharField(
        choices=INDICATOR_CHOICES, max_length=1, blank=True
    )
    reference_1 = models.CharField(max_length=30, blank=True)
    reference_2 = models.CharField(max_length=30, blank=True)
    expiry_date = models.DateField(blank=True)
    billed_period = models.CharField(max_length=2, blank=True)
    cycle = models.CharField(max_length=3, blank=True)
    details = models.CharField(max_length=17, blank=True)

    def __str__(self):
        return f"{self.name} {self.control_file.name}"
