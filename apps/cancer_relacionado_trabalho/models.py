from django.db import models


class CancerRelacionadoTrabalho(models.Model):
    """
    Ficha de Investigação - DRT_Câncer Relacionado ao Trabalho
    Dicionário de Dados SINAN NET - Versão 5.0
    Campos 31 a 55 + campos de controle
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

    nu_tempo_trabalho = models.CharField(
        max_length=2,
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
    # Campo 34 - Registro/CNPJ/CPF
    # -------------------------------------------------------------------------

    nu_cnpj_cpf = models.CharField(
        max_length=18,
        null=True,
        blank=True,
        verbose_name="CNPJ/CPF do contratante",
        help_text="Número de registro/CNPJ ou CPF do contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Nome da empresa ou empregador
    # -------------------------------------------------------------------------

    no_empresa = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Nome da empresa ou empregador",
        help_text="Nome da empresa ou empregador contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Código da atividade Econômica (CNAE)
    # -------------------------------------------------------------------------

    co_cnae = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="CNAE",
        help_text="Classificação Nacional da Atividade Econômica do Contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - UF
    # -------------------------------------------------------------------------

    co_uf_empresa = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF da empresa",
        help_text="Unidade da Federação da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Município
    # -------------------------------------------------------------------------

    co_municipio_empresa = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município da empresa",
        help_text="Município da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Distrito
    # -------------------------------------------------------------------------

    co_distrito_empresa = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Distrito da empresa",
        help_text="Código do distrito da empresa contratante.",
    )
    no_distrito_empresa = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Nome do distrito da empresa",
        help_text="Nome do distrito da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Bairro
    # -------------------------------------------------------------------------

    co_bairro_empresa = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name="Código do bairro da empresa",
        help_text="Código do bairro da empresa contratante.",
    )
    no_bairro_empresa = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Bairro da empresa",
        help_text="Nome do bairro da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Endereço
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
    # Campo 42 - Número
    # -------------------------------------------------------------------------

    nu_numero_empresa = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Número do endereço da empresa",
        help_text="Número do lote da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Ponto de Referência
    # -------------------------------------------------------------------------

    no_referencia_empresa = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Ponto de referência da empresa",
        help_text="Ponto de referência da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - (DDD) Telefone
    # -------------------------------------------------------------------------

    ds_ddd_empresa = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name="DDD e Telefone da empresa",
        help_text="DDD e telefone da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - O empregador é empresa Terceirizada
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
    # Campo 46 - Tempo de exposição ao agente de risco
    # -------------------------------------------------------------------------

    nu_tempo_exposicao_risco = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Tempo de exposição ao agente de risco",
        help_text="Quantidade de tempo de exposição ao agente de risco.",
    )

    class UnidadeTempoExposicao(models.TextChoices):
        HORA = '1', 'Hora'
        DIA = '2', 'Dia'
        MESES = '3', 'Meses'
        ANOS = '4', 'Anos'

    tp_tempo_exposicao_risco = models.CharField(
        max_length=1,
        choices=UnidadeTempoExposicao.choices,
        null=True,
        blank=True,
        verbose_name="Unidade de tempo de exposição",
        help_text="Unidade de medida do tempo de exposição.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Regime de tratamento
    # -------------------------------------------------------------------------

    class RegimeTratamento(models.TextChoices):
        HOSPITALAR = '1', 'Hospitalar'
        AMBULATORIAL = '2', 'Ambulatorial'

    st_regime_tratamento = models.CharField(
        max_length=1,
        choices=RegimeTratamento.choices,
        null=True,
        blank=True,
        verbose_name="Regime de tratamento",
        help_text="O tratamento ocorreu em regime hospitalar ou ambulatorial.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Diagnóstico específico (CID 10)
    # -------------------------------------------------------------------------

    co_cid_diagnostico = models.CharField(
        max_length=4,
        verbose_name="CID-10 do diagnóstico",
        help_text="Código CID-10 do diagnóstico específico.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Exposição a agentes de risco (16 subcampos)
    # -------------------------------------------------------------------------

    st_exp_asbesto_amianto = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Asbesto ou Amianto",
        help_text="Exposição a asbesto ou amianto durante a vida profissional.",
    )
    st_exp_cadmio = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Cádmio ou seus compostos",
        help_text="Exposição a cádmio ou seus compostos durante a vida profissional.",
    )
    st_exp_silica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Sílica livre, arsênico e seus compostos arsenicais",
        help_text="Exposição a sílica livre, arsênico e seus compostos arsenicais durante a vida profissional.",
    )
    st_exp_cromo = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Cromo ou seus compostos tóxicos",
        help_text="Exposição a cromo ou seus compostos tóxicos durante a vida profissional.",
    )
    st_exp_amina_aromatica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Aminas Aromáticas",
        help_text="Exposição a aminas aromáticas durante a vida profissional.",
    )
    st_exp_composto_niquel = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Composto de Níquel",
        help_text="Exposição a compostos de níquel durante a vida profissional.",
    )
    st_exp_benzeno = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Benzeno ou seus homólogos tóxicos",
        help_text="Exposição a benzeno ou seus homólogos tóxicos durante a vida profissional.",
    )
    st_exp_radiacao_ionizante = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Radiações Ionizantes",
        help_text="Exposição a radiações ionizantes durante a vida profissional.",
    )
    st_exp_alcatrao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Alcatrão, breu, betume, hulha mineral, parafina",
        help_text="Exposição a alcatrão, breu, betume, hulha mineral, parafina e produtos ou resíduos dessas substâncias durante a vida profissional.",
    )
    st_exp_radiacao_nao_ionizante = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Radiações não Ionizantes",
        help_text="Exposição a radiações não ionizantes durante a vida profissional.",
    )
    st_exp_hidrocarboneto = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Hidrocarbonetos alifáticos ou aromáticos",
        help_text="Exposição a hidrocarbonetos alifáticos ou aromáticos (seus derivados halogenados) durante a vida profissional.",
    )
    st_exp_hormonio = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Hormônios",
        help_text="Exposição a hormônios durante a vida profissional.",
    )
    st_exp_oleo_mineral = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Óleos Minerais",
        help_text="Exposição a óleos minerais durante a vida profissional.",
    )
    st_exp_antineoplasico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Antineoplásicos",
        help_text="Exposição a antineoplásicos durante a vida profissional.",
    )
    st_exp_berilio = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Berílio e seus compostos tóxicos",
        help_text="Exposição a berílio e seus compostos tóxicos durante a vida profissional.",
    )
    st_exp_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição - Outros agentes",
        help_text="Exposição a outros agentes de risco durante a vida profissional.",
    )
    ds_exp_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outros agentes (especificar)",
        help_text="Especificação de outros agentes de risco.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Hábito de fumar
    # -------------------------------------------------------------------------

    class HabitoFumar(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        EX_FUMANTE = '3', 'Ex-fumante'
        IGNORADO = '9', 'Ignorado'

    tp_habito_fumar = models.CharField(
        max_length=1,
        choices=HabitoFumar.choices,
        null=True,
        blank=True,
        verbose_name="Hábito de fumar",
        help_text="Hábito de fumar do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Tempo de exposição ao tabaco
    # -------------------------------------------------------------------------

    nu_tempo_exposicao_tabaco = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Tempo de exposição ao tabaco",
        help_text="Quantidade de tempo de exposição ao tabaco.",
    )

    class UnidadeTempoTabaco(models.TextChoices):
        HORA = '1', 'Hora'
        DIA = '2', 'Dia'
        MESES = '3', 'Meses'
        ANOS = '4', 'Anos'

    tp_tempo_exposicao_tabaco = models.CharField(
        max_length=1,
        choices=UnidadeTempoTabaco.choices,
        null=True,
        blank=True,
        verbose_name="Unidade de tempo - Exposição ao tabaco",
        help_text="Unidade de medida do tempo de exposição ao tabaco.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Há ou houve outros trabalhadores com a mesma doença no local de trabalho?
    # -------------------------------------------------------------------------

    st_trabalhador_mesma_doenca = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outros trabalhadores com a mesma doença",
        help_text="Se há ou houve outros trabalhadores com a mesma doença no local de trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Evolução do caso
    # -------------------------------------------------------------------------

    class EvolucaoCaso(models.TextChoices):
        SEM_EVIDENCIA_DOENCA = '1', 'Sem evidência da doença (remissão completa)'
        REMISSAO_PARCIAL = '2', 'Remissão parcial'
        DOENCA_ESTAVEL = '3', 'Doença estável'
        DOENCA_PROGRESSAO = '4', 'Doença em Progressão'
        FORA_POSSIBILIDADE_TERAPEUTICA = '5', 'Fora de possibilidade terapêutica'
        OBITO_CANCER_TRABALHO = '6', 'Óbito por câncer relacionado ao trabalho'
        OBITO_OUTRAS_CAUSAS = '7', 'Óbito por outras causas'
        NAO_SE_APLICA = '8', 'Não se aplica'
        IGNORADO = '9', 'Ignorado'

    tp_evolucao_caso = models.CharField(
        max_length=1,
        choices=EvolucaoCaso.choices,
        null=True,
        blank=True,
        verbose_name="Evolução do caso",
        help_text="Evolução da situação do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Data do óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito. Obrigatório se evolução = 6 ou 7. Deve ser >= data do diagnóstico.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Foi emitida a comunicação de Acidente de Trabalho
    # -------------------------------------------------------------------------

    tp_comunicacao_cat = models.CharField(
        max_length=1,
        choices=SimNaoNaoSeAplicaIgnorado.choices,
        verbose_name="Comunicação de Acidente de Trabalho - CAT",
        help_text="Se foi emitida a comunicação de Acidente de Trabalho (CAT).",
    )

    # -------------------------------------------------------------------------
    # Informações Complementares e observações
    # -------------------------------------------------------------------------

    ds_observacao = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Observações",
        help_text="Informações complementares e observações a respeito do caso quando necessário.",
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
        db_table = 'cancer_relacionado_trabalho'
        verbose_name = 'Câncer Relacionado ao Trabalho'
        verbose_name_plural = 'Câncer Relacionado ao Trabalho'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Câncer Relacionado Trabalho – {self.co_cbo_ocupacao}"