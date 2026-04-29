from django.db import models


class FebreNilo(models.Model):
    """
    Ficha de Investigação - Febre do Nilo (Ocidental)
    Dicionário de Dados SINAN NET - Versão 5.0
    Revisado em setembro/2015
    Campos 31 a 88 + campos de controle
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

    class ResultadoExame(models.TextChoices):
        REAGENTE = '1', 'Reagente'
        NAO_REAGENTE = '2', 'Não reagente'
        INCONCLUSIVO = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'

    class ResultadoIsolamentoViral(models.TextChoices):
        DETECTADO = '1', 'Detectado'
        NAO_DETECTADO = '2', 'Não detectado'
        INCONCLUSIVO = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'

    class ResultadoPCR(models.TextChoices):
        POSITIVO = '1', 'Positivo'
        NEGATIVO = '2', 'Negativo'
        INCONCLUSIVO = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'

    class AspectoLiquor(models.TextChoices):
        LIMPIDO = '1', 'Límpido'
        PURULENTO = '2', 'Purulento'
        HEMORRAGICO = '3', 'Hemorrágico'
        TURVO = '4', 'Turvo'
        XANTOCROMICO = '5', 'Xantocrômico'
        OUTRO = '6', 'Outro'
        IGNORADO = '9', 'Ignorado'

    class LocalizacaoParalisia(models.TextChoices):
        MMSS = '1', 'MMSS'
        MMII = '2', 'MMII'
        AMBOS = '3', 'Ambos'

    class ClassificacaoFinal(models.TextChoices):
        CONFIRMADO = '1', 'Confirmado'
        DESCARTADO = '2', 'Descartado'

    class CriterioConfirmacao(models.TextChoices):
        LABORATORIAL = '1', 'Laboratorial'
        VINCULO_EPIDEMIOLOGICO = '2', 'Vínculo Epidemiológico'
        CLINICO = '3', 'Clínico'

    class Autoctone(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        INDETERMINADO = '3', 'Indeterminado'

    class EvolucaoCaso(models.TextChoices):
        CURA = '1', 'Cura'
        OBITO_FNO = '2', 'Óbito por FNO'
        OBITO_OUTRA_CAUSA = '3', 'Óbito por outra causa'
        IGNORADO = '9', 'Ignorado'

    # -------------------------------------------------------------------------
    # Campo 31 - Data da Investigação
    # -------------------------------------------------------------------------

    dt_investigacao = models.DateField(
        verbose_name="Data da investigação",
        help_text="Data em que ocorreu a investigação (1ª visita ao paciente). Deve ser >= data da notificação e <= data atual.",
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
    # Campo 33 - Viajou nos últimos 15 dias?
    # -------------------------------------------------------------------------

    st_viagem_15_dia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Viajou nos últimos 15 dias",
        help_text="Se o paciente viajou nos últimos 15 dias.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Data de ida
    # -------------------------------------------------------------------------

    dt_ida = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de ida",
        help_text="Data de ida da viagem realizada nos últimos 15 dias.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Data de retorno
    # -------------------------------------------------------------------------

    dt_volta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de retorno",
        help_text="Data de retorno da viagem realizada nos últimos 15 dias.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - UF da viagem
    # -------------------------------------------------------------------------

    co_uf_viagem = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF da viagem",
        help_text="UF da viagem realizada nos últimos 15 dias.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - País da viagem
    # -------------------------------------------------------------------------

    co_pais_viagem = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="País da viagem",
        help_text="País da viagem realizada nos últimos 15 dias.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Município da viagem
    # -------------------------------------------------------------------------

    co_municipio_viagem = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município da viagem",
        help_text="Município da viagem realizada nos últimos 15 dias.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Vacinado contra febre amarela
    # -------------------------------------------------------------------------

    st_vacinado_febre_amarela = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Vacinado contra febre amarela",
        help_text="Se o paciente tem história vacinal contra febre amarela.",
    )
    dt_vacinado_febre_amarela = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da vacina febre amarela",
        help_text="Data da vacina contra febre amarela. Deve ser > data de nascimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Infecção prévia (3 subcampos)
    # -------------------------------------------------------------------------

    st_infeccao_previa_dengue = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Infecção prévia - Dengue",
        help_text="Se teve infecção prévia por dengue.",
    )
    dt_infeccao_dengue = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da infecção - Dengue",
        help_text="Data da infecção prévia por dengue.",
    )
    st_infec_previa_febre_amarela = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Infecção prévia - Febre Amarela",
        help_text="Se teve infecção prévia por febre amarela.",
    )
    dt_infeccao_febre_amarela = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da infecção - Febre Amarela",
        help_text="Data da infecção prévia por febre amarela.",
    )
    st_infeccao_previa_arbovirose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Infecção prévia - Outra Arbovirose",
        help_text="Se teve infecção prévia por outra arbovirose.",
    )
    ds_tipo_arbovirose = models.CharField(
        max_length=35,
        null=True,
        blank=True,
        verbose_name="Tipo de arbovirose (especificar)",
        help_text="Especificação da arbovirose.",
    )
    dt_infeccao_arbovirose = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da infecção - Arbovirose",
        help_text="Data da infecção prévia por arbovirose.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Realizou transfusão sanguínea nos últimos 15 dias
    # -------------------------------------------------------------------------

    st_transfusao_sanguinea = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Realizou transfusão sanguínea nos últimos 15 dias",
        help_text="Se realizou transfusão sanguínea nos últimos 15 dias.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Data da Transfusão
    # -------------------------------------------------------------------------

    dt_transfusao_sanguinea = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da transfusão",
        help_text="Data da transfusão sanguínea.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - UF da transfusão
    # -------------------------------------------------------------------------

    co_uf_transfusao_sanguinea = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF da transfusão",
        help_text="UF onde ocorreu a transfusão.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Município do hospital onde realizou transfusão
    # -------------------------------------------------------------------------

    co_municipio_hospital_transf = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município do hospital",
        help_text="Município do hospital onde realizou a transfusão.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Nome do Hospital onde realizou a transfusão
    # -------------------------------------------------------------------------

    co_hospital_transf_uson = models.DecimalField(
        max_digits=8,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Código do hospital",
        help_text="Código do hospital onde realizou a transfusão.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Aleitamento materno
    # -------------------------------------------------------------------------

    st_aleitamento_materno = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Aleitamento materno",
        help_text="Se o paciente está recebendo aleitamento materno.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Esteve em áreas onde tiveram cavalos e/ou aves mortas ou doentes
    # -------------------------------------------------------------------------

    st_animal_morto = models.CharField(
        max_length=2,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Esteve em áreas com cavalos/aves mortas ou doentes",
        help_text="Se esteve em áreas onde tiveram cavalos e/ou aves mortas ou doentes nos últimos 15 dias.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Ocorreu hospitalização
    # -------------------------------------------------------------------------

    st_hospitalizacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Ocorreu hospitalização",
        help_text="Se ocorreu hospitalização.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Data da Internação
    # -------------------------------------------------------------------------

    dt_internacao = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da internação",
        help_text="Data da hospitalização.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - UF da hospitalização
    # -------------------------------------------------------------------------

    co_uf_hospitalizacao = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF da hospitalização",
        help_text="UF onde ocorreu hospitalização.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Município do hospital
    # -------------------------------------------------------------------------

    co_municipio_hospitalizacao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município do hospital",
        help_text="Município do hospital onde ocorreu hospitalização.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Nome do Hospital
    # -------------------------------------------------------------------------

    co_estabelecimento_hospitalizacao = models.DecimalField(
        max_digits=8,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Código do hospital",
        help_text="Código do hospital onde ocorreu hospitalização.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Sinais e sintomas (18 subcampos)
    # -------------------------------------------------------------------------

    st_sintoma_convulsao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Convulsões",
        help_text="Se o paciente apresentou convulsões.",
    )
    st_rigidez_nuca = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Rigidez de nuca",
        help_text="Se o paciente apresentou rigidez de nuca.",
    )
    st_confusao_mental = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Confusão mental",
        help_text="Se o paciente apresentou confusão mental.",
    )
    st_coma = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Coma",
        help_text="Se o paciente apresentou coma.",
    )
    st_diarreia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Diarréia",
        help_text="Se o paciente apresentou diarréia.",
    )
    st_vomito = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Vômito",
        help_text="Se o paciente apresentou vômito.",
    )
    st_nausea = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Náusea",
        help_text="Se o paciente apresentou náusea.",
    )
    st_dor_abdominal = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Dor abdominal",
        help_text="Se o paciente apresentou dor abdominal.",
    )
    st_mialgia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Mialgia",
        help_text="Se o paciente apresentou mialgia.",
    )
    st_artralgia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Artralgia",
        help_text="Se o paciente apresentou artralgia.",
    )
    st_cefaleia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Cefaléia",
        help_text="Se o paciente apresentou cefaléia.",
    )
    st_exantema = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exantema",
        help_text="Se o paciente apresentou exantema.",
    )
    st_febre = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Febre",
        help_text="Se o paciente apresentou febre.",
    )
    st_dor_ocular = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Dor ocular",
        help_text="Se o paciente apresentou dor ocular.",
    )
    st_linfadenopatia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Linfadenopatia",
        help_text="Se o paciente apresentou linfadenopatia.",
    )
    st_fraqueza_muscular = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Fraqueza muscular",
        help_text="Se o paciente apresentou fraqueza muscular.",
    )
    st_mmss = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Fraqueza em MMSS",
        help_text="Se fraqueza muscular em membros superiores.",
    )
    st_mmii = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Fraqueza em MMII",
        help_text="Se fraqueza muscular em membros inferiores.",
    )
    st_paralisia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Paralisia",
        help_text="Se o paciente apresentou paralisia.",
    )
    ds_local_paralisia = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Local da paralisia",
        help_text="Local da paralisia (se paralisia = Sim).",
    )
    st_prostracao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Prostração",
        help_text="Se o paciente apresentou prostração.",
    )
    st_tremor_extremidade = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Tremores de extremidades",
        help_text="Se o paciente apresentou tremores de extremidades.",
    )
    st_outro_sintoma = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outros sintomas",
        help_text="Se o paciente apresentou outros sintomas.",
    )
    ds_outro_sintoma = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outros sintomas (especificar)",
        help_text="Especificação de outros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Leucograma (4 subcampos)
    # -------------------------------------------------------------------------

    nu_leucocito_leucograma = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Leucócitos",
        help_text="Número de leucócitos.",
    )
    nu_monocito_leucograma = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Monócitos (%)",
        help_text="Percentual de monócitos.",
    )
    nu_neutrofilo_leucograma = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Neutrófilos (%)",
        help_text="Percentual de neutrófilos.",
    )
    nu_eosinofilo_leucograma = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Eosinófilos (%)",
        help_text="Percentual de eosinófilos.",
    )
    nu_linfocito_leucograma = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Linfócitos (%)",
        help_text="Percentual de linfócitos.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Hemograma (4 subcampos)
    # -------------------------------------------------------------------------

    nu_hemacia_hemograma = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Hemácias",
        help_text="Número de hemácias.",
    )
    nu_hemoglobina_hemograma = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Hemoglobina",
        help_text="Valor da hemoglobina.",
    )
    nu_hematocrito_hemograma = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Hematócrito",
        help_text="Hematócrito.",
    )
    nu_plaqueta_hemograma = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Plaquetas",
        help_text="Número de plaquetas.",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - Punção lombar
    # -------------------------------------------------------------------------

    st_puncao_lombar = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Punção lombar",
        help_text="Se realizou punção lombar.",
    )

    # -------------------------------------------------------------------------
    # Campo 57 - Data da punção
    # -------------------------------------------------------------------------

    dt_puncao_lombar = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da punção lombar",
        help_text="Data da punção lombar. Deve ser > data de nascimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 58 - Aspecto do líquor
    # -------------------------------------------------------------------------

    tp_aspecto_liquor = models.CharField(
        max_length=1,
        choices=AspectoLiquor.choices,
        null=True,
        blank=True,
        verbose_name="Aspecto do líquor",
        help_text="Aspecto do líquor.",
    )

    # -------------------------------------------------------------------------
    # Campo 59 - Citoquímica - líquor (8 subcampos)
    # -------------------------------------------------------------------------

    nu_hemacia_citoquimica = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Hemácias no líquor",
        help_text="Número de hemácias no líquor.",
    )
    nu_leucocito_citoquimica = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Leucócitos no líquor",
        help_text="Número de leucócitos no líquor.",
    )
    nu_monocito_citoquimica = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Monócitos no líquor (%)",
        help_text="Percentual de monócitos no líquor.",
    )
    nu_glicose_citoquimica = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Glicose no líquor",
        help_text="Valor da glicose no líquor.",
    )
    nu_cloreto_citoquimica = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Cloreto no líquor",
        help_text="Valor de cloreto no líquor.",
    )
    nu_neutrofilo_citoquimica = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Neutrófilos no líquor (%)",
        help_text="Percentual de neutrófilos no líquor.",
    )
    nu_eosinofilo_citoquimica = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Eosinófilos no líquor (%)",
        help_text="Percentual de eosinófilos no líquor.",
    )
    nu_linfocito_citoquimica = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Linfócitos no líquor (%)",
        help_text="Percentual de linfócitos no líquor.",
    )
    nu_proteina_citoquimica = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Proteína no líquor",
        help_text="Valor de proteína no líquor.",
    )

    # -------------------------------------------------------------------------
    # Campo 60 - Líquor - ELISA
    # -------------------------------------------------------------------------

    tp_liquor_elisa_igm = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Líquor - ELISA IgM",
        help_text="Resultado do ELISA IgM do líquor.",
    )
    tp_liquor_elisa_igg = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Líquor - ELISA IgG",
        help_text="Resultado do ELISA IgG do líquor.",
    )

    # -------------------------------------------------------------------------
    # Campo 61 - Líquor - soroneutralização
    # -------------------------------------------------------------------------

    tp_liquor_soroneutralizacao = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Líquor - Soroneutralização",
        help_text="Resultado da soroneutralização do IgM no líquor.",
    )

    # -------------------------------------------------------------------------
    # Campo 62 - Data da coleta (S1)
    # -------------------------------------------------------------------------

    dt_coleta_s1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta (Soro 1)",
        help_text="Data da 1ª coleta de soro.",
    )

    # -------------------------------------------------------------------------
    # Campo 63 - Soro - ELISA (S1)
    # -------------------------------------------------------------------------

    tp_soro_elisa_s1_igm = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Soro 1 - ELISA IgM",
        help_text="Resultado do ELISA IgM no soro da 1ª amostra.",
    )
    tp_soro_elisa_s1_igg = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Soro 1 - ELISA IgG",
        help_text="Resultado do ELISA IgG no soro da 1ª amostra.",
    )

    # -------------------------------------------------------------------------
    # Campo 64 - Soro - soroneutralização (S1)
    # -------------------------------------------------------------------------

    tp_soroneutralizacao_s1 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Soro 1 - Soroneutralização",
        help_text="Resultado da soroneutralização IgM no soro da 1ª amostra.",
    )

    # -------------------------------------------------------------------------
    # Campo 65 - Data da coleta (S2)
    # -------------------------------------------------------------------------

    dt_coleta_s2 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta (Soro 2)",
        help_text="Data da 2ª coleta de soro. Deve ser > data da 1ª coleta.",
    )

    # -------------------------------------------------------------------------
    # Campo 66 - Soro - ELISA (S2)
    # -------------------------------------------------------------------------

    tp_soro_elisa_s2_igm = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Soro 2 - ELISA IgM",
        help_text="Resultado do ELISA IgM no soro da 2ª amostra.",
    )
    tp_soro_elisa_s2_igg = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Soro 2 - ELISA IgG",
        help_text="Resultado do ELISA IgG no soro da 2ª amostra.",
    )

    # -------------------------------------------------------------------------
    # Campo 67 - Soro - soroneutralização (S2)
    # -------------------------------------------------------------------------

    tp_soroneutralizacao_s2 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Soro 2 - Soroneutralização",
        help_text="Resultado da soroneutralização IgM no soro da 2ª amostra.",
    )

    # -------------------------------------------------------------------------
    # Campo 68 - Material coletado (PCR) - 4 subcampos
    # -------------------------------------------------------------------------

    st_material_coletopcr_sangue = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="PCR - Sangue coletado",
        help_text="Se houve coleta de sangue para PCR.",
    )
    st_material_coletopcr_liquor = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="PCR - Líquor coletado",
        help_text="Se houve coleta de líquor para PCR.",
    )
    st_material_coletopcr_tecido = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="PCR - Tecido coletado",
        help_text="Se houve coleta de tecido para PCR.",
    )
    ds_material_coletopcr = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Tecido coletado (especificar)",
        help_text="Especificar qual tecido coletado para PCR.",
    )

    # -------------------------------------------------------------------------
    # Campo 69 - Data da coleta (PCR)
    # -------------------------------------------------------------------------

    dt_material_coletopcr = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta (PCR)",
        help_text="Data da coleta do material para PCR.",
    )

    # -------------------------------------------------------------------------
    # Campo 70 - PCR
    # -------------------------------------------------------------------------

    tp_pcr = models.CharField(
        max_length=1,
        choices=ResultadoPCR.choices,
        null=True,
        blank=True,
        verbose_name="Resultado do PCR",
        help_text="Resultado do exame de PCR.",
    )

    # -------------------------------------------------------------------------
    # Campo 71 - Material coletado (Isolamento Viral - IV)
    # -------------------------------------------------------------------------

    st_material_coletado_iv_sangue = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Isolamento Viral - Sangue coletado",
        help_text="Se houve coleta de sangue para isolamento viral.",
    )
    st_material_coletado_iv_liquor = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Isolamento Viral - Líquor coletado",
        help_text="Se houve coleta de líquor para isolamento viral.",
    )
    st_material_coletado_iv_tecido = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Isolamento Viral - Tecido coletado",
        help_text="Se houve coleta de tecido para isolamento viral.",
    )
    ds_material_colet_iv = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Tecido coletado (especificar)",
        help_text="Especificar qual tecido coletado para isolamento viral.",
    )

    # -------------------------------------------------------------------------
    # Campo 72 - Data da coleta (IV)
    # -------------------------------------------------------------------------

    dt_material_coletado_iv = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta (Isolamento Viral)",
        help_text="Data da coleta do material para isolamento viral.",
    )

    # -------------------------------------------------------------------------
    # Campo 73 - Isolamento viral (IV)
    # -------------------------------------------------------------------------

    tp_isolamento_viral_iv = models.CharField(
        max_length=1,
        choices=ResultadoIsolamentoViral.choices,
        null=True,
        blank=True,
        verbose_name="Resultado do Isolamento Viral",
        help_text="Resultado do isolamento viral.",
    )

    # -------------------------------------------------------------------------
    # Campo 74 - Material coletado (Anátomo-patológico - AP)
    # -------------------------------------------------------------------------

    st_material_colet_ap_cerebro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="AP - Cérebro coletado",
        help_text="Se houve coleta de cérebro para AP.",
    )
    st_material_colet_ap_viscere = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="AP - Vísceras coletadas",
        help_text="Se houve coleta de vísceras para AP.",
    )
    ds_material_colet_ap = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outras vísceras (especificar)",
        help_text="Especificar quais outras vísceras coletadas.",
    )

    # -------------------------------------------------------------------------
    # Campo 75 - Anátomo-patológico
    # -------------------------------------------------------------------------

    tp_anato_patol_histopatologico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Histopatológico",
        help_text="Resultado do histopatológico.",
    )
    tp_anato_patol_imunohistoquimica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Imunohistoquímica",
        help_text="Resultado da imunohistoquímica.",
    )

    # -------------------------------------------------------------------------
    # Campo 76 - Data da coleta (AP)
    # -------------------------------------------------------------------------

    dt_coleta_ap = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta (AP)",
        help_text="Data da coleta do material para AP. Deve ser > data de nascimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 77 - Classificação final
    # -------------------------------------------------------------------------

    tp_classificacao_final = models.CharField(
        max_length=1,
        choices=ClassificacaoFinal.choices,
        null=True,
        blank=True,
        verbose_name="Classificação final",
        help_text="Classificação final do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 78 - Critério de confirmação/descarte
    # -------------------------------------------------------------------------

    tp_confirmacao_descarte = models.CharField(
        max_length=1,
        choices=CriterioConfirmacao.choices,
        null=True,
        blank=True,
        verbose_name="Critério de confirmação/descarte",
        help_text="Critério utilizado para confirmação do caso ou descarte do suspeito.",
    )

    # -------------------------------------------------------------------------
    # Campo 79 - O caso é Autóctone de residência?
    # -------------------------------------------------------------------------

    tp_autoctone_residencia = models.CharField(
        max_length=1,
        choices=Autoctone.choices,
        null=True,
        blank=True,
        verbose_name="Caso autóctone do município de residência",
        help_text="Indica se o caso é autóctone do município de residência.",
    )

    # -------------------------------------------------------------------------
    # Campo 80 - UF (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_uf_infeccao = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF provável da infecção",
        help_text="Unidade Federada onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 81 - País (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_pais_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="País provável da infecção",
        help_text="País onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 82 - Município (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_municipio_infeccao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município provável da infecção",
        help_text="Código do município onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 83 - Distrito (provável de infecção)
    # -------------------------------------------------------------------------

    co_distrito_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Distrito provável da infecção",
        help_text="Código do distrito provável de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 84 - Bairro (provável de infecção)
    # -------------------------------------------------------------------------

    co_bairro_infeccao = models.DecimalField(
        max_digits=8,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Código do bairro provável da infecção",
        help_text="Código do bairro provável de infecção.",
    )
    no_bairro_infeccao = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Bairro provável da infecção",
        help_text="Nome do bairro provável de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 85 - Doença relacionada ao trabalho
    # -------------------------------------------------------------------------

    st_doenca_trabalho = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Doença relacionada ao trabalho",
        help_text="Se a doença é relacionada ao trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 86 - Evolução do caso
    # -------------------------------------------------------------------------

    tp_evolucao_caso = models.CharField(
        max_length=1,
        choices=EvolucaoCaso.choices,
        null=True,
        blank=True,
        verbose_name="Evolução do caso",
        help_text="Evolução do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 87 - Data do óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito. Obrigatório se evolução = 2 ou 3.",
    )

    # -------------------------------------------------------------------------
    # Campo 88 - Data do encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento",
        help_text="Data de encerramento da investigação.",
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
        db_table = 'febre_nilo'
        verbose_name = 'Febre do Nilo Ocidental'
        verbose_name_plural = 'Febre do Nilo Ocidental'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Febre do Nilo – {self.dt_investigacao}"