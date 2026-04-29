from django.db import models


class Difteria(models.Model):
    """
    Ficha de Investigação - Difteria
    Dicionário de Dados SINAN NET - Versão 5.0
    Campos 31 a 66 + campos de controle
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
    # Campo 31 - Data da Investigação
    # -------------------------------------------------------------------------

    dt_investigacao = models.DateField(
        verbose_name="Data da investigação",
        help_text="Data em que ocorreu a investigação (1ª ação desenvolvida após a notificação). Deve ser >= data da notificação.",
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
    # Campo 33 - Contato Com Caso Suspeito ou Confirmado de Difteria
    # -------------------------------------------------------------------------

    class ContatoDifteria(models.TextChoices):
        DOMICILIO = '1', 'Domicílio'
        VIZINHANCA = '2', 'Vizinhança'
        TRABALHO = '3', 'Trabalho'
        CRECHE_ESCOLA = '4', 'Creche/escola'
        POSTO_SAUDE_HOSPITAL = '5', 'Posto de saúde/hospital'
        OUTRO_ESTADO_MUNICIPIO = '6', 'Outro Estado/Município'
        OUTRO = '7', 'Outro'
        SEM_HISTORIA_CONTATO = '8', 'Sem história de contato'
        IGNORADO = '9', 'Ignorado'

    tp_contato_difteria = models.CharField(
        max_length=1,
        choices=ContatoDifteria.choices,
        null=True,
        blank=True,
        verbose_name="Contato com caso suspeito ou confirmado",
        help_text="Local em que o paciente teve contato com caso semelhante nas últimas 2 semanas.",
    )
    ds_contato_difteria_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro contato (especificar)",
        help_text="Especificação quando contato = 7 (Outro).",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Nome do Contato
    # -------------------------------------------------------------------------

    no_contato = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Nome do contato",
        help_text="Nome completo do contato.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Endereço do Contato
    # -------------------------------------------------------------------------

    no_endereco_contato = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Endereço do contato",
        help_text="Endereço completo do contato.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - N.º de Doses da Vacina Tríplice (DTP) ou Tetravalente (DTP+Hib) ou Dupla (DT ou dT)
    # -------------------------------------------------------------------------

    class DosesVacina(models.TextChoices):
        UMA = '1', 'Uma'
        DUAS = '2', 'Duas'
        TRES = '3', 'Três'
        TRES_MAIS_1_REFORCO = '4', 'Três + 1 reforço'
        TRES_MAIS_2_REFORCOS = '5', 'Três + 2 reforços'
        NUNCA_VACINADO = '6', 'Nunca vacinado'
        IGNORADO = '9', 'Ignorado'

    tp_dose_vacina = models.CharField(
        max_length=1,
        choices=DosesVacina.choices,
        null=True,
        blank=True,
        verbose_name="Nº de doses da vacina",
        help_text="Número de doses da vacina tríplice (DTP) ou tetravalente (DTP+Hib) ou dupla (DT ou dT) recebidas.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Data da última dose
    # -------------------------------------------------------------------------

    dt_ultima_dose = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da última dose",
        help_text="Data da última dose da vacina. Não pode ser posterior à data de notificação, nem anterior à data de nascimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Sinais e Sintomas (6 subcampos)
    # -------------------------------------------------------------------------

    st_sinais_edema_ganglionar = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Edema ganglionar",
        help_text="Informa se o paciente apresentou edema ganglionar.",
    )
    st_sinais_edema_pescoco = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Edema de pescoço",
        help_text="Informa se o paciente apresentou edema de pescoço.",
    )
    st_sinais_febre = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Febre",
        help_text="Informa se o paciente apresentou febre.",
    )
    st_sinais_prostracao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Prostração",
        help_text="Informa se o paciente apresentou prostração.",
    )
    st_sinais_pseudomembrana = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pseudomembrana",
        help_text="Informa se o paciente apresentou pseudomembranas.",
    )
    st_sinais_palidez = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Palidez",
        help_text="Informa se o paciente apresentou palidez.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Temperatura Corporal
    # -------------------------------------------------------------------------

    nu_temperatura_corporal = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Temperatura corporal (°C)",
        help_text="Temperatura corporal apresentada durante a fase inicial da doença, em graus centígrados.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Localização da Pseudomembrana (Placas) - 11 subcampos
    # -------------------------------------------------------------------------

    st_pseudomembrana_nasal = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pseudomembrana - Cavidade Nasal",
        help_text="Informa se a pseudomembrana está localizada na cavidade nasal.",
    )
    st_pseudomembrana_amigdala = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pseudomembrana - Amígdalas",
        help_text="Informa se a pseudomembrana está localizada nas amígdalas.",
    )
    st_pseudomembrana_cordao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pseudomembrana - Cordão Umbilical",
        help_text="Informa se a pseudomembrana está localizada no cordão umbilical.",
    )
    st_pseudomembrana_faringe = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pseudomembrana - Faringe",
        help_text="Informa se a pseudomembrana está localizada na faringe.",
    )
    st_pseudomembrana_laringe = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pseudomembrana - Laringe",
        help_text="Informa se a pseudomembrana está localizada na laringe.",
    )
    st_pseudomembrana_genital = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pseudomembrana - Órgãos Genitais",
        help_text="Informa se a pseudomembrana está localizada nos órgãos genitais.",
    )
    st_pseudomembrana_palato = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pseudomembrana - Palato",
        help_text="Informa se a pseudomembrana está localizada no palato.",
    )
    st_pseudomembrana_auditivo = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pseudomembrana - Conduto Auditivo",
        help_text="Informa se a pseudomembrana está localizada no conduto auditivo.",
    )
    st_pseudomembrana_traqueia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pseudomembrana - Traquéia",
        help_text="Informa se a pseudomembrana está localizada na traquéia.",
    )
    st_pseudomembrana_pele = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pseudomembrana - Pele",
        help_text="Informa se a pseudomembrana está localizada na pele.",
    )
    st_pseudomembrana_conjuntiva = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pseudomembrana - Conjuntiva",
        help_text="Informa se a pseudomembrana está localizada na conjuntiva.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Complicações (7 subcampos)
    # -------------------------------------------------------------------------

    st_complicacao_miocardite = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Miocardite",
        help_text="Informa se a complicação foi miocardite.",
    )
    st_complicacao_nefrite = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Nefrite",
        help_text="Informa se a complicação foi nefrite.",
    )
    st_complicacao_paralisia_bilateral = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Paralisia bilateral e simétrica das extremidades",
        help_text="Informa se a complicação foi paralisia bilateral e simétrica das extremidades.",
    )
    st_complicacao_paralisia_palato = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Paralisia do palato",
        help_text="Informa se a complicação foi paralisia do palato (regurgitação, líquido pelo nariz, voz anasalada).",
    )
    st_complicacao_arritmia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Arritmias cardíacas",
        help_text="Informa se a complicação foram arritmias cardíacas.",
    )
    st_complicacao_paralisia_musculos = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Paralisia dos músculos intercostais e diafragma",
        help_text="Informa se a complicação foi paralisia dos músculos intercostais e diafragma.",
    )
    st_complicacao_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outras complicações",
        help_text="Informa se houve outras complicações não especificadas.",
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
        help_text="Informa se o paciente foi internado devido ao agravo.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Data da Internação
    # -------------------------------------------------------------------------

    dt_internacao = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da internação",
        help_text="Data de internação. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - UF
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
        help_text="Código do município onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Nome do Hospital
    # -------------------------------------------------------------------------

    co_unidade_hospital = models.DecimalField(
        max_digits=8,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Código do hospital",
        help_text="Código da unidade hospitalar (CNES).",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Material Coletado
    # -------------------------------------------------------------------------

    class MaterialColetado(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        NAO_COLETADO = '4', 'Não coletado'
        IGNORADO = '9', 'Ignorado'

    st_material_coletado = models.CharField(
        max_length=1,
        choices=MaterialColetado.choices,
        null=True,
        blank=True,
        verbose_name="Material coletado",
        help_text="Informa se material foi coletado para exame.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Data da Coleta
    # -------------------------------------------------------------------------

    dt_coleta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta",
        help_text="Data em que foi colhido o material. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Cultura para Difteria
    # -------------------------------------------------------------------------

    class CulturaDifteria(models.TextChoices):
        POSITIVA_C_DIPHTHERIAE = '1', 'Positiva para C. diphteriae'
        NEGATIVA_C_DIPHTHERIAE = '2', 'Negativa para C. diphteriae'
        NAO_REALIZADA = '3', 'Não realizada'
        IGNORADO = '9', 'Ignorado'

    tp_cultura_difteria = models.CharField(
        max_length=1,
        choices=CulturaDifteria.choices,
        null=True,
        blank=True,
        verbose_name="Cultura para difteria",
        help_text="Resultado da cultura para C. diphtheriae.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Provas de Toxigenicidade
    # -------------------------------------------------------------------------

    class ProvaToxigenicidade(models.TextChoices):
        POSITIVA = '1', 'Positiva'
        NEGATIVA = '2', 'Negativa'
        NAO_REALIZADA = '3', 'Não realizada'
        IGNORADO = '9', 'Ignorado'

    tp_prova_toxigenicidade = models.CharField(
        max_length=1,
        choices=ProvaToxigenicidade.choices,
        null=True,
        blank=True,
        verbose_name="Provas de toxigenicidade",
        help_text="Resultado das provas de toxigenicidade.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Data da Aplicação do Soro
    # -------------------------------------------------------------------------

    dt_aplicacao_soro = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da aplicação do soro",
        help_text="Data de aplicação do soro. Não pode ser anterior à data de internação.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Antibiótico
    # -------------------------------------------------------------------------

    st_antibiotico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Antibiótico",
        help_text="Informa se o paciente foi tratado com antibiótico.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Data da Administração do Antibiótico
    # -------------------------------------------------------------------------

    dt_antibiotico = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da administração do antibiótico",
        help_text="Data de início da administração do antibiótico. Deve ser > data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Realizada Identificação dos Comunicantes Íntimos
    # -------------------------------------------------------------------------

    st_comunicante_intimo = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Identificação dos comunicantes íntimos",
        help_text="Informa se foi realizada identificação dos comunicantes íntimos.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Se Sim, Quantos?
    # -------------------------------------------------------------------------

    qt_comunicante_intimo = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Quantidade de comunicantes íntimos",
        help_text="Número de comunicantes íntimos identificados.",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - Quantos casos secundários foram confirmados entre os comunicantes
    # -------------------------------------------------------------------------

    class CasosSecundarios(models.TextChoices):
        NENHUM = '1', 'Nenhum'
        UM = '2', 'Um'
        DOIS_OU_MAIS = '3', 'Dois ou mais'
        IGNORADO = '9', 'Ignorado'

    tp_comunicante_confirmado = models.CharField(
        max_length=1,
        choices=CasosSecundarios.choices,
        null=True,
        blank=True,
        verbose_name="Casos secundários confirmados",
        help_text="Número de casos secundários confirmados entre os comunicantes.",
    )

    # -------------------------------------------------------------------------
    # Campo 57 - Realizada Coleta de Material dos Comunicantes
    # -------------------------------------------------------------------------

    st_comunicante_material = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Coleta de material dos comunicantes",
        help_text="Informa se foi realizada coleta de material de comunicantes.",
    )

    # -------------------------------------------------------------------------
    # Campo 58 - Se Sim, Em Quantos?
    # -------------------------------------------------------------------------

    qt_comunicante_material = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Comunicantes com coleta de material",
        help_text="Número de comunicantes em que foi coletado o material.",
    )

    # -------------------------------------------------------------------------
    # Campo 59 - Quantos portadores foram identificados entre os comunicantes?
    # -------------------------------------------------------------------------

    qt_comunicante_portador = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Portadores identificados",
        help_text="Número de portadores identificados entre os comunicantes.",
    )

    # -------------------------------------------------------------------------
    # Campo 60 - Medidas de Prevenção/Controle
    # -------------------------------------------------------------------------

    class MedidaPrevencao(models.TextChoices):
        BLOQUEIO_VACINAL = '1', 'Bloqueio vacinal'
        QUIMIOPROFILAXIA = '2', 'Quimioprofilaxia'
        AMBOS = '3', 'Ambos'
        NAO = '4', 'Não'
        IGNORADO = '9', 'Ignorado'

    st_medida_prevencao = models.CharField(
        max_length=1,
        choices=MedidaPrevencao.choices,
        null=True,
        blank=True,
        verbose_name="Medidas de prevenção/controle",
        help_text="Tipo de bloqueio realizado.",
    )

    # -------------------------------------------------------------------------
    # Campo 61 - Classificação Final
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
        help_text="Classificação final da notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 62 - Critério de Confirmação/Descarte
    # -------------------------------------------------------------------------

    class CriterioConfirmacao(models.TextChoices):
        CULTURA_COM_TOXIGENICIDADE = '1', 'Cultura com prova de toxigenicidade'
        CULTURA_SEM_TOXIGENICIDADE = '2', 'Cultura sem prova de toxigenicidade'
        VINCULO_EPIDEMIOLOGICO = '3', 'Vínculo epidemiológico'
        MORTE_POS_CLINICA_COMPATIVEL = '4', 'Morte pós clínica compatível'
        CLINICO = '5', 'Clínico'
        NECROPSIA = '6', 'Necrópsia'

    tp_criterio_confirmacao = models.CharField(
        max_length=1,
        choices=CriterioConfirmacao.choices,
        null=True,
        blank=True,
        verbose_name="Critério de confirmação/descarte",
        help_text="Critério utilizado para confirmação do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 63 - Doença Relacionada ao Trabalho
    # -------------------------------------------------------------------------

    st_doenca_trabalho = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Doença relacionada ao trabalho",
        help_text="Informa se o paciente adquiriu a doença em decorrência das condições/situação de trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 64 - Evolução
    # -------------------------------------------------------------------------

    class EvolucaoCaso(models.TextChoices):
        CURA_COM_SEQUELA = '1', 'Cura com sequela'
        CURA_SEM_SEQUELA = '2', 'Cura sem sequela'
        OBITO_POR_DIFTERIA = '3', 'Óbito por difteria'
        OBITO_POR_OUTRAS_CAUSAS = '4', 'Óbito por outras causas'
        IGNORADO = '9', 'Ignorado'

    tp_evolucao_caso = models.CharField(
        max_length=1,
        choices=EvolucaoCaso.choices,
        null=True,
        blank=True,
        verbose_name="Evolução do caso",
        help_text="Evolução do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 65 - Data do Óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito. Obrigatório se evolução = 3 ou 4. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 66 - Data do Encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento",
        help_text="Data do encerramento da investigação. Obrigatório quando classificação final preenchida.",
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
        db_table = 'difteria'
        verbose_name = 'Difteria'
        verbose_name_plural = 'Difteria'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Difteria – {self.dt_investigacao}"