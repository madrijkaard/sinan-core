from django.db import models


class AcidenteTrabalhoGrave(models.Model):
    """
    Ficha de Investigação - DRT Acidente Trabalho Grave
    Dicionário de Dados SINAN NET - Versão 5.0
    Campos 31 a 68 + campos de controle
    """

    # -------------------------------------------------------------------------
    # Campos de controle (infraestrutura)
    # -------------------------------------------------------------------------

    id = models.BigAutoField(
        primary_key=True,
        verbose_name="ID",
        help_text="Chave primária do registro",
    )
    code = models.CharField(
        max_length=10,
        verbose_name="Código",
        help_text="Código de identificação do registro",
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de criação",
        help_text="Timestamp de criação do registro",
    )
    created_by = models.CharField(
        max_length=256,
        verbose_name="Criado por",
        help_text="Usuário que criou o registro",
    )
    last_modified_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Data de última modificação",
        help_text="Timestamp da última modificação do registro",
    )
    last_modified_by = models.CharField(
        max_length=256,
        verbose_name="Modificado por",
        help_text="Usuário que realizou a última modificação",
    )
    status = models.CharField(
        max_length=20,
        verbose_name="Status",
        help_text="Status do registro",
    )

    # -------------------------------------------------------------------------
    # Choices reutilizáveis
    # -------------------------------------------------------------------------

    class SimNaoIgnorado(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        IGNORADO = '9', 'Ignorado'

    class SimNaoNaoSeAplicaIgnorado(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        NAO_SE_APLICA = '3', 'Não se aplica'
        IGNORADO = '9', 'Ignorado'

    # -------------------------------------------------------------------------
    # Campo 31 - Ocupação
    # -------------------------------------------------------------------------

    co_cbo_ocupacao = models.CharField(
        max_length=6,
        verbose_name="Ocupação (CBO)",
        help_text="Ocupação do indivíduo que sofreu o agravo.",
    )

    # -------------------------------------------------------------------------
    # Campo 32 - Situação no mercado de trabalho
    # -------------------------------------------------------------------------

    class SituacaoMercadoTrabalho(models.TextChoices):
        EMPREGADO_REGISTRADO = '01', 'Empregado registrado com carteira assinada'
        EMPREGADO_NAO_REGISTRADO = '02', 'Empregado não registrado'
        AUTONOMO = '03', 'Autônomo/conta própria'
        SERVIDOR_PUBLICO_ESTATUTARIO = '04', 'Servidor público estatutário'
        SERVIDOR_PUBLICO_CELETISTA = '05', 'Servidor público celetista'
        APOSENTADO = '06', 'Aposentado'
        DESEMPREGADO = '07', 'Desempregado'
        TRABALHO_TEMPORARIO = '08', 'Trabalho temporário'
        COOPERATIVADO = '09', 'Cooperativado'
        TRABALHADOR_AVULSO = '10', 'Trabalhador avulso'
        EMPREGADOR = '11', 'Empregador'
        OUTROS = '12', 'Outros'
        IGNORADO = '99', 'Ignorado'

    tp_mercado_trabalho = models.CharField(
        max_length=2,
        choices=SituacaoMercadoTrabalho.choices,
        null=True,
        blank=True,
        verbose_name="Situação no mercado de trabalho",
        help_text="Situação de trabalho do indivíduo que sofreu o agravo.",
    )

    # -------------------------------------------------------------------------
    # Campo 33 - Tempo de trabalho na ocupação
    # -------------------------------------------------------------------------

    nu_tempo_trabalho = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Tempo de trabalho na ocupação",
        help_text="Quantidade de tempo trabalhado na ocupação.",
    )

    class UnidadeTempoTrabalho(models.TextChoices):
        HORA = '1', 'Hora'
        DIAS = '2', 'Dias'
        MESES = '3', 'Meses'
        ANOS = '4', 'Anos'

    tp_tempo_trabalho = models.CharField(
        max_length=1,
        choices=UnidadeTempoTrabalho.choices,
        null=True,
        blank=True,
        verbose_name="Unidade de tempo",
        help_text="Unidade de medida do tempo de trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Local onde ocorreu o acidente
    # -------------------------------------------------------------------------

    class LocalAcidente(models.TextChoices):
        INSTALACOES_CONTRATANTE = '1', 'Instalações do Contratante'
        VIA_PUBLICA = '2', 'Via Pública'
        INSTALACOES_TERCEIROS = '3', 'Instalações de terceiros'
        DOMICILIO_PROPRIO = '4', 'Domicílio próprio'
        IGNORADO = '9', 'Ignorado'

    tp_local_acidente = models.CharField(
        max_length=1,
        choices=LocalAcidente.choices,
        verbose_name="Local onde ocorreu o acidente",
        help_text="Local onde ocorreu o acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Registro/CNPJ/CPF
    # -------------------------------------------------------------------------

    nu_cnpj_cpf = models.CharField(
        max_length=18,
        null=True,
        blank=True,
        verbose_name="CNPJ/CPF do contratante",
        help_text="Número de registro/CNPJ ou CPF do contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Nome da empresa ou empregador
    # -------------------------------------------------------------------------

    no_empresa = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Nome da empresa ou empregador",
        help_text="Nome da empresa ou empregador contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Código da atividade Econômica (CNAE)
    # -------------------------------------------------------------------------

    co_cnae = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="CNAE",
        help_text="Classificação Nacional da Atividade Econômica do Contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - UF
    # -------------------------------------------------------------------------

    co_uf_empresa = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF da empresa",
        help_text="Unidade da Federação da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Município
    # -------------------------------------------------------------------------

    co_municipio_empresa = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município da empresa",
        help_text="Município da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Distrito
    # -------------------------------------------------------------------------

    co_distrito_empresa = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Distrito da empresa",
        help_text="Distrito da empresa contratante.",
    )
    no_distrito_empresa = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Nome do distrito da empresa",
        help_text="Nome do distrito da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Bairro
    # -------------------------------------------------------------------------

    co_bairro_empresa = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name="Código do bairro da empresa",
        help_text="Código do bairro da empresa contratante.",
    )
    no_bairro_empresa = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Bairro da empresa",
        help_text="Bairro da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Endereço
    # -------------------------------------------------------------------------

    co_endereco_empresa = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Código do endereço da empresa",
        help_text="Código do endereço da empresa contratante.",
    )
    no_endereco_empresa = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Endereço da empresa",
        help_text="Endereço da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Número
    # -------------------------------------------------------------------------

    nu_numero_empresa = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Número do endereço da empresa",
        help_text="Número do lote da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Ponto de Referência
    # -------------------------------------------------------------------------

    no_referencia_empresa = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Ponto de referência da empresa",
        help_text="Ponto de referência da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - (DDD) Telefone
    # -------------------------------------------------------------------------

    nu_ddd_empresa = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name="DDD da empresa",
        help_text="DDD do telefone da empresa contratante.",
    )
    nu_telefone_empresa = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Telefone da empresa",
        help_text="Telefone da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - O empregador é empresa Terceirizada
    # -------------------------------------------------------------------------

    tp_empresa_terceirizada = models.CharField(
        max_length=2,
        choices=SimNaoNaoSeAplicaIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Empregador é empresa terceirizada",
        help_text="O empregador é de alguma empresa terceirizada.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Se empresa terceirizada, Qual o CNAE da empresa terceirizada
    # -------------------------------------------------------------------------

    co_cnae_principal = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="CNAE da empresa principal",
        help_text="CNAE da empresa terceirizadora/principal.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - CNPJ da empresa principal
    # -------------------------------------------------------------------------

    nu_cnpj_principal = models.CharField(
        max_length=18,
        null=True,
        blank=True,
        verbose_name="CNPJ da empresa principal",
        help_text="CNPJ da empresa principal (terceirizadora).",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Razão social (Nome da Empresa)
    # -------------------------------------------------------------------------

    no_razao_social_principal = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Razão social da empresa principal",
        help_text="Nome da empresa principal (terceirizadora).",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Hora do Acidente
    # -------------------------------------------------------------------------

    nu_hr_acidente = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Hora do acidente",
        help_text="Hora em que ocorreu o acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Minutos do Acidente
    # -------------------------------------------------------------------------

    nu_minuto_acidente = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Minutos do acidente",
        help_text="Minutos em que ocorreu o acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Horas após início da jornada
    # -------------------------------------------------------------------------

    nu_hr_inicio_jornada = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Horas após início da jornada",
        help_text="Horas decorridas após o início da jornada de trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Minutos após início da jornada
    # -------------------------------------------------------------------------

    nu_minuto_inicio_jornada = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Minutos após início da jornada",
        help_text="Minutos decorridos após o início da jornada de trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - UF
    # -------------------------------------------------------------------------

    co_uf_acidente = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF do local do acidente",
        help_text="Unidade Federativa do local do acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Município de ocorrência do acidente
    # -------------------------------------------------------------------------

    co_municipio_acidente = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município de ocorrência do acidente",
        help_text="Município onde ocorreu o acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Código da Causa do Acidente CID 10 (de V01 a Y98)
    # -------------------------------------------------------------------------

    co_cid_causa_acidente = models.CharField(
        max_length=4,
        verbose_name="CID-10 da causa do acidente",
        help_text="Código CID-10 da causa do acidente (V01 a Y98).",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Tipo de Acidente
    # -------------------------------------------------------------------------

    class TipoAcidente(models.TextChoices):
        TIPICO = '1', 'Típico'
        TRAJETO = '2', 'Trajeto'
        IGNORADO = '9', 'Ignorado'

    tp_acidente = models.CharField(
        max_length=1,
        choices=TipoAcidente.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de acidente",
        help_text="Tipo de acidente (típico ou trajeto).",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - Houve Outros Trabalhadores Atingidos?
    # -------------------------------------------------------------------------

    st_trabalhador_atingido_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Houve outros trabalhadores atingidos",
        help_text="Se outros trabalhadores foram atingidos pelo acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 57 - Se Sim, Quantos
    # -------------------------------------------------------------------------

    nu_trabalhador_atingido = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name="Número de trabalhadores atingidos",
        help_text="Quantidade de outros trabalhadores atingidos.",
    )

    # -------------------------------------------------------------------------
    # Campo 58 - Ocorreu Atendimento Médico?
    # -------------------------------------------------------------------------

    st_atendimento_medico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Ocorreu atendimento médico",
        help_text="Se ocorreu atendimento médico ao acidentado.",
    )

    # -------------------------------------------------------------------------
    # Campo 59 - Data do Atendimento
    # -------------------------------------------------------------------------

    dt_atendimento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do atendimento",
        help_text="Data do atendimento médico.",
    )

    # -------------------------------------------------------------------------
    # Campo 60 - UF do Atendimento
    # -------------------------------------------------------------------------

    co_uf_atendimento = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF do atendimento",
        help_text="Unidade Federativa do local do atendimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 61 - Município do Atendimento
    # -------------------------------------------------------------------------

    co_municipio_atendimento = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município do atendimento",
        help_text="Município onde ocorreu o atendimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 62 - Nome da Unidade de Saúde de Atendimento
    # -------------------------------------------------------------------------

    co_unidade_atendimento = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Código da unidade de atendimento",
        help_text="Código da unidade de saúde de atendimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 63 - Partes do corpo atingida (3 subcampos)
    # -------------------------------------------------------------------------

    class ParteCorpo(models.TextChoices):
        OLHO = '01', 'Olho'
        CABECA = '02', 'Cabeça'
        PESCOCO = '03', 'Pescoço'
        TORAX = '04', 'Tórax'
        ABDOME = '05', 'Abdome'
        MAO = '06', 'Mão'
        MEMBRO_SUPERIOR = '07', 'Membro superior'
        MEMBRO_INFERIOR = '08', 'Membro inferior'
        PE = '09', 'Pé'
        TODO_CORPO = '10', 'Todo o corpo'
        OUTRO = '11', 'Outro'
        IGNORADO = '99', 'Ignorado'

    tp_parte_corpo_1 = models.CharField(
        max_length=2,
        choices=ParteCorpo.choices,
        null=True,
        blank=True,
        verbose_name="Parte do corpo atingida 1",
        help_text="Parte do corpo atingida no acidente - 1ª ocorrência.",
    )
    tp_parte_corpo_2 = models.CharField(
        max_length=2,
        choices=ParteCorpo.choices,
        null=True,
        blank=True,
        verbose_name="Parte do corpo atingida 2",
        help_text="Parte do corpo atingida no acidente - 2ª ocorrência.",
    )
    tp_parte_corpo_3 = models.CharField(
        max_length=2,
        choices=ParteCorpo.choices,
        null=True,
        blank=True,
        verbose_name="Parte do corpo atingida 3",
        help_text="Parte do corpo atingida no acidente - 3ª ocorrência.",
    )

    # -------------------------------------------------------------------------
    # Campo 64 - Diagnóstico da lesão CID 10
    # -------------------------------------------------------------------------

    co_cid_lesao = models.CharField(
        max_length=4,
        verbose_name="CID-10 da lesão",
        help_text="Código CID-10 do diagnóstico da lesão.",
    )

    # -------------------------------------------------------------------------
    # Campo 65 - Regime de Tratamento
    # -------------------------------------------------------------------------

    class RegimeTratamento(models.TextChoices):
        HOSPITALAR = '1', 'Hospitalar'
        AMBULATORIAL = '2', 'Ambulatório'
        AMBOS = '3', 'Ambos'
        IGNORADO = '9', 'Ignorado'

    tp_regime_tratamento = models.CharField(
        max_length=1,
        choices=RegimeTratamento.choices,
        null=True,
        blank=True,
        verbose_name="Regime de tratamento",
        help_text="Tipo de tratamento recebido.",
    )

    # -------------------------------------------------------------------------
    # Campo 66 - Evolução do caso
    # -------------------------------------------------------------------------

    class EvolucaoCaso(models.TextChoices):
        CURA = '1', 'Cura'
        INCAPACIDADE_TEMPORARIA = '2', 'Incapacidade temporária'
        INCAPACIDADE_PARCIAL_PERMANENTE = '3', 'Incapacidade parcial permanente'
        INCAPACIDADE_TOTAL_PERMANENTE = '4', 'Incapacidade total permanente'
        OBITO_ACIDENTE_TRABALHO = '5', 'Óbito por acidente de trabalho grave'
        OBITO_OUTRAS_CAUSAS = '6', 'Óbito por outras causas'
        OUTRO = '7', 'Outro'
        IGNORADO = '9', 'Ignorado'

    tp_evolucao_caso = models.CharField(
        max_length=1,
        choices=EvolucaoCaso.choices,
        null=True,
        blank=True,
        verbose_name="Evolução do caso",
        help_text="Evolução do paciente após o acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 67 - Se Óbito, Data do Óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito. Deve ser >= data do acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 68 - Foi emitida a Comunicação de Acidente no Trabalho - CAT
    # -------------------------------------------------------------------------

    class ComunicacaoCAT(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        NAO_SE_APLICA = '3', 'Não se aplica'
        IGNORADO = '9', 'Ignorado'

    tp_comunicacao_cat = models.CharField(
        max_length=1,
        choices=ComunicacaoCAT.choices,
        verbose_name="Comunicação de Acidente no Trabalho - CAT",
        help_text="Se foi emitida a Comunicação de Acidente no Trabalho (CAT).",
    )

    # -------------------------------------------------------------------------
    # Informações complementares e observações
    # -------------------------------------------------------------------------

    ds_observacao_acidente = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Observações",
        help_text="Descrição sumária de como ocorreu o acidente/atividades/causas/condições/objeto/agentes.",
    )

    # -------------------------------------------------------------------------
    # Campo de lote - Transferência vertical da investigação
    # -------------------------------------------------------------------------

    nu_lote_vertical = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Lote de transferência vertical",
        help_text="Identificador do lote de transferência vertical da investigação entre níveis do sistema.",
    )

    class Meta:
        db_table = 'acidente_trabalho_grave'
        verbose_name = 'Acidente de Trabalho Grave'
        verbose_name_plural = 'Acidentes de Trabalho Graves'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Acidente Trabalho Grave – {self.co_cbo_ocupacao}"