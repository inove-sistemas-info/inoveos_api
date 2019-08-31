from django.db import models

class Permissoes(models.Model):
    idpermissao = models.AutoField(db_column='idPermissao', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=80)
    permissoes = models.TextField(blank=True, null=True)
    situacao = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissoes'
