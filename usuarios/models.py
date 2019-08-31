from django.db import models
from permissoes.models import Permissoes

class Usuarios(models.Model):
    idusuarios = models.AutoField(db_column='idUsuarios', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=80)
    rg = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=20)
    rua = models.CharField(max_length=70, blank=True, null=True)
    numero = models.CharField(max_length=15, blank=True, null=True)
    bairro = models.CharField(max_length=45, blank=True, null=True)
    cidade = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=80)
    senha = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    celular = models.CharField(max_length=20, blank=True, null=True)
    situacao = models.IntegerField()
    datacadastro = models.DateField(db_column='dataCadastro')  # Field name made lowercase.
    permissoes = models.ForeignKey(Permissoes, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuarios'