# Generated by Django 2.2 on 2019-08-31 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Os',
            fields=[
                ('idos', models.AutoField(db_column='idOs', primary_key=True, serialize=False)),
                ('dataabertura', models.DateTimeField(blank=True, db_column='dataAbertura', null=True)),
                ('datafinal', models.DateTimeField(blank=True, db_column='dataFinal', null=True)),
                ('agendamento', models.TextField(blank=True, null=True)),
                ('datapausa', models.DateField(blank=True, db_column='dataPausa', null=True)),
                ('descricaoproduto', models.TextField(blank=True, db_column='descricaoProduto', null=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('meiosolicitacao', models.CharField(db_column='meioSolicitacao', max_length=45)),
                ('categoria', models.CharField(max_length=15)),
                ('status', models.CharField(blank=True, max_length=45, null=True)),
                ('motivopausa', models.TextField(blank=True, db_column='motivoPausa', null=True)),
                ('timeline', models.TextField(blank=True, null=True)),
                ('laudotecnico', models.TextField(blank=True, db_column='laudoTecnico', null=True)),
                ('valortotal', models.CharField(blank=True, db_column='valorTotal', max_length=15, null=True)),
                ('urgente', models.IntegerField(blank=True, null=True)),
                ('modificada', models.DateTimeField()),
            ],
            options={
                'db_table': 'os',
                'managed': False,
            },
        ),
    ]