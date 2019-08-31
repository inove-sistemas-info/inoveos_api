from django.db import models

class Clientes(models.Model):
    idclientes = models.AutoField(db_column='idClientes', primary_key=True)  # Field name made lowercase.
    nomecliente = models.CharField(db_column='nomeCliente', max_length=255)  # Field name made lowercase.
    funcionarios = models.TextField(blank=True, null=True)
    sexo = models.CharField(max_length=20, blank=True, null=True)
    pessoa_fisica = models.IntegerField()
    documento = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    telefonesadicionais = models.TextField(db_column='telefonesAdicionais', blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100)
    datacadastro = models.DateField(db_column='dataCadastro', blank=True, null=True)  # Field name made lowercase.
    rua = models.CharField(max_length=70, blank=True, null=True)
    numero = models.CharField(max_length=15, blank=True, null=True)
    bairro = models.CharField(max_length=45, blank=True, null=True)
    cidade = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    cep = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'
