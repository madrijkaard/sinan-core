from django.db import models


class GestanteHiv(models.Model):
    """
    Ficha de Investigação - Gestante HIV
    Dicionário de Dados SINAN NET - Versão 5.0
    Campos 31 a 47 + campos de controle
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
    # Campo 31 - Ocupação
    # -------------------------------------------------------------------------

    co_cbo_ocupacao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Ocupação (CBO)",
        help_text="Código CBO da ocupação exercida pela gestante.",
    )

    # -------------------------------------------------------------------------
    # Campo 32 - Evidência laboratorial do HIV
    # -------------------------------------------------------------------------

    class EvidenciaLaboratorial(models.TextChoices):
        ANTES_PRENATAL = '1', 'Antes do pré-natal'
        DURANTE_PRENATAL = '2', 'Durante o pré-natal'
        DURANTE_PARTO = '3', 'Durante o parto'
        APOS_PARTO = '4', 'Após o parto'

    tp_evidencia_laboratorial = models.CharField(
        max_length=1,
        choices=EvidenciaLaboratorial.choices,
        verbose_name="Evidência laboratorial do HIV",
        help_text="Momento em que foi realizada a coleta do material no qual se evidenciou o diagnóstico laboratorial da infecção pelo HIV na gestante/parturiente.",
    )

    # -------------------------------------------------------------------------
    # Campo 33 - Fez/Faz pré-natal
    # -------------------------------------------------------------------------

    st_fez_prenatal = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Fez/faz pré-natal",
        help_text="Registra se a gestante HIV+ ou com diagnóstico confirmado de aids fez ou faz pré-natal.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - UF de realização do Pré-Natal
    # -------------------------------------------------------------------------

    co_uf_prenatal = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de realização do pré-natal",
        help_text="Sigla da UF de localização da Unidade de Saúde de realização do pré-natal.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Município de realização do Pré-Natal
    # -------------------------------------------------------------------------

    co_municipio_prenatal = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município de realização do pré-natal",
        help_text="Código do município de localização da Unidade de Saúde de realização do pré-natal.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Unidade de realização do pré-natal
    # -------------------------------------------------------------------------

    co_unidade_prenatal = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Unidade de realização do pré-natal",
        help_text="Código CNES da unidade de saúde de realização do pré-natal.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Nº da Gestante no SISPRENATAL
    # -------------------------------------------------------------------------

    nu_sisprenatal = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Nº da gestante no SISPRENATAL",
        help_text="Número identificador da gestante no cadastro do SISPRENATAL.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Uso de Anti-retrovirais para profilaxia
    # -------------------------------------------------------------------------

    st_anti_retroviral = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Uso de anti-retrovirais para profilaxia",
        help_text="Gestante HIV+ em terapia com anti-retrovirais para profilaxia.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Data do início do uso de anti-retroviral para profilaxia
    # -------------------------------------------------------------------------

    dt_ini_anti_retroviral = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do início do uso de anti-retroviral",
        help_text="Data de início de uso de anti-retroviral para profilaxia.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - UF do local do parto
    # -------------------------------------------------------------------------

    co_uf_parto = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF do local do parto",
        help_text="UF de localização da ocorrência do parto.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Município do local do parto
    # -------------------------------------------------------------------------

    co_municipio_parto = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município do local do parto",
        help_text="Código do município de localização da ocorrência do parto.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Local de realização do parto
    # -------------------------------------------------------------------------

    co_unidade_parto = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Local de realização do parto",
        help_text="Código CNES da unidade de saúde onde ocorreu o parto.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Data do parto
    # -------------------------------------------------------------------------

    dt_parto = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do parto",
        help_text="Data em que ocorreu o parto.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Tipo do parto
    # -------------------------------------------------------------------------

    class TipoParto(models.TextChoices):
        VAGINAL = '1', 'Vaginal'
        CESAREA_ELETIVA = '2', 'Cesárea eletiva'
        CESAREA_URGENCIA = '3', 'Cesárea de urgência'
        NAO_SE_APLICA = '4', 'Não se aplica'

    tp_parto = models.CharField(
        max_length=1,
        choices=TipoParto.choices,
        null=True,
        blank=True,
        verbose_name="Tipo do parto",
        help_text="Tipo de parto realizado.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Fez uso de profilaxia anti-retroviral durante o parto
    # -------------------------------------------------------------------------

    st_uso_anti_retroviral_parto = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Uso de profilaxia anti-retroviral durante o parto",
        help_text="Anti-retrovirais administrados durante o parto.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Evolução da gravidez
    # -------------------------------------------------------------------------

    class EvolucaoGravidez(models.TextChoices):
        NASCIDO_VIVO = '1', 'Nascido vivo'
        NATIMORTO = '2', 'Natimorto'
        ABORTO = '3', 'Aborto'
        NAO_SE_APLICA = '4', 'Não se aplica'

    tp_evolucao_gravidez = models.CharField(
        max_length=1,
        choices=EvolucaoGravidez.choices,
        null=True,
        blank=True,
        verbose_name="Evolução da gravidez",
        help_text="Evolução da gravidez.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Início da profilaxia com anti-retroviral na criança (horas)
    # -------------------------------------------------------------------------

    class InicioProfilaxiaCrianca(models.TextChoices):
        PRIMEIRAS_24H = '1', 'Nas primeiras 24h'
        APOS_24H = '2', 'Após 24h do nascimento'
        NAO_SE_APLICA = '3', 'Não se aplica'
        NAO_REALIZADO = '4', 'Não realizado'
        IGNORADO = '9', 'Ignorado'

    tp_profilaxia_anti_retroviral = models.CharField(
        max_length=1,
        choices=InicioProfilaxiaCrianca.choices,
        null=True,
        blank=True,
        verbose_name="Início da profilaxia com anti-retroviral na criança",
        help_text="Início da administração do anti-retroviral, em número de horas, a partir do nascimento.",
    )

    # -------------------------------------------------------------------------
    # Informações complementares e observações
    # -------------------------------------------------------------------------

    ds_observacao = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Observações",
        help_text="Informações complementares e observações a respeito do caso.",
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
        db_table = 'gestante_hiv'
        verbose_name = 'Gestante HIV'
        verbose_name_plural = 'Gestantes HIV'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Gestante HIV – {self.tp_evidencia_laboratorial}"