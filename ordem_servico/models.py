from django.db import models
from usuarios.models import Usuarios
from clientes.models import Clientes

class Os(models.Model):
    idos = models.AutoField(db_column='idOs', primary_key=True)  # Field name made lowercase.
    dataabertura = models.DateTimeField(db_column='dataAbertura', blank=True, null=True)  # Field name made lowercase.
    datafinal = models.DateTimeField(db_column='dataFinal', blank=True, null=True)  # Field name made lowercase.
    agendamento = models.TextField(blank=True, null=True)
    datapausa = models.DateField(db_column='dataPausa', blank=True, null=True)  # Field name made lowercase.
    descricaoproduto = models.TextField(db_column='descricaoProduto', blank=True, null=True)  # Field name made lowercase.
    descricao = models.TextField(blank=True, null=True)
    meiosolicitacao = models.CharField(db_column='meioSolicitacao', max_length=45)  # Field name made lowercase.
    categoria = models.CharField(max_length=15)
    status = models.CharField(max_length=45, blank=True, null=True)
    motivopausa = models.TextField(db_column='motivoPausa', blank=True, null=True)  # Field name made lowercase.
    timeline = models.TextField(blank=True, null=True)
    laudotecnico = models.TextField(db_column='laudoTecnico', blank=True, null=True)  # Field name made lowercase.
    valortotal = models.CharField(db_column='valorTotal', max_length=15, blank=True, null=True)  # Field name made lowercase.
    clientes = models.ForeignKey(Clientes, models.DO_NOTHING)
    usuarios = models.ForeignKey(Usuarios, models.DO_NOTHING, blank=True, null=True)
    urgente = models.IntegerField(blank=True, null=True)
    modificada = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'os'
