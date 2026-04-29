from django.db import models


class Coqueluche(models.Model):
    """
    Ficha de Investigação - Coqueluche
    Dicionário de Dados SINAN NET - Versão 5.0
    Revisado fevereiro/2012
    Campos 31 a 64 + campos de controle
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
        help_text="Data completa do início da investigação. Deve ser >= data da notificação e <= data atual.",
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
    # Campo 33 - A Unidade Notificante É Sentinela?
    # -------------------------------------------------------------------------

    st_unidade_sentinela = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Unidade notificante é sentinela",
        help_text="Informa se a unidade de saúde que notificou o caso é considerada sentinela.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Contato com caso suspeito ou confirmado de coqueluche
    # -------------------------------------------------------------------------

    class ContatoCoqueluche(models.TextChoices):
        DOMICILIO = '1', 'Domicílio'
        VIZINHANCA = '2', 'Vizinhança'
        TRABALHO = '3', 'Trabalho'
        CRECHE_ESCOLA = '4', 'Creche/escola'
        POSTO_SAUDE_HOSPITAL = '5', 'Posto de saúde/hospital'
        OUTRO_ESTADO_MUNICIPIO = '6', 'Outro Estado/Município'
        OUTRO = '7', 'Outro'
        SEM_HISTORIA_CONTATO = '8', 'Sem história de contato'
        IGNORADO = '9', 'Ignorado'

    tp_contato_coqueluche = models.CharField(
        max_length=1,
        choices=ContatoCoqueluche.choices,
        null=True,
        blank=True,
        verbose_name="Contato com caso suspeito ou confirmado",
        help_text="Local em que o paciente teve contato com caso semelhante nos últimos 14 dias.",
    )
    ds_contato_coqueluche_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro contato (especificar)",
        help_text="Especificação quando contato = 7 (Outro).",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Nome do Contato
    # -------------------------------------------------------------------------

    no_contato = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Nome do contato",
        help_text="Nome completo do contato.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Endereço do Contato
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
    # Campo 37 - Nº de doses de vacina tríplice (DPT) ou tetravalente (DTP + Hib)
    # -------------------------------------------------------------------------

    class DosesVacina(models.TextChoices):
        UMA = '1', 'Uma'
        DUAS = '2', 'Duas'
        TRES = '3', 'Três'
        TRES_MAIS_1_REFORCO = '4', 'Três + 1 Reforço'
        TRES_MAIS_2_REFORCOS = '5', 'Três + 2 Reforços'
        NUNCA_VACINADO = '6', 'Nunca Vacinado'
        IGNORADO = '9', 'Ignorado'

    tp_dose_vacina = models.CharField(
        max_length=1,
        choices=DosesVacina.choices,
        null=True,
        blank=True,
        verbose_name="Nº de doses da vacina",
        help_text="Número de doses da vacina tríplice (DPT) ou tetravalente (DTP+Hib) recebidas.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Data da Última Dose
    # -------------------------------------------------------------------------

    dt_ultima_dose = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da última dose",
        help_text="Data da última dose da vacina tríplice (DTP) recebida. Deve ser > data de nascimento e <= data atual.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Data do Início da Tosse
    # -------------------------------------------------------------------------

    dt_inicio_tosse = models.DateField(
        verbose_name="Data do início da tosse",
        help_text="Data do início da tosse. Deve ser inferior a 14 dias antes da data de notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Sinais e Sintomas
    # -------------------------------------------------------------------------

    st_sinais_tosse = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Tosse",
        help_text="Informa se o paciente apresentou tosse.",
    )
    st_sinais_tosse_paroxistica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Tosse paroxística",
        help_text="Informa se o paciente apresentou tosse paroxística (tosse súbita incontrolável com tossidas rápidas e curtas).",
    )
    st_sinais_respiracao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Respiração ruidosa (guincho)",
        help_text="Informa se o paciente apresentou respiração ruidosa ao final da crise de tosse (guincho).",
    )
    st_sinais_cianose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Cianose",
        help_text="Informa se o paciente apresentou cianose.",
    )
    st_sinais_vomito = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Vômitos pós-tosse",
        help_text="Informa se o paciente apresentou vômitos pós-tosse.",
    )
    st_sinais_apneia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Apnéia",
        help_text="Informa se o paciente apresentou apnéia.",
    )
    st_sinais_temperatura_menor_38 = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Temperatura < 38°C",
        help_text="Informa se o paciente apresentou temperatura < 38°C.",
    )
    st_sinais_temperatura_maior_38 = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Temperatura >= 38°C",
        help_text="Informa se o paciente apresentou temperatura >= 38°C.",
    )
    st_sinais_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outros sinais/sintomas",
        help_text="Informa se o paciente apresentou outros sintomas.",
    )
    ds_sinais_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outros sinais/sintomas (especificar)",
        help_text="Especificação de outros sinais e sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Complicações
    # -------------------------------------------------------------------------

    st_complicacao_pneumonia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pneumonia ou broncopneumonia",
        help_text="Informa se o paciente apresentou pneumonia ou broncopneumonia.",
    )
    st_complicacao_encefalopatia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Encefalopatia (convulsões)",
        help_text="Informa se o paciente apresentou encefalopatia (convulsões).",
    )
    st_complicacao_desidratacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Desidratação",
        help_text="Informa se o paciente apresentou desidratação.",
    )
    st_complicacao_otite = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Otite",
        help_text="Informa se o paciente apresentou otite.",
    )
    st_complicacao_desnutricao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Desnutrição",
        help_text="Informa se o paciente apresentou desnutrição.",
    )
    st_complicacao_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outras complicações",
        help_text="Informa se o paciente apresentou outras complicações.",
    )
    ds_complicacao_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outras complicações (especificar)",
        help_text="Especificação de outras complicações.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Ocorreu Hospitalização
    # -------------------------------------------------------------------------

    st_ocorreu_hospitalizacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Ocorreu hospitalização",
        help_text="Informa se o paciente foi hospitalizado.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Data da Internação
    # -------------------------------------------------------------------------

    dt_internacao = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da internação",
        help_text="Data de internação. Obrigatório se hospitalização = Sim.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - UF do Hospital
    # -------------------------------------------------------------------------

    co_uf_hospital = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF do hospital",
        help_text="Sigla da UF onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Município do Hospital
    # -------------------------------------------------------------------------

    co_municipio_hospital = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município do hospital",
        help_text="Código do município onde está localizado o hospital.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Nome do Hospital
    # -------------------------------------------------------------------------

    co_unidade_hospital = models.DecimalField(
        max_digits=8,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Código do hospital (CNES)",
        help_text="Código do hospital onde o paciente foi internado (CNES).",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Utilizou Antibiótico
    # -------------------------------------------------------------------------

    st_utilizou_antibiotico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Utilizou antibiótico",
        help_text="Informa se o paciente fez uso de antibióticos/antimicrobianos no tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Data da Administração do Antibiótico
    # -------------------------------------------------------------------------

    dt_antibiotico = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da administração do antibiótico",
        help_text="Data da administração do antibiótico. Obrigatório se utilizou antibiótico = Sim.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Coleta de Material da Nasofaringe
    # -------------------------------------------------------------------------

    st_coleta_material = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Coleta de material da nasofaringe",
        help_text="Informa se foi realizada coleta de material da nasofaringe.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Data da Coleta do Material
    # -------------------------------------------------------------------------

    dt_coleta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta do material",
        help_text="Data da coleta do material da nasofaringe. Obrigatório se coleta = Sim.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Resultado da Cultura
    # -------------------------------------------------------------------------

    class ResultadoCultura(models.TextChoices):
        POSITIVA = '1', 'Positiva'
        NEGATIVA = '2', 'Negativa'
        NAO_REALIZADA = '3', 'Não realizada'
        IGNORADO = '9', 'Ignorado'

    tp_resultado_cultura = models.CharField(
        max_length=1,
        choices=ResultadoCultura.choices,
        null=True,
        blank=True,
        verbose_name="Resultado da cultura",
        help_text="Resultado da cultura do material da nasofaringe (Bordetella pertussis).",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Realizada Identificação dos Comunicantes Íntimos
    # -------------------------------------------------------------------------

    st_identificacao_comunicante = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Identificação dos comunicantes íntimos",
        help_text="Informa se foram identificados comunicantes íntimos.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Se Sim, Quantos?
    # -------------------------------------------------------------------------

    qt_identificacao = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Quantidade de comunicantes íntimos",
        help_text="Número de comunicantes íntimos identificados.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Quantos Casos Secundários Foram Confirmados Entre os Comunicantes
    # -------------------------------------------------------------------------

    class CasosSecundarios(models.TextChoices):
        NENHUM = '0', 'Nenhum'
        UM = '1', 'Um'
        DOIS_OU_MAIS = '2', 'Dois ou mais'
        IGNORADO = '9', 'Ignorado'

    tp_caso_confirmado = models.CharField(
        max_length=1,
        choices=CasosSecundarios.choices,
        null=True,
        blank=True,
        verbose_name="Casos secundários confirmados",
        help_text="Número de casos secundários identificados entre os comunicantes.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Realizada Coleta de Material da Nasofaringe dos Comunicantes
    # -------------------------------------------------------------------------

    st_coleta_material_comunicante = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Coleta de material dos comunicantes",
        help_text="Informa se foi realizada coleta de material da nasofaringe dos comunicantes.",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - Se Sim, em Quantos?
    # -------------------------------------------------------------------------

    qt_comunicante = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Quantidade de comunicantes com coleta",
        help_text="Número de comunicantes em que foi coletado o material.",
    )

    # -------------------------------------------------------------------------
    # Campo 57 - Em Quantos Comunicantes o Resultado da Cultura Foi Positivo?
    # -------------------------------------------------------------------------

    nu_comunicante_positivo = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Comunicantes com cultura positiva",
        help_text="Número de comunicantes com resultado da cultura positivo.",
    )

    # -------------------------------------------------------------------------
    # Campo 58 - Medidas de Prevenção/Controle
    # -------------------------------------------------------------------------

    class MedidaControle(models.TextChoices):
        BLOQUEIO_VACINAL = '1', 'Bloqueio vacinal'
        QUIMIOPROFILAXIA = '2', 'Quimioprofilaxia'
        AMBOS = '3', 'Ambos'
        NAO = '4', 'Não'
        IGNORADO = '9', 'Ignorado'

    tp_medida_controle = models.CharField(
        max_length=1,
        choices=MedidaControle.choices,
        null=True,
        blank=True,
        verbose_name="Medidas de prevenção/controle",
        help_text="Informa se foi realizado bloqueio e qual tipo.",
    )

    # -------------------------------------------------------------------------
    # Campo 59 - Classificação Final
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
    # Campo 60 - Critério de Confirmação/Descarte
    # -------------------------------------------------------------------------

    class CriterioConfirmacao(models.TextChoices):
        LABORATORIAL = '1', 'Laboratorial'
        VINCULO_EPIDEMIOLOGICO = '2', 'Vínculo Epidemiológico'
        CLINICO = '3', 'Clínico'

    tp_criterio_confirmacao = models.CharField(
        max_length=1,
        choices=CriterioConfirmacao.choices,
        null=True,
        blank=True,
        verbose_name="Critério de confirmação/descarte",
        help_text="Critério utilizado para confirmação do caso ou descarte do suspeito.",
    )

    # -------------------------------------------------------------------------
    # Campo 61 - Doença Relacionada ao Trabalho
    # -------------------------------------------------------------------------

    st_doenca_trabalho = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Doença relacionada ao trabalho",
        help_text="Se a doença adquirida está relacionada às condições/situação de trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 62 - Evolução
    # -------------------------------------------------------------------------

    class EvolucaoCaso(models.TextChoices):
        CURA = '1', 'Cura'
        OBITO_COQUELUCHE = '2', 'Óbito por coqueluche'
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
    # Campo 63 - Data do Óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito. Obrigatório se evolução = 2 ou 3.",
    )

    # -------------------------------------------------------------------------
    # Campo 64 - Data do Encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento",
        help_text="Data do encerramento do caso. Obrigatório se classificação final preenchida.",
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
        db_table = 'coqueluche'
        verbose_name = 'Coqueluche'
        verbose_name_plural = 'Coqueluche'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Coqueluche – {self.dt_investigacao}"