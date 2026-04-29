from django.db import models


class DoencaChagas(models.Model):
    """
    Ficha de Investigação - Doença de Chagas
    Dicionário de Dados SINAN NET - Versão 5.0
    Revisado em Julho/2010
    Campos 31 a 70 + campos de controle
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

    class SimNaoNaoRealizadoIgnorado(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        NAO_REALIZADO = '3', 'Não realizado'
        IGNORADO = '9', 'Ignorado'

    class ResultadoExame(models.TextChoices):
        POSITIVO = '1', 'Positivo'
        NEGATIVO = '2', 'Negativo'
        NAO_REALIZADO = '3', 'Não realizado'
        IGNORADO = '9', 'Ignorado'

    class ResultadoSorologia(models.TextChoices):
        REAGENTE = '1', 'Reagente'
        NAO_REAGENTE = '2', 'Não reagente'
        INCONCLUSIVO = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'

    # -------------------------------------------------------------------------
    # Campo 31 - Data da investigação
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
    # Campo 33 - Deslocamento UF 1, Município 1; UF 2, Município 2; UF 3, Município 3
    # -------------------------------------------------------------------------

    co_uf_desloca_1 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Deslocamento - UF 1",
        help_text="UF de deslocamento no período de 15 meses anteriores ao início dos sintomas.",
    )
    co_municipio_desloca_1 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Deslocamento - Município 1",
        help_text="Município de deslocamento no período de 15 meses anteriores ao início dos sintomas.",
    )
    co_uf_desloca_2 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Deslocamento - UF 2",
        help_text="UF de deslocamento no período de 15 meses anteriores ao início dos sintomas.",
    )
    co_municipio_desloca_2 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Deslocamento - Município 2",
        help_text="Município de deslocamento no período de 15 meses anteriores ao início dos sintomas.",
    )
    co_uf_desloca_3 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Deslocamento - UF 3",
        help_text="UF de deslocamento no período de 15 meses anteriores ao início dos sintomas.",
    )
    co_municipio_desloca_3 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Deslocamento - Município 3",
        help_text="Município de deslocamento no período de 15 meses anteriores ao início dos sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Presença de vestígios de triatomídeos Intra-Domicílio
    # -------------------------------------------------------------------------

    class PresencaVestigios(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        NAO_REALIZADO = '3', 'Não realizado'
        IGNORADO = '9', 'Ignorado'

    tp_presenca_triatomideos = models.CharField(
        max_length=1,
        choices=PresencaVestigios.choices,
        verbose_name="Presença de vestígios de triatomídeos intra-domicílio",
        help_text="Presença de vestígios de triatomídeos intra-domicílio.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Data do encontro dos vestígios
    # -------------------------------------------------------------------------

    dt_encontro_parasito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encontro dos vestígios",
        help_text="Data do encontro do parasito. Habilitado se campo 34 = 1 (Sim).",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - História de uso de sangue ou hemoderivados nos últimos 120 dias
    # -------------------------------------------------------------------------

    st_uso_sangue_hemoderivados = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="História de uso de sangue ou hemoderivados",
        help_text="História de uso de sangue ou hemoderivados nos últimos 120 dias.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Existência de controle sorológico na Unidade de Hemoterapia
    # -------------------------------------------------------------------------

    st_controle_sorologico = models.CharField(
        max_length=1,
        choices=SimNaoNaoSeAplicaIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Controle sorológico na unidade de hemoterapia",
        help_text="Existência de controle sorológico na unidade de hemoterapia onde o paciente fez uso de sangue ou hemoderivados.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Manipulação de Material com T. Cruzi
    # -------------------------------------------------------------------------

    tp_manipulacao_tcruzi = models.CharField(
        max_length=1,
        choices=SimNaoNaoSeAplicaIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Manipulação de material com T. Cruzi",
        help_text="Se o paciente manipulou material com Trypanosoma cruzi.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Menor ou igual a 9 meses de idade: Mãe com infecção chagásica
    # -------------------------------------------------------------------------

    tp_recem_nascido = models.CharField(
        max_length=1,
        choices=SimNaoNaoSeAplicaIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Mãe com infecção chagásica",
        help_text="Se o recém-nascido é filho de mãe com infecção chagásica.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Possibilidade de transmissão por via oral
    # -------------------------------------------------------------------------

    st_transmissao_oral = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Possibilidade de transmissão por via oral",
        help_text="Possibilidade de transmissão por via oral.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Sinais e sintomas (12 subcampos)
    # -------------------------------------------------------------------------

    st_sinais_assintomatico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Assintomático",
        help_text="Se o paciente é assintomático. Se sim, pular para campo 42.",
    )
    st_sinais_edema = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Edema",
        help_text="Se o paciente apresentou edema.",
    )
    st_sinais_meningoencefalite = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Sinais de meningoencefalite",
        help_text="Se o paciente apresentou meningoencefalite.",
    )
    st_sinais_poliadenopatia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Poliadenopatia",
        help_text="Se o paciente apresentou poliadenopatia.",
    )
    st_sinais_febre_persistente = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Febre persistente",
        help_text="Se o paciente apresentou febre persistente.",
    )
    st_sinais_hepatomegalia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Hepatomegalia",
        help_text="Se o paciente apresentou hepatomegalia.",
    )
    st_sinais_icc = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Sinais de ICC",
        help_text="Se o paciente apresentou sinais de Insuficiência Cardíaca Congestiva.",
    )
    st_sinais_taquicardia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Taquicardia persistente",
        help_text="Se o paciente apresentou taquicardia persistente.",
    )
    st_sinais_astenia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Astenia",
        help_text="Se o paciente apresentou astenia.",
    )
    st_sinais_esplenomegalia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Esplenomegalia",
        help_text="Se o paciente apresentou esplenomegalia.",
    )
    st_sinais_chagoma = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Chagoma de inoculação",
        help_text="Se o paciente apresentou chagoma de inoculação (sinal de Romana ou outro).",
    )
    st_sinal_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outros sinais/sintomas",
        help_text="Se o paciente apresentou outros sinais e sintomas.",
    )
    ds_sinal_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outros sinais/sintomas (especificar)",
        help_text="Especificação de outros sinais e sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Exames Realizados - Parasitológico Direto - Data da Coleta
    # -------------------------------------------------------------------------

    dt_coleta_parasita_direto = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Parasitológico Direto",
        help_text="Data de coleta do material para exame parasitológico direto.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Exames Realizados - Parasitológico Direto (3 subcampos)
    # -------------------------------------------------------------------------

    tp_parasitologico_fresco = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Parasitológico - Exame a fresco",
        help_text="Resultado do exame parasitológico a fresco.",
    )
    tp_parasitologico_hematocrito = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Parasitológico - Micro-hematócrito/QBC",
        help_text="Resultado do exame parasitológico micro-hematócrito/QBC.",
    )
    tp_parasitologico_outro = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Parasitológico - Outro",
        help_text="Resultado de outro exame parasitológico.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Exames Realizados - Parasitológico Indireto - Data da Coleta
    # -------------------------------------------------------------------------

    dt_coleta_parasita_indireto = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Parasitológico Indireto",
        help_text="Data de coleta do material para exame parasitológico indireto.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 (continuação) - Xenodiagnóstico
    # -------------------------------------------------------------------------

    tp_xenodiagnostico = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Xenodiagnóstico",
        help_text="Resultado do xenodiagnóstico.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Hemocultura
    # -------------------------------------------------------------------------

    tp_hemocultivo = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Hemocultura",
        help_text="Resultado da hemocultura.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Data da Coleta S1
    # -------------------------------------------------------------------------

    dt_coleta_s1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Soro 1",
        help_text="Data de coleta do material para sorologia (1ª amostra).",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Data da Coleta S2
    # -------------------------------------------------------------------------

    dt_coleta_s2 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Soro 2",
        help_text="Data de coleta do material para sorologia (2ª amostra).",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Resultados ELISA (IgM e IgG para S1 e S2)
    # -------------------------------------------------------------------------

    tp_elisa_igm_s1 = models.CharField(
        max_length=1,
        choices=ResultadoSorologia.choices,
        null=True,
        blank=True,
        verbose_name="ELISA - IgM Soro 1",
        help_text="Resultado do ELISA IgM para 1ª amostra.",
    )
    tp_elisa_igg_s1 = models.CharField(
        max_length=1,
        choices=ResultadoSorologia.choices,
        null=True,
        blank=True,
        verbose_name="ELISA - IgG Soro 1",
        help_text="Resultado do ELISA IgG para 1ª amostra.",
    )
    tp_elisa_igm_s2 = models.CharField(
        max_length=1,
        choices=ResultadoSorologia.choices,
        null=True,
        blank=True,
        verbose_name="ELISA - IgM Soro 2",
        help_text="Resultado do ELISA IgM para 2ª amostra.",
    )
    tp_elisa_igg_s2 = models.CharField(
        max_length=1,
        choices=ResultadoSorologia.choices,
        null=True,
        blank=True,
        verbose_name="ELISA - IgG Soro 2",
        help_text="Resultado do ELISA IgG para 2ª amostra.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Resultados Hemoaglutinação (IgM e IgG para S1 e S2)
    # -------------------------------------------------------------------------

    tp_hemoaglutinacao_igm_s1 = models.CharField(
        max_length=1,
        choices=ResultadoSorologia.choices,
        null=True,
        blank=True,
        verbose_name="Hemoaglutinação - IgM Soro 1",
        help_text="Resultado da hemoaglutinação IgM para 1ª amostra.",
    )
    tp_hemoaglutinacao_igg_s1 = models.CharField(
        max_length=1,
        choices=ResultadoSorologia.choices,
        null=True,
        blank=True,
        verbose_name="Hemoaglutinação - IgG Soro 1",
        help_text="Resultado da hemoaglutinação IgG para 1ª amostra.",
    )
    tp_hemoaglutinacao_igm_s2 = models.CharField(
        max_length=1,
        choices=ResultadoSorologia.choices,
        null=True,
        blank=True,
        verbose_name="Hemoaglutinação - IgM Soro 2",
        help_text="Resultado da hemoaglutinação IgM para 2ª amostra.",
    )
    tp_hemoaglutinacao_igg_s2 = models.CharField(
        max_length=1,
        choices=ResultadoSorologia.choices,
        null=True,
        blank=True,
        verbose_name="Hemoaglutinação - IgG Soro 2",
        help_text="Resultado da hemoaglutinação IgG para 2ª amostra.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Resultados Imunofluorescência Indireta - IFI (IgM e IgG para S1 e S2)
    # -------------------------------------------------------------------------

    tp_resultado_igm_s1 = models.CharField(
        max_length=1,
        choices=ResultadoSorologia.choices,
        null=True,
        blank=True,
        verbose_name="IFI - IgM Soro 1",
        help_text="Resultado da imunofluorescência indireta IgM para 1ª amostra.",
    )
    ds_resultado_titulo_igm_s1 = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name="IFI - Título IgM Soro 1",
        help_text="Título da imunofluorescência indireta IgM para 1ª amostra.",
    )
    tp_resultado_igm_s2 = models.CharField(
        max_length=1,
        choices=ResultadoSorologia.choices,
        null=True,
        blank=True,
        verbose_name="IFI - IgM Soro 2",
        help_text="Resultado da imunofluorescência indireta IgM para 2ª amostra.",
    )
    ds_resultado_titulo_igm_s2 = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name="IFI - Título IgM Soro 2",
        help_text="Título da imunofluorescência indireta IgM para 2ª amostra.",
    )
    tp_resultado_igg_s1 = models.CharField(
        max_length=1,
        choices=ResultadoSorologia.choices,
        null=True,
        blank=True,
        verbose_name="IFI - IgG Soro 1",
        help_text="Resultado da imunofluorescência indireta IgG para 1ª amostra.",
    )
    ds_resultado_titulo_igg_s1 = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name="IFI - Título IgG Soro 1",
        help_text="Título da imunofluorescência indireta IgG para 1ª amostra.",
    )
    tp_resultado_igg_s2 = models.CharField(
        max_length=1,
        choices=ResultadoSorologia.choices,
        null=True,
        blank=True,
        verbose_name="IFI - IgG Soro 2",
        help_text="Resultado da imunofluorescência indireta IgG para 2ª amostra.",
    )
    ds_resultado_titulo_igg_s2 = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name="IFI - Título IgG Soro 2",
        help_text="Título da imunofluorescência indireta IgG para 2ª amostra.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Data da Coleta do Histopatológico
    # -------------------------------------------------------------------------

    dt_coleta_histopatologico = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Histopatológico",
        help_text="Data da coleta do exame histopatológico.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Resultado do Histopatológico
    # -------------------------------------------------------------------------

    tp_resultado_necropsia = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado do histopatológico",
        help_text="Resultado do exame histopatológico.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Tipo de Tratamento (Específico e Sintomático)
    # -------------------------------------------------------------------------

    st_tratamento_especifico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Tratamento específico",
        help_text="Se o paciente recebeu tratamento específico.",
    )
    st_tratamento_sintomatico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Tratamento sintomático",
        help_text="Se o paciente recebeu tratamento sintomático.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Droga Utilizada no Tratamento Específico
    # -------------------------------------------------------------------------

    class DrogaUtilizada(models.TextChoices):
        BENZNIDAZOL = '1', 'Benznidazol'
        OUTRO = '2', 'Outro'

    tp_droga_utilizada = models.CharField(
        max_length=1,
        choices=DrogaUtilizada.choices,
        null=True,
        blank=True,
        verbose_name="Droga utilizada",
        help_text="Droga utilizada no tratamento específico.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Tempo de Tratamento
    # -------------------------------------------------------------------------

    qt_dia_tratamento = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Tempo de tratamento (dias)",
        help_text="Tempo de tratamento em dias.",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - Medidas Tomadas (5 subcampos)
    # -------------------------------------------------------------------------

    tp_ocorre_triatomideos = models.CharField(
        max_length=1,
        choices=SimNaoNaoSeAplicaIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Controle de triatomídeos",
        help_text="Se ocorreu controle de triatomídeos.",
    )
    tp_ocorre_bioseguranca = models.CharField(
        max_length=1,
        choices=SimNaoNaoSeAplicaIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Implantação de normas de biosegurança",
        help_text="Se ocorreu implantação de normas de biosegurança em laboratório.",
    )
    tp_ocorre_fiscalizacao = models.CharField(
        max_length=1,
        choices=SimNaoNaoSeAplicaIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Fiscalização sanitária",
        help_text="Se ocorreu fiscalização sanitária em Unidade de Hemoterapia.",
    )
    tp_ocorre_outro = models.CharField(
        max_length=1,
        choices=SimNaoNaoSeAplicaIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outras medidas",
        help_text="Se ocorreu outra medida de controle.",
    )
    ds_ocorre_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outras medidas (especificar)",
        help_text="Descrição de outras medidas de controle.",
    )

    # -------------------------------------------------------------------------
    # Campo 57 - Classificação Final
    # -------------------------------------------------------------------------

    class ClassificacaoFinal(models.TextChoices):
        CONFIRMADO = '1', 'Confirmado'
        DESCARTADO = '2', 'Descartado'

    tp_classificacao_final = models.CharField(
        max_length=1,
        choices=ClassificacaoFinal.choices,
        null=True,
        blank=True,
        verbose_name="Classificação final",
        help_text="Classificação final da investigação.",
    )

    # -------------------------------------------------------------------------
    # Campo 58 - Critério de Confirmação/Descarte
    # -------------------------------------------------------------------------

    class CriterioConfirmacao(models.TextChoices):
        LABORATORIO = '1', 'Laboratório'
        CLINICO_EPIDEMIOLOGICO = '2', 'Clínico-epidemiológico'
        CLINICO = '3', 'Clínico'

    tp_criterio_confirmacao = models.CharField(
        max_length=1,
        choices=CriterioConfirmacao.choices,
        null=True,
        blank=True,
        verbose_name="Critério de confirmação/descarte",
        help_text="Critério utilizado para confirmação/descarte da investigação.",
    )

    # -------------------------------------------------------------------------
    # Campo 59 - Evolução do caso
    # -------------------------------------------------------------------------

    class EvolucaoCaso(models.TextChoices):
        VIVO = '1', 'Vivo'
        OBITO_CHAGAS = '2', 'Óbito por Chagas'
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
    # Campo 60 - Data do Óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito. Obrigatório se evolução = 2 ou 3.",
    )

    # -------------------------------------------------------------------------
    # Campo 61 - Modo Provável da Infecção
    # -------------------------------------------------------------------------

    class ModoTransmissao(models.TextChoices):
        TRANSFUSIONAL = '1', 'Transfusional'
        VETORIAL = '2', 'Vetorial'
        TRANSPLACENTARIA = '3', 'Transplacentária'
        ACIDENTAL = '4', 'Acidental'
        ORAL = '5', 'Oral'
        OUTRA = '6', 'Outra'
        IGNORADA = '9', 'Ignorada'

    st_modo_transmissao = models.CharField(
        max_length=1,
        choices=ModoTransmissao.choices,
        null=True,
        blank=True,
        verbose_name="Modo provável da infecção",
        help_text="Fonte provável da infecção.",
    )
    ds_modo_infeccao_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro modo de infecção (especificar)",
        help_text="Especificação quando modo = 6 (Outra).",
    )

    # -------------------------------------------------------------------------
    # Campo 62 - Local Provável de Infecção
    # -------------------------------------------------------------------------

    class LocalInfeccao(models.TextChoices):
        UNIDADE_HEMOTERAPIA = '1', 'Unidade de hemoterapia'
        DOMICILIO = '2', 'Domicílio'
        LABORATORIO = '3', 'Laboratório'
        OUTRO = '4', 'Outro'
        IGNORADO = '9', 'Ignorado'

    tp_local_infeccao = models.CharField(
        max_length=1,
        choices=LocalInfeccao.choices,
        null=True,
        blank=True,
        verbose_name="Local provável de infecção",
        help_text="Local provável da infecção (no período de 90 dias).",
    )

    # -------------------------------------------------------------------------
    # Campo 63 - O caso é Autóctone de residência?
    # -------------------------------------------------------------------------

    class Autoctone(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        INDETERMINADO = '3', 'Indeterminado'

    tp_autoctone_residencia = models.CharField(
        max_length=1,
        choices=Autoctone.choices,
        null=True,
        blank=True,
        verbose_name="Caso autóctone do município de residência",
        help_text="Indica se o caso é autóctone do município de residência.",
    )

    # -------------------------------------------------------------------------
    # Campo 64 - UF (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_uf_infeccao = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF provável da infecção",
        help_text="Unidade Federada onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 65 - País (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_pais_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="País provável da infecção",
        help_text="País onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 66 - Município (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_municipio_infeccao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município provável da infecção",
        help_text="Código do município onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 67 - Distrito (provável de infecção)
    # -------------------------------------------------------------------------

    co_distrito_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Distrito provável da infecção",
        help_text="Código do distrito provável de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 68 - Bairro (provável de infecção)
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
    # Campo 69 - Doença relacionada ao trabalho
    # -------------------------------------------------------------------------

    st_doenca_trabalho = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Doença relacionada ao trabalho",
        help_text="Informa se a doença está relacionada ao ambiente de trabalho do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 70 - Data do Encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento",
        help_text="Data do encerramento do caso. Deve ser >= data da investigação.",
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
        db_table = 'doenca_chagas'
        verbose_name = 'Doença de Chagas'
        verbose_name_plural = 'Doença de Chagas'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Doença de Chagas – {self.dt_investigacao}"