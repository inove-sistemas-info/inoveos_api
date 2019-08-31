from django.db import models

class ObservacoesOs(models.Model):
    idobs = models.AutoField(db_column='idObs', primary_key=True)  # Field name made lowercase.
    os_id = models.IntegerField()
    usuario_id = models.IntegerField()
    dataobs = models.DateTimeField(db_column='dataObs')  # Field name made lowercase.
    observacao = models.TextField()

    class Meta:
        managed = False
        db_table = 'observacoes_os'
