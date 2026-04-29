from django.db import models


class FebreAmarela(models.Model):
    """
    Ficha de Investigação - Febre Amarela
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

    class ResultadoExame(models.TextChoices):
        REAGENTE = '1', 'Reagente'
        NAO_REAGENTE = '2', 'Não reagente'
        INCONCLUSIVO = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'

    class ClassificacaoFinal(models.TextChoices):
        FEBRE_AMARELA_SILVESTRE = '1', 'Febre Amarela silvestre'
        FEBRE_AMARELA_URBANA = '2', 'Febre Amarela urbana'
        DESCARTADO = '3', 'Descartado'

    class CriterioConfirmacao(models.TextChoices):
        LABORATORIAL = '1', 'Laboratorial'
        CLINICO_EPIDEMIOLOGICO = '2', 'Clínico-epidemiológico'

    class EvolucaoCaso(models.TextChoices):
        CURA = '1', 'Cura'
        OBITO_FEBRE_AMARELA = '2', 'Óbito por febre amarela'
        OBITO_OUTRAS_CAUSAS = '3', 'Óbito por outras causas'
        IGNORADO = '9', 'Ignorado'

    class Autoctone(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        INDETERMINADO = '3', 'Indeterminado'

    class AtividadeInfeccao(models.TextChoices):
        TRABALHO = '1', 'Trabalho'
        TURISMO = '2', 'Turismo'
        LAZER = '3', 'Lazer'
        IGNORADO = '9', 'Ignorado'

    # -------------------------------------------------------------------------
    # Campo 31 - Data da investigação
    # -------------------------------------------------------------------------

    dt_investigacao = models.DateField(
        verbose_name="Data da investigação",
        help_text="Data do início da investigação. Deve ser >= data da notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 32 - Ocupação / Ramo de Atividade Econômica
    # -------------------------------------------------------------------------

    co_cbo_ocupacao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Ocupação (CBO)",
        help_text="Código CBO da ocupação exercida pelo paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 33 - Dados da investigação entomológica e epizootias (3 subcampos)
    # -------------------------------------------------------------------------

    st_ento_ocorrencia_epizootia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Ocorrência de epizootias",
        help_text="Ocorrência de epizootias (mortandade de macacos).",
    )
    st_ento_isolamento_virus = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Isolamento de vírus em mosquitos",
        help_text="Isolamento de vírus em mosquitos.",
    )
    st_ento_presenca_mosquito = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Presença de mosquito Aedes aegypti em área urbana",
        help_text="Presença de mosquito Aedes aegypti em área urbana (observar período de viremia do paciente).",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Vacinado contra Febre Amarela
    # -------------------------------------------------------------------------

    st_vacinado_febre_amarela = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Vacinado contra Febre Amarela",
        help_text="Se o paciente foi vacinado contra febre amarela.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Data da vacinação
    # -------------------------------------------------------------------------

    dt_vacinado_febre_amarela = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da vacinação",
        help_text="Data da vacinação contra febre amarela. Deve ser <= data de notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - UF da vacinação
    # -------------------------------------------------------------------------

    co_uf_antecedente = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF da vacinação",
        help_text="UF em que foi realizada a vacinação.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Município da vacinação
    # -------------------------------------------------------------------------

    co_municipio_antecedente = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município da vacinação",
        help_text="Código do município em que foi realizada a vacinação.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Unidade de Saúde da vacinação
    # -------------------------------------------------------------------------

    co_unidade_antecedente = models.DecimalField(
        max_digits=8,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Unidade de saúde da vacinação",
        help_text="Código da unidade de saúde onde o paciente foi vacinado.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Sinais e sintomas (4 subcampos)
    # -------------------------------------------------------------------------

    st_sinais_dor_abdominal = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Dor abdominal",
        help_text="Se o paciente apresentou dor abdominal.",
    )
    st_sinais_hemorragico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Sinais hemorrágicos",
        help_text="Se o paciente apresentou sinais hemorrágicos (hematêmese, melena, epistaxe, gengivorragia, etc.).",
    )
    st_sinais_faget = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Sinal de Faget",
        help_text="Se o paciente apresentou Sinal de Faget (temperatura alta e frequência cardíaca lenta).",
    )
    st_sinais_excrecao_renal = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Distúrbios de excreção renal",
        help_text="Se o paciente apresentou distúrbios de excreção renal (oligúria e/ou anúria).",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Ocorreu Hospitalização
    # -------------------------------------------------------------------------

    st_ocorreu_hospitalizacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Ocorreu hospitalização",
        help_text="Se o paciente foi hospitalizado.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Data da internação
    # -------------------------------------------------------------------------

    dt_internacao = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da internação",
        help_text="Data do início da internação. Deve ser >= data do início dos sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - UF de hospitalização
    # -------------------------------------------------------------------------

    co_uf_hospital = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de hospitalização",
        help_text="Sigla da UF onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Município do hospital
    # -------------------------------------------------------------------------

    co_municipio_hospital = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município do hospital",
        help_text="Código do município onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Unidade de Saúde
    # -------------------------------------------------------------------------

    co_unidade_hospital = models.DecimalField(
        max_digits=8,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Unidade de saúde hospitalar",
        help_text="Código da unidade de saúde onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Exames Inespecíficos (4 subcampos)
    # -------------------------------------------------------------------------

    nu_exame_bilirrubina_total = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Bilirrubina Total (mg/dl)",
        help_text="Maior valor encontrado de Bilirrubina Total (4 dígitos, sendo 2 decimais).",
    )
    nu_exame_ast = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="AST (TGO) UI",
        help_text="Maior valor encontrado de AST/TGO (máximo 5 dígitos, sem casas decimais).",
    )
    nu_exame_bilirrubina_direta = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Bilirrubina Direta (mg/dl)",
        help_text="Maior valor encontrado de Bilirrubina Direta (4 dígitos, sendo 2 decimais).",
    )
    nu_exame_alt = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="ALT (TGP) UI",
        help_text="Maior valor encontrado de ALT/TGP (máximo 5 dígitos, sem casas decimais).",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Exame sorológico: Data da coleta 1ª amostra
    # -------------------------------------------------------------------------

    dt_sorologico_coleta_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - 1ª amostra sorologia",
        help_text="Data da coleta da 1ª amostra de sorologia. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Exame sorológico: Resultado 1ª amostra
    # -------------------------------------------------------------------------

    tp_sorologico_resultado_1 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - 1ª amostra sorologia",
        help_text="Resultado da 1ª amostra de sorologia (IgM).",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Exame sorológico: Data da coleta 2ª amostra
    # -------------------------------------------------------------------------

    dt_sorologico_coleta_2 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - 2ª amostra sorologia",
        help_text="Data da coleta da 2ª amostra de sorologia. Deve ser >= data da 1ª coleta.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Exame sorológico: Resultado 2ª amostra
    # -------------------------------------------------------------------------

    tp_sorologico_resultado_2 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - 2ª amostra sorologia",
        help_text="Resultado da 2ª amostra de sorologia (IgM).",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Isolamento Viral – material coletado
    # -------------------------------------------------------------------------

    st_viral_coletado = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Material coletado para isolamento viral",
        help_text="Se foi colhido material para realização de isolamento viral.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Data da coleta - Isolamento Viral
    # -------------------------------------------------------------------------

    dt_viral_coleta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - Isolamento Viral",
        help_text="Data da coleta do material para isolamento viral. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Resultado do isolamento
    # -------------------------------------------------------------------------

    tp_resultado_isolamento = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado do isolamento viral",
        help_text="Resultado do isolamento viral.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Histopatologia - Resultado
    # -------------------------------------------------------------------------

    tp_histopatologia = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado da histopatologia",
        help_text="Resultado do exame de histopatologia.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Imunohistoquímica - Resultado
    # -------------------------------------------------------------------------

    tp_imunohistoquimica = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado da imunohistoquímica",
        help_text="Resultado do exame de imunohistoquímica.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Data da coleta do PCR
    # -------------------------------------------------------------------------

    dt_pcr_coleta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta - PCR",
        help_text="Data da coleta do material para PCR. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - Resultado do RT-PCR
    # -------------------------------------------------------------------------

    tp_pcr_resultado = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado do RT-PCR",
        help_text="Resultado do exame de RT-PCR.",
    )

    # -------------------------------------------------------------------------
    # Campo 57 - Classificação final
    # -------------------------------------------------------------------------

    tp_classificacao_final = models.CharField(
        max_length=1,
        choices=ClassificacaoFinal.choices,
        null=True,
        blank=True,
        verbose_name="Classificação final",
        help_text="Conclusão da investigação.",
    )
    ds_classificacao_final = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Classificação final - descartado (especificar)",
        help_text="Especificação do diagnóstico do caso descartado.",
    )

    # -------------------------------------------------------------------------
    # Campo 58 - Critério de Confirmação / Descarte
    # -------------------------------------------------------------------------

    tp_criterio_confirmacao = models.CharField(
        max_length=1,
        choices=CriterioConfirmacao.choices,
        null=True,
        blank=True,
        verbose_name="Critério de confirmação/descarte",
        help_text="Critério utilizado para confirmação ou descarte do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 59 - O caso é Autóctone de residência?
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
    # Campo 60 - UF (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_uf_infeccao = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF provável da infecção",
        help_text="Unidade Federada onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 61 - País (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_pais_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="País provável da infecção",
        help_text="País onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 62 - Município (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_municipio_infeccao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município provável da infecção",
        help_text="Código do município onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 63 - Distrito (provável de infecção)
    # -------------------------------------------------------------------------

    co_distrito_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Distrito provável da infecção",
        help_text="Código do distrito provável de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 64 - Bairro (provável de infecção)
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
    # Campo 65 - Localidade
    # -------------------------------------------------------------------------

    no_localidade_infeccao = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Localidade de infecção",
        help_text="Localidade provável de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 66 - Doença relacionada ao trabalho
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
    # Campo 67 - Atividade desenvolvida no local provável de infecção
    # -------------------------------------------------------------------------

    tp_atividade_infeccao = models.CharField(
        max_length=1,
        choices=AtividadeInfeccao.choices,
        null=True,
        blank=True,
        verbose_name="Atividade desenvolvida no local provável de infecção",
        help_text="Atividade realizada no local provável de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 68 - Evolução do caso
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
    # Campo 69 - Data do Óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 70 - Data de Encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de encerramento",
        help_text="Data do encerramento da investigação. Deve ser >= data da investigação.",
    )

    # -------------------------------------------------------------------------
    # Informações complementares - Deslocamento (3 conjuntos)
    # -------------------------------------------------------------------------

    dt_info_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de deslocamento 1",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )
    dt_info_2 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de deslocamento 2",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )
    dt_info_3 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de deslocamento 3",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )

    co_uf_obs1 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de deslocamento 1",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )
    co_uf_obs2 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de deslocamento 2",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )
    co_uf_obs3 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de deslocamento 3",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )

    co_municipio_obs1 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município de deslocamento 1",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )
    co_municipio_obs2 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município de deslocamento 2",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )
    co_municipio_obs3 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município de deslocamento 3",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )

    co_pais_obs1 = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name="País de deslocamento 1",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )
    co_pais_obs2 = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name="País de deslocamento 2",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )
    co_pais_obs3 = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name="País de deslocamento 3",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )

    ds_transporte1 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Meio de transporte 1",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )
    ds_transporte2 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Meio de transporte 2",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )
    ds_transporte3 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Meio de transporte 3",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan NET.",
    )

    # -------------------------------------------------------------------------
    # Observações complementares
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
        db_table = 'febre_amarela'
        verbose_name = 'Febre Amarela'
        verbose_name_plural = 'Febre Amarela'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Febre Amarela – {self.dt_investigacao}"