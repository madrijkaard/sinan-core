from django.db import models


class Hantavirose(models.Model):
    """
    Ficha de Investigação - Hantavirose
    Dicionário de Dados SINAN NET - Versão 5.0
    Revisado em julho/2010
    Campos 31 a 69 + campos de controle
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

    class ResultadoExame(models.TextChoices):
        REAGENTE = '1', 'Reagente'
        NAO_REAGENTE = '2', 'Não reagente'
        INCONCLUSIVO = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'

    class ClassificacaoFinal(models.TextChoices):
        CONFIRMADO = '1', 'Confirmado'
        DESCARTADO = '2', 'Descartado'

    class FormaClinica(models.TextChoices):
        PRODROMICA_INESPECIFICA = '1', 'Prodrômica ou inespecífica'
        SINDROME_CARDIOPULMONAR = '2', 'Síndrome cardiopulmonar por hantavírus'

    class CriterioDiagnostico(models.TextChoices):
        LABORATORIAL = '1', 'Laboratorial'
        CLINICO_EPIDEMIOLOGICO = '2', 'Clínico-Epidemiológico'

    class Autoctone(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        INDETERMINADO = '3', 'Indeterminado'

    class EvolucaoCaso(models.TextChoices):
        CURA = '1', 'Cura'
        OBITO_HANTAVIROSE = '2', 'Óbito por hantavirose'
        OBITO_OUTRA_CAUSA = '3', 'Óbito por outra causa'
        IGNORADO = '9', 'Ignorado'

    # -------------------------------------------------------------------------
    # Campo 31 - Data da investigação
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
    # Campo 33 - Atividades de risco (8 subcampos)
    # -------------------------------------------------------------------------

    st_atividade_treinamento = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Treinamento militar em parques, área rural ou silvestre",
        help_text="Nas últimas 8 semanas, desenvolveu ou expôs-se a esta atividade.",
    )
    st_atividade_desmatamento = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Desmatamento, plantio agrícola",
        help_text="Nas últimas 8 semanas, desenvolveu ou expôs-se a esta atividade.",
    )
    st_atividade_exposicao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição a casa abandonada, depósito, porão",
        help_text="Nas últimas 8 semanas, desenvolveu ou expôs-se a esta atividade.",
    )
    st_atividade_moagem = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Moagem/armazenamento de grãos, fardos de lenha",
        help_text="Nas últimas 8 semanas, desenvolveu ou expôs-se a esta atividade.",
    )
    st_atividade_barraca = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Dormiu em barraca, galpão, paiol",
        help_text="Nas últimas 8 semanas, desenvolveu ou expôs-se a esta atividade.",
    )
    st_atividade_transporte = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Transporte/carregamento de cargas",
        help_text="Nas últimas 8 semanas, desenvolveu ou expôs-se a esta atividade.",
    )
    st_atividade_pesca = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pescou, caçou ou ecoturismo",
        help_text="Nas últimas 8 semanas, desenvolveu ou expôs-se a esta atividade.",
    )
    st_atividade_contato_rato = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Contato com rato ou vestígios",
        help_text="Teve contato direto e/ou viu rato vivo ou morto ou suas excretas/vestígios.",
    )
    st_atividade_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outras atividades/exposições",
        help_text="Outras atividades de risco não listadas.",
    )
    ds_atividade_outro = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Outras atividades (especificar)",
        help_text="Especificação de outras atividades de risco.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Data do 1º atendimento
    # -------------------------------------------------------------------------

    dt_atendimento_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do 1º atendimento",
        help_text="Data do primeiro atendimento do paciente. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Local do 1º atendimento
    # -------------------------------------------------------------------------

    no_local_atendimento_1 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Local do 1º atendimento",
        help_text="Local do primeiro atendimento do paciente (US ou Clínica ou Hospital – Município/UF).",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Manifestações clínicas (22 subcampos)
    # -------------------------------------------------------------------------

    st_manifestacao_febre = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Febre",
        help_text="Se o paciente apresentou febre.",
    )
    st_manifestacao_tosse_seca = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Tosse seca",
        help_text="Se o paciente apresentou tosse seca.",
    )
    st_manifestacao_dispneia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Dispnéia",
        help_text="Se o paciente apresentou dispnéia.",
    )
    st_manifestacao_insuf_respira = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Insuficiência Respiratória Aguda",
        help_text="Se o paciente apresentou insuficiência respiratória/SARA.",
    )
    st_manifestacao_cefaleia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Cefaléia",
        help_text="Se o paciente apresentou cefaléia.",
    )
    st_manifestacao_mialgia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Mialgia generalizada",
        help_text="Se o paciente apresentou mialgia.",
    )
    st_manifestacao_dor_lombar = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Dor lombar",
        help_text="Se o paciente apresentou dor lombar.",
    )
    st_manifestacao_dor_abdominal = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Dor abdominal",
        help_text="Se o paciente apresentou dor abdominal.",
    )
    st_manifestacao_hipotensao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Hipotensão",
        help_text="Se o paciente apresentou hipotensão.",
    )
    st_manifestacao_choque = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Choque",
        help_text="Se o paciente apresentou choque.",
    )
    st_manifestacao_nausea = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Náusea/vômito",
        help_text="Se o paciente apresentou náusea/vômitos.",
    )
    st_manifestacao_diarreia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Diarréia",
        help_text="Se o paciente apresentou diarréia.",
    )
    st_manifestacao_dor_toracica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Dor torácica",
        help_text="Se o paciente apresentou dor torácica.",
    )
    st_manifestacao_tontura = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Tontura/vertigem",
        help_text="Se o paciente apresentou tontura/vertigens.",
    )
    st_manifestacao_insuf_cardiaca = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Insuficiência cardíaca",
        help_text="Se o paciente apresentou insuficiência cardíaca.",
    )
    st_manifestacao_insuf_renal = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Insuficiência renal",
        help_text="Se o paciente apresentou insuficiência renal.",
    )
    st_manifestacao_sintoma_neuro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Sintomas neurológicos",
        help_text="Se o paciente apresentou sintomas neurológicos.",
    )
    st_manifestacao_astenia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Astenia",
        help_text="Se o paciente apresentou astenia.",
    )
    st_manifestacao_petequias = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Petéquias",
        help_text="Se o paciente apresentou petéquias.",
    )
    st_manifestacao_hemor_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outras manifestações hemorrágicas",
        help_text="Se o paciente apresentou outras manifestações hemorrágicas.",
    )
    ds_manifestacao_hemor_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Manifestações hemorrágicas (especificar)",
        help_text="Especificação de outras manifestações hemorrágicas.",
    )
    st_manifestacao_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outras manifestações clínicas",
        help_text="Se o paciente apresentou outras manifestações clínicas.",
    )
    ds_manifestacao_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outras manifestações (especificar)",
        help_text="Especificação de outras manifestações clínicas.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Colheu amostra de sangue para exames clínicos/bioquímicos
    # -------------------------------------------------------------------------

    st_amostra_sangue = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Colheu amostra de sangue",
        help_text="Se foi colhida amostra de sangue para exames clínicos/bioquímicos.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Resultados A (6 subcampos)
    # -------------------------------------------------------------------------

    st_resultado_hematocrito = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Hematócrito > 45%",
        help_text="Resultado do exame de hematócrito.",
    )
    st_resultado_trombocitopenia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Trombocitopenia",
        help_text="Resultado do exame de trombocitopenia.",
    )
    st_resultado_linfocito = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Linfócitos atípicos",
        help_text="Resultado do exame de linfócitos atípicos.",
    )
    st_resultado_aumento = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Aumento de ureia e creatinina",
        help_text="Resultado do exame de ureia e creatinina.",
    )
    st_resultado_tgo = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="TGO",
        help_text="Resultado do exame de TGO.",
    )
    ds_resultado_tgo = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="TGO (especificar)",
        help_text="Especificação do resultado de TGO quando positivo.",
    )
    st_resultado_tgp = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="TGP",
        help_text="Resultado do exame de TGP.",
    )
    ds_resultado_tgp = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="TGP (especificar)",
        help_text="Especificação do resultado de TGP quando positivo.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Resultado B (Leucócitos)
    # -------------------------------------------------------------------------

    class ResultadoLeucocitos(models.TextChoices):
        NORMAIS = '1', 'Normais'
        AUMENTADOS_COM_DESVIO = '2', 'Aumentados com desvio à esquerda'
        DIMINUIDOS = '3', 'Diminuídos (Leucopenia)'
        AUMENTADOS_SEM_DESVIO = '4', 'Aumentados sem desvio à esquerda'
        NAO_REALIZADO = '5', 'Não realizado'
        IGNORADO = '9', 'Ignorado'

    tp_resultado_b = models.CharField(
        max_length=1,
        choices=ResultadoLeucocitos.choices,
        null=True,
        blank=True,
        verbose_name="Resultado B - Leucócitos",
        help_text="Resultado do exame de leucócitos.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Realizou radiografia do tórax
    # -------------------------------------------------------------------------

    st_radiografia_torax = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Realizou radiografia do tórax",
        help_text="Se o paciente realizou radiografia do tórax.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Alterações radiológicas (4 subcampos)
    # -------------------------------------------------------------------------

    st_alteracao_difuso = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Infiltrado pulmonar difuso",
        help_text="Se o exame radiológico apresentou este resultado.",
    )
    st_alteracao_localizado = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Infiltrado pulmonar localizado",
        help_text="Se o exame radiológico apresentou este resultado.",
    )
    st_alteracao_pleural = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Derrame pleural",
        help_text="Se o exame radiológico apresentou este resultado.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Data da coleta do IgM
    # -------------------------------------------------------------------------

    dt_coleta_sorologia = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta do IgM",
        help_text="Data da coleta da amostra de IgM. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Resultado IgM
    # -------------------------------------------------------------------------

    tp_resultado_igm = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado IgM",
        help_text="Resultado do exame de IgM.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Resultado Imunohistoquímica
    # -------------------------------------------------------------------------

    tp_resultado_imunohistoquimica = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado imunohistoquímica",
        help_text="Resultado do exame de imunohistoquímica.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Data da coleta do RT-PCR
    # -------------------------------------------------------------------------

    dt_coleta_sangue = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta do RT-PCR",
        help_text="Data da coleta da amostra do RT-PCR. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Resultado RT-PCR
    # -------------------------------------------------------------------------

    tp_resultado_rt_pcr = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado RT-PCR",
        help_text="Resultado do exame de RT-PCR.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Ocorreu Hospitalização
    # -------------------------------------------------------------------------

    st_ocorreu_hospitalizacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Ocorreu hospitalização",
        help_text="Se o paciente foi hospitalizado.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Data da internação
    # -------------------------------------------------------------------------

    dt_internacao = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da internação",
        help_text="Data da internação. Deve ser >= data dos primeiros sintomas e >= data do 1º atendimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - UF do hospital
    # -------------------------------------------------------------------------

    co_uf_hospital = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF do hospital",
        help_text="Sigla da unidade federada onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Município do hospital
    # -------------------------------------------------------------------------

    co_municipio_hospital = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município do hospital",
        help_text="Código do município onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Nome do Hospital
    # -------------------------------------------------------------------------

    co_unidade_hospital = models.DecimalField(
        max_digits=8,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Código do hospital",
        help_text="Código da unidade hospitalar onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Suporte Terapêutico (7 subcampos)
    # -------------------------------------------------------------------------

    st_terapeutico_respirador = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Respirador mecânico",
        help_text="Se o paciente ficou no respirador mecânico.",
    )
    st_terapeutico_antiviral = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Medicamento antiviral (Ribavirina)",
        help_text="Se o paciente usou antiviral.",
    )
    st_terapeutico_corticoide = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Corticóide",
        help_text="Se o paciente usou corticóide.",
    )
    st_terapeutico_cpap = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="CPAP/BIPAP",
        help_text="Se o paciente usou CPAP/BIPAP.",
    )
    st_terapeutico_droga = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Drogas vasoativas",
        help_text="Se o paciente usou drogas vasoativas (dopamina, dobutamina ou similares).",
    )
    st_terapeutico_antibiotico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Antibióticos",
        help_text="Se o paciente usou antibióticos.",
    )
    st_terapeutico_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outro tipo de tratamento",
        help_text="Se o paciente recebeu outro tipo de tratamento.",
    )
    ds_terapeutico_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro tratamento (especificar)",
        help_text="Especificação de outro tipo de tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Classificação final
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
    # Campo 54 - Forma clínica
    # -------------------------------------------------------------------------

    st_forma_clinica = models.CharField(
        max_length=1,
        choices=FormaClinica.choices,
        null=True,
        blank=True,
        verbose_name="Forma clínica",
        help_text="Forma clínica da hantavirose. Obrigatório se classificação final = Confirmado.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Critério Diagnóstico
    # -------------------------------------------------------------------------

    st_criterio_diagnostico = models.CharField(
        max_length=1,
        choices=CriterioDiagnostico.choices,
        null=True,
        blank=True,
        verbose_name="Critério diagnóstico",
        help_text="Critério utilizado para confirmação ou descarte do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - O caso é Autóctone de residência?
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
    # Campo 57 - UF (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_uf_infeccao = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF provável da infecção",
        help_text="Unidade Federada onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 58 - País (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_pais_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="País provável da infecção",
        help_text="País onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 59 - Município (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_municipio_infeccao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município provável da infecção",
        help_text="Código do município onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 60 - Distrito (provável de infecção)
    # -------------------------------------------------------------------------

    co_distrito_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Distrito provável da infecção",
        help_text="Código do distrito provável de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 61 - Bairro (provável de infecção)
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
    # Campo 62 - Zona do Provável local de infecção
    # -------------------------------------------------------------------------

    class ZonaInfeccao(models.TextChoices):
        URBANA = '1', 'Urbana'
        RURAL = '2', 'Rural'
        PERI_URBANA = '3', 'Peri-urbana'
        IGNORADO = '9', 'Ignorado'

    tp_zona_infeccao = models.CharField(
        max_length=1,
        choices=ZonaInfeccao.choices,
        null=True,
        blank=True,
        verbose_name="Zona do local provável de infecção",
        help_text="Caracterização da zona do local provável de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 63 - Tipo de Ambiente onde provavelmente ocorreu a infecção
    # -------------------------------------------------------------------------

    class AmbienteInfeccao(models.TextChoices):
        DOMICILIAR = '1', 'Domiciliar'
        TRABALHO = '2', 'Trabalho'
        LAZER = '3', 'Lazer'
        OUTRO = '4', 'Outro'
        IGNORADO = '9', 'Ignorado'

    tp_ambiente_infeccao = models.CharField(
        max_length=1,
        choices=AmbienteInfeccao.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de ambiente",
        help_text="Tipo de ambiente onde provavelmente ocorreu a infecção.",
    )
    ds_ambiente_infeccao_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro ambiente (especificar)",
        help_text="Especificação quando ambiente = 4 (Outro).",
    )

    # -------------------------------------------------------------------------
    # Campo 64 - Localização do LPI em relação à Sede do Município
    # -------------------------------------------------------------------------

    nu_localizacao_lpi = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Distância da Sede do Município (km)",
        help_text="Distância em quilômetros da sede do município.",
    )

    class DirecaoLocalizacao(models.TextChoices):
        SUL = '1', 'Sul'
        NORTE = '2', 'Norte'
        LESTE = '3', 'Leste'
        OESTE = '4', 'Oeste'

    tp_localizacao_lpi = models.CharField(
        max_length=1,
        choices=DirecaoLocalizacao.choices,
        null=True,
        blank=True,
        verbose_name="Direção do LPI",
        help_text="Localização/Direção do LPI em relação à sede do município.",
    )

    # -------------------------------------------------------------------------
    # Campo 65 - Evolução do caso
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
    # Campo 66 - Data do óbito ou da alta hospitalar
    # -------------------------------------------------------------------------

    dt_evolucao = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito ou alta hospitalar",
        help_text="Data do óbito ou da alta hospitalar. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 67 - Se óbito, realizou autópsia
    # -------------------------------------------------------------------------

    st_realizou_autopsia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Realizou autópsia",
        help_text="Se foi realizada autópsia.",
    )

    # -------------------------------------------------------------------------
    # Campo 68 - Doença relacionada ao trabalho
    # -------------------------------------------------------------------------

    st_doenca_trabalho = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Doença relacionada ao trabalho",
        help_text="Se o paciente adquiriu a doença em decorrência das condições/situação do trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 69 - Data do encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento",
        help_text="Data do encerramento da investigação. Deve ser >= data da investigação.",
    )

    # -------------------------------------------------------------------------
    # Observações
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
        db_table = 'hantavirose'
        verbose_name = 'Hantavirose'
        verbose_name_plural = 'Hantavirose'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Hantavirose – {self.dt_investigacao}"