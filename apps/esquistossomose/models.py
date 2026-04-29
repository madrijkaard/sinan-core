from django.db import models


class Esquistossomose(models.Model):
    """
    Ficha de Investigação - Esquistossomose
    Dicionário de Dados SINAN NET - Versão 5.0
    Revisado em março 2012
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

    class PositivoNegativoNaoRealizado(models.TextChoices):
        POSITIVO = '1', 'Positivo'
        NEGATIVO = '2', 'Negativo'
        NAO_REALIZADO = '3', 'Não realizado'

    class Autoctone(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        INDETERMINADO = '3', 'Indeterminado'

    # -------------------------------------------------------------------------
    # Campo 31 - Data da Investigação
    # -------------------------------------------------------------------------

    dt_investigacao = models.DateField(
        verbose_name="Data da investigação",
        help_text="Data em que ocorreu a investigação (1ª visita ao portador). Deve ser >= data da notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 32 - Ocupação / Ramo de atividade
    # -------------------------------------------------------------------------

    co_cbo_ocupacao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Ocupação (CBO)",
        help_text="Código CBO da ocupação exercida pelo paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 33 - Data da Coproscopia
    # -------------------------------------------------------------------------

    dt_coproscopia = models.DateField(
        verbose_name="Data da coproscopia",
        help_text="Data de realização da coproscopia. Deve ser >= data do diagnóstico.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Análise Quantitativa (Kato-Katz)
    # -------------------------------------------------------------------------

    nu_kato_katz = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Número de ovos (Kato-Katz)",
        help_text="Número de ovos encontrados no exame Kato-Katz. 0 (zero) ou 1 (um) ou mais ovos.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Análise Qualitativa (Hoffman)
    # -------------------------------------------------------------------------

    st_hoffman = models.CharField(
        max_length=1,
        choices=PositivoNegativoNaoRealizado.choices,
        null=True,
        blank=True,
        verbose_name="Exame Hoffman",
        help_text="Resultado do exame Hoffman (positivo, negativo ou não realizado).",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Outros exames
    # -------------------------------------------------------------------------

    st_outro = models.CharField(
        max_length=1,
        choices=PositivoNegativoNaoRealizado.choices,
        null=True,
        blank=True,
        verbose_name="Outros exames",
        help_text="Resultado de outros exames (positivo, negativo ou não realizado).",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Outros exames, especificar
    # -------------------------------------------------------------------------

    ds_exame_outro = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Outros exames (especificar)",
        help_text="Nome do outro exame realizado. Habilitado se campo 36 diferente de 3 (não realizado).",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Fez Tratamento?
    # -------------------------------------------------------------------------

    class Tratamento(models.TextChoices):
        SIM_PRAZIQUANTEL = '1', 'Sim, Praziquantel'
        SIM_OXAMINIUINE = '2', 'Sim, Oxaminiuine'
        NAO = '3', 'Não'
        IGNORADO = '9', 'Ignorado'

    tp_tratamento = models.CharField(
        max_length=1,
        choices=Tratamento.choices,
        verbose_name="Fez tratamento",
        help_text="Se o paciente fez tratamento para esquistossomose.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Data do tratamento
    # -------------------------------------------------------------------------

    dt_tratamento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do tratamento",
        help_text="Data do tratamento. Obrigatório se tratamento = 1 ou 2.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Caso não tenha feito tratamento, qual o motivo?
    # -------------------------------------------------------------------------

    class MotivoNaoTratamento(models.TextChoices):
        CONTRA_INDICACAO = '1', 'Contra-indicação'
        RECUSA = '2', 'Recusa'
        AUSENTE = '3', 'Ausente'
        IGNORADO = '9', 'Ignorado'

    tp_nao_tratamento = models.CharField(
        max_length=1,
        choices=MotivoNaoTratamento.choices,
        null=True,
        blank=True,
        verbose_name="Motivo da não realização do tratamento",
        help_text="Motivo quando tratamento = 3 (Não).",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Resultado da análise de verificação de cura (3 amostras)
    # -------------------------------------------------------------------------

    class ResultadoCura(models.TextChoices):
        ZERO = '0', '0 (zero)'
        UM_OU_MAIS = '1', '1 ou mais'
        NAO_REALIZADO = '2', 'Não realizado'

    st_cura_afirmativo_1 = models.CharField(
        max_length=1,
        choices=ResultadoCura.choices,
        null=True,
        blank=True,
        verbose_name="Verificação de cura - 1ª amostra",
        help_text="Resultado da 1ª amostra para verificação de cura.",
    )
    st_cura_afirmativo_2 = models.CharField(
        max_length=1,
        choices=ResultadoCura.choices,
        null=True,
        blank=True,
        verbose_name="Verificação de cura - 2ª amostra",
        help_text="Resultado da 2ª amostra para verificação de cura.",
    )
    st_cura_afirmativo_3 = models.CharField(
        max_length=1,
        choices=ResultadoCura.choices,
        null=True,
        blank=True,
        verbose_name="Verificação de cura - 3ª amostra",
        help_text="Resultado da 3ª amostra para verificação de cura.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Data do resultado da 3ª amostra
    # -------------------------------------------------------------------------

    dt_resultado_amostra3 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do resultado da 3ª amostra",
        help_text="Data do resultado da 3ª amostra. Obrigatório se resultado = 0 ou 1.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Especificar forma clínica
    # -------------------------------------------------------------------------

    class FormaClinica(models.TextChoices):
        INTESTINAL = '1', 'Intestinal'
        HEPATO_INTESTINAL = '2', 'Hepato intestinal'
        HEPATO_ESPLENICA = '3', 'Hepato esplênica'
        AGUDA = '4', 'Aguda'
        OUTRA = '5', 'Outra'

    tp_anatomo_clinica = models.CharField(
        max_length=1,
        choices=FormaClinica.choices,
        null=True,
        blank=True,
        verbose_name="Forma clínica",
        help_text="Classificação da forma anátomo-clínica da esquistossomose.",
    )
    ds_anatomo_clinica_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outra forma clínica (especificar)",
        help_text="Especificação quando forma clínica = 5 (Outra).",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - O caso é autóctone do município de residência?
    # -------------------------------------------------------------------------

    tp_autoctone_residencia = models.CharField(
        max_length=1,
        choices=Autoctone.choices,
        verbose_name="Caso autóctone do município de residência",
        help_text="Indica se o caso é autóctone do município de residência.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - UF (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_uf_infeccao = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF provável da infecção",
        help_text="Unidade Federada provável da fonte de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - País (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_pais_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="País provável da infecção",
        help_text="País provável da fonte de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Município (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_municipio_infeccao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município provável da infecção",
        help_text="Município provável da fonte de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Distrito (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_distrito_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Distrito provável da infecção",
        help_text="Distrito provável da fonte de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Bairro (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_bairro_infeccao = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name="Código do bairro provável da infecção",
        help_text="Código do bairro provável da fonte de infecção.",
    )
    no_bairro_infeccao = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Bairro provável da infecção",
        help_text="Nome do bairro provável da fonte de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Nome da propriedade (se área rural)
    # -------------------------------------------------------------------------

    no_propriedade_infeccao = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Nome da propriedade (área rural)",
        help_text="Nome da propriedade onde ocorreu a transmissão, se área rural.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Nome da coleção hídrica
    # -------------------------------------------------------------------------

    no_colecao_infeccao = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Nome da coleção hídrica",
        help_text="Nome da coleção hídrica onde ocorreu a transmissão.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Doença relacionada ao trabalho
    # -------------------------------------------------------------------------

    st_doenca_trabalho = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Doença relacionada ao trabalho",
        help_text="Se o caso está relacionado ao trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Evolução do caso
    # -------------------------------------------------------------------------

    class EvolucaoCaso(models.TextChoices):
        CURA = '1', 'Cura'
        NAO_CURA = '2', 'Não Cura'
        OBITO_ESQUISTOSSOMOSE = '3', 'Óbito por esquistossomose'
        OBITO_OUTRAS_CAUSAS = '4', 'Óbito por outras causas'
        IGNORADO = '9', 'Ignorado'

    tp_evolucao_caso = models.CharField(
        max_length=1,
        choices=EvolucaoCaso.choices,
        null=True,
        blank=True,
        verbose_name="Evolução do caso",
        help_text="Evolução do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Data do óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito. Obrigatório se evolução = 3 ou 4. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Data do encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento",
        help_text="Data do encerramento do caso. Deve ser >= data da investigação.",
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
        db_table = 'esquistossomose'
        verbose_name = 'Esquistossomose'
        verbose_name_plural = 'Esquistossomose'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Esquistossomose – {self.dt_investigacao}"