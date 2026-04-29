from django.db import models


class FebreMaculosa(models.Model):
    """
    Ficha de Investigação - Febre Maculosa
    Dicionário de Dados SINAN NET - Versão 5.0
    Revisado em julho/2010
    Campos 31 a 63 + campos de controle
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
        POSITIVO = '1', 'Positivo'
        NEGATIVO = '2', 'Negativo'
        INCONCLUSIVO = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'

    class ResultadoIsolamento(models.TextChoices):
        DETECTADO = '1', 'Detectado'
        NAO_DETECTADO = '2', 'Não Detectado'
        NAO_REALIZADO = '3', 'Não realizado'

    class ClassificacaoFinal(models.TextChoices):
        CONFIRMADO = '1', 'Confirmado'
        DESCARTADO = '2', 'Descartado'

    class CriterioConfirmacao(models.TextChoices):
        LABORATORIO = '1', 'Laboratório'
        CLINICO_EPIDEMIOLOGICO = '2', 'Clínico-Epidemiológico'
        CLINICO = '3', 'Clínico'

    class Autoctone(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        INDETERMINADO = '3', 'Indeterminado'

    class EvolucaoCaso(models.TextChoices):
        CURA = '1', 'Cura'
        OBITO_MACULOSA = '2', 'Óbito por febre maculosa'
        OBITO_OUTRA_CAUSA = '3', 'Óbito por outra causa'
        IGNORADO = '9', 'Ignorado'

    class ZonaInfeccao(models.TextChoices):
        URBANA = '1', 'Urbana'
        RURAL = '2', 'Rural'
        PERI_URBANA = '3', 'Peri-Urbana'
        IGNORADO = '9', 'Ignorado'

    class AmbienteInfeccao(models.TextChoices):
        DOMICILIAR = '1', 'Domiciliar'
        TRABALHO = '2', 'Trabalho'
        LAZER = '3', 'Lazer'
        OUTRO = '4', 'Outro'
        IGNORADO = '9', 'Ignorado'

    # -------------------------------------------------------------------------
    # Campo 31 - Data da Investigação
    # -------------------------------------------------------------------------

    dt_investigacao = models.DateField(
        verbose_name="Data da investigação",
        help_text="Data de investigação do caso. Deve ser >= data da notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 32 - Ocupação/Ramo de atividade Econômica
    # -------------------------------------------------------------------------

    co_cbo_ocupacao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Ocupação (CBO)",
        help_text="Código CBO da ocupação exercida pelo paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 33 - Sinais e Sintomas (20 subcampos)
    # -------------------------------------------------------------------------

    st_sinais_febre = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Febre",
        help_text="Se o paciente apresentou febre.",
    )
    st_sinais_cefaleia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Cefaleia",
        help_text="Se o paciente apresentou cefaleia.",
    )
    st_sinais_abdominal = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Dor abdominal",
        help_text="Se o paciente apresentou dor abdominal.",
    )
    st_sinais_mialgia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Mialgia",
        help_text="Se o paciente apresentou mialgia.",
    )
    st_sinais_nausea = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Náusea/vômito",
        help_text="Se o paciente apresentou náusea ou vômito.",
    )
    st_sinais_exantema = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Exantema",
        help_text="Se o paciente apresentou exantema.",
    )
    st_sinais_diarreia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Diarréia",
        help_text="Se o paciente apresentou diarréia.",
    )
    st_sinais_ictericia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Icterícia",
        help_text="Se o paciente apresentou icterícia.",
    )
    st_sinais_hiperemia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Hiperemia conjuntival",
        help_text="Se o paciente apresentou hiperemia conjuntival.",
    )
    st_sinais_hepatomegalia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Hepatomegalia/Esplenomegalia",
        help_text="Se o paciente apresentou hepatomegalia ou esplenomegalia.",
    )
    st_sinais_petequias = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Petéquias",
        help_text="Se o paciente apresentou petéquias.",
    )
    st_sinais_hemorragicas = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Manifestações hemorrágicas",
        help_text="Se o paciente apresentou manifestações hemorrágicas.",
    )
    st_sinais_linfadenopatia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Linfadenopatia",
        help_text="Se o paciente apresentou linfadenopatia.",
    )
    st_sinais_convulsao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Convulsão",
        help_text="Se o paciente apresentou convulsão.",
    )
    st_sinais_necrose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Necrose de extremidades",
        help_text="Se o paciente apresentou necrose de extremidades.",
    )
    st_sinais_prostacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Prostração",
        help_text="Se o paciente apresentou prostração.",
    )
    st_sinais_choque = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Choque/Hipotensão",
        help_text="Se o paciente apresentou choque ou hipotensão.",
    )
    st_sinais_estupor = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Estupor/Coma",
        help_text="Se o paciente apresentou estupor ou coma.",
    )
    st_sinais_sufusao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Sufusão hemorrágica",
        help_text="Se o paciente apresentou sufusão hemorrágica.",
    )
    st_sinais_respiratorias = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Alterações respiratórias",
        help_text="Se o paciente apresentou alterações respiratórias.",
    )
    st_sinais_oliguria = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Oligúria/Anúria",
        help_text="Se o paciente apresentou oligúria ou anúria.",
    )
    st_sinais_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Outros sinais/sintomas",
        help_text="Se o paciente apresentou outros sinais ou sintomas.",
    )
    ds_sinais_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outros sinais/sintomas (especificar)",
        help_text="Especificação de outros sinais ou sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Teve contato com animais? (6 subcampos)
    # -------------------------------------------------------------------------

    st_contato_animal_carrapato = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Contato com carrapato",
        help_text="Se o paciente teve contato com carrapato.",
    )
    st_contato_animal_capivara = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Contato com capivara",
        help_text="Se o paciente teve contato com capivara.",
    )
    st_contato_animal_caogato = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Contato com cão/gato",
        help_text="Se o paciente teve contato com cão ou gato.",
    )
    st_contato_animal_bovino = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Contato com bovinos",
        help_text="Se o paciente teve contato com bovinos.",
    )
    st_contato_animal_equino = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Contato com equinos",
        help_text="Se o paciente teve contato com equinos.",
    )
    st_contato_animal_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Contato com outros animais",
        help_text="Se o paciente teve contato com outros animais.",
    )
    ds_contato_animal_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outros animais (especificar)",
        help_text="Especificação de outros animais.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Frequentou ambientes com vegetação
    # -------------------------------------------------------------------------

    st_frequentou_ambiente = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Frequentou ambientes com vegetação",
        help_text="Se o paciente frequentou ambientes com vegetação (mata, floresta, rios, cachoeiras, etc.).",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Ocorreu Hospitalização
    # -------------------------------------------------------------------------

    st_ocorreu_hospitalizacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Ocorreu hospitalização",
        help_text="Se ocorreu hospitalização.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Data da Internação
    # -------------------------------------------------------------------------

    dt_internacao = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da internação",
        help_text="Data da hospitalização. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Data da alta
    # -------------------------------------------------------------------------

    dt_alta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da alta",
        help_text="Data da alta hospitalar.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - UF do hospital
    # -------------------------------------------------------------------------

    co_uf_hospital = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF do hospital",
        help_text="UF do hospital onde ocorreu o tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Município do Hospital
    # -------------------------------------------------------------------------

    co_municipio_hospital = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município do hospital",
        help_text="Município do hospital onde ocorreu o tratamento.",
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
        help_text="Código do hospital onde ocorreu o tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Diagnóstico Laboratorial
    # -------------------------------------------------------------------------

    st_diagnostico_laboratorial = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Diagnóstico laboratorial",
        help_text="Se houve diagnóstico laboratorial.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Amostras S1 e S2 com resultados
    # -------------------------------------------------------------------------

    dt_amostra_s1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta S1",
        help_text="Data da amostra S1.",
    )
    dt_amostra_s2 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta S2",
        help_text="Data da amostra S2.",
    )

    # S1 Results
    tp_sorologia_igm_s1 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado S1 - IgM",
        help_text="Resultado da amostra S1 para IgM.",
    )
    nu_sorologia_igm_titulos_s1 = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name="Títulos S1 - IgM",
        help_text="Títulos da amostra S1 para IgM.",
    )
    tp_sorologia_igg_s1 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado S1 - IgG",
        help_text="Resultado da amostra S1 para IgG.",
    )
    nu_sorologia_igg_titulos_s1 = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name="Títulos S1 - IgG",
        help_text="Títulos da amostra S1 para IgG.",
    )

    # S2 Results
    tp_sorologia_igm_s2 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado S2 - IgM",
        help_text="Resultado da amostra S2 para IgM.",
    )
    nu_sorologia_igm_titulos_s2 = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name="Títulos S2 - IgM",
        help_text="Títulos da amostra S2 para IgM.",
    )
    tp_sorologia_igg_s2 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado S2 - IgG",
        help_text="Resultado da amostra S2 para IgG.",
    )
    nu_sorologia_igg_titulos_s2 = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name="Títulos S2 - IgG",
        help_text="Títulos da amostra S2 para IgG.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Data da coleta (Isolamento)
    # -------------------------------------------------------------------------

    dt_coleta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta",
        help_text="Data da coleta para isolamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Resultado Isolamento
    # -------------------------------------------------------------------------

    tp_outro_exame_isolamento = models.CharField(
        max_length=1,
        choices=ResultadoIsolamento.choices,
        null=True,
        blank=True,
        verbose_name="Resultado do isolamento",
        help_text="Resultado do isolamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Agente
    # -------------------------------------------------------------------------

    ds_agente = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Agente",
        help_text="Agente identificado. Obrigatório se isolamento = 1 (Detectado).",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Resultado Histopatologia
    # -------------------------------------------------------------------------

    tp_histopatologia = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado da histopatologia",
        help_text="Resultado da histopatologia.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Resultado Imunohistoquímica
    # -------------------------------------------------------------------------

    tp_outro_exame_imunohisto = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado da imunohistoquímica",
        help_text="Resultado da imunohistoquímica.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Classificação Final
    # -------------------------------------------------------------------------

    tp_classificacao_final = models.CharField(
        max_length=1,
        choices=ClassificacaoFinal.choices,
        null=True,
        blank=True,
        verbose_name="Classificação final",
        help_text="Diagnóstico definitivo.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Critério Confirmação/Descarte
    # -------------------------------------------------------------------------

    tp_confirmacao_descarte = models.CharField(
        max_length=1,
        choices=CriterioConfirmacao.choices,
        null=True,
        blank=True,
        verbose_name="Critério de confirmação/descarte",
        help_text="Critério utilizado para confirmação ou descarte.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Se descartado, especificar diagnóstico
    # -------------------------------------------------------------------------

    ds_diagnostico_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Diagnóstico descartado (especificar)",
        help_text="Especificação do diagnóstico quando descartado.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - O caso é Autóctone de residência?
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
    # Campo 53 - UF (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_uf_infeccao = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF provável da infecção",
        help_text="Unidade Federada onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - País (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_pais_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="País provável da infecção",
        help_text="País onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Município (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_municipio_infeccao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município provável da infecção",
        help_text="Código do município onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - Distrito (provável de infecção)
    # -------------------------------------------------------------------------

    co_distrito_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Distrito provável da infecção",
        help_text="Código do distrito provável de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 57 - Bairro (provável de infecção)
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
    # Campo 58 - Característica do Local Provável de Infecção - Zona
    # -------------------------------------------------------------------------

    tp_zona = models.CharField(
        max_length=1,
        choices=ZonaInfeccao.choices,
        null=True,
        blank=True,
        verbose_name="Zona do local provável de infecção",
        help_text="Característica do local provável de infecção - Zona.",
    )

    # -------------------------------------------------------------------------
    # Campo 59 - Característica do Local Provável de Infecção - Ambiente
    # -------------------------------------------------------------------------

    tp_ambiente = models.CharField(
        max_length=1,
        choices=AmbienteInfeccao.choices,
        null=True,
        blank=True,
        verbose_name="Ambiente do local provável de infecção",
        help_text="Característica do local provável de infecção - Ambiente.",
    )

    # -------------------------------------------------------------------------
    # Campo 60 - Doença relacionada ao Trabalho
    # -------------------------------------------------------------------------

    st_doenca_trabalho = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Doença relacionada ao trabalho",
        help_text="Se a doença está relacionada ao ambiente de trabalho do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 61 - Evolução
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
    # Campo 62 - Data do Óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 63 - Data do encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento",
        help_text="Data do encerramento. Deve ser >= data da investigação.",
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
        db_table = 'febre_maculosa'
        verbose_name = 'Febre Maculosa'
        verbose_name_plural = 'Febre Maculosa'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Febre Maculosa – {self.dt_investigacao}"