from django.db import models


class Botulismo(models.Model):
    """
    Ficha de Investigação - Botulismo
    Dicionário de Dados SINAN NET - Versão 5.0
    Revisado em julho/2010
    Campos 31 a 79 + campos complementares + campos de controle
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

    class ResultadoToxina(models.TextChoices):
        PRESENCA = '1', 'Presença de toxina'
        AUSENCIA = '2', 'Ausência de toxina'
        INCONCLUSIVO = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'

    class TipoToxina(models.TextChoices):
        A = '1', 'A'
        B = '2', 'B'
        AB = '3', 'AB'
        E = '4', 'E'
        F = '5', 'F'
        G = '6', 'G'
        OUTRA = '7', 'Outra'
        IGNORADO = '9', 'Ignorado'

    class ReflexoNeurologico(models.TextChoices):
        NORMAIS = '1', 'Normais'
        AUMENTADOS = '2', 'Aumentados'
        REDUZIDOS_AUSENTES = '3', 'Reduzidos/Ausentes'
        IGNORADO = '9', 'Ignorado'

    class ExposicaoAlimento(models.TextChoices):
        UNICA = '1', 'Única'
        MULTIPLA = '2', 'Múltipla'
        IGNORADO = '9', 'Ignorado'

    class RealizadoNaoRealizado(models.TextChoices):
        REALIZADO = '1', 'Realizado'
        NAO_REALIZADO = '2', 'Não realizado'

    # -------------------------------------------------------------------------
    # Campo 31 - Data da Investigação
    # -------------------------------------------------------------------------

    dt_investigacao = models.DateField(
        verbose_name="Data da investigação",
        help_text="Data em que ocorreu a investigação (1ª visita ao paciente). Deve ser >= data da notificação.",
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
    # Campo 33 - Data do 1º atendimento
    # -------------------------------------------------------------------------

    dt_atendimento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do 1º atendimento",
        help_text="Data do 1º atendimento médico. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Nº total de atendimentos até a suspeição clínica
    # -------------------------------------------------------------------------

    nu_atendimento = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Nº total de atendimentos até a suspeição clínica",
        help_text="Número total de atendimentos até a suspeita clínica de botulismo. 0 (zero) se não houve atendimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Data da suspeição clínica
    # -------------------------------------------------------------------------

    dt_suspeicao = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da suspeição clínica",
        help_text="Data da suspeita clínica. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Ocorreu Hospitalização
    # -------------------------------------------------------------------------

    st_ocorreu_hospitalizacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Ocorreu hospitalização",
        help_text="Informa se o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Data da Internação
    # -------------------------------------------------------------------------

    dt_internacao = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da internação",
        help_text="Habilitado se ocorreu hospitalização = Sim. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Data da alta hospitalar
    # -------------------------------------------------------------------------

    dt_alta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da alta hospitalar",
        help_text="Habilitado se ocorreu hospitalização = Sim. Deve ser >= data da internação.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - UF de internação
    # -------------------------------------------------------------------------

    co_uf_hospital = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de internação",
        help_text="Sigla da UF onde o paciente foi internado. Habilitado se ocorreu hospitalização = Sim.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Município do Hospital
    # -------------------------------------------------------------------------

    co_municipio_hospital = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município do hospital",
        help_text="Código do município onde o paciente foi internado. Habilitado se ocorreu hospitalização = Sim.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Nome do Hospital
    # -------------------------------------------------------------------------

    co_unidade_hospital = models.DecimalField(
        max_digits=7,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Código do hospital",
        help_text="Código da unidade hospitalar.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Sinais e Sintomas
    # -------------------------------------------------------------------------

    st_sinais_febre = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Febre",
        help_text="Informa se o paciente apresentou febre.",
    )
    st_sinais_nausea = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Náuseas",
        help_text="Informa se o paciente apresentou náuseas.",
    )
    st_sinais_vomito = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Vômitos",
        help_text="Informa se o paciente apresentou vômitos.",
    )
    st_sinais_diarreia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Diarréia",
        help_text="Informa se o paciente apresentou diarréia.",
    )
    st_sinais_constipacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Constipação",
        help_text="Informa se o paciente apresentou constipação.",
    )
    st_sinais_cefaleia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Cefaléia",
        help_text="Informa se o paciente apresentou cefaléia.",
    )
    st_sinais_tontura = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Tontura",
        help_text="Informa se o paciente apresentou tontura.",
    )
    st_sinais_visao_turva = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Visão turva",
        help_text="Informa se o paciente apresentou visão turva.",
    )
    st_sinais_diplopia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Diplopia",
        help_text="Informa se o paciente apresentou diplopia (visão dupla).",
    )
    st_sinais_disartria = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Disartria",
        help_text="Informa se o paciente apresentou disartria (dificuldade para falar).",
    )
    st_sinais_disfonia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Disfonia",
        help_text="Informa se o paciente apresentou disfonia (alteração da voz).",
    )
    st_sinais_disfagia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Disfagia",
        help_text="Informa se o paciente apresentou disfagia (dificuldade para engolir).",
    )
    st_sinais_boca_seca = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Boca seca",
        help_text="Informa se o paciente apresentou boca seca.",
    )
    st_sinais_ferimento = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Ferimento",
        help_text="Informa se o paciente apresenta ferimento aberto ou em cicatrização.",
    )
    st_sinais_flacidez_pescoco = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Flacidez de pescoço",
        help_text="Informa se o paciente apresentou flacidez de pescoço.",
    )
    st_sinais_dispneia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Dispnéia",
        help_text="Informa se o paciente apresentou dispnéia.",
    )
    st_sinais_insuf_respiratoria = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Insuficiência respiratória",
        help_text="Informa se o paciente apresentou insuficiência respiratória.",
    )
    st_sinais_insuf_cardiaca = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Insuficiência cardíaca",
        help_text="Informa se o paciente apresentou insuficiência cardíaca.",
    )
    st_sinais_coma = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Coma",
        help_text="Informa se o paciente entrou em coma.",
    )
    st_sinais_parestesia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Parestesia",
        help_text="Informa se o paciente apresentou parestesia.",
    )
    ds_sinais_parestesia_onde = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Parestesia (local)",
        help_text="Local onde o paciente apresentou parestesia. Habilitado se parestesia = Sim.",
    )
    st_sinais_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outros sinais/sintomas",
        help_text="Informa se o paciente apresentou outros sinais ou sintomas.",
    )
    ds_sinais_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outros sinais/sintomas (especificar)",
        help_text="Especificação de outros sinais e sintomas. Habilitado se outros = Sim.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Exame Neurológico
    # -------------------------------------------------------------------------

    st_exame_ptose_palpebral = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Ptose palpebral",
        help_text="Informa se o exame neurológico apresentou ptose palpebral.",
    )
    st_exame_oftalmoparesia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Oftalmoparesia / Oftalmoplegia",
        help_text="Informa se o exame neurológico apresentou oftalmoparesia ou oftalmoplegia.",
    )
    st_exame_midriase = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Midríase",
        help_text="Informa se o exame neurológico apresentou midríase.",
    )
    st_exame_paralisia_facial = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Paralisia Facial",
        help_text="Informa se o exame neurológico apresentou paralisia facial.",
    )
    st_exame_musculatura_bulbar = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Comprometimento da Musculatura Bulbar",
        help_text="Informa se o exame neurológico apresentou comprometimento da musculatura bulbar.",
    )
    st_exame_fraq_membro_sup = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Fraqueza em Membros Superiores",
        help_text="Informa se o exame neurológico apresentou fraqueza em membros superiores.",
    )
    st_exame_fraq_membro_inf = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Fraqueza em Membros Inferiores",
        help_text="Informa se o exame neurológico apresentou fraqueza em membros inferiores.",
    )
    st_exame_fraq_descendente = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Fraqueza Descendente",
        help_text="Informa se o exame neurológico apresentou fraqueza descendente.",
    )
    st_exame_fraq_simetrica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Fraqueza Simétrica",
        help_text="Informa se o exame neurológico apresentou fraqueza simétrica.",
    )
    st_exame_altera_sensibilidade = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Alterações de Sensibilidade",
        help_text="Informa se o exame neurológico apresentou alterações de sensibilidade.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Reflexos Neurológicos
    # -------------------------------------------------------------------------

    tp_reflexo_neurologico = models.CharField(
        max_length=1,
        choices=ReflexoNeurologico.choices,
        null=True,
        blank=True,
        verbose_name="Reflexos neurológicos",
        help_text="Reflexos neurológicos do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Suspeita de transmissão alimentar
    # -------------------------------------------------------------------------

    st_transmissao_alimentar = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Suspeita de transmissão alimentar",
        help_text="Informa se o caso de botulismo é de suspeita de origem alimentar.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Alimento suspeito
    # -------------------------------------------------------------------------

    ds_alimento_suspeito = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Alimento suspeito",
        help_text="Se o caso for de origem alimentar, informar qual foi o alimento suspeito.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Produção do alimento suspeito
    # -------------------------------------------------------------------------

    st_alimento_industrial = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Alimento industrial/comercial",
        help_text="Informa se o alimento suspeito é comercializado e/ou produzido em indústria alimentícia.",
    )
    st_alimento_caseira = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Alimento caseiro",
        help_text="Informa se o alimento é produzido de forma artesanal.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Especificação do alimento industrial
    # -------------------------------------------------------------------------

    ds_alimento_industrial = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Especificação do alimento industrial",
        help_text="Nome comercial, nome da empresa produtora, data de validade e lote do alimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Exposição ao alimento
    # -------------------------------------------------------------------------

    tp_exposicao_alimento = models.CharField(
        max_length=1,
        choices=ExposicaoAlimento.choices,
        null=True,
        blank=True,
        verbose_name="Exposição ao alimento",
        help_text="Informa se o paciente ingeriu o alimento suspeito apenas uma vez (exposição única).",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Tempo decorrido (única)
    # -------------------------------------------------------------------------

    ds_hr_unica_ingest_sintoma = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Tempo decorrido (única) - horas",
        help_text="Tempo decorrido entre ingestão do alimento suspeito e início dos sintomas (em horas).",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Tempo decorrido (múltipla - primeira ingestão)
    # -------------------------------------------------------------------------

    ds_hr_multi_ini_ingest_sintoma = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Tempo decorrido (múltipla - 1ª ingestão) - horas",
        help_text="Tempo decorrido entre a 1ª ingestão do alimento suspeito e início dos sintomas (em horas).",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Tempo decorrido (múltipla - última ingestão)
    # -------------------------------------------------------------------------

    ds_hr_multi_fim_ingest_sintoma = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Tempo decorrido (múltipla - última ingestão) - horas",
        help_text="Tempo decorrido entre a última ingestão do alimento suspeito e início dos sintomas (em horas).",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Local da ingestão
    # -------------------------------------------------------------------------

    st_local_domicilio = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Local da ingestão - Domicílio",
        help_text="Informa se a ingestão foi no domicílio do paciente.",
    )
    st_local_creche = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Local da ingestão - Creche/Escola",
        help_text="Informa se a ingestão foi em creche ou escola.",
    )
    st_local_trabalho = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Local da ingestão - Trabalho",
        help_text="Informa se a ingestão foi no trabalho.",
    )
    st_local_restaurante = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Local da ingestão - Restaurante/Bar/Lanchonete",
        help_text="Informa se a ingestão foi em restaurante, bar ou lanchonete.",
    )
    st_local_festa = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Local da ingestão - Festa",
        help_text="Informa se a ingestão foi em uma festa.",
    )
    st_local_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Local da ingestão - Outro",
        help_text="Informa se a ingestão foi em outro local não listado.",
    )
    ds_local_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Local da ingestão - Outro (especificar)",
        help_text="Especificação do local da ingestão quando outro = Sim.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - UF da ingestão
    # -------------------------------------------------------------------------

    co_uf_ingestao = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF da ingestão",
        help_text="Unidade Federada da ingestão do alimento suspeito.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Município da ingestão
    # -------------------------------------------------------------------------

    co_municipio_ingestao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município da ingestão",
        help_text="Código do município onde ingeriu o alimento suspeito.",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - Número de comensais
    # -------------------------------------------------------------------------

    nu_pessoa_consume_alimento = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Número de comensais",
        help_text="Número de pessoas que ingeriram o alimento suspeito.",
    )

    # -------------------------------------------------------------------------
    # Campo 57 - Tratamento
    # -------------------------------------------------------------------------

    st_trata_ventilatoria = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Assistência ventilatória",
        help_text="Informa se o paciente necessitou de assistência ventilatória (ventilação mecânica).",
    )
    st_trata_antibioticoterapia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Antibioticoterapia",
        help_text="Informa se o paciente foi tratado com antibiótico.",
    )
    st_trata_soro_antibutilinico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Soro antibotulínico",
        help_text="Informa se o paciente foi tratado com soro antibotulínico.",
    )
    st_trata_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outro tratamento",
        help_text="Informa se o paciente necessitou fazer outro tipo de tratamento.",
    )
    ds_trata_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro tratamento (especificar)",
        help_text="Descrição de outro tipo de tratamento (ex. traqueostomia).",
    )

    # -------------------------------------------------------------------------
    # Campo 58 - Data da administração do soro
    # -------------------------------------------------------------------------

    dt_soro_antibutilinico = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da administração do soro",
        help_text="Data da administração do soro antibotulínico. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 59 - Soro foi após coleta de material clínico?
    # -------------------------------------------------------------------------

    st_antibutilinico_coleta = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Soro foi após coleta de material clínico?",
        help_text="Informa se a administração do soro foi posterior à coleta de material clínico do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 60 - Coleta de materiais - Soro
    # -------------------------------------------------------------------------

    st_botuli_soro_coletado = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Material coletado - Soro",
        help_text="Informa se foi coletado soro do paciente.",
    )
    dt_botuli_soro_coleta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Soro",
        help_text="Data da coleta do soro. Deve ser >= data do 1º atendimento.",
    )
    st_botuli_soro_resultado = models.CharField(
        max_length=1,
        choices=ResultadoToxina.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Soro",
        help_text="Resultado da análise do soro do paciente.",
    )
    tp_botuli_soro_toxina = models.CharField(
        max_length=1,
        choices=TipoToxina.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de toxina - Soro",
        help_text="Tipo de toxina botulínica presente no soro.",
    )

    # -------------------------------------------------------------------------
    # Campo 60 - Coleta de materiais - Fezes
    # -------------------------------------------------------------------------

    st_botuli_fezes_coletado = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Material coletado - Fezes",
        help_text="Informa se foi coletado fezes do paciente.",
    )
    dt_botuli_fezes_coleta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Fezes",
        help_text="Data da coleta das fezes. Deve ser >= data do 1º atendimento.",
    )
    st_botuli_fezes_resultado = models.CharField(
        max_length=1,
        choices=ResultadoToxina.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Fezes",
        help_text="Resultado da análise das fezes do paciente.",
    )
    tp_botuli_fezes_toxina = models.CharField(
        max_length=1,
        choices=TipoToxina.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de toxina - Fezes",
        help_text="Tipo de toxina botulínica presente nas fezes.",
    )

    # -------------------------------------------------------------------------
    # Campo 60 - Coleta de materiais - Alimento 1
    # -------------------------------------------------------------------------

    st_botuli_alimento1_coletado = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Material coletado - Alimento 1",
        help_text="Informa se foi coletado alimento suspeito 1 para análise.",
    )
    ds_botuli_alimento1_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Especificação - Alimento 1",
        help_text="Especificação do alimento suspeito 1.",
    )
    dt_botuli_alimento1_coleta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Alimento 1",
        help_text="Data da coleta do alimento 1. Deve ser >= data do 1º atendimento.",
    )
    st_botuli_alimento1_resultado = models.CharField(
        max_length=1,
        choices=ResultadoToxina.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Alimento 1",
        help_text="Resultado da análise do alimento 1.",
    )
    tp_botuli_alimento1_toxina = models.CharField(
        max_length=1,
        choices=TipoToxina.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de toxina - Alimento 1",
        help_text="Tipo de toxina botulínica presente no alimento 1.",
    )

    # -------------------------------------------------------------------------
    # Campo 60 - Coleta de materiais - Alimento 2
    # -------------------------------------------------------------------------

    st_botuli_alimento2_coletado = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Material coletado - Alimento 2",
        help_text="Informa se foi coletado alimento suspeito 2 para análise.",
    )
    ds_botuli_alimento2_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Especificação - Alimento 2",
        help_text="Especificação do alimento suspeito 2.",
    )
    dt_botuli_alimento2_coleta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Alimento 2",
        help_text="Data da coleta do alimento 2. Deve ser >= data do 1º atendimento.",
    )
    st_botuli_alimento2_resultado = models.CharField(
        max_length=1,
        choices=ResultadoToxina.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Alimento 2",
        help_text="Resultado da análise do alimento 2.",
    )
    tp_botuli_alimento2_toxina = models.CharField(
        max_length=1,
        choices=TipoToxina.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de toxina - Alimento 2",
        help_text="Tipo de toxina botulínica presente no alimento 2.",
    )

    # -------------------------------------------------------------------------
    # Campo 60 - Coleta de materiais - Outros
    # -------------------------------------------------------------------------

    tp_botuli_coletado_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Material coletado - Outros",
        help_text="Informa se houve coleta de outro alimento ou material clínico.",
    )
    ds_botuli_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Especificação - Outros materiais",
        help_text="Especificação do outro material coletado.",
    )
    dt_botuli_coleta_outro = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Outros materiais",
        help_text="Data da coleta do outro material. Deve ser >= data do 1º atendimento.",
    )
    tp_botuli_resultado_outro = models.CharField(
        max_length=1,
        choices=ResultadoToxina.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Outros materiais",
        help_text="Resultado da análise do outro material.",
    )
    tp_botuli_toxina_outro = models.CharField(
        max_length=1,
        choices=TipoToxina.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de toxina - Outros materiais",
        help_text="Tipo de toxina botulínica presente no outro material.",
    )

    # -------------------------------------------------------------------------
    # Campo 61 - Exames complementares - Líquor
    # -------------------------------------------------------------------------

    tp_liquor = models.CharField(
        max_length=1,
        choices=RealizadoNaoRealizado.choices,
        null=True,
        blank=True,
        verbose_name="Líquor coletado",
        help_text="Informa se líquor foi coletado.",
    )

    # -------------------------------------------------------------------------
    # Campo 62 - Data da coleta do líquor
    # -------------------------------------------------------------------------

    dt_liquor_coleta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta do líquor",
        help_text="Data da coleta do líquor. Deve ser >= data do 1º atendimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 63 - Número de células/mm³ (líquor)
    # -------------------------------------------------------------------------

    nu_liquor_celula = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name="Número de células/mm³",
        help_text="Número de células por mm³ no líquor.",
    )

    # -------------------------------------------------------------------------
    # Campo 64 - Proteínas mg% (líquor)
    # -------------------------------------------------------------------------

    nu_liquor_proteina = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name="Proteínas mg%",
        help_text="Quantidade de proteínas mg% no líquor.",
    )

    # -------------------------------------------------------------------------
    # Campo 65 - Eletroneuromiografia
    # -------------------------------------------------------------------------

    st_eletroneuromiografia = models.CharField(
        max_length=1,
        choices=RealizadoNaoRealizado.choices,
        null=True,
        blank=True,
        verbose_name="Eletroneuromiografia",
        help_text="Informa se houve exame complementar de eletroneuromiografia.",
    )

    # -------------------------------------------------------------------------
    # Campo 66 - Data da realização da eletroneuromiografia
    # -------------------------------------------------------------------------

    dt_eletroneuro_realizada = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da eletroneuromiografia",
        help_text="Data do exame de eletroneuromiografia. Deve ser >= data do 1º atendimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 67 - Neurocondução Sensitiva
    # -------------------------------------------------------------------------

    class Neuroconducao(models.TextChoices):
        NORMAL = '1', 'Normal'
        DIMINUICAO_AMPLITUDE = '2', 'Diminuição de amplitude'
        LENTIFICACOES = '3', 'Lentificações'

    tp_eletroneuro_sensitiva = models.CharField(
        max_length=1,
        choices=Neuroconducao.choices,
        null=True,
        blank=True,
        verbose_name="Neurocondução sensitiva",
        help_text="Resultado da neurocondução sensitiva.",
    )

    # -------------------------------------------------------------------------
    # Campo 68 - Neurocondução Motora
    # -------------------------------------------------------------------------

    tp_eletroneuro_motora = models.CharField(
        max_length=1,
        choices=Neuroconducao.choices,
        null=True,
        blank=True,
        verbose_name="Neurocondução motora",
        help_text="Resultado da neurocondução motora.",
    )

    # -------------------------------------------------------------------------
    # Campo 69 - Estimulação repetitiva
    # -------------------------------------------------------------------------

    class EstimulacaoRepetitiva(models.TextChoices):
        NORMAL = '1', 'Normal'
        DECREMENTO = '2', 'Decremento (freq baixa)'
        INCREMENTO = '3', 'Incremento (freq alta)'

    tp_eletroneuro_repetitiva = models.CharField(
        max_length=1,
        choices=EstimulacaoRepetitiva.choices,
        null=True,
        blank=True,
        verbose_name="Estimulação repetitiva",
        help_text="Resultado da estimulação repetitiva.",
    )

    # -------------------------------------------------------------------------
    # Campo 70 - Classificação final
    # -------------------------------------------------------------------------

    class ClassificacaoFinal(models.TextChoices):
        CONFIRMADO = '1', 'Confirmado'
        DESCARTADO = '2', 'Descartado (especificar outro agente)'

    tp_classificacao_final = models.CharField(
        max_length=1,
        choices=ClassificacaoFinal.choices,
        null=True,
        blank=True,
        verbose_name="Classificação final",
        help_text="Informa se o caso foi confirmado ou descartado.",
    )

    # -------------------------------------------------------------------------
    # Campo 70 - Especificação se descartado
    # -------------------------------------------------------------------------

    ds_classificacao_final = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Especificação (agente)",
        help_text="Especificar outro agente se descartado.",
    )

    # -------------------------------------------------------------------------
    # Campo 71 - Critério de confirmação/descarte
    # -------------------------------------------------------------------------

    class CriterioConfirmacao(models.TextChoices):
        LABORATORIAL = '1', 'Laboratorial'
        CLINICO_EPIDEMIOLOGICO = '2', 'Clínico-epidemiológico'

    tp_criterio_confirmacao = models.CharField(
        max_length=1,
        choices=CriterioConfirmacao.choices,
        null=True,
        blank=True,
        verbose_name="Critério de confirmação/descarte",
        help_text="Critério em que o caso foi confirmado ou descartado.",
    )

    # -------------------------------------------------------------------------
    # Campo 72 - Forma de botulismo
    # -------------------------------------------------------------------------

    class FormaBotulismo(models.TextChoices):
        ALIMENTAR = '1', 'Alimentar'
        INTESTINAL = '2', 'Intestinal'
        POR_FERIMENTO = '3', 'Por ferimento'
        OUTRA = '4', 'Outra'

    tp_botulismo = models.CharField(
        max_length=1,
        choices=FormaBotulismo.choices,
        null=True,
        blank=True,
        verbose_name="Forma de botulismo",
        help_text="Forma de transmissão do botulismo.",
    )

    # -------------------------------------------------------------------------
    # Campo 73 - Presença de toxina botulínica na amostra
    # -------------------------------------------------------------------------

    st_botulonica_clinica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Toxina na amostra clínica",
        help_text="Informa se houve isolamento de toxina botulínica na amostra clínica.",
    )
    st_botulonica_bromatologica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Toxina na amostra bromatológica",
        help_text="Informa se houve isolamento de toxina botulínica na amostra bromatológica.",
    )

    # -------------------------------------------------------------------------
    # Campo 74 - Tipo de toxina isolada
    # -------------------------------------------------------------------------

    tp_tox_isolada_clinica = models.CharField(
        max_length=1,
        choices=TipoToxina.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de toxina - Amostra clínica",
        help_text="Tipo de toxina botulínica na amostra clínica.",
    )
    tp_tox_isolada_bromatologica = models.CharField(
        max_length=1,
        choices=TipoToxina.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de toxina - Amostra bromatológica",
        help_text="Tipo de toxina botulínica na amostra bromatológica.",
    )

    # -------------------------------------------------------------------------
    # Campo 75 - Causa/alimento incriminado
    # -------------------------------------------------------------------------

    ds_causa = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Causa/alimento incriminado",
        help_text="Causa do botulismo (ex. ferimento) e/ou alimento incriminado ou potencialmente suspeito.",
    )

    # -------------------------------------------------------------------------
    # Campo 76 - Doença relacionada ao trabalho
    # -------------------------------------------------------------------------

    st_doenca_trabalho = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Doença relacionada ao trabalho",
        help_text="Informa se o paciente adquiriu a doença em decorrência das condições/situação do trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 77 - Evolução do Caso
    # -------------------------------------------------------------------------

    class EvolucaoCaso(models.TextChoices):
        CURA = '1', 'Cura'
        OBITO_BOTULISMO = '2', 'Óbito por botulismo'
        OBITO_OUTRAS_CAUSAS = '3', 'Óbito por outras causas'
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
    # Campo 78 - Data do óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 79 - Data do encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento",
        help_text="Data de encerramento da investigação. Deve ser >= data da investigação.",
    )

    # -------------------------------------------------------------------------
    # Informações complementares (campos extras do dicionário)
    # -------------------------------------------------------------------------

    ds_tp_alimento_1 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Tipo de alimento 1",
        help_text="Alimento potencialmente suspeito, ingerido nos últimos 10 dias anteriores ao início dos sintomas.",
    )
    ds_tp_alimento_2 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Tipo de alimento 2",
        help_text="Alimento potencialmente suspeito, ingerido nos últimos 10 dias anteriores ao início dos sintomas.",
    )
    ds_local_consumo_1 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Local de consumo 1",
        help_text="Local de consumo do alimento potencialmente suspeito.",
    )
    ds_local_consumo_2 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Local de consumo 2",
        help_text="Local de consumo do alimento potencialmente suspeito.",
    )
    ds_observacao = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Observações",
        help_text="Informações adicionais a respeito do caso.",
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
        db_table = 'botulismo'
        verbose_name = 'Botulismo'
        verbose_name_plural = 'Botulismos'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Botulismo – {self.dt_investigacao}"