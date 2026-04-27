from django.db import models


class AnimaisPeconhentos(models.Model):
    """
    Ficha de Investigação - Acidente por Animais Peçonhentos
    Dicionário de Dados SINAN NET - Versão 5.0
    Campos 31 a 59 + campos de controle
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
    # Campo 31 - Data da investigação
    # -------------------------------------------------------------------------

    dt_investigacao = models.DateField(
        verbose_name="Data da investigação",
        help_text="Data da investigação do caso. Deve ser >= data da notificação.",
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
    # Campo 33 - Data do acidente
    # -------------------------------------------------------------------------

    dt_acidente = models.DateField(
        verbose_name="Data do acidente",
        help_text=(
            "Data do acidente. Deve ser anterior ou igual à data de diagnóstico "
            "e de notificação, e no máximo 2 anos antes dessas datas."
        ),
    )

    # -------------------------------------------------------------------------
    # Campo 34 - UF de ocorrência
    # -------------------------------------------------------------------------

    co_uf_ocorrencia = models.CharField(
        max_length=2,
        verbose_name="UF de ocorrência",
        help_text="Unidade Federativa onde ocorreu o acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Município de ocorrência
    # -------------------------------------------------------------------------

    co_municipio_ocorrencia = models.CharField(
        max_length=6,
        verbose_name="Município de ocorrência",
        help_text="Código do município onde ocorreu o acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Localidade da ocorrência
    # -------------------------------------------------------------------------

    ds_localidade_ocorrencia = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Localidade da ocorrência",
        help_text="Descrição da localidade onde ocorreu o acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Zona de ocorrência
    # -------------------------------------------------------------------------

    class ZonaOcorrencia(models.TextChoices):
        URBANA     = '1', 'Urbana'
        RURAL      = '2', 'Rural'
        PERIURBANA = '3', 'Periurbana'
        IGNORADO   = '9', 'Ignorado'

    tp_zona_ocorrencia = models.CharField(
        max_length=1,
        choices=ZonaOcorrencia.choices,
        null=True,
        blank=True,
        verbose_name="Zona de ocorrência",
        help_text="Zona onde ocorreu o acidente (urbana, rural, periurbana ou ignorado).",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Tempo decorrido picada/atendimento
    # -------------------------------------------------------------------------

    class TempoDecorrido(models.TextChoices):
        ATE_1H    = '1', '0 - 1h'
        DE_1_3H   = '2', '1 - 3h'
        DE_3_6H   = '3', '3 - 6h'
        DE_6_12H  = '4', '6 - 12h'
        DE_12_24H = '5', '12 - 24h'
        ACIMA_24H = '6', '24h ou mais'
        IGNORADO  = '9', 'Ignorado'

    tp_tempo_decorrido = models.CharField(
        max_length=1,
        choices=TempoDecorrido.choices,
        null=True,
        blank=True,
        verbose_name="Tempo decorrido picada/atendimento",
        help_text="Tempo decorrido entre o acidente e o atendimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Local da picada
    # -------------------------------------------------------------------------

    class LocalPicada(models.TextChoices):
        CABECA      = '01', 'Cabeça'
        BRACO       = '02', 'Braço'
        ANTEBRACO   = '03', 'Ante-Braço'
        MAO         = '04', 'Mão'
        DEDO_MAO    = '05', 'Dedo da Mão'
        TRONCO      = '06', 'Tronco'
        COXA        = '07', 'Coxa'
        PERNA       = '08', 'Perna'
        PE          = '09', 'Pé'
        DEDO_PE     = '10', 'Dedo do Pé'
        IGNORADO    = '99', 'Ignorado'

    tp_local_picada = models.CharField(
        max_length=2,
        choices=LocalPicada.choices,
        verbose_name="Local da picada",
        help_text="Localização da picada no corpo do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Manifestações locais
    # -------------------------------------------------------------------------

    class SimNaoIgnorado(models.TextChoices):
        SIM      = '1', 'Sim'
        NAO      = '2', 'Não'
        IGNORADO = '9', 'Ignorado'

    st_manifestacao_local = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Manifestações locais",
        help_text="Informa se houve manifestações locais.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Se manifestações locais sim, especificar
    # -------------------------------------------------------------------------

    st_manifestacao_dor = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Manifestação local - Dor",
        help_text="Se manifestações locais = Sim, informa se houve dor.",
    )
    st_manifestacao_edema = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Manifestação local - Edema",
        help_text="Se manifestações locais = Sim, informa se houve edema.",
    )
    st_manifestacao_equimose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Manifestação local - Equimose",
        help_text="Se manifestações locais = Sim, informa se houve equimose.",
    )
    st_manifestacao_necrose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Manifestação local - Necrose",
        help_text="Se manifestações locais = Sim, informa se houve necrose.",
    )
    st_manifestacao_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Manifestação local - Outras",
        help_text="Se manifestações locais = Sim, informa se houve outras manifestações.",
    )
    ds_manifestacao_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Manifestação local - Outras (descrição)",
        help_text="Especificação de outras manifestações locais.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Manifestações sistêmicas
    # -------------------------------------------------------------------------

    st_manifestacao_sistemica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Manifestações sistêmicas",
        help_text="Informa se houve manifestações sistêmicas.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Se manifestações sistêmicas sim, especificar
    # -------------------------------------------------------------------------

    st_manifestacao_sist_neuropara = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Manifestação sistêmica - Neuroparalítica",
        help_text="Se sistêmicas = Sim, informa se houve manifestações neuroparalíticas (ptose palpebral, turvação visual).",
    )
    st_manifestacao_sist_hemorrag = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Manifestação sistêmica - Hemorrágica",
        help_text="Se sistêmicas = Sim, informa se houve manifestações hemorrágicas (gengivorragia, outros sangramentos).",
    )
    st_manifestacao_sist_vagais = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Manifestação sistêmica - Vagais",
        help_text="Se sistêmicas = Sim, informa se houve manifestações vagais (vômitos/diarréia).",
    )
    st_manifestacao_sist_miolitica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Manifestação sistêmica - Miolítica/Hemolítica",
        help_text="Se sistêmicas = Sim, informa se houve manifestações miolíticas (mialgia, anemia, urina escura).",
    )
    st_manifestacao_sist_renal = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Manifestação sistêmica - Renal",
        help_text="Se sistêmicas = Sim, informa se houve manifestações renais (oligúria/anúria).",
    )
    st_manifestacao_sist_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Manifestação sistêmica - Outras",
        help_text="Se sistêmicas = Sim, informa se houve outras manifestações sistêmicas.",
    )
    ds_manifestacao_sist_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Manifestação sistêmica - Outras (descrição)",
        help_text="Especificação de outras manifestações sistêmicas.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Tempo de coagulação
    # -------------------------------------------------------------------------

    class TempoCoagulacao(models.TextChoices):
        NORMAL       = '1', 'Normal'
        ALTERADO     = '2', 'Alterado'
        NAO_REALIZADO = '9', 'Não realizado'

    tp_tempo_coagulacao = models.CharField(
        max_length=1,
        choices=TempoCoagulacao.choices,
        null=True,
        blank=True,
        verbose_name="Tempo de coagulação",
        help_text="Resultado do tempo de coagulação.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Tipo de acidente (animal)
    # -------------------------------------------------------------------------

    class TipoAnimal(models.TextChoices):
        SERPENTE  = '1', 'Serpente'
        ARANHA    = '2', 'Aranha'
        ESCORPIAO = '3', 'Escorpião'
        LAGARTA   = '4', 'Lagarta'
        ABELHA    = '5', 'Abelha'
        OUTROS    = '6', 'Outros'
        IGNORADO  = '9', 'Ignorado'

    tp_animal = models.CharField(
        max_length=1,
        choices=TipoAnimal.choices,
        verbose_name="Tipo de acidente (animal)",
        help_text="Animal responsável pela agressão.",
    )
    ds_animal_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro animal (descrição)",
        help_text="Especificação do animal quando tp_animal = Outros.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Serpente – Tipo de acidente
    # -------------------------------------------------------------------------

    class TipoSerpente(models.TextChoices):
        BOTROPICO            = '1', 'Botrópico'
        CROTALICO            = '2', 'Crotálico'
        ELAPIDICO            = '3', 'Elapídico',
        LAQUETICO            = '4', 'Laquético'
        NAO_PECONHENTA       = '5', 'Serpente não peçonhenta'
        IGNORADO             = '9', 'Ignorado'

    tp_serpente = models.CharField(
        max_length=1,
        choices=TipoSerpente.choices,
        null=True,
        blank=True,
        verbose_name="Serpente – tipo de acidente",
        help_text="Tipo de acidente ofídico conforme manifestações clínicas. Obrigatório se tp_animal = Serpente.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Aranha – Tipo de acidente
    # -------------------------------------------------------------------------

    class TipoAranha(models.TextChoices):
        FONEUTRISMO   = '1', 'Foneutrismo'
        LOXOSCELISMO  = '2', 'Loxoscelismo'
        LATRODECTISMO = '3', 'Latrodectismo'
        OUTRA_ARANHA  = '4', 'Outra aranha'
        IGNORADO      = '9', 'Ignorado'

    tp_aranha = models.CharField(
        max_length=1,
        choices=TipoAranha.choices,
        null=True,
        blank=True,
        verbose_name="Aranha – tipo de acidente",
        help_text="Tipo de acidente araneídico conforme manifestações clínicas. Obrigatório se tp_animal = Aranha.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Lagarta – Tipo de acidente
    # -------------------------------------------------------------------------

    class TipoLagarta(models.TextChoices):
        LONOMIA      = '1', 'Lonomia'
        OUTRA_LAGARTA = '2', 'Outra lagarta'
        IGNORADO     = '9', 'Ignorado'

    tp_lagarta = models.CharField(
        max_length=1,
        choices=TipoLagarta.choices,
        null=True,
        blank=True,
        verbose_name="Lagarta – tipo de acidente",
        help_text="Tipo de acidente por lagarta conforme manifestações clínicas. Obrigatório se tp_animal = Lagarta.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Classificação do caso
    # -------------------------------------------------------------------------

    class ClassificacaoCaso(models.TextChoices):
        LEVE     = '1', 'Leve'
        MODERADO = '2', 'Moderado'
        GRAVE    = '3', 'Grave'
        IGNORADO = '9', 'Ignorado'

    tp_classificacao_caso = models.CharField(
        max_length=1,
        choices=ClassificacaoCaso.choices,
        null=True,
        blank=True,
        verbose_name="Classificação do caso",
        help_text="Classificação da gravidade do envenenamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Soroterapia
    # -------------------------------------------------------------------------

    st_soroterapia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Soroterapia",
        help_text="Informa se foi realizada soroterapia.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Se soroterapia sim, número de ampolas por tipo de soro
    # -------------------------------------------------------------------------

    nu_antibotropico = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Ampolas – Antibotrópico (SAB)",
        help_text="Número de ampolas de soro antibotrópico aplicadas.",
    )
    nu_anticrotalico = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Ampolas – Anticrotálico (SAC)",
        help_text="Número de ampolas de soro anticrotálico aplicadas.",
    )
    nu_antiaracnidico = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Ampolas – Antiaracnídico (SAAr)",
        help_text="Número de ampolas de soro antiaracnídico aplicadas.",
    )
    nu_antibotropico_laquetico = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Ampolas – Antibotrópico-Laquético (SABL)",
        help_text="Número de ampolas de soro antibotrópico-laquético aplicadas.",
    )
    nu_antielapidico = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Ampolas – Antielapídico (SAEL)",
        help_text="Número de ampolas de soro antielapídico aplicadas.",
    )
    nu_antiloxoscelico = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Ampolas – Antiloxoscélico (SALox)",
        help_text="Número de ampolas de soro antiloxoscélico aplicadas.",
    )
    nu_antilbotropico_crotalico = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Ampolas – Antibotrópico-Crotálico (SABC)",
        help_text="Número de ampolas de soro antibotrópico-crotálico aplicadas.",
    )
    nu_antiescorpionico = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Ampolas – Antiescorpiônico (SAEsc)",
        help_text="Número de ampolas de soro antiescorpiônico aplicadas.",
    )
    nu_antilonomico = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Ampolas – Antilonômico (SALon)",
        help_text="Número de ampolas de soro antilonômico aplicadas.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Complicações locais
    # -------------------------------------------------------------------------

    st_complicacao_local = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Complicações locais",
        help_text="Informa se houve complicações locais.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Se complicações locais sim, especificar
    # -------------------------------------------------------------------------

    st_complicacao_local_infeccao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Complicação local – Infecção Secundária",
        help_text="Se complicações locais = Sim, informa se houve infecção secundária.",
    )
    st_complicacao_local_necrose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Complicação local – Necrose Extensa",
        help_text="Se complicações locais = Sim, informa se houve necrose extensa.",
    )
    st_complicacao_local_sindrome = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Complicação local – Síndrome Comportamental",
        help_text="Se complicações locais = Sim, informa se houve síndrome comportamental.",
    )
    st_complicacao_local_deficit = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Complicação local – Déficit Funcional",
        help_text="Se complicações locais = Sim, informa se houve déficit funcional.",
    )
    st_complicacao_local_amputacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Complicação local – Amputação",
        help_text="Se complicações locais = Sim, informa se houve amputação.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Complicações sistêmicas
    # -------------------------------------------------------------------------

    st_complicacao_sistemica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Complicações sistêmicas",
        help_text="Informa se houve complicações sistêmicas.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Se complicações sistêmicas sim, especificar
    # -------------------------------------------------------------------------

    st_complicacao_sist_renal = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Complicação sistêmica – Insuficiência Renal",
        help_text="Se complicações sistêmicas = Sim, informa se houve insuficiência renal.",
    )
    st_complicacao_sist_respiratoria = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Complicação sistêmica – Insuficiência Respiratória/Edema Pulmonar Agudo",
        help_text="Se complicações sistêmicas = Sim, informa se houve insuficiência respiratória.",
    )
    st_complicacao_sist_septicemia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Complicação sistêmica – Septicemia",
        help_text="Se complicações sistêmicas = Sim, informa se houve septicemia.",
    )
    st_complicacao_sist_choque = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Complicação sistêmica – Choque",
        help_text="Se complicações sistêmicas = Sim, informa se houve choque.",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - Acidente relacionado ao trabalho
    # -------------------------------------------------------------------------

    st_acidente_trabalho = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Acidente relacionado ao trabalho",
        help_text="Informa se o acidente é relacionado ao trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 57 - Evolução do caso
    # -------------------------------------------------------------------------

    class EvolucaoCaso(models.TextChoices):
        CURA                 = '1', 'Cura'
        OBITO_PECONHENTO     = '2', 'Óbito por acidente por animais peçonhentos'
        OBITO_OUTRAS_CAUSAS  = '3', 'Óbito por outras causas'
        IGNORADO             = '9', 'Ignorado'

    tp_evolucao_caso = models.CharField(
        max_length=1,
        choices=EvolucaoCaso.choices,
        null=True,
        blank=True,
        verbose_name="Evolução do caso",
        help_text="Desfecho clínico do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 58 - Data do óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text=(
            "Data do óbito. Habilitado quando evolução = Óbito. "
            "Deve ser >= data de diagnóstico e data do acidente."
        ),
    )

    # -------------------------------------------------------------------------
    # Campo 59 - Data do encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento",
        help_text=(
            "Data do encerramento do caso. Obrigatório quando evolução estiver preenchida. "
            "Deve ser >= data de investigação."
        ),
    )

    # -------------------------------------------------------------------------
    # Campos complementares
    # -------------------------------------------------------------------------

    ds_observacao = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Observações",
        help_text="Informações complementares: outros dados clínicos, laboratoriais, laudos, etc.",
    )

    nu_lote_vertical = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Lote de transferência vertical",
        help_text="Identificador do lote de transferência vertical da investigação entre níveis do sistema.",
    )

    class Meta:
        db_table = 'animais_peconhentos'
        verbose_name = 'Acidente por Animais Peçonhentos'
        verbose_name_plural = 'Acidentes por Animais Peçonhentos'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Acidente {self.tp_animal} – {self.dt_acidente}"