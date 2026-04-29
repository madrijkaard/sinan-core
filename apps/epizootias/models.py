from django.db import models


class Epizootias(models.Model):
    """
    Ficha de Investigação - Epizootias
    Dicionário de Dados SINAN NET - Versão 5.0
    Campos 1 a 29 + campos de controle e campos internos
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
    # Campo - Número da notificação (antes do campo 1)
    # -------------------------------------------------------------------------

    nu_notificacao = models.CharField(
        max_length=7,
        verbose_name="Número da notificação",
        help_text="Número da notificação - chave para identificação do registro no sistema.",
    )

    # -------------------------------------------------------------------------
    # Campo 1 - Tipo de Notificação
    # -------------------------------------------------------------------------

    tp_notificacao = models.CharField(
        max_length=1,
        default='2',
        verbose_name="Tipo de notificação",
        help_text="Identifica o tipo da notificação. Preenchido com 2 (Individual).",
    )

    # -------------------------------------------------------------------------
    # Campo 2 - Agravo
    # -------------------------------------------------------------------------

    id_agravo = models.CharField(
        max_length=4,
        verbose_name="Agravo",
        help_text="Código do agravo notificado (EPIZOOTIA).",
    )

    # -------------------------------------------------------------------------
    # Campo 3 - Data da notificação
    # -------------------------------------------------------------------------

    dt_notificacao = models.DateField(
        verbose_name="Data da notificação",
        help_text="Data da notificação - chave para identificação do registro no sistema.",
    )

    # -------------------------------------------------------------------------
    # Campo 4 - UF de notificação
    # -------------------------------------------------------------------------

    sg_uf_not = models.CharField(
        max_length=2,
        verbose_name="UF de notificação",
        help_text="UF de notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 5 - Município de Notificação
    # -------------------------------------------------------------------------

    id_municipio = models.CharField(
        max_length=6,
        verbose_name="Município de notificação",
        help_text="Código do município de notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 6 - Unidade de Saúde (ou outra fonte notificadora)
    # -------------------------------------------------------------------------

    id_unidade = models.CharField(
        max_length=7,
        verbose_name="Unidade de saúde notificadora",
        help_text="Unidade que notificou o agravo.",
    )

    # -------------------------------------------------------------------------
    # Campo 7 - Data do início da epizootia
    # -------------------------------------------------------------------------

    dt_ini_epi = models.DateField(
        verbose_name="Data do início da epizootia",
        help_text="Data do início da epizootia. Não deve ser maior que a data da notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 8 - Fonte da informação
    # -------------------------------------------------------------------------

    ds_fonte_no = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Fonte da informação",
        help_text="Fonte da informação da epizootia.",
    )

    # -------------------------------------------------------------------------
    # Campo 9 - Telefone da fonte de informação
    # -------------------------------------------------------------------------

    nu_fon_fn = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        verbose_name="Telefone da fonte de informação",
        help_text="DDD e telefone da fonte de informação.",
    )

    # -------------------------------------------------------------------------
    # Campo 10 - UF de ocorrência
    # -------------------------------------------------------------------------

    co_uf_ocor = models.CharField(
        max_length=2,
        verbose_name="UF de ocorrência",
        help_text="UF de ocorrência da epizootia.",
    )

    # -------------------------------------------------------------------------
    # Campo 11 - Município de ocorrência
    # -------------------------------------------------------------------------

    co_mu_ocor = models.CharField(
        max_length=6,
        verbose_name="Município de ocorrência",
        help_text="Município de ocorrência da epizootia.",
    )

    # -------------------------------------------------------------------------
    # Campo 12 - Distrito
    # -------------------------------------------------------------------------

    co_di_ocor = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Distrito de ocorrência",
        help_text="Distrito de ocorrência da epizootia.",
    )

    # -------------------------------------------------------------------------
    # Campo 13 - Bairro
    # -------------------------------------------------------------------------

    no_ba_ocor = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Bairro de ocorrência",
        help_text="Bairro de ocorrência da epizootia.",
    )

    # -------------------------------------------------------------------------
    # Campo 14 - Logradouro
    # -------------------------------------------------------------------------

    no_log_oco = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Logradouro",
        help_text="Logradouro de ocorrência da epizootia.",
    )

    # -------------------------------------------------------------------------
    # Campo 15 - Número
    # -------------------------------------------------------------------------

    num_oco = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Número",
        help_text="Número do endereço.",
    )

    # -------------------------------------------------------------------------
    # Campo 16 - Complemento
    # -------------------------------------------------------------------------

    comp_oco = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Complemento",
        help_text="Complemento do endereço.",
    )

    # -------------------------------------------------------------------------
    # Campo 17 - Geo campo 1
    # -------------------------------------------------------------------------

    co_geo1 = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Geo campo 1",
        help_text="Coordenada geográfica 1.",
    )

    # -------------------------------------------------------------------------
    # Campo 18 - Geo campo 2
    # -------------------------------------------------------------------------

    co_geo2 = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Geo campo 2",
        help_text="Coordenada geográfica 2.",
    )

    # -------------------------------------------------------------------------
    # Campo 19 - Ponto de referência
    # -------------------------------------------------------------------------

    ds_ref_oco = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Ponto de referência",
        help_text="Ponto de referência do local.",
    )

    # -------------------------------------------------------------------------
    # Campo 20 - CEP
    # -------------------------------------------------------------------------

    nu_cep_oco = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name="CEP",
        help_text="CEP do local de ocorrência.",
    )

    # -------------------------------------------------------------------------
    # Campo 21 - (DDD) Telefone da fonte notificadora
    # -------------------------------------------------------------------------

    tel_oco = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        verbose_name="Telefone da fonte notificadora",
        help_text="DDD e telefone da fonte notificadora.",
    )

    # -------------------------------------------------------------------------
    # Campo 22 - Zona
    # -------------------------------------------------------------------------

    class ZonaOcorrencia(models.TextChoices):
        URBANA = '1', 'Urbana'
        RURAL = '2', 'Rural'
        PERIURBANA = '3', 'Periurbana'
        IGNORADO = '9', 'Ignorado'

    tp_zn_oco = models.CharField(
        max_length=1,
        choices=ZonaOcorrencia.choices,
        null=True,
        blank=True,
        verbose_name="Zona",
        help_text="Zona onde ocorreu a epizootia.",
    )

    # -------------------------------------------------------------------------
    # Campo 23 - Ambiente
    # -------------------------------------------------------------------------

    class Ambiente(models.TextChoices):
        DOMICILIO = '1', 'Domicílio'
        PARQUE_PRACA_ZOO = '2', 'Parque, praça ou zoológico'
        AREA_SILVESTRE = '3', 'Área Silvestre'
        RESERVA_ECOLOGICA = '4', 'Reserva ecológica'
        OUTRO = '5', 'Outro'

    tp_amb_oco = models.CharField(
        max_length=1,
        choices=Ambiente.choices,
        null=True,
        blank=True,
        verbose_name="Ambiente",
        help_text="Ambiente onde ocorreu a epizootia.",
    )
    ds_out_amb = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro ambiente (especificar)",
        help_text="Especificação quando ambiente = 5 (Outro).",
    )

    # -------------------------------------------------------------------------
    # Campo 24 - Houve coleta de material para exame laboratorial
    # -------------------------------------------------------------------------

    st_mat_col = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Houve coleta de material",
        help_text="Se houve coleta de material para exame laboratorial.",
    )

    # -------------------------------------------------------------------------
    # Campo 25 - Data da coleta do material
    # -------------------------------------------------------------------------

    dt_col_mat = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta do material",
        help_text="Data da coleta do material. Deve ser >= data de início da epizootia e <= data atual.",
    )

    # -------------------------------------------------------------------------
    # Campo 26 - Material coletado (11 subcampos)
    # -------------------------------------------------------------------------

    st_mat_fig = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Material coletado - Fígado",
        help_text="Se fígado foi coletado para exame laboratorial.",
    )
    st_mat_rim = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Material coletado - Rim",
        help_text="Se rim foi coletado para exame laboratorial.",
    )
    st_mat_baco = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Material coletado - Baço",
        help_text="Se baço foi coletado para exame laboratorial.",
    )
    st_mat_cer = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Material coletado - Cérebro",
        help_text="Se cérebro foi coletado para exame laboratorial.",
    )
    st_mat_cor = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Material coletado - Coração",
        help_text="Se coração foi coletado para exame laboratorial.",
    )
    st_mat_fez = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Material coletado - Fezes",
        help_text="Se fezes foram coletadas para exame laboratorial.",
    )
    st_mat_sor = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Material coletado - Soro",
        help_text="Se soro foi coletado para exame laboratorial.",
    )
    st_mat_sangue_total = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Material coletado - Sangue Total",
        help_text="Se sangue total foi coletado para exame laboratorial.",
    )
    st_mat_out = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Material coletado - Outro",
        help_text="Se outro material foi coletado para exame laboratorial.",
    )
    ds_mat_qual = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro material (especificar)",
        help_text="Especificação quando outro material = Sim.",
    )

    # -------------------------------------------------------------------------
    # Campo 27 - Animais acometidos (até 2 opções + Outros)
    # -------------------------------------------------------------------------

    class AnimalAcometido(models.TextChoices):
        AVE = '1', 'Ave'
        BOVIDEO = '2', 'Bovídeo'
        CANINO = '3', 'Canino'
        EQUIDEO = '4', 'Eqüídeo'
        FELINO = '5', 'Felino'
        MORCEGO = '6', 'Morcego'
        PRIMATA_NAO_HUMANO = '7', 'Primata não humano'
        CANIDEO_SILVESTRE = '8', 'Canídeo silvestre'
        OUTRO = '9', 'Outro'

    # Opção 1
    st_animal_acometido_1 = models.CharField(
        max_length=1,
        choices=AnimalAcometido.choices,
        null=True,
        blank=True,
        verbose_name="Animais acometidos - Opção 1",
        help_text="Primeiro tipo de animal acometido.",
    )
    nu_acometido_doente_1 = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name="Opção 1 - Doentes",
        help_text="Número de doentes - Opção 1.",
    )
    nu_acometido_morto_1 = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name="Opção 1 - Mortos",
        help_text="Número de mortos - Opção 1.",
    )

    # Opção 2
    st_animal_acometido_2 = models.CharField(
        max_length=1,
        choices=AnimalAcometido.choices,
        null=True,
        blank=True,
        verbose_name="Animais acometidos - Opção 2",
        help_text="Segundo tipo de animal acometido.",
    )
    nu_acometido_doente_2 = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name="Opção 2 - Doentes",
        help_text="Número de doentes - Opção 2.",
    )
    nu_acometido_morto_2 = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name="Opção 2 - Mortos",
        help_text="Número de mortos - Opção 2.",
    )

    # Outros (quando opção 1 ou 2 = 9)
    ds_animal_acometido = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Outros animais acometidos (especificar)",
        help_text="Especificação quando animal = 9 (Outro).",
    )

    # -------------------------------------------------------------------------
    # Campo 28 - Suspeita diagnóstica (1ª, 2ª e 3ª)
    # -------------------------------------------------------------------------

    class SuspeitaDiagnostica(models.TextChoices):
        RAIVA = '1', 'Raiva'
        ENCEFALITE_EQUINA = '2', 'Encefalite eqüina'
        FEBRE_NILO_OCIDENTAL = '3', 'Febre por Vírus do Nilo Ocidental'
        ENCEFALITE_ESPONGIFORME_BOVINA = '4', 'Encefalite espongiforme bovina'
        FEBRE_AMARELA = '5', 'Febre amarela'
        INFLUENZA_AVIARIA = '6', 'Influenza aviária'
        OUTRO = '7', 'Outro'

    tp_susp_1 = models.CharField(
        max_length=1,
        choices=SuspeitaDiagnostica.choices,
        null=True,
        blank=True,
        verbose_name="1ª Suspeita diagnóstica",
        help_text="Primeira suspeita diagnóstica.",
    )
    tp_susp_2 = models.CharField(
        max_length=1,
        choices=SuspeitaDiagnostica.choices,
        null=True,
        blank=True,
        verbose_name="2ª Suspeita diagnóstica",
        help_text="Segunda suspeita diagnóstica.",
    )
    tp_susp_3 = models.CharField(
        max_length=1,
        choices=SuspeitaDiagnostica.choices,
        null=True,
        blank=True,
        verbose_name="3ª Suspeita diagnóstica",
        help_text="Terceira suspeita diagnóstica.",
    )
    ds_su_out3 = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outra suspeita diagnóstica (especificar)",
        help_text="Especificação quando qualquer suspeita = 7 (Outro).",
    )

    # -------------------------------------------------------------------------
    # Campo 29 - Resultado laboratorial (8 subcampos)
    # -------------------------------------------------------------------------

    st_res_raiva = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Raiva",
        help_text="Resultado laboratorial para Raiva.",
    )
    st_res_encef_equina = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Encefalite eqüina",
        help_text="Resultado laboratorial para Encefalite eqüina.",
    )
    st_res_febre_nilo = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Febre do Nilo",
        help_text="Resultado laboratorial para Febre do Nilo Ocidental.",
    )
    st_res_espong_bovina = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Encefalite espongiforme bovina",
        help_text="Resultado laboratorial para Encefalite espongiforme bovina.",
    )
    st_res_febre_amarela = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Febre Amarela",
        help_text="Resultado laboratorial para Febre Amarela.",
    )
    st_res_influenza = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Influenza",
        help_text="Resultado laboratorial para Influenza aviária.",
    )
    st_res_out = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Outros",
        help_text="Resultado laboratorial para outros agravos.",
    )
    ds_res_esp = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Especificar outros resultados",
        help_text="Especificação quando outros resultados = Positivo.",
    )

    # -------------------------------------------------------------------------
    # Observações
    # -------------------------------------------------------------------------

    ds_observacao = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Observações",
        help_text="Observações a respeito do caso se necessário.",
    )

    # -------------------------------------------------------------------------
    # Campos internos (preenchidos automaticamente pelo sistema)
    # -------------------------------------------------------------------------

    sem_not = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        editable=False,
        verbose_name="Semana epidemiológica da notificação",
        help_text="Semana epidemiológica em que o caso foi notificado.",
    )
    nu_ano = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        editable=False,
        verbose_name="Ano da notificação",
        help_text="Ano da notificação.",
    )
    sem_pri = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        editable=False,
        verbose_name="Semana epidemiológica dos primeiros sintomas",
        help_text="Semana epidemiológica dos primeiros sintomas/diagnóstico.",
    )
    dt_digita = models.DateField(
        auto_now_add=True,
        editable=False,
        verbose_name="Data de digitação",
        help_text="Data de digitação da primeira inclusão da notificação no sistema.",
    )
    dt_transus = models.DateField(
        null=True,
        blank=True,
        editable=False,
        verbose_name="Data de transferência - Unidade de Saúde",
        help_text="Data de transferência do registro da Unidade de Saúde para nível superior.",
    )
    dt_transdm = models.DateField(
        null=True,
        blank=True,
        editable=False,
        verbose_name="Data de transferência - Distrito Municipal",
        help_text="Data de transferência do registro do Distrito Municipal para nível superior.",
    )
    dt_transsm = models.DateField(
        null=True,
        blank=True,
        editable=False,
        verbose_name="Data de transferência - Secretaria Municipal",
        help_text="Data de transferência do registro da Secretaria Municipal para nível superior.",
    )
    dt_transrm = models.DateField(
        null=True,
        blank=True,
        editable=False,
        verbose_name="Data de transferência - Regional Municipal",
        help_text="Data de transferência do registro da Regional Municipal para nível superior.",
    )
    dt_transrsr = models.DateField(
        null=True,
        blank=True,
        editable=False,
        verbose_name="Data de transferência - Regional de Saúde",
        help_text="Data de transferência do registro da Regional de Saúde para nível superior.",
    )
    dt_transse = models.DateField(
        null=True,
        blank=True,
        editable=False,
        verbose_name="Data de transferência - Secretaria Estadual",
        help_text="Data de transferência do registro da Secretaria Estadual para nível superior.",
    )
    nu_lote_v = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        editable=False,
        verbose_name="Número do lote vertical",
        help_text="Identificador do lote da transferência vertical.",
    )
    nu_lote_h = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        editable=False,
        verbose_name="Número do lote horizontal",
        help_text="Identificador do lote da transferência horizontal.",
    )
    cs_flxret = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        editable=False,
        verbose_name="Fluxo de retorno",
        help_text="Identifica se o registro está habilitado ou foi enviado pelo fluxo de retorno.",
    )
    flxrecebi = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        editable=False,
        verbose_name="Recebida por fluxo de retorno",
        help_text="Identifica se o registro foi recebido pelo fluxo de retorno.",
    )

    class Meta:
        db_table = 'epizootias'
        verbose_name = 'Epizootia'
        verbose_name_plural = 'Epizootias'
        ordering = ['-dt_notificacao']

    def __str__(self):
        return f"[{self.nu_notificacao}] Epizootia – {self.dt_ini_epi}"