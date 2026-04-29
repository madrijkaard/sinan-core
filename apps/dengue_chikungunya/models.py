from django.db import models


class DengueChikungunya(models.Model):
    """
    Ficha de Investigação - Dengue e Chikungunya
    Dicionário de Dados SINAN ONLINE
    Revisado em: 21/10/2015
    Campos 31 a 71 + campos de controle
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

    class SimNao(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'

    class SimNaoIgnorado(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        IGNORADO = '9', 'Ignorado'

    class ResultadoExame(models.TextChoices):
        REAGENTE = '1', 'Reagente'
        NAO_REAGENTE = '2', 'Não Reagente'
        INCONCLUSIVO = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'

    class ClassificacaoFinal(models.TextChoices):
        DESCARTADO = '5', 'Descartado'
        DENGUE = '10', 'Dengue'
        DENGUE_SINAIS_ALARME = '11', 'Dengue com sinais de alarme'
        DENGUE_GRAVE = '12', 'Dengue grave'
        CHIKUNGUNYA = '13', 'Chikungunya'

    class CriterioConfirmacao(models.TextChoices):
        LABORATORIO = '1', 'Laboratório'
        CLINICO_EPIDEMIOLOGICO = '2', 'Clínico Epidemiológico'
        EM_INVESTIGACAO = '3', 'Em investigação'

    class EvolucaoCaso(models.TextChoices):
        CURA = '1', 'Cura'
        OBITO_AGRAVO = '2', 'Óbito pelo agravo'
        OBITO_OUTRAS_CAUSAS = '3', 'Óbito por outras causas'
        OBITO_INVESTIGACAO = '4', 'Óbito em investigação'
        IGNORADO = '9', 'Ignorado'

    class ApresentacaoClinicaChik(models.TextChoices):
        AGUDA = '1', 'Aguda'
        CRONICA = '2', 'Crônica'

    class Autoctone(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        INDETERMINADO = '3', 'Indeterminado'

    # -------------------------------------------------------------------------
    # Campo 2 - Agravo/doença (primeiro campo do dicionário)
    # -------------------------------------------------------------------------

    class Agravo(models.TextChoices):
        DENGUE = '1', 'Dengue'
        CHIKUNGUNYA = '2', 'Chikungunya'

    tp_agravo = models.CharField(
        max_length=1,
        choices=Agravo.choices,
        verbose_name="Agravo/doença",
        help_text="Especifica a suspeição do agravo.",
    )

    # -------------------------------------------------------------------------
    # Campo 31 - Data da Investigação
    # -------------------------------------------------------------------------

    dt_investigacao = models.DateField(
        verbose_name="Data da investigação",
        help_text="Data da investigação. Não pode ser anterior à data de notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 32 - Ocupação/ramo de atividade econômica
    # -------------------------------------------------------------------------

    co_cbo_ocupacao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Ocupação (CBO)",
        help_text="Código CBO da ocupação exercida pelo paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 33 - Sinais clínicos (13 subcampos)
    # -------------------------------------------------------------------------

    st_febre = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Febre",
        help_text="Informa se o paciente apresentou febre.",
    )
    st_mialgia = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Mialgia",
        help_text="Informa se o paciente apresentou mialgia.",
    )
    st_cefaleia = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Cefaleia",
        help_text="Informa se o paciente apresentou cefaleia.",
    )
    st_exantema = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Exantema",
        help_text="Informa se o paciente apresentou exantema.",
    )
    st_vomito = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Vômito",
        help_text="Informa se o paciente apresentou vômito.",
    )
    st_nausea = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Náusea",
        help_text="Informa se o paciente apresentou náusea.",
    )
    st_dor_costas = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Dor nas costas",
        help_text="Informa se o paciente apresentou dor nas costas.",
    )
    st_conjuntivite = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Conjuntivite",
        help_text="Informa se o paciente apresentou conjuntivite.",
    )
    st_artrite = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Artrite",
        help_text="Informa se o paciente apresentou artrite.",
    )
    st_artralgia_intensa = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Artralgia intensa",
        help_text="Informa se o paciente apresentou artralgia intensa.",
    )
    st_petequias = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Petéquias",
        help_text="Informa se o paciente apresentou petéquias.",
    )
    st_leucopenia = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Leucopenia",
        help_text="Informa se o paciente apresentou leucopenia.",
    )
    st_laco = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Prova do laço",
        help_text="Informa se a prova do laço foi positiva.",
    )
    st_dor_retroorbital = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Dor retroorbital",
        help_text="Informa se o paciente apresentou dor retroorbital.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Doenças pré-existentes (7 subcampos)
    # -------------------------------------------------------------------------

    st_diabetes = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Diabetes",
        help_text="Informa se o paciente tem diabetes.",
    )
    st_hematologicas = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Doenças hematológicas",
        help_text="Informa se o paciente tem doenças hematológicas.",
    )
    st_hepatopatias = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Hepatopatias",
        help_text="Informa se o paciente tem hepatopatias.",
    )
    st_renal_cronica = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Doença renal crônica",
        help_text="Informa se o paciente tem doença renal crônica.",
    )
    st_hipertensao = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Hipertensão arterial",
        help_text="Informa se o paciente tem hipertensão arterial.",
    )
    st_acido_peptico = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Doença ácido-péptica",
        help_text="Informa se o paciente tem doença ácido-péptica.",
    )
    st_auto_imune = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        verbose_name="Doenças auto-imunes",
        help_text="Informa se o paciente tem doenças auto-imunes.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Exame sorológico (IgM) Chikungunya Soro 1
    # -------------------------------------------------------------------------

    dt_coleta_chik_s1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Chikungunya Soro 1 (IgM)",
        help_text="Data da coleta do exame sorológico (IgM) Chikungunya soro 1.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Exame sorológico (IgM) Chikungunya Soro 2
    # -------------------------------------------------------------------------

    dt_coleta_chik_s2 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Chikungunya Soro 2 (IgM)",
        help_text="Data da coleta do exame sorológico (IgM) Chikungunya soro 2.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Exame PRNT
    # -------------------------------------------------------------------------

    dt_coleta_prnt = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - PRNT",
        help_text="Data da coleta do exame PRNT.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Resultados dos exames Chikungunya e PRNT
    # -------------------------------------------------------------------------

    tp_result_chik_s1 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Chikungunya Soro 1 (IgM)",
        help_text="Resultado do exame sorológico (IgM) soro 1 para Chikungunya.",
    )
    tp_result_chik_s2 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Chikungunya Soro 2 (IgM)",
        help_text="Resultado do exame sorológico (IgM) soro 2 para Chikungunya.",
    )
    tp_result_prnt = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - PRNT",
        help_text="Resultado do exame PRNT.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Exame sorológico (IgM) Dengue - Data da Coleta
    # -------------------------------------------------------------------------

    dt_coleta_soro_dengue = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Dengue (IgM)",
        help_text="Data da coleta do exame sorológico (IgM) Dengue.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Exame sorológico (IgM) Dengue - Resultado
    # -------------------------------------------------------------------------

    tp_result_soro_dengue = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Dengue (IgM)",
        help_text="Resultado do exame sorológico (IgM) Dengue.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Exame NS1 - Data da Coleta
    # -------------------------------------------------------------------------

    dt_coleta_ns1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - NS1",
        help_text="Data da coleta do exame NS1 (Sorologia ELISA).",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Exame NS1 - Resultado
    # -------------------------------------------------------------------------

    class ResultadoNS1(models.TextChoices):
        POSITIVO = '1', 'Positivo'
        NEGATIVO = '2', 'Negativo'
        INCONCLUSIVO = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'

    tp_result_ns1 = models.CharField(
        max_length=1,
        choices=ResultadoNS1.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - NS1",
        help_text="Resultado do exame NS1 (Sorologia ELISA).",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Isolamento Viral
    # -------------------------------------------------------------------------

    dt_coleta_isolamento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Isolamento Viral",
        help_text="Data da coleta do isolamento viral.",
    )
    tp_result_isolamento = models.CharField(
        max_length=1,
        choices=ResultadoNS1.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Isolamento Viral",
        help_text="Resultado do exame de isolamento viral.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - RT-PCR (nota: campo 44 está pulado no dicionário)
    # -------------------------------------------------------------------------

    dt_coleta_rtpcr = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - RT-PCR",
        help_text="Data da coleta do exame de RT-PCR.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - RT-PCR Resultado
    # -------------------------------------------------------------------------

    tp_result_rtpcr = models.CharField(
        max_length=1,
        choices=ResultadoNS1.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - RT-PCR",
        help_text="Resultado do exame de RT-PCR.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Sorotipo
    # -------------------------------------------------------------------------

    class Sorotipo(models.TextChoices):
        DEN_1 = '1', 'DEN 1'
        DEN_2 = '2', 'DEN 2'
        DEN_3 = '3', 'DEN 3'
        DEN_4 = '4', 'DEN 4'

    tp_sorotipo = models.CharField(
        max_length=1,
        choices=Sorotipo.choices,
        null=True,
        blank=True,
        verbose_name="Sorotipo",
        help_text="Sorotipo do vírus Dengue identificado.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Histopatologia Resultado
    # -------------------------------------------------------------------------

    tp_result_histopatologia = models.CharField(
        max_length=1,
        choices=ResultadoNS1.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Histopatologia",
        help_text="Resultado do exame de histopatologia.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Imunohistoquímica Resultado
    # -------------------------------------------------------------------------

    tp_result_imunohistoquimica = models.CharField(
        max_length=1,
        choices=ResultadoNS1.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Imunohistoquímica",
        help_text="Resultado do exame de imunohistoquímica.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Ocorreu Hospitalização?
    # -------------------------------------------------------------------------

    st_ocorreu_hospitalizacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Ocorreu hospitalização",
        help_text="Informa se ocorreu hospitalização.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Data da Internação
    # -------------------------------------------------------------------------

    dt_internacao = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da internação",
        help_text="Data de internação do paciente. Habilitado se hospitalização = Sim.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - UF de Hospitalização
    # -------------------------------------------------------------------------

    co_uf_hospital = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de hospitalização",
        help_text="Sigla da UF onde o paciente foi hospitalizado.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Município do Hospital
    # -------------------------------------------------------------------------

    co_municipio_hospital = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município do hospital",
        help_text="Código do município onde o paciente foi hospitalizado.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Nome do Hospital
    # -------------------------------------------------------------------------

    co_unidade_hospital = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name="Código do hospital (CNES)",
        help_text="Código da unidade de saúde onde o paciente foi hospitalizado.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - (DDD) e Telefone do Hospital
    # -------------------------------------------------------------------------

    nu_ddd_hospital = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="DDD do hospital",
        help_text="Código DDD do telefone da unidade de saúde.",
    )
    nu_telefone_hospital = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Telefone do hospital",
        help_text="Telefone da unidade de saúde onde o paciente foi hospitalizado.",
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
    # Campo 62 - Classificação
    # -------------------------------------------------------------------------

    tp_classificacao_final = models.CharField(
        max_length=2,
        choices=ClassificacaoFinal.choices,
        null=True,
        blank=True,
        verbose_name="Classificação",
        help_text="Classificação final do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 63 - Critério de Confirmação/Descarte
    # -------------------------------------------------------------------------

    tp_criterio_confirmacao = models.CharField(
        max_length=1,
        choices=CriterioConfirmacao.choices,
        null=True,
        blank=True,
        verbose_name="Critério de confirmação/descarte",
        help_text="Critério utilizado para confirmação/descarte do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 64 - Apresentação clínica Chikungunya
    # -------------------------------------------------------------------------

    tp_apresentacao_clinica_chik = models.CharField(
        max_length=1,
        choices=ApresentacaoClinicaChik.choices,
        null=True,
        blank=True,
        verbose_name="Apresentação clínica - Chikungunya",
        help_text="Apresentação clínica do caso de Chikungunya (aguda ou crônica).",
    )

    # -------------------------------------------------------------------------
    # Campo 65 - Evolução do Caso
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
    # Campo 66 - Data do Óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito. Obrigatório se evolução = 2, 3 ou 4.",
    )

    # -------------------------------------------------------------------------
    # Campo 67 - Data do Encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento",
        help_text="Data do encerramento do caso. Obrigatório quando classificação preenchida e critério diferente de 3.",
    )

    # -------------------------------------------------------------------------
    # Campo 68 - Dengue com sinais de alarme (11 subcampos)
    # -------------------------------------------------------------------------

    st_alarme_hipotensao = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de alarme - Hipotensão",
        help_text="Informa se o paciente apresentou hipotensão.",
    )
    st_alarme_queda_plaquetas = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de alarme - Queda abrupta de plaquetas",
        help_text="Informa se o paciente apresentou queda abrupta de plaquetas.",
    )
    st_alarme_vomitos_persistentes = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de alarme - Vômitos persistentes",
        help_text="Informa se o paciente apresentou vômitos persistentes.",
    )
    st_alarme_dor_abdominal = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de alarme - Dor abdominal",
        help_text="Informa se o paciente apresentou dor abdominal intensa.",
    )
    st_alarme_letargia = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de alarme - Letargia ou irritabilidade",
        help_text="Informa se o paciente apresentou letargia ou irritabilidade.",
    )
    st_alarme_sangramento = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de alarme - Sangramento de mucosa/outras hemorragias",
        help_text="Informa se o paciente apresentou sangramento de mucosa ou outras hemorragias.",
    )
    st_alarme_aumento_hematocrito = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de alarme - Aumento do hematócrito",
        help_text="Informa se o paciente apresentou aumento do hematócrito.",
    )
    st_alarme_hepatomegalia = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de alarme - Hepatomegalia",
        help_text="Informa se o paciente apresentou hepatomegalia.",
    )
    st_alarme_acumulo_liquidos = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de alarme - Acúmulo de líquidos",
        help_text="Informa se o paciente apresentou acúmulo de líquidos.",
    )

    # -------------------------------------------------------------------------
    # Campo 69 - Data de início dos sintomas (sinais de alarme)
    # -------------------------------------------------------------------------

    dt_inicio_sinais_alarme = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de início dos sinais de alarme",
        help_text="Data do primeiro sinal de alarme manifestado.",
    )

    # -------------------------------------------------------------------------
    # Campo 70 - Dengue grave (13 subcampos)
    # -------------------------------------------------------------------------

    st_gravidade_pulso_debil = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - Pulso débil ou indetectável",
        help_text="Informa se o paciente apresentou pulso débil ou indetectável.",
    )
    st_gravidade_pa_convergente = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - PA convergente",
        help_text="Informa se o paciente apresentou pressão arterial convergente.",
    )
    st_gravidade_enchimento_capilar = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - Tempo de enchimento capilar",
        help_text="Informa se o paciente apresentou alteração no tempo de enchimento capilar.",
    )
    st_gravidade_insuf_respiratoria = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - Acúmulo de líquidos com insuficiência respiratória",
        help_text="Informa se o paciente apresentou acúmulo de líquidos com insuficiência respiratória.",
    )
    st_gravidade_taquicardia = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - Taquicardia",
        help_text="Informa se o paciente apresentou taquicardia.",
    )
    st_gravidade_extremidades_frias = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - Extremidades frias",
        help_text="Informa se o paciente apresentou extremidades frias.",
    )
    st_gravidade_hipotensao_tardia = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - Hipotensão arterial em fase tardia",
        help_text="Informa se o paciente apresentou hipotensão arterial em fase tardia.",
    )
    st_gravidade_hematemese = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - Hematêmese",
        help_text="Informa se o paciente apresentou hematêmese.",
    )
    st_gravidade_melena = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - Melena",
        help_text="Informa se o paciente apresentou melena.",
    )
    st_gravidade_metrorragia = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - Metrorragia volumosa",
        help_text="Informa se o paciente apresentou metrorragia volumosa.",
    )
    st_gravidade_sangramento_snc = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - Sangramento do SNC",
        help_text="Informa se o paciente apresentou sangramento do sistema nervoso central.",
    )
    st_gravidade_ast_alt = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - AST/ALT > 1.000",
        help_text="Informa se o paciente apresentou AST/ALT maior que 1.000.",
    )
    st_gravidade_miocardite = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - Miocardite",
        help_text="Informa se o paciente apresentou miocardite.",
    )
    st_gravidade_alteracao_consciencia = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - Alteração da consciência",
        help_text="Informa se o paciente apresentou alteração da consciência.",
    )
    st_gravidade_outros_orgaos = models.CharField(
        max_length=1,
        choices=SimNao.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de gravidade - Outros órgãos",
        help_text="Informa se o paciente apresentou comprometimento de outros órgãos.",
    )

    # -------------------------------------------------------------------------
    # Campo 71 - Data de início dos sintomas (Dengue grave)
    # -------------------------------------------------------------------------

    dt_inicio_sinais_gravidade = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de início dos sintomas de Dengue grave",
        help_text="Data do primeiro sinal de gravidade manifestado.",
    )

    # -------------------------------------------------------------------------
    # Observações adicionais
    # -------------------------------------------------------------------------

    ds_observacao = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Observações",
        help_text="Informações complementares e observações adicionais a respeito do caso.",
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
        db_table = 'dengue_chikungunya'
        verbose_name = 'Dengue / Chikungunya'
        verbose_name_plural = 'Dengue / Chikungunya'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] {self.get_tp_agravo_display()} – {self.dt_investigacao}"