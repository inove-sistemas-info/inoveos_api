# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Anexos(models.Model):
    idanexos = models.AutoField(db_column='idAnexos', primary_key=True)  # Field name made lowercase.
    anexo = models.CharField(max_length=45, blank=True, null=True)
    thumb = models.CharField(max_length=45, blank=True, null=True)
    url = models.CharField(max_length=300, blank=True, null=True)
    path = models.CharField(max_length=300, blank=True, null=True)
    os = models.ForeignKey('Os', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'anexos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categorias(models.Model):
    idcategorias = models.AutoField(db_column='idCategorias', primary_key=True)  # Field name made lowercase.
    categoria = models.CharField(max_length=80, blank=True, null=True)
    cadastro = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class CiSessions(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    ip_address = models.CharField(max_length=45)
    timestamp = models.PositiveIntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'ci_sessions'


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


class Contas(models.Model):
    idcontas = models.AutoField(db_column='idContas', primary_key=True)  # Field name made lowercase.
    conta = models.CharField(max_length=45, blank=True, null=True)
    banco = models.CharField(max_length=45, blank=True, null=True)
    numero = models.CharField(max_length=45, blank=True, null=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cadastro = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contas'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Documentos(models.Model):
    iddocumentos = models.AutoField(db_column='idDocumentos', primary_key=True)  # Field name made lowercase.
    documento = models.CharField(max_length=70, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    file = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(max_length=300, blank=True, null=True)
    url = models.CharField(max_length=300, blank=True, null=True)
    cadastro = models.DateField(blank=True, null=True)
    categoria = models.CharField(max_length=80, blank=True, null=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    tamanho = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentos'


class Emitente(models.Model):
    nome = models.CharField(max_length=255, blank=True, null=True)
    cnpj = models.CharField(max_length=45, blank=True, null=True)
    ie = models.CharField(max_length=50, blank=True, null=True)
    rua = models.CharField(max_length=70, blank=True, null=True)
    numero = models.CharField(max_length=15, blank=True, null=True)
    bairro = models.CharField(max_length=45, blank=True, null=True)
    cidade = models.CharField(max_length=45, blank=True, null=True)
    uf = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    url_logo = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emitente'


class Equipamentos(models.Model):
    idequipamentos = models.AutoField(db_column='idEquipamentos', primary_key=True)  # Field name made lowercase.
    equipamento = models.CharField(max_length=150)
    num_serie = models.CharField(max_length=80, blank=True, null=True)
    modelo = models.CharField(max_length=80, blank=True, null=True)
    cor = models.CharField(max_length=45, blank=True, null=True)
    descricao = models.CharField(max_length=150, blank=True, null=True)
    tensao = models.CharField(max_length=45, blank=True, null=True)
    potencia = models.CharField(max_length=45, blank=True, null=True)
    voltagem = models.CharField(max_length=45, blank=True, null=True)
    data_fabricacao = models.DateField(blank=True, null=True)
    marcas = models.ForeignKey('Marcas', models.DO_NOTHING, blank=True, null=True)
    clientes = models.ForeignKey(Clientes, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipamentos'


class EquipamentosOs(models.Model):
    idequipamentos_os = models.AutoField(db_column='idEquipamentos_os', primary_key=True)  # Field name made lowercase.
    defeito_declarado = models.CharField(max_length=200, blank=True, null=True)
    defeito_encontrado = models.CharField(max_length=200, blank=True, null=True)
    solucao = models.CharField(max_length=45, blank=True, null=True)
    equipamentos = models.ForeignKey(Equipamentos, models.DO_NOTHING, blank=True, null=True)
    os = models.ForeignKey('Os', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipamentos_os'


class ItensDeVendas(models.Model):
    iditens = models.AutoField(db_column='idItens', primary_key=True)  # Field name made lowercase.
    subtotal = models.CharField(db_column='subTotal', max_length=45, blank=True, null=True)  # Field name made lowercase.
    quantidade = models.IntegerField(blank=True, null=True)
    vendas = models.ForeignKey('Vendas', models.DO_NOTHING)
    produtos = models.ForeignKey('Produtos', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'itens_de_vendas'


class Lancamentos(models.Model):
    idlancamentos = models.AutoField(db_column='idLancamentos', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=255, blank=True, null=True)
    valor = models.CharField(max_length=15)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(blank=True, null=True)
    baixado = models.IntegerField(blank=True, null=True)
    cliente_fornecedor = models.CharField(max_length=255, blank=True, null=True)
    forma_pgto = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    anexo = models.CharField(max_length=250, blank=True, null=True)
    clientes = models.ForeignKey(Clientes, models.DO_NOTHING, blank=True, null=True)
    categorias = models.ForeignKey(Categorias, models.DO_NOTHING, blank=True, null=True)
    contas = models.ForeignKey(Contas, models.DO_NOTHING, blank=True, null=True)
    vendas_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lancamentos'


class Logs(models.Model):
    idlogs = models.AutoField(db_column='idLogs', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(max_length=80, blank=True, null=True)
    tarefa = models.CharField(max_length=100, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs'


class Marcas(models.Model):
    idmarcas = models.AutoField(db_column='idMarcas', primary_key=True)  # Field name made lowercase.
    marca = models.CharField(max_length=100, blank=True, null=True)
    cadastro = models.DateField(blank=True, null=True)
    situacao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marcas'


class ObservacoesOs(models.Model):
    idobs = models.AutoField(db_column='idObs', primary_key=True)  # Field name made lowercase.
    os_id = models.IntegerField()
    usuario_id = models.IntegerField()
    dataobs = models.DateTimeField(db_column='dataObs')  # Field name made lowercase.
    observacao = models.TextField()

    class Meta:
        managed = False
        db_table = 'observacoes_os'


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
    usuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, blank=True, null=True)
    lancamento = models.ForeignKey(Lancamentos, models.DO_NOTHING, db_column='lancamento', blank=True, null=True)
    urgente = models.IntegerField(blank=True, null=True)
    modificada = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'os'


class Permissoes(models.Model):
    idpermissao = models.AutoField(db_column='idPermissao', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=80)
    permissoes = models.TextField(blank=True, null=True)
    situacao = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissoes'


class Produtos(models.Model):
    idprodutos = models.AutoField(db_column='idProdutos', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=80)
    unidade = models.CharField(max_length=10, blank=True, null=True)
    precocompra = models.DecimalField(db_column='precoCompra', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    precovenda = models.DecimalField(db_column='precoVenda', max_digits=10, decimal_places=2)  # Field name made lowercase.
    estoque = models.IntegerField()
    estoqueminimo = models.IntegerField(db_column='estoqueMinimo', blank=True, null=True)  # Field name made lowercase.
    saida = models.IntegerField(blank=True, null=True)
    entrada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produtos'


class ProdutosOs(models.Model):
    idprodutos_os = models.AutoField(db_column='idProdutos_os', primary_key=True)  # Field name made lowercase.
    quantidade = models.IntegerField()
    os = models.ForeignKey(Os, models.DO_NOTHING)
    produtos = models.ForeignKey(Produtos, models.DO_NOTHING)
    subtotal = models.CharField(db_column='subTotal', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produtos_os'


class Servicos(models.Model):
    idservicos = models.AutoField(db_column='idServicos', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'servicos'


class ServicosOs(models.Model):
    idservicos_os = models.AutoField(db_column='idServicos_os', primary_key=True)  # Field name made lowercase.
    os = models.ForeignKey(Os, models.DO_NOTHING)
    servicos = models.ForeignKey(Servicos, models.DO_NOTHING)
    subtotal = models.CharField(db_column='subTotal', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicos_os'


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


class Vendas(models.Model):
    idvendas = models.AutoField(db_column='idVendas', primary_key=True)  # Field name made lowercase.
    datavenda = models.DateField(db_column='dataVenda', blank=True, null=True)  # Field name made lowercase.
    valortotal = models.CharField(db_column='valorTotal', max_length=45, blank=True, null=True)  # Field name made lowercase.
    desconto = models.CharField(max_length=45, blank=True, null=True)
    faturado = models.IntegerField(blank=True, null=True)
    clientes = models.ForeignKey(Clientes, models.DO_NOTHING)
    usuarios = models.ForeignKey(Usuarios, models.DO_NOTHING, blank=True, null=True)
    lancamentos = models.ForeignKey(Lancamentos, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendas'
