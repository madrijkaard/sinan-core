from django.db import models


class Pair(models.Model):
    """
    Ficha de Investigação - DRT_PAIR (Perda Auditiva Induzida por Ruído)
    Dicionário de Dados SINAN NET - Versão 5.0
    Campos 31 a 60 + campos de controle
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

    class SimNao(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'

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
        help_text="Unidade de Federação da empresa contratante.",
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
        max_length=4,
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
        verbose_name="Número da empresa",
        help_text="Número da empresa contratante.",
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
        max_length=3,
        null=True,
        blank=True,
        verbose_name="DDD da empresa",
        help_text="DDD do telefone da empresa contratante.",
    )
    ds_telefone_empresa = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name="Telefone da empresa",
        help_text="Telefone da empresa contratante.",
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
    # Campo 46 - Agravos associados (8 subcampos)
    # -------------------------------------------------------------------------

    st_doenca_hipertensao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Hipertensão arterial",
        help_text="Condição associada ao agravo - Hipertensão Arterial.",
    )
    st_doenca_tuberculose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Tuberculose",
        help_text="Condição associada ao agravo - Tuberculose.",
    )
    st_doenca_diabetes = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Diabetes Mellitus",
        help_text="Condição associada ao agravo - Diabetes Mellitus.",
    )
    st_doenca_asma = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Asma",
        help_text="Condição associada ao agravo - Asma.",
    )
    st_doenca_hanseniase = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Hanseníase",
        help_text="Condição associada ao agravo - Hanseníase.",
    )
    st_doenca_transtorno_mental = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Transtorno mental",
        help_text="Condição associada ao agravo - Transtorno Mental.",
    )
    st_doenca_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outra doença associada",
        help_text="Condição associada ao agravo - outra doença.",
    )
    ds_doenca_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outra doença associada (especificar)",
        help_text="Especificação quando outra doença associada = Sim.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Tempo de exposição ao agente de risco
    # -------------------------------------------------------------------------

    nu_tempo_exposicao_risco = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Tempo de exposição ao agente de risco",
        help_text="Quantidade de tempo de exposição ao agente de risco.",
    )

    class UnidadeTempoExposicao(models.TextChoices):
        HORA = 'H', 'Hora'
        DIAS = 'D', 'Dias'
        MESES = 'M', 'Meses'
        ANOS = 'A', 'Anos'

    tp_tempo_exposicao_risco = models.CharField(
        max_length=1,
        choices=UnidadeTempoExposicao.choices,
        null=True,
        blank=True,
        verbose_name="Unidade de tempo de exposição",
        help_text="Unidade de medida do tempo de exposição.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Regime de tratamento
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
        help_text="Regime de tratamento (hospitalar ou ambulatorial).",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Tipo de Ruído Predominante
    # -------------------------------------------------------------------------

    class TipoRuido(models.TextChoices):
        CONTINUO = '1', 'Ruído Contínuo'
        INTERMITENTE = '2', 'Ruído Intermitente'
        AMBOS = '3', 'Ambos'
        IGNORADO = '9', 'Ignorado'

    tp_ruido = models.CharField(
        max_length=1,
        choices=TipoRuido.choices,
        verbose_name="Tipo de ruído predominante",
        help_text="Ruído predominante que causou a perda auditiva.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Exposição Concomitante a Ruído e Solvente a Base de Tolueno
    # -------------------------------------------------------------------------

    st_exposicao_solvente = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição concomitante a ruído e solvente",
        help_text="Houve exposição concomitante a ruído e Solvente a Base de Tolueno.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Exposição Concomitante a Ruído e Metais Pesados
    # -------------------------------------------------------------------------

    st_exposicao_metal = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição concomitante a ruído e metais pesados",
        help_text="Houve exposição concomitante a ruído e Metais Pesados.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Exposição Concomitante a Ruído e Medicamentos Ototóxicos
    # -------------------------------------------------------------------------

    st_exposicao_medicamento = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição concomitante a ruído e medicamentos ototóxicos",
        help_text="Houve exposição concomitante a ruído e Medicamentos Ototóxicos.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Exposição Concomitante a Ruído e Gases Tóxicos
    # -------------------------------------------------------------------------

    st_exposicao_gas = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição concomitante a ruído e gases tóxicos",
        help_text="Houve exposição concomitante a ruído e gases tóxicos.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Exposição Concomitante a Ruído e Outros
    # -------------------------------------------------------------------------

    st_exposicao_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição concomitante a ruído e outros agentes",
        help_text="Houve exposição concomitante a ruído e outros produto/outra situação.",
    )
    ds_exposicao_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outros agentes (especificar)",
        help_text="Especificação quando exposição a outros agentes = Sim.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Sintomas (5 subcampos)
    # -------------------------------------------------------------------------

    st_sintoma_zumbido = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Zumbido",
        help_text="Sintoma - Zumbido.",
    )
    st_sintoma_tontura = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Tontura",
        help_text="Sintoma - Tontura.",
    )
    st_sintoma_dificuldade_fala = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Dificuldade para compreensão da fala",
        help_text="Sintoma - Dificuldade para compreensão da fala.",
    )
    st_sintoma_cefaleia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Cefaléia",
        help_text="Sintoma - Cefaléia.",
    )
    st_sintoma_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outros sintomas",
        help_text="Outros sintomas presentes.",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - Diagnóstico Específico CID 10
    # -------------------------------------------------------------------------

    co_cid_diagnostico = models.CharField(
        max_length=4,
        verbose_name="CID-10 do diagnóstico",
        help_text="Diagnóstico específico - CID 10.",
    )

    # -------------------------------------------------------------------------
    # Campo 57 - Houve afastamento do trabalho para tratamento?
    # -------------------------------------------------------------------------

    st_afastamento_trabalho = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Houve afastamento do trabalho para tratamento",
        help_text="Se houve afastamento do trabalho para tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 58 - Tempo de afastamento do trabalho para tratamento
    # -------------------------------------------------------------------------

    nu_tempo_afastamento_trabalho = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Tempo de afastamento do trabalho",
        help_text="Quantidade de tempo de afastamento do trabalho para tratamento.",
    )

    class UnidadeTempoAfastamento(models.TextChoices):
        HORA = '1', 'Hora'
        DIAS = '2', 'Dias'
        MESES = '3', 'Meses'
        ANOS = '4', 'Anos'

    tp_tempo_afastamento_trabalho = models.CharField(
        max_length=1,
        choices=UnidadeTempoAfastamento.choices,
        null=True,
        blank=True,
        verbose_name="Unidade de tempo de afastamento",
        help_text="Unidade de medida do tempo de afastamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 59 - Com afastamento do trabalho
    # -------------------------------------------------------------------------

    class EvolucaoAfastamento(models.TextChoices):
        MELHORA = '1', 'Melhora'
        PIORA = '2', 'Piora'
        IGNORADO = '9', 'Ignorado'

    tp_afastamento_trabalho = models.CharField(
        max_length=1,
        choices=EvolucaoAfastamento.choices,
        null=True,
        blank=True,
        verbose_name="Evolução com afastamento",
        help_text="Evolução da situação de saúde do paciente com afastamento do trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 60 - Há ou houve outros trabalhadores com a mesma doença no local de trabalho
    # -------------------------------------------------------------------------

    st_trabalhador_mesma_doenca = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outros trabalhadores com a mesma doença",
        help_text="Se outros trabalhadores sofreram ou não o mesmo agravo no local de trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 61 - Conduta geral (8 subcampos)
    # Nota: No dicionário é campo 57, mas aqui uso 61 para consistência
    # -------------------------------------------------------------------------

    st_conduta_afastamento_risco = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - Afastamento do agente de risco com mudança de função",
        help_text="Afastamento do agente de risco com mudança de função e/ou posto de trabalho.",
    )
    st_conduta_protecao_individual = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - Proteção individual",
        help_text="Adoção de proteção individual.",
    )
    st_conduta_mudanca_trabalho = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - Mudança na organização do trabalho",
        help_text="Adoção de mudança na organização do trabalho.",
    )
    st_conduta_nenhum = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - Nenhuma",
        help_text="Nenhuma atitude tomada em relação ao agravo.",
    )
    st_conduta_protecao_coletiva = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - Proteção coletiva",
        help_text="Adoção de proteção coletiva.",
    )
    st_conduta_afasta_trabalho = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - Afastamento do local de trabalho",
        help_text="Afastamento do local de trabalho.",
    )
    st_conduta_outro = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - Outros",
        help_text="Outras atitudes tomadas em relação ao agravo.",
    )
    ds_conduta_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outras condutas (especificar)",
        help_text="Especificação quando conduta outro = 1 (Sim).",
    )

    # -------------------------------------------------------------------------
    # Campo 62 - Evolução do caso
    # -------------------------------------------------------------------------

    class EvolucaoCaso(models.TextChoices):
        CURA = '1', 'Cura'
        CURA_NAO_CONFIRMADA = '2', 'Cura não confirmada'
        INCAPACIDADE_TEMPORARIA = '3', 'Incapacidade temporária'
        INCAPACIDADE_PERMANENTE_PARCIAL = '4', 'Incapacidade permanente parcial'
        INCAPACIDADE_PERMANENTE_TOTAL = '5', 'Incapacidade permanente total'
        OBITO_DOENCA_TRABALHO = '6', 'Óbito por doença relacionada ao trabalho'
        OBITO_OUTRA_CAUSA = '7', 'Óbito por outra causa'
        OUTRO = '8', 'Outro'
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
    # Campo 63 - Data do óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito. Obrigatório se evolução = 6 ou 7. Deve ser >= data do diagnóstico.",
    )

    # -------------------------------------------------------------------------
    # Campo 64 - Foi emitida a comunicação de acidente do trabalho
    # -------------------------------------------------------------------------

    tp_comunicacao_cat = models.CharField(
        max_length=1,
        choices=SimNaoNaoSeAplicaIgnorado.choices,
        verbose_name="Comunicação de Acidente de Trabalho - CAT",
        help_text="Se foi emitida a comunicação de acidente do trabalho (CAT).",
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
        db_table = 'pair'
        verbose_name = 'PAIR - Perda Auditiva Induzida por Ruído'
        verbose_name_plural = 'PAIR - Perda Auditiva Induzida por Ruído'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] PAIR – {self.co_cbo_ocupacao}"