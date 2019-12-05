# Generated by Django 2.2 on 2019-08-31 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('idclientes', models.AutoField(db_column='idClientes', primary_key=True, serialize=False)),
                ('nomecliente', models.CharField(db_column='nomeCliente', max_length=255)),
                ('funcionarios', models.TextField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, max_length=20, null=True)),
                ('pessoa_fisica', models.IntegerField()),
                ('documento', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
                ('telefonesadicionais', models.TextField(blank=True, db_column='telefonesAdicionais', null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(max_length=100)),
                ('datacadastro', models.DateField(blank=True, db_column='dataCadastro', null=True)),
                ('rua', models.CharField(blank=True, max_length=70, null=True)),
                ('numero', models.CharField(blank=True, max_length=15, null=True)),
                ('bairro', models.CharField(blank=True, max_length=45, null=True)),
                ('cidade', models.CharField(blank=True, max_length=45, null=True)),
                ('estado', models.CharField(blank=True, max_length=20, null=True)),
                ('cep', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'clientes',
                'managed': False,
            },
        ),
    ]