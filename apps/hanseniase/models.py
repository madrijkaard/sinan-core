from django.db import models


class Hanseniase(models.Model):
    """
    Ficha de Investigação - Hanseníase (com campos de acompanhamento)
    Dicionário de Dados SINAN NET - Versão 5.0
    Campos 31 a 43 (investigação) + campos de acompanhamento (1 a 20)
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

    # -------------------------------------------------------------------------
    # Campo 31 - Nº de Prontuário
    # -------------------------------------------------------------------------

    ds_prontuario = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Nº de prontuário",
        help_text="Número/caractere atribuído pela unidade de saúde - identificador do prontuário.",
    )

    # -------------------------------------------------------------------------
    # Campo 32 - Ocupação
    # -------------------------------------------------------------------------

    co_cbo_ocupacao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Ocupação (CBO)",
        help_text="Código CBO da ocupação exercida pelo paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 33 - Nº de lesões cutâneas
    # -------------------------------------------------------------------------

    nu_lesao_cultanea = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Nº de lesões cutâneas",
        help_text="Número de lesões dermatológicas apresentadas pelo paciente por ocasião do diagnóstico.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Forma Clínica
    # -------------------------------------------------------------------------

    class FormaClinica(models.TextChoices):
        INDETERMINADA = '1', 'I - Indeterminada'
        TUBERCULOIDE = '2', 'T - Tuberculóide'
        DIMORFA = '3', 'D - Dimorfa'
        VIRCHOWIANA = '4', 'V - Virchowiana'
        NAO_CLASSIFICADO = '5', 'Não classificado'

    tp_forma_clinica = models.CharField(
        max_length=1,
        choices=FormaClinica.choices,
        null=True,
        blank=True,
        verbose_name="Forma clínica",
        help_text="Forma clínica inicial por ocasião do diagnóstico, segundo classificação de Madrid.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Classificação Operacional
    # -------------------------------------------------------------------------

    class ClassificacaoOperacional(models.TextChoices):
        PB = '1', 'PB - Paucibacilar'
        MB = '2', 'MB - Multibacilar'

    tp_classific_operacional = models.CharField(
        max_length=1,
        choices=ClassificacaoOperacional.choices,
        verbose_name="Classificação operacional",
        help_text="Classificação operacional, por ocasião do diagnóstico, para eleição do esquema terapêutico.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Nº de nervos afetados
    # -------------------------------------------------------------------------

    nu_nervo_afetado = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Nº de nervos afetados",
        help_text="Número de nervos afetados.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Avaliação do Grau de Incapacidade Física no Diagnóstico
    # -------------------------------------------------------------------------

    class GrauIncapacidade(models.TextChoices):
        GRAU_ZERO = '0', 'Grau zero'
        GRAU_I = '1', 'Grau I'
        GRAU_II = '2', 'Grau II'
        NAO_AVALIADO = '3', 'Não avaliado'

    tp_incapacidade_fisica = models.CharField(
        max_length=1,
        choices=GrauIncapacidade.choices,
        null=True,
        blank=True,
        verbose_name="Grau de incapacidade física no diagnóstico",
        help_text="Avaliação do grau de incapacidade física por ocasião do diagnóstico.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Modo de entrada
    # -------------------------------------------------------------------------

    class ModoEntrada(models.TextChoices):
        CASO_NOVO = '1', 'Caso novo'
        TRANSFERENCIA_MESMO_MUNICIPIO = '2', 'Transferência do mesmo município (outra unidade)'
        TRANSFERENCIA_OUTRO_MUNICIPIO = '3', 'Transferência de outro município (mesma UF)'
        TRANSFERENCIA_OUTRO_ESTADO = '4', 'Transferência de outro estado'
        TRANSFERENCIA_OUTRO_PAIS = '5', 'Transferência de outro país'
        RECIDIVA = '6', 'Recidiva'
        OUTROS_REINGRESSOS = '7', 'Outros reingressos'
        IGNORADO = '9', 'Ignorado'

    tp_modo_entrada = models.CharField(
        max_length=1,
        choices=ModoEntrada.choices,
        verbose_name="Modo de entrada",
        help_text="Modo de entrada do paciente no sistema.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Modo de detecção de caso novo
    # -------------------------------------------------------------------------

    class ModoDeteccao(models.TextChoices):
        ENCAMINHAMENTO = '1', 'Encaminhamento'
        DEMANDA_ESPONTANEA = '2', 'Demanda espontânea'
        EXAME_COLETIVIDADE = '3', 'Exame de coletividade'
        EXAME_CONTATOS = '4', 'Exame de contatos'
        OUTROS_MODOS = '5', 'Outros modos'
        IGNORADO = '9', 'Ignorado'

    tp_caso_novo = models.CharField(
        max_length=1,
        choices=ModoDeteccao.choices,
        null=True,
        blank=True,
        verbose_name="Modo de detecção de caso novo",
        help_text="Modo de detecção do caso novo. Habilitado quando modo de entrada = 1.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Baciloscopia
    # -------------------------------------------------------------------------

    class Baciloscopia(models.TextChoices):
        POSITIVA = '1', 'Positiva'
        NEGATIVA = '2', 'Negativa'
        NAO_REALIZADA = '3', 'Não realizada'
        IGNORADO = '9', 'Ignorado'

    tp_baciloscopia = models.CharField(
        max_length=1,
        choices=Baciloscopia.choices,
        null=True,
        blank=True,
        verbose_name="Baciloscopia",
        help_text="Resultado da baciloscopia.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Data do início do tratamento
    # -------------------------------------------------------------------------

    dt_ini_tratamento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do início do tratamento",
        help_text="Data do início do tratamento. Deve ser >= data do diagnóstico.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Esquema terapêutico inicial
    # -------------------------------------------------------------------------

    class EsquemaTerapeutico(models.TextChoices):
        PQT_PB_6_DOSES = '1', 'PQT/PB/6 doses'
        PQT_MB_12_DOSES = '2', 'PQT/MB/12 doses'
        OUTROS_ESQUEMAS = '3', 'Outros Esquemas Substitutos'

    tp_esquema_terapeutico = models.CharField(
        max_length=1,
        choices=EsquemaTerapeutico.choices,
        null=True,
        blank=True,
        verbose_name="Esquema terapêutico inicial",
        help_text="Esquema terapêutico inicial.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Nº de contatos registrados
    # -------------------------------------------------------------------------

    nu_contato_registrado = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Nº de contatos registrados",
        help_text="Número de pessoas que residam ou tenham residido, nos últimos 5 anos com o doente, a contar da data do diagnóstico.",
    )

    # -------------------------------------------------------------------------
    # Campo interno - Identifica migração
    # -------------------------------------------------------------------------

    st_importado = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        editable=False,
        verbose_name="Registro migrado",
        help_text="Identifica se o registro é oriundo da rotina de migração da base Windows.",
    )

    # =========================================================================
    # TELA DE ACOMPANHAMENTO (Campos 1 a 20)
    # =========================================================================

    # -------------------------------------------------------------------------
    # Campo 1 - UF de atendimento atual
    # -------------------------------------------------------------------------

    co_uf_atual = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de atendimento atual",
        help_text="Sigla da UF onde está localizada a unidade de saúde responsável pelo tratamento atual do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 2 - Município de atendimento atual
    # -------------------------------------------------------------------------

    co_municipio_atual = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município de atendimento atual",
        help_text="Código do município onde está localizada a unidade de saúde responsável pelo tratamento atual.",
    )

    # -------------------------------------------------------------------------
    # Campo 3 - Número de notificação atual
    # -------------------------------------------------------------------------

    nu_notificacao_atual = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Número de notificação atual",
        help_text="Número da ficha de notificação/investigação enviada pela unidade de saúde atualmente responsável pelo paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 4 - Data de notificação atual
    # -------------------------------------------------------------------------

    dt_notificacao_atual = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de notificação atual",
        help_text="Data de notificação do caso pela unidade de saúde responsável pelo tratamento atual do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 5 - Unidade de atendimento atual
    # -------------------------------------------------------------------------

    co_unidade_atual = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Unidade de atendimento atual (CNES)",
        help_text="Código CNES da unidade de saúde responsável pelo tratamento atual do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 6 - UF de residência atual
    # -------------------------------------------------------------------------

    co_uf_residencia_atual = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de residência atual",
        help_text="Sigla da UF de residência atual do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 7 - Município de residência atual
    # -------------------------------------------------------------------------

    co_municipio_residencia_atual = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município de residência atual",
        help_text="Código IBGE do município de residência atual do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 8 - CEP
    # -------------------------------------------------------------------------

    nu_cep_residencia_atual = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name="CEP",
        help_text="Código postal da residência atual do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 10 - Bairro de residência atual
    # -------------------------------------------------------------------------

    co_bairro_residencia_atual = models.DecimalField(
        max_digits=8,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Código do bairro de residência atual",
        help_text="Código do bairro de residência atual do paciente.",
    )
    no_bairro_residencia_atual = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Bairro de residência atual",
        help_text="Nome do bairro de residência atual do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 11 - Data do último comparecimento
    # -------------------------------------------------------------------------

    dt_ultimo_comparecimento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do último comparecimento",
        help_text="Data do último comparecimento do paciente na unidade de saúde ou atendimento por agente de saúde. Deve ser >= data do início do tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 12 - Classificação operacional atual
    # -------------------------------------------------------------------------

    tp_classific_operacao_atual = models.CharField(
        max_length=1,
        choices=ClassificacaoOperacional.choices,
        null=True,
        blank=True,
        verbose_name="Classificação operacional atual",
        help_text="Classificação operacional do caso para eleição do esquema terapêutico adequado.",
    )

    # -------------------------------------------------------------------------
    # Campo 13 - Avaliação de incapacidade física no momento da cura
    # -------------------------------------------------------------------------

    tp_incapacidade_fisica_cura = models.CharField(
        max_length=1,
        choices=GrauIncapacidade.choices,
        null=True,
        blank=True,
        verbose_name="Avaliação de incapacidade física na cura",
        help_text="Avaliação do grau de incapacidade física no momento da cura.",
    )

    # -------------------------------------------------------------------------
    # Campo 14 - Esquema terapêutico atual
    # -------------------------------------------------------------------------

    tp_esquema_terapeutico_atual = models.CharField(
        max_length=1,
        choices=EsquemaTerapeutico.choices,
        null=True,
        blank=True,
        verbose_name="Esquema terapêutico atual",
        help_text="Esquema terapêutico em uso.",
    )

    # -------------------------------------------------------------------------
    # Campo 15 - Número de doses supervisionadas
    # -------------------------------------------------------------------------

    nu_dose_recebida = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Número de doses supervisionadas",
        help_text="Número de doses supervisionadas recebidas sob supervisão.",
    )

    # -------------------------------------------------------------------------
    # Campo 16 - Episódio Reacional Durante o Tratamento
    # -------------------------------------------------------------------------

    class EpisodioReacional(models.TextChoices):
        TIPO_1 = '1', 'Reação tipo 1'
        TIPO_2 = '2', 'Reação tipo 2'
        TIPO_1_E_2 = '3', 'Reação tipo 1 e 2'

    tp_reacao_tratamento = models.CharField(
        max_length=1,
        choices=EpisodioReacional.choices,
        null=True,
        blank=True,
        verbose_name="Episódio reacional durante o tratamento",
        help_text="Tipo de reação apresentada pelo paciente durante tratamento da hanseníase.",
    )

    # -------------------------------------------------------------------------
    # Campo 17 - Data de mudança do Esquema
    # -------------------------------------------------------------------------

    dt_mudanca_esquema = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de mudança do esquema",
        help_text="Data de mudança de esquema terapêutico (se pertinente).",
    )

    # -------------------------------------------------------------------------
    # Campo 18 - Número de contatos examinados
    # -------------------------------------------------------------------------

    nu_contato_examinado = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Número de contatos examinados",
        help_text="Número de contatos intradomiciliares submetidos a exame dermatoneurológico. Deve ser <= número de contatos registrados.",
    )

    # -------------------------------------------------------------------------
    # Campo 19 - Tipo de Saída
    # -------------------------------------------------------------------------

    class TipoSaida(models.TextChoices):
        CURA = '1', 'Cura'
        TRANSFERENCIA_MESMO_MUNICIPIO = '2', 'Transferência p/ mesmo município'
        TRANSFERENCIA_OUTRO_MUNICIPIO = '3', 'Transferência p/ outro município'
        TRANSFERENCIA_OUTRO_ESTADO = '4', 'Transferência p/ outro Estado'
        TRANSFERENCIA_OUTRO_PAIS = '5', 'Transferência p/ outro país'
        OBITO = '6', 'Óbito'
        ABANDONO = '7', 'Abandono'
        ERRO_DIAGNOSTICO = '8', 'Erro diagnóstico'
        TRANSFERENCIA_NAO_ESPECIFICADA = '9', 'Transferência não especificada'

    tp_alta = models.CharField(
        max_length=1,
        choices=TipoSaida.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de saída",
        help_text="Tipo de saída/alta do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 20 - Data da alta
    # -------------------------------------------------------------------------

    dt_alta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da alta",
        help_text="Data da alta. Deve ser >= data de início de tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo interno - Vinculação
    # -------------------------------------------------------------------------

    class Vinculacao(models.TextChoices):
        NAO_VINCULADA = '0', 'Não Vinculada'
        VINCULADA = '1', 'Vinculada'

    st_vincula = models.CharField(
        max_length=1,
        choices=Vinculacao.choices,
        null=True,
        blank=True,
        editable=False,
        verbose_name="Vinculação",
        help_text="Indica se a notificação foi vinculada.",
    )

    # -------------------------------------------------------------------------
    # Campo de lote - Transferência vertical da investigação
    # -------------------------------------------------------------------------

    nu_lote_vertical = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Lote de transferência vertical",
        help_text="Identificador do lote de transferência vertical da investigação e acompanhamento entre níveis do sistema.",
    )

    class Meta:
        db_table = 'hanseniase'
        verbose_name = 'Hanseníase'
        verbose_name_plural = 'Hanseníase'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Hanseníase – {self.ds_prontuario}"