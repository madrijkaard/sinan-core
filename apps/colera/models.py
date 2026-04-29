from django.db import models


class Colera(models.Model):
    """
    Ficha de Investigação - Cólera
    Dicionário de Dados SINAN NET - Versão 5.0
    Revisado fevereiro/2012
    Campos 31 a 71 + campos complementares + campos de controle
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

    # -------------------------------------------------------------------------
    # Campo 31 - Data da investigação
    # -------------------------------------------------------------------------

    dt_investigacao = models.DateField(
        verbose_name="Data da investigação",
        help_text="Data da investigação do caso. Deve ser >= data da notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 32 - Ocupação / Ramo de atividade
    # -------------------------------------------------------------------------

    co_cbo_ocupacao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Ocupação (CBO)",
        help_text="Código CBO da ocupação exercida pelo paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 33 - Contato com caso suspeito ou confirmado de cólera
    # -------------------------------------------------------------------------

    class ContatoCaso(models.TextChoices):
        DOMICILIO = '1', 'Domicílio'
        VIZINHANCA = '2', 'Vizinhança'
        TRABALHO = '3', 'Trabalho'
        CRECHE_ESCOLA = '4', 'Creche/escola'
        POSTO_SAUDE_HOSPITAL = '5', 'Posto de saúde/hospital'
        OUTRO_ESTADO_MUNICIPIO = '6', 'Outro estado/município'
        OUTROS = '7', 'Outros'
        SEM_HISTORIA_CONTATO = '8', 'Sem história de contato'
        IGNORADO = '9', 'Ignorado'

    tp_contato_caso_suspeito = models.CharField(
        max_length=1,
        choices=ContatoCaso.choices,
        null=True,
        blank=True,
        verbose_name="Contato com caso suspeito ou confirmado",
        help_text="Local em que o paciente teve contato com caso semelhante nos últimos 10 dias.",
    )
    ds_caso_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outros contatos (especificar)",
        help_text="Especificação quando contato = 7 (Outros).",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Nome do contato
    # -------------------------------------------------------------------------

    no_contato = models.CharField(
        max_length=40,
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
    # Campo 36 - Endereço do contato
    # -------------------------------------------------------------------------

    co_endereco_contato = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Código do endereço do contato",
        help_text="Código do endereço completo do contato.",
    )
    no_endereco_contato = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Endereço do contato",
        help_text="Endereço completo do contato.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Sugestão de vínculo
    # -------------------------------------------------------------------------

    class Vinculo(models.TextChoices):
        AGUA_NAO_TRATADA = '1', 'Consumo de água não tratada'
        EXPOSICAO_ESGOTO = '2', 'Exposição à esgoto'
        ALIMENTO = '3', 'Alimento'
        DESLOCAMENTO = '4', 'Deslocamento'
        OUTROS = '5', 'Outros'
        IGNORADO = '9', 'Ignorado'

    tp_vinculo = models.CharField(
        max_length=1,
        choices=Vinculo.choices,
        verbose_name="Sugestão de vínculo",
        help_text="Para direcionar a investigação quanto à suspeita da fonte de contaminação.",
    )
    ds_vinculo_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outros vínculos (especificar)",
        help_text="Especificação quando vínculo = 5 (Outros).",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Sinais e Sintomas
    # -------------------------------------------------------------------------

    st_sinais_assintomatico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Assintomático",
        help_text="Se sim, desabilita campos de sintomas e pula para campo 44.",
    )
    st_sinais_diarreia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Diarréia",
        help_text="Informa se o paciente apresentou diarréia.",
    )
    st_sinais_caimbra = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Câimbras",
        help_text="Informa se o paciente apresentou câimbras.",
    )
    st_sinais_febre = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Febre",
        help_text="Informa se o paciente teve febre.",
    )
    st_sinais_vomito = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Vômitos",
        help_text="Informa se o paciente teve vômitos.",
    )
    st_sinais_abdominal = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Dor Abdominal",
        help_text="Informa se o paciente apresentou dor abdominal.",
    )
    st_sinais_choque = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Choque",
        help_text="Informa se o paciente entrou em estado de choque.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Desidratação
    # -------------------------------------------------------------------------

    class Desidratacao(models.TextChoices):
        NAO = '1', 'Não'
        ALGUM_GRAU = '2', 'Algum grau'
        GRAVE = '3', 'Grave'
        IGNORADO = '9', 'Ignorado'

    tp_desidratacao = models.CharField(
        max_length=1,
        choices=Desidratacao.choices,
        null=True,
        blank=True,
        verbose_name="Desidratação",
        help_text="Grau de desidratação do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Característica da Diarréia
    # -------------------------------------------------------------------------

    class CaracteristicaDiarrreia(models.TextChoices):
        AQUOSA_AMARELADA = '1', 'Aquosa/amarelada'
        AQUOSA_AGUA_ARROZ = '2', 'Aquosa/água de arroz'
        PASTOSA = '3', 'Pastosa'
        IGNORADO = '9', 'Ignorado'

    tp_caracteristica_diarreia = models.CharField(
        max_length=1,
        choices=CaracteristicaDiarrreia.choices,
        null=True,
        blank=True,
        verbose_name="Característica da diarréia",
        help_text="Como apresentava-se a diarréia.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Freqüência/Dia
    # -------------------------------------------------------------------------

    class FrequenciaDia(models.TextChoices):
        ATE_5 = '1', 'Até 5 evacuações'
        DE_6_A_10 = '2', 'De 6 a 10 evacuações'
        DE_11_A_20 = '3', 'De 11 a 20 evacuações'
        ACIMA_20 = '4', 'Acima de 20 evacuações'

    tp_frequencia_dia = models.CharField(
        max_length=1,
        choices=FrequenciaDia.choices,
        null=True,
        blank=True,
        verbose_name="Frequência por dia",
        help_text="Quantas evacuações o paciente teve durante 24 horas.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Presença de sangue
    # -------------------------------------------------------------------------

    st_presenca_sangue = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Presença de sangue",
        help_text="Se há presença de sangue nas fezes do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Presença de muco
    # -------------------------------------------------------------------------

    st_presenca_muco = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Presença de muco",
        help_text="Se há presença de muco nas fezes do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Tipo de atendimento
    # -------------------------------------------------------------------------

    class TipoAtendimento(models.TextChoices):
        HOSPITALAR = '1', 'Hospitalar'
        AMBULATORIAL = '2', 'Ambulatorial'
        DOMICILIAR = '3', 'Domiciliar'
        NENHUM = '4', 'Nenhum'
        IGNORADO = '9', 'Ignorado'

    tp_atendimento = models.CharField(
        max_length=1,
        choices=TipoAtendimento.choices,
        verbose_name="Tipo de atendimento",
        help_text="Tipo de atendimento recebido pelo paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Data do atendimento
    # -------------------------------------------------------------------------

    dt_atendimento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do atendimento",
        help_text="Obrigatório se tipo de atendimento = 1, 2 ou 3. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Data da internação
    # -------------------------------------------------------------------------

    dt_internacao = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da internação",
        help_text="Se hospitalar, data da internação. Deve ser >= data do atendimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - UF do hospital
    # -------------------------------------------------------------------------

    co_uf_hospital = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF do hospital",
        help_text="Sigla da UF onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Município do hospital
    # -------------------------------------------------------------------------

    co_municipio_hospital = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município do hospital",
        help_text="Código do município onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Nome do hospital
    # -------------------------------------------------------------------------

    co_unidade_hospital = models.DecimalField(
        max_digits=8,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Código do hospital",
        help_text="Código da unidade hospitalar.",
    )
    no_unidade_hospital = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Nome do hospital",
        help_text="Nome do hospital onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Material colhido (Fezes e Vômito)
    # -------------------------------------------------------------------------

    st_materia_colhido_fezes = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Material colhido - Fezes",
        help_text="Se foi colhido fezes para exame.",
    )
    st_materia_colhido_vomito = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Material colhido - Vômito",
        help_text="Se foi colhido vômito para exame.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Data da coleta
    # -------------------------------------------------------------------------

    dt_coleta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta",
        help_text="Obrigatório se fezes ou vômito colhidos = Sim. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Uso de antibiótico antes da coleta
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
    # Campo 53 - Qual antibiótico
    # -------------------------------------------------------------------------

    ds_uso_antibiotico = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Antibiótico utilizado",
        help_text="Especificação do antibiótico usado.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Resultado
    # -------------------------------------------------------------------------

    class ResultadoExame(models.TextChoices):
        POSITIVO = '1', 'Positivo'
        NEGATIVO = '2', 'Negativo'

    st_resultado = models.CharField(
        max_length=1,
        choices=ResultadoExame.choices,
        null=True,
        blank=True,
        verbose_name="Resultado",
        help_text="Se o exame foi positivo ou negativo.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Caso positivo (sorotipo)
    # -------------------------------------------------------------------------

    class Sorotipo(models.TextChoices):
        OGAWA = '1', 'Ogawa'
        INABA = '2', 'Inaba'
        HIKOJIMA = '3', 'Hikoijima'
        OUTRO_SOROTIPO = '4', 'Outro sorotipo'
        NAO_VIBRIO = '5', 'Não vibrio'

    tp_caso_positivo = models.CharField(
        max_length=1,
        choices=Sorotipo.choices,
        null=True,
        blank=True,
        verbose_name="Sorotipo",
        help_text="Sorotipo identificado no caso positivo.",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - Caso negativo (especificar outro agente)
    # -------------------------------------------------------------------------

    ds_caso_negativo = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Caso negativo - especificar",
        help_text="Outro agente etiológico identificado.",
    )

    # -------------------------------------------------------------------------
    # Campo 57 - Reidratação
    # -------------------------------------------------------------------------

    class Reidratacao(models.TextChoices):
        VIA_ORAL = '1', 'Via oral'
        VENOSA = '2', 'Venosa'
        ORAL_VENOSA = '3', 'Oral - Venosa'

    tp_reidratacao = models.CharField(
        max_length=1,
        choices=Reidratacao.choices,
        null=True,
        blank=True,
        verbose_name="Reidratação",
        help_text="Tipo de tratamento recebido pelo paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 58 - Utilizou antibióticos
    # -------------------------------------------------------------------------

    st_utilizou_antibiotico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Utilizou antibióticos",
        help_text="Se o paciente foi tratado com antibióticos.",
    )

    # -------------------------------------------------------------------------
    # Campo 59 - Qual antibiótico
    # -------------------------------------------------------------------------

    ds_utilizou_antibiotico = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Antibiótico utilizado no tratamento",
        help_text="Especificação do antibiótico utilizado no tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 60 - Classificação final
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
        help_text="Classificação final do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 61 - Critério de confirmação/descarte
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
        help_text="Define se o caso foi confirmado por laboratório ou clínico-epidemiológico.",
    )

    # -------------------------------------------------------------------------
    # Campo 62 - O caso é autóctone de residência?
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
    # Campo 63 - UF (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_uf_infeccao = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF provável da infecção",
        help_text="Unidade Federada onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 64 - País (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_pais_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="País provável da infecção",
        help_text="País onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 65 - Município (provável da fonte de infecção)
    # -------------------------------------------------------------------------

    co_municipio_infeccao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município provável da infecção",
        help_text="Código do município onde o paciente foi provavelmente infectado.",
    )

    # -------------------------------------------------------------------------
    # Campo 66 - Distrito (provável de infecção)
    # -------------------------------------------------------------------------

    co_distrito_infeccao = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Distrito provável da infecção",
        help_text="Código do distrito provável de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 67 - Bairro (provável de infecção)
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
    # Campo 69 - Evolução do caso
    # -------------------------------------------------------------------------

    class EvolucaoCaso(models.TextChoices):
        CURA = '1', 'Cura'
        OBITO_COLERA = '2', 'Óbito por cólera'
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
    # Campo 70 - Data do óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito, obrigatória se evolução = 2 ou 3.",
    )

    # -------------------------------------------------------------------------
    # Campo 71 - Data do encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento",
        help_text="Obrigatório quando classificação final estiver preenchido. Deve ser >= data da investigação.",
    )

    # -------------------------------------------------------------------------
    # Informações complementares - Deslocamento (3 conjuntos)
    # -------------------------------------------------------------------------

    dt_complementar_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de deslocamento 1",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )
    dt_complementar_2 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de deslocamento 2",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )
    dt_complementar_3 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de deslocamento 3",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )

    co_uf_complementar_1 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de deslocamento 1",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )
    co_uf_complementar_2 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de deslocamento 2",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )
    co_uf_complementar_3 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF de deslocamento 3",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )

    co_municipio_complementar_1 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município de deslocamento 1",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )
    co_municipio_complementar_2 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município de deslocamento 2",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )
    co_municipio_complementar_3 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município de deslocamento 3",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )

    co_pais_complementar_1 = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="País de deslocamento 1",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )
    co_pais_complementar_2 = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="País de deslocamento 2",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )
    co_pais_complementar_3 = models.DecimalField(
        max_digits=3,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="País de deslocamento 3",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )

    ds_complementar_meio_transp_1 = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Meio de transporte 1",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )
    ds_complementar_meio_transp_2 = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Meio de transporte 2",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )
    ds_complementar_meio_transp_3 = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Meio de transporte 3",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )

    # -------------------------------------------------------------------------
    # Informações complementares - Alimentos consumidos (4 itens)
    # -------------------------------------------------------------------------

    ds_complementar_tp_alimento_1 = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Tipo de alimento 1",
        help_text="Alimentos consumidos na última semana e sugestivos de contaminação.",
    )
    ds_complementar_tp_alimento_2 = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Tipo de alimento 2",
        help_text="Alimentos consumidos na última semana e sugestivos de contaminação.",
    )
    ds_complementar_tp_alimento_3 = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Tipo de alimento 3",
        help_text="Alimentos consumidos na última semana e sugestivos de contaminação.",
    )
    ds_complementar_tp_alimento_4 = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Tipo de alimento 4",
        help_text="Alimentos consumidos na última semana e sugestivos de contaminação.",
    )

    ds_complementar_local_1 = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Local de consumo 1",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )
    ds_complementar_local_2 = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Local de consumo 2",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )
    ds_complementar_local_3 = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Local de consumo 3",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
    )
    ds_complementar_local_4 = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="Local de consumo 4",
        help_text="Dado não exportado, disponível na notificação visualizada pelo Sinan.",
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
        db_table = 'colera'
        verbose_name = 'Cólera'
        verbose_name_plural = 'Cólera'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Cólera – {self.dt_investigacao}"