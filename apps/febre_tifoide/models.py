from django.db import models


class FebreTifoide(models.Model):
    """
    Ficha de Investigação - Febre Tifóide
    Dicionário de Dados SINAN NET - Versão 5.0
    Revisado em julho/2010
    Campos 31 a 59 + campos complementares + campos de controle
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

    class ContatoCaso(models.TextChoices):
        DOMICILIO = '1', 'Domicílio'
        VIZINHANCA = '2', 'Vizinhança'
        TRABALHO = '3', 'Trabalho'
        CRECHE_ESCOLA = '4', 'Creche/escola'
        POSTO_SAUDE_HOSPITAL = '5', 'Posto de saúde/hospital'
        OUTRO_ESTADO_MUNICIPIO = '6', 'Outro Estado/Município'
        OUTROS = '7', 'Outros'
        SEM_HISTORIA_CONTATO = '8', 'Sem história de contato'
        IGNORADO = '9', 'Ignorado'

    class SugestaoVinculo(models.TextChoices):
        AGUA_NAO_TRATADA = '1', 'Consumo de água não tratada'
        EXPOSICAO_ESGOTO = '2', 'Exposição à esgoto'
        ALIMENTO_SUSPEITO = '3', 'Alimento suspeito'
        DESLOCAMENTO = '4', 'Deslocamento'
        OUTROS = '5', 'Outros'
        IGNORADO = '9', 'Ignorado'

    class TipoAtendimento(models.TextChoices):
        HOSPITALAR = '1', 'Hospitalar'
        AMBULATORIAL = '2', 'Ambulatorial'
        DOMICILIAR = '3', 'Domiciliar'
        NENHUM = '4', 'Nenhum'
        IGNORADO = '9', 'Ignorado'

    class ResultadoExame(models.TextChoices):
        SALMONELLA_TYPHI = '1', 'Salmonella typhi'
        SALMONELLA_SPP = '2', 'Salmonella SPP'
        NEGATIVO = '3', 'Negativo'
        OUTRO_AGENTE = '4', 'Outro agente'

    class ClassificacaoFinal(models.TextChoices):
        CONFIRMADO = '1', 'Confirmado'
        DESCARTADO = '2', 'Descartado'

    class CriterioConfirmacao(models.TextChoices):
        LABORATORIAL = '1', 'Laboratorial'
        CLINICO_EPIDEMIOLOGICO = '2', 'Clínico epidemiológico'

    class Autoctone(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        INDETERMINADO = '3', 'Indeterminado'

    class EvolucaoCaso(models.TextChoices):
        CURA = '1', 'Cura'
        OBITO_TIFOIDE = '2', 'Óbito por febre tifóide'
        OBITO_OUTRAS_CAUSAS = '3', 'Óbito por outras causas'
        IGNORADO = '9', 'Ignorado'

    # -------------------------------------------------------------------------
    # Campo 31 - Data da Investigação
    # -------------------------------------------------------------------------

    dt_investigacao = models.DateField(
        verbose_name="Data da investigação",
        help_text="Data em que ocorreu a investigação (1ª visita ao paciente). Deve ser >= data da notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 32 - Ocupação/Ramo de atividade
    # -------------------------------------------------------------------------

    co_cbo_ocupacao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Ocupação (CBO)",
        help_text="Código CBO da ocupação exercida pelo paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 33 - Contato compatível com caso de febre tifóide
    # -------------------------------------------------------------------------

    tp_contato_caso_febre = models.CharField(
        max_length=1,
        choices=ContatoCaso.choices,
        null=True,
        blank=True,
        verbose_name="Contato com caso de febre tifóide",
        help_text="Local de contato com caso semelhante até 45 dias antes do início dos sintomas.",
    )
    ds_contato_caso_febre_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro contato (especificar)",
        help_text="Especificação quando contato = 7 (Outros).",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Nome do contato
    # -------------------------------------------------------------------------

    no_contato = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Nome do contato",
        help_text="Nome completo do contato.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - (DDD) Telefone
    # -------------------------------------------------------------------------

    nu_ddd = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="DDD do contato",
        help_text="DDD do telefone do contato.",
    )
    nu_telefone = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Telefone do contato",
        help_text="Telefone do contato.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Sugestão de vínculo
    # -------------------------------------------------------------------------

    tp_sugestao = models.CharField(
        max_length=1,
        choices=SugestaoVinculo.choices,
        verbose_name="Sugestão de vínculo",
        help_text="Identificar fontes de infecção mais comuns.",
    )
    ds_sugestao_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outros vínculos (especificar)",
        help_text="Especificação de outros tipos de vínculos.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Sinais e sintomas (14 subcampos)
    # -------------------------------------------------------------------------

    st_sinais_assintomatico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Assintomático",
        help_text="Se o paciente é assintomático. Se sim, pular para campo 39.",
    )
    st_sinais_febre = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Febre",
        help_text="Se o paciente teve febre.",
    )
    st_sinais_cefaleia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Cefaléia",
        help_text="Se o paciente teve cefaléia.",
    )
    st_sinais_diarreia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Diarréia",
        help_text="Se o paciente teve diarréia.",
    )
    st_sinais_constipacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Constipação",
        help_text="Se o paciente apresentou constipação.",
    )
    st_sinais_astenia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Astenia",
        help_text="Se o paciente apresentou astenia.",
    )
    st_sinais_tosse = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Tosse",
        help_text="Se o paciente teve tosse.",
    )
    st_sinais_esplenomegalia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Esplenomegalia",
        help_text="Se o paciente apresentou esplenomegalia.",
    )
    st_sinais_roseola_tica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Roséola tífica",
        help_text="Se foi identificada roséola tífica no paciente.",
    )
    st_sinais_nauseas = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Náuseas",
        help_text="Se o paciente apresentou náuseas.",
    )
    st_sinais_vomitos = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Vômitos",
        help_text="Se o paciente apresentou vômitos.",
    )
    st_sinais_dor_abdominal = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Dor abdominal",
        help_text="Se o paciente apresentou dor abdominal.",
    )
    st_sinais_dissociacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Dissociação pulso/temperatura",
        help_text="Se o paciente teve dissociação pulso/temperatura.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Complicações (4 subcampos)
    # -------------------------------------------------------------------------

    st_complicacao_enterorragia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Enterorragia",
        help_text="Se o paciente apresentou enterorragia.",
    )
    st_complicacao_perfuracao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Perfuração intestinal",
        help_text="Se o paciente apresentou perfuração intestinal.",
    )
    st_complicacao_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outras complicações",
        help_text="Se o paciente apresentou outras complicações.",
    )
    ds_complicacao_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outras complicações (especificar)",
        help_text="Especificação quando outras complicações = Sim.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Tipo de atendimento
    # -------------------------------------------------------------------------

    tp_atendimento = models.CharField(
        max_length=1,
        choices=TipoAtendimento.choices,
        verbose_name="Tipo de atendimento",
        help_text="Tipo de atendimento recebido pelo paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Data do atendimento
    # -------------------------------------------------------------------------

    dt_atendimento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do atendimento",
        help_text="Obrigatório se tipo de atendimento = 1, 2 ou 3. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - UF do Hospital
    # -------------------------------------------------------------------------

    co_uf_atendimento = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF do hospital",
        help_text="Sigla da UF onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Município do hospital
    # -------------------------------------------------------------------------

    co_municipio_atendimento = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município do hospital",
        help_text="Nome completo do município onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Nome do hospital
    # -------------------------------------------------------------------------

    co_unidade_atendimento = models.DecimalField(
        max_digits=7,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Código do hospital",
        help_text="Código do hospital onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Material coletado (3 subcampos)
    # -------------------------------------------------------------------------

    st_material_coletado_sangue = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Material coletado - Sangue",
        help_text="Se foi colhido sangue para exame.",
    )
    st_material_coletado_fezes = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Material coletado - Fezes",
        help_text="Se foi colhido fezes para exame.",
    )
    st_material_coletado_urina = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Material coletado - Urina",
        help_text="Se foi colhido urina para exame.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Uso de antibiótico antes da coleta do material
    # -------------------------------------------------------------------------

    st_uso_antibiotico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Uso de antibiótico antes da coleta",
        help_text="Se o paciente fez uso de antibiótico antes da coleta para exame.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Exames Laboratoriais (Hemocultura, Urocultura, Coprocultura, Outros)
    # -------------------------------------------------------------------------

    # Hemocultura (até 3 amostras)
    dt_hemocultura_coleta_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Hemocultura - Data da 1ª coleta",
        help_text="Data da 1ª coleta de hemocultura.",
    )
    tp_hemocultura_resultado_1 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Hemocultura - Resultado da 1ª coleta",
        help_text="Resultado da 1ª coleta de hemocultura.",
    )
    ds_hemocultura_resultado_1 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Hemocultura - Resultado da 1ª coleta (especificar)",
        help_text="Especificação quando resultado = 4 (Outro agente).",
    )
    dt_hemocultura_coleta_2 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Hemocultura - Data da 2ª coleta",
        help_text="Data da 2ª coleta de hemocultura.",
    )
    tp_hemocultura_resultado_2 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Hemocultura - Resultado da 2ª coleta",
        help_text="Resultado da 2ª coleta de hemocultura.",
    )
    ds_hemocultura_resultado_2 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Hemocultura - Resultado da 2ª coleta (especificar)",
        help_text="Especificação quando resultado = 4 (Outro agente).",
    )
    dt_hemocultura_coleta_3 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Hemocultura - Data da 3ª coleta",
        help_text="Data da 3ª coleta de hemocultura.",
    )
    tp_hemocultura_resultado_3 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Hemocultura - Resultado da 3ª coleta",
        help_text="Resultado da 3ª coleta de hemocultura.",
    )
    ds_hemocultura_resultado_3 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Hemocultura - Resultado da 3ª coleta (especificar)",
        help_text="Especificação quando resultado = 4 (Outro agente).",
    )

    # Urocultura (até 3 amostras)
    dt_urocultura_coleta_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Urocultura - Data da 1ª coleta",
        help_text="Data da 1ª coleta de urocultura.",
    )
    tp_urocultura_resultado_1 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Urocultura - Resultado da 1ª coleta",
        help_text="Resultado da 1ª coleta de urocultura.",
    )
    ds_urocultura_resultado_1 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Urocultura - Resultado da 1ª coleta (especificar)",
        help_text="Especificação quando resultado = 4 (Outro agente).",
    )
    dt_urocultura_coleta_2 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Urocultura - Data da 2ª coleta",
        help_text="Data da 2ª coleta de urocultura.",
    )
    tp_urocultura_resultado_2 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Urocultura - Resultado da 2ª coleta",
        help_text="Resultado da 2ª coleta de urocultura.",
    )
    ds_urocultura_resultado_2 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Urocultura - Resultado da 2ª coleta (especificar)",
        help_text="Especificação quando resultado = 4 (Outro agente).",
    )
    dt_urocultura_coleta_3 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Urocultura - Data da 3ª coleta",
        help_text="Data da 3ª coleta de urocultura.",
    )
    tp_urocultura_resultado_3 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Urocultura - Resultado da 3ª coleta",
        help_text="Resultado da 3ª coleta de urocultura.",
    )
    ds_urocultura_resultado_3 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Urocultura - Resultado da 3ª coleta (especificar)",
        help_text="Especificação quando resultado = 4 (Outro agente).",
    )

    # Coprocultura (até 3 amostras)
    dt_coprocultura_coleta_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Coprocultura - Data da 1ª coleta",
        help_text="Data da 1ª coleta de coprocultura.",
    )
    tp_coprocultura_resultado_1 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Coprocultura - Resultado da 1ª coleta",
        help_text="Resultado da 1ª coleta de coprocultura.",
    )
    ds_coprocultura_resultado_1 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Coprocultura - Resultado da 1ª coleta (especificar)",
        help_text="Especificação quando resultado = 4 (Outro agente).",
    )
    dt_coprocultura_coleta_2 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Coprocultura - Data da 2ª coleta",
        help_text="Data da 2ª coleta de coprocultura.",
    )
    tp_coprocultura_resultado_2 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Coprocultura - Resultado da 2ª coleta",
        help_text="Resultado da 2ª coleta de coprocultura.",
    )
    ds_coprocultura_resultado_2 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Coprocultura - Resultado da 2ª coleta (especificar)",
        help_text="Especificação quando resultado = 4 (Outro agente).",
    )
    dt_coprocultura_coleta_3 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Coprocultura - Data da 3ª coleta",
        help_text="Data da 3ª coleta de coprocultura.",
    )
    tp_coprocultura_resultado_3 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Coprocultura - Resultado da 3ª coleta",
        help_text="Resultado da 3ª coleta de coprocultura.",
    )
    ds_coprocultura_resultado_3 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Coprocultura - Resultado da 3ª coleta (especificar)",
        help_text="Especificação quando resultado = 4 (Outro agente).",
    )

    # Outros exames (até 3 amostras)
    dt_outro_coleta_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Outro exame - Data da 1ª coleta",
        help_text="Data da 1ª coleta de outro exame.",
    )
    tp_outro_resultado_1 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Outro exame - Resultado da 1ª coleta",
        help_text="Resultado da 1ª coleta de outro exame.",
    )
    ds_outro_resultado_1 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro exame - Resultado da 1ª coleta (especificar)",
        help_text="Especificação quando resultado = 4 (Outro agente).",
    )
    dt_outro_coleta_2 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Outro exame - Data da 2ª coleta",
        help_text="Data da 2ª coleta de outro exame.",
    )
    tp_outro_resultado_2 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Outro exame - Resultado da 2ª coleta",
        help_text="Resultado da 2ª coleta de outro exame.",
    )
    ds_outro_resultado_2 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro exame - Resultado da 2ª coleta (especificar)",
        help_text="Especificação quando resultado = 4 (Outro agente).",
    )
    dt_outro_coleta_3 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Outro exame - Data da 3ª coleta",
        help_text="Data da 3ª coleta de outro exame.",
    )
    tp_outro_resultado_3 = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Outro exame - Resultado da 3ª coleta",
        help_text="Resultado da 3ª coleta de outro exame.",
    )
    ds_outro_resultado_3 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro exame - Resultado da 3ª coleta (especificar)",
        help_text="Especificação quando resultado = 4 (Outro agente).",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Antibióticos utilizados no tratamento (6 subcampos)
    # -------------------------------------------------------------------------

    st_antibio_trata_cloranfenicol = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Cloranfenicol",
        help_text="Se o paciente fez uso de Cloranfenicol durante o tratamento.",
    )
    st_antibio_trata_ampicilina = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Ampicilina",
        help_text="Se o paciente fez uso de Ampicilina durante o tratamento.",
    )
    st_antibio_trata_sulfametoxazol = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Sulfametoxazol+Trimetoprima",
        help_text="Se o paciente fez uso de Sulfametoxazol+Trimetoprima durante o tratamento.",
    )
    st_antibio_trata_quinolona = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Quinolona",
        help_text="Se o paciente fez uso de Quinolona durante o tratamento.",
    )
    st_antibio_trata_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outros antibióticos",
        help_text="Se o paciente usou outros tipos de antibióticos.",
    )
    ds_antibio_trata_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outros antibióticos (especificar)",
        help_text="Especificação do nome do antibiótico.",
    )
    nu_tempo_uso = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Tempo de uso (dias)",
        help_text="Tempo de uso do antibiótico em dias.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Classificação final
    # -------------------------------------------------------------------------

    tp_classificacao_final = models.CharField(
        max_length=1,
        choices=ClassificacaoFinal.choices,
        null=True,
        blank=True,
        verbose_name="Classificação final",
        help_text="Confirma ou descarta o caso de Febre Tifóide.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Critério de confirmação/Descarte
    # -------------------------------------------------------------------------

    tp_criterio_confirmacao = models.CharField(
        max_length=1,
        choices=CriterioConfirmacao.choices,
        null=True,
        blank=True,
        verbose_name="Critério de confirmação/descarte",
        help_text="Define se o caso foi confirmado por laboratório ou clínico-epidemiológico.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - O caso é Autóctone de residência?
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
    # Campo 51 - UF (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_uf_infeccao = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF provável da infecção",
        help_text="Unidade Federada onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - País (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_pais_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="País provável da infecção",
        help_text="País onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Município (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_municipio_infeccao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município provável da infecção",
        help_text="Código do município onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Distrito (provável de infecção)
    # -------------------------------------------------------------------------

    co_distrito_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Distrito provável da infecção",
        help_text="Código do distrito provável de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Bairro (provável de infecção)
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
    # Campo 56 - Doença relacionada ao trabalho
    # -------------------------------------------------------------------------

    st_doenca_trabalho = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Doença relacionada ao trabalho",
        help_text="Se a doença está relacionada ao trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 57 - Evolução do caso
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
    # Campo 58 - Data do óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito. Obrigatório se evolução = 2 ou 3.",
    )

    # -------------------------------------------------------------------------
    # Campo 59 - Data do encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento",
        help_text="Data do encerramento da investigação. Obrigatório quando classificação final preenchida.",
    )

    # -------------------------------------------------------------------------
    # Informações complementares - Deslocamento (3 conjuntos)
    # -------------------------------------------------------------------------

    dt_complementar_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de deslocamento 1",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )
    dt_complementar_2 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de deslocamento 2",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )
    dt_complementar_3 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de deslocamento 3",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )

    co_uf_complementar_1 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de deslocamento 1",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )
    co_uf_complementar_2 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de deslocamento 2",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )
    co_uf_complementar_3 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de deslocamento 3",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )

    co_municipio_complementar_1 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município de deslocamento 1",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )
    co_municipio_complementar_2 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município de deslocamento 2",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )
    co_municipio_complementar_3 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município de deslocamento 3",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )

    co_pais_complementar_1 = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name="País de deslocamento 1",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )
    co_pais_complementar_2 = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name="País de deslocamento 2",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )
    co_pais_complementar_3 = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name="País de deslocamento 3",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )

    ds_meio_trans_complementar_1 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Meio de transporte 1",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )
    ds_meio_trans_complementar_2 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Meio de transporte 2",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )
    ds_meio_trans_complementar_3 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Meio de transporte 3",
        help_text="Dado não exportado, disponível na base original SINAN.",
    )

    # -------------------------------------------------------------------------
    # Informações complementares - Alimentos consumidos (4 itens)
    # -------------------------------------------------------------------------

    ds_complementa_tp_alimento_1 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Tipo de alimento 1",
        help_text="Alimentos consumidos na última semana e sugestivo de contaminação.",
    )
    ds_complementa_tp_alimento_2 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Tipo de alimento 2",
        help_text="Alimentos consumidos na última semana e sugestivo de contaminação.",
    )
    ds_complementa_tp_alimento_3 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Tipo de alimento 3",
        help_text="Alimentos consumidos na última semana e sugestivo de contaminação.",
    )
    ds_complementa_tp_alimento_4 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Tipo de alimento 4",
        help_text="Alimentos consumidos na última semana e sugestivo de contaminação.",
    )

    ds_complementa_local_1 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Local de consumo 1",
        help_text="Local de consumo do alimento suspeito.",
    )
    ds_complementa_local_2 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Local de consumo 2",
        help_text="Local de consumo do alimento suspeito.",
    )
    ds_complementa_local_3 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Local de consumo 3",
        help_text="Local de consumo do alimento suspeito.",
    )
    ds_complementa_local_4 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Local de consumo 4",
        help_text="Local de consumo do alimento suspeito.",
    )

    # -------------------------------------------------------------------------
    # Observações adicionais
    # -------------------------------------------------------------------------

    ds_observacao = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Observações",
        help_text="Informações adicionais a respeito do caso se necessário.",
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
        db_table = 'febre_tifoide'
        verbose_name = 'Febre Tifóide'
        verbose_name_plural = 'Febre Tifóide'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Febre Tifóide – {self.dt_investigacao}"