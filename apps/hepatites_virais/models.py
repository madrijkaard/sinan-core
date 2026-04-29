from django.db import models


class HepatitesVirais(models.Model):
    """
    Ficha de Investigação - Hepatites Virais
    Dicionário de Dados SINAN NET - Versão 5.0
    Revisado em julho/2010
    Campos 31 a 52 + campos de controle
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

    class ResultadoMarcador(models.TextChoices):
        REAGENTE = '1', 'Reagente'
        NAO_REAGENTE = '2', 'Não reagente'
        INCONCLUSIVO = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'
        IGNORADO = '9', 'Ignorado'

    # -------------------------------------------------------------------------
    # Campo 31 - Data de investigação
    # -------------------------------------------------------------------------

    dt_investigacao = models.DateField(
        verbose_name="Data de investigação",
        help_text="Data em que ocorreu o início da investigação do caso. Deve ser >= data da notificação.",
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
    # Campo 33 - Suspeita
    # -------------------------------------------------------------------------

    class Suspeita(models.TextChoices):
        HEPATITE_A = '1', 'Hepatite A'
        HEPATITE_B_C = '2', 'Hepatite B/C'
        NAO_ESPECIFICADA = '3', 'Não especificada'

    tp_suspeita = models.CharField(
        max_length=1,
        choices=Suspeita.choices,
        verbose_name="Suspeita",
        help_text="Tipo de hepatite viral da qual o paciente é suspeito.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Tomou vacina para Hepatite A
    # -------------------------------------------------------------------------

    class SituacaoVacinal(models.TextChoices):
        COMPLETA = '1', 'Completa'
        INCOMPLETA = '2', 'Incompleta'
        NAO_VACINADO = '3', 'Não vacinado'
        IGNORADO = '9', 'Ignorado'

    tp_vacina_hepatite_a = models.CharField(
        max_length=1,
        choices=SituacaoVacinal.choices,
        verbose_name="Vacina Hepatite A",
        help_text="Situação vacinal para hepatite A.",
    )
    tp_vacina_hepatite_b = models.CharField(
        max_length=1,
        choices=SituacaoVacinal.choices,
        verbose_name="Vacina Hepatite B",
        help_text="Situação vacinal para hepatite B.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Institucionalizado em
    # -------------------------------------------------------------------------

    class Institucionalizado(models.TextChoices):
        CRECHE = '1', 'Creche'
        ESCOLA = '2', 'Escola'
        ASILO = '3', 'Asilo'
        EMPRESA = '4', 'Empresa'
        PENITENCIARIA = '5', 'Penitenciária'
        HOSPITAL_CLINICA = '6', 'Hospital/Clínica'
        OUTRAS = '7', 'Outras'
        NAO_INSTITUCIONALIZADO = '8', 'Não institucionalizado'
        IGNORADO = '9', 'Ignorado'

    tp_institucionalizado = models.CharField(
        max_length=1,
        choices=Institucionalizado.choices,
        verbose_name="Institucionalizado",
        help_text="Tipo de instituição onde o paciente está institucionalizado.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Agravos associados
    # -------------------------------------------------------------------------

    st_agravo_associado_aids = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="HIV/AIDS associado",
        help_text="Infecção pelo HIV/AIDS diagnosticada no paciente.",
    )
    st_agravo_associado_dst_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Outras DSTs associadas",
        help_text="Outras DSTs diagnosticadas no paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Contato com paciente portador de VHB ou VHC (3 subcampos)
    # -------------------------------------------------------------------------

    class ContatoTempo(models.TextChoices):
        SIM_MENOS_6_MESES = '1', 'Sim há menos de 6 meses'
        SIM_MAIS_6_MESES = '2', 'Sim há mais de seis meses'
        NAO = '3', 'Não'
        IGNORADO = '9', 'Ignorado'

    tp_contato_paciente_vhb_sexual = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Contato sexual com portador VHB/VHC",
        help_text="Paciente teve contato sexual com portador de VHB ou VHC.",
    )
    tp_contato_paciente_vhb_domiciliar = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Contato domiciliar (não sexual) com portador VHB/VHC",
        help_text="Paciente teve contato domiciliar (não sexual) com portador de VHB ou VHC.",
    )
    tp_contato_paciente_vhb_ocupacional = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Contato ocupacional com portador VHB/VHC",
        help_text="Paciente teve exposição ocupacional com portador de VHB ou VHC.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Exposições (16 subcampos)
    # -------------------------------------------------------------------------

    tp_exp_medicamento_injetavel = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Medicamentos injetáveis",
        help_text="Uso de medicamentos injetáveis.",
    )
    tp_exp_tatuagem = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Tatuagem/Piercing",
        help_text="Submeteu-se a tatuagem ou piercing.",
    )
    tp_exp_material_biologico = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Acidente com material biológico",
        help_text="Acidente com material biológico.",
    )
    tp_exp_droga_inalavel = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Drogas inaláveis ou crack",
        help_text="Uso de drogas inaláveis ou crack.",
    )
    tp_exp_acupuntura = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Acupuntura",
        help_text="Submeteu-se a acupuntura.",
    )
    tp_exp_transfusao_sangue = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Transfusão de sangue/derivados",
        help_text="Transfusão de sangue ou hemoderivados.",
    )
    tp_exp_droga_injetavel = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Drogas injetáveis",
        help_text="Uso de drogas injetáveis.",
    )
    tp_exp_trata_cirurgico = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Tratamento cirúrgico",
        help_text="Submeteu-se a tratamento cirúrgico.",
    )
    tp_exp_agua_contaminada = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Água/alimento contaminado",
        help_text="Exposição a água ou alimento contaminado.",
    )
    tp_exp_trata_dentario = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Tratamento dentário",
        help_text="Submeteu-se a tratamento dentário.",
    )
    tp_exp_parceiro_sexual = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Três ou mais parceiros sexuais",
        help_text="Teve três ou mais parceiros sexuais.",
    )
    tp_exp_hemodialise = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Hemodiálise",
        help_text="Submeteu-se a hemodiálise.",
    )
    tp_exp_transplante = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Transplante",
        help_text="Submeteu-se a transplante.",
    )
    tp_exp_outro = models.CharField(
        max_length=1,
        choices=ContatoTempo.choices,
        verbose_name="Outras exposições",
        help_text="Outras situações de risco.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Data do Acidente ou Transfusão ou Transplante
    # -------------------------------------------------------------------------

    dt_evento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do acidente/transfusão/transplante",
        help_text="Data do acidente com material biológico, transfusão de sangue/derivados ou transplante. Deve ser <= data de investigação.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Local/Município da exposição (3 conjuntos)
    # -------------------------------------------------------------------------

    # Conjunto 1
    co_uf_exposicao_1 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF da exposição 1",
        help_text="UF do local de exposição.",
    )
    co_municipio_exposicao_1 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município da exposição 1",
        help_text="Município do local de exposição.",
    )
    ds_local_exposicao_1 = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Local da exposição 1",
        help_text="Local/nome da instituição de exposição.",
    )
    nu_telefone_exposicao_1 = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Telefone da exposição 1",
        help_text="Telefone do local de exposição.",
    )

    # Conjunto 2
    co_uf_exposicao_2 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF da exposição 2",
        help_text="UF do local de exposição.",
    )
    co_municipio_exposicao_2 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município da exposição 2",
        help_text="Município do local de exposição.",
    )
    ds_local_exposicao_2 = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Local da exposição 2",
        help_text="Local/nome da instituição de exposição.",
    )
    nu_telefone_exposicao_2 = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Telefone da exposição 2",
        help_text="Telefone do local de exposição.",
    )

    # Conjunto 3
    co_uf_exposicao_3 = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF da exposição 3",
        help_text="UF do local de exposição.",
    )
    co_municipio_exposicao_3 = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município da exposição 3",
        help_text="Município do local de exposição.",
    )
    ds_local_exposicao_3 = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Local da exposição 3",
        help_text="Local/nome da instituição de exposição.",
    )
    nu_telefone_exposicao_3 = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Telefone da exposição 3",
        help_text="Telefone do local de exposição.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Dados dos comunicantes (5 comunicantes)
    # Nota: Estes campos são preenchidos apenas na ficha em papel
    # -------------------------------------------------------------------------

    # Comunicante 1
    ds_comunicante_nome_1 = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Comunicante 1 - Nome",
        help_text="Nome do comunicante (preenchimento apenas na ficha).",
    )
    ds_comunicante_idade_1 = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Comunicante 1 - Idade",
        help_text="Idade do comunicante (D-dias, M-meses, A-anos).",
    )
    tp_comunicante_contato_1 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 1 - Tipo de contato",
        help_text="Tipo de contato do comunicante com caso suspeito.",
    )
    st_comunicante_hbsag_1 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 1 - HBsAg",
        help_text="Status sorológico do comunicante.",
    )
    st_comunicante_anti_hbc_total_1 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 1 - Anti-HBc total",
        help_text="Status sorológico do comunicante.",
    )
    st_comunicante_anti_hcv_1 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 1 - Anti-HCV",
        help_text="Status sorológico do comunicante.",
    )
    tp_comunicante_vacina_hb_1 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 1 - Indicado vacina Hepatite B",
        help_text="Necessidade de vacinação do comunicante.",
    )
    tp_comunicante_imunoglobina_1 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 1 - Indicado Imunoglobulina HB",
        help_text="Necessidade de indicação da Imunoglobulina anti hepatite B.",
    )

    # Comunicante 2
    ds_comunicante_nome_2 = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Comunicante 2 - Nome",
        help_text="Nome do comunicante (preenchimento apenas na ficha).",
    )
    ds_comunicante_idade_2 = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Comunicante 2 - Idade",
        help_text="Idade do comunicante (D-dias, M-meses, A-anos).",
    )
    tp_comunicante_contato_2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 2 - Tipo de contato",
        help_text="Tipo de contato do comunicante com caso suspeito.",
    )
    st_comunicante_hbsag_2 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 2 - HBsAg",
        help_text="Status sorológico do comunicante.",
    )
    st_comunicante_anti_hbc_total_2 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 2 - Anti-HBc total",
        help_text="Status sorológico do comunicante.",
    )
    st_comunicante_anti_hcv_2 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 2 - Anti-HCV",
        help_text="Status sorológico do comunicante.",
    )
    tp_comunicante_vacina_hb_2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 2 - Indicado vacina Hepatite B",
        help_text="Necessidade de vacinação do comunicante.",
    )
    tp_comunicante_imunoglobina_2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 2 - Indicado Imunoglobulina HB",
        help_text="Necessidade de indicação da Imunoglobulina anti hepatite B.",
    )

    # Comunicante 3
    ds_comunicante_nome_3 = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Comunicante 3 - Nome",
        help_text="Nome do comunicante (preenchimento apenas na ficha).",
    )
    ds_comunicante_idade_3 = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Comunicante 3 - Idade",
        help_text="Idade do comunicante (D-dias, M-meses, A-anos).",
    )
    tp_comunicante_contato_3 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 3 - Tipo de contato",
        help_text="Tipo de contato do comunicante com caso suspeito.",
    )
    st_comunicante_hbsag_3 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 3 - HBsAg",
        help_text="Status sorológico do comunicante.",
    )
    st_comunicante_anti_hbc_total_3 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 3 - Anti-HBc total",
        help_text="Status sorológico do comunicante.",
    )
    st_comunicante_anti_hcv_3 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 3 - Anti-HCV",
        help_text="Status sorológico do comunicante.",
    )
    tp_comunicante_vacina_hb_3 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 3 - Indicado vacina Hepatite B",
        help_text="Necessidade de vacinação do comunicante.",
    )
    tp_comunicante_imunoglobina_3 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 3 - Indicado Imunoglobulina HB",
        help_text="Necessidade de indicação da Imunoglobulina anti hepatite B.",
    )

    # Comunicante 4
    ds_comunicante_nome_4 = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Comunicante 4 - Nome",
        help_text="Nome do comunicante (preenchimento apenas na ficha).",
    )
    ds_comunicante_idade_4 = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Comunicante 4 - Idade",
        help_text="Idade do comunicante (D-dias, M-meses, A-anos).",
    )
    tp_comunicante_contato_4 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 4 - Tipo de contato",
        help_text="Tipo de contato do comunicante com caso suspeito.",
    )
    st_comunicante_hbsag_4 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 4 - HBsAg",
        help_text="Status sorológico do comunicante.",
    )
    st_comunicante_anti_hbc_total_4 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 4 - Anti-HBc total",
        help_text="Status sorológico do comunicante.",
    )
    st_comunicante_anti_hcv_4 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 4 - Anti-HCV",
        help_text="Status sorológico do comunicante.",
    )
    tp_comunicante_vacina_hb_4 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 4 - Indicado vacina Hepatite B",
        help_text="Necessidade de vacinação do comunicante.",
    )
    tp_comunicante_imunoglobina_4 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 4 - Indicado Imunoglobulina HB",
        help_text="Necessidade de indicação da Imunoglobulina anti hepatite B.",
    )

    # Comunicante 5
    ds_comunicante_nome_5 = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Comunicante 5 - Nome",
        help_text="Nome do comunicante (preenchimento apenas na ficha).",
    )
    ds_comunicante_idade_5 = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Comunicante 5 - Idade",
        help_text="Idade do comunicante (D-dias, M-meses, A-anos).",
    )
    tp_comunicante_contato_5 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 5 - Tipo de contato",
        help_text="Tipo de contato do comunicante com caso suspeito.",
    )
    st_comunicante_hbsag_5 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 5 - HBsAg",
        help_text="Status sorológico do comunicante.",
    )
    st_comunicante_anti_hbc_total_5 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 5 - Anti-HBc total",
        help_text="Status sorológico do comunicante.",
    )
    st_comunicante_anti_hcv_5 = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Comunicante 5 - Anti-HCV",
        help_text="Status sorológico do comunicante.",
    )
    tp_comunicante_vacina_hb_5 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 5 - Indicado vacina Hepatite B",
        help_text="Necessidade de vacinação do comunicante.",
    )
    tp_comunicante_imunoglobina_5 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        verbose_name="Comunicante 5 - Indicado Imunoglobulina HB",
        help_text="Necessidade de indicação da Imunoglobulina anti hepatite B.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Paciente encaminhado de
    # -------------------------------------------------------------------------

    class EncaminhadoDe(models.TextChoices):
        BANCO_SANGUE = '1', 'Banco de Sangue'
        CTA = '2', 'Centro de Testagem e Aconselhamento (CTA)'
        NAO_SE_APLICA = '3', 'Não se aplica'

    st_paciente_banco_sangue = models.CharField(
        max_length=1,
        choices=EncaminhadoDe.choices,
        null=True,
        blank=True,
        verbose_name="Paciente encaminhado de",
        help_text="Serviço que encaminhou o paciente à unidade notificadora.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Data da coleta da amostra realizada em Banco de Sangue ou CTA
    # -------------------------------------------------------------------------

    dt_coleta_sorologia_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta (Banco de Sangue/CTA)",
        help_text="Data da coleta da amostra para sorologia realizada no Banco de Sangue ou CTA. Deve ser <= data da investigação.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Resultado da Sorologia do Banco de Sangue ou CTA (3 marcadores)
    # -------------------------------------------------------------------------

    tp_resultado_hbsag = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - HBsAg (Banco de Sangue/CTA)",
        help_text="Resultado da sorologia para HBsAg.",
    )
    tp_resultado_antihbc = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Anti-HBc total (Banco de Sangue/CTA)",
        help_text="Resultado da sorologia para Anti-HBc total.",
    )
    tp_resultado_antihcv = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Resultado - Anti-HCV (Banco de Sangue/CTA)",
        help_text="Resultado da sorologia para Anti-HCV.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Data da coleta da sorologia (investigação)
    # -------------------------------------------------------------------------

    dt_coleta_sorologia_2 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta da sorologia (investigação)",
        help_text="Data da coleta da amostra para sorologia realizada na ocasião da investigação.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Resultados sorológicos/virológicos (11 marcadores)
    # -------------------------------------------------------------------------

    tp_soro_antihav_igm = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Anti-HAV IgM",
        help_text="Resultado da sorologia para Anti-HAV IgM.",
    )
    tp_soro_antihbs = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Anti-HBs",
        help_text="Resultado da sorologia para Anti-HBs.",
    )
    tp_soro_anti_hdv_igm = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Anti-HDV IgM",
        help_text="Resultado da sorologia para Anti-HDV IgM.",
    )
    tp_soro_hbsag = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="HBsAg",
        help_text="Resultado da sorologia para HBsAg.",
    )
    tp_soro_hbeag = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="HBeAg",
        help_text="Resultado da sorologia para HBeAg.",
    )
    tp_soro_anti_hev_igm = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Anti-HEV IgM",
        help_text="Resultado da sorologia para Anti-HEV IgM.",
    )
    tp_soro_antihbc_igm = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Anti-HBc IgM",
        help_text="Resultado da sorologia para Anti-HBc IgM.",
    )
    tp_soro_antihbe = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Anti-HBe",
        help_text="Resultado da sorologia para Anti-HBe.",
    )
    tp_soro_antihcv = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Anti-HCV",
        help_text="Resultado da sorologia para Anti-HCV.",
    )
    tp_soro_antihbc_total = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Anti-HBc total",
        help_text="Resultado da sorologia para Anti-HBc total.",
    )
    tp_soro_anti_hdv_total = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="Anti-HDV total",
        help_text="Resultado da sorologia para Anti-HDV total.",
    )
    tp_soro_hcv_rna = models.CharField(
        max_length=1,
        choices=ResultadoMarcador.choices,
        null=True,
        blank=True,
        verbose_name="HCV-RNA",
        help_text="Resultado de exame de biologia molecular HCV-RNA.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Genótipo para HCV
    # -------------------------------------------------------------------------

    class GenotipoHCV(models.TextChoices):
        GENOTIPO_1 = '1', 'Genótipo 1'
        GENOTIPO_2 = '2', 'Genótipo 2'
        GENOTIPO_3 = '3', 'Genótipo 3'
        GENOTIPO_4 = '4', 'Genótipo 4'
        GENOTIPO_5 = '5', 'Genótipo 5'
        GENOTIPO_6 = '6', 'Genótipo 6'
        NAO_SE_APLICA = '7', 'Não se aplica'
        IGNORADO = '9', 'Ignorado'

    tp_genotipo_vhc = models.CharField(
        max_length=1,
        choices=GenotipoHCV.choices,
        null=True,
        blank=True,
        verbose_name="Genótipo para HCV",
        help_text="Genótipo do VHC.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Classificação final
    # -------------------------------------------------------------------------

    class ClassificacaoFinal(models.TextChoices):
        CONFIRMACAO_LABORATORIAL = '1', 'Confirmação laboratorial'
        CONFIRMACAO_CLINICO_EPIDEMIOLOGICA = '2', 'Confirmação clínico-epidemiológica'
        DESCARTADO = '3', 'Descartado'
        CICATRIZ_SOROLOGICA = '4', 'Cicatriz sorológica'
        INCONCLUSIVO = '8', 'Inconclusivo'

    tp_classificacao_final = models.CharField(
        max_length=1,
        choices=ClassificacaoFinal.choices,
        null=True,
        blank=True,
        verbose_name="Classificação final",
        help_text="Critério de diagnóstico do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Forma Clínica
    # -------------------------------------------------------------------------

    class FormaClinica(models.TextChoices):
        HEPATITE_AGUDA = '1', 'Hepatite Aguda'
        HEPATITE_CRONICA_PORTADOR = '2', 'Hepatite Crônica/Portador Assintomático'
        HEPATITE_FULMINANTE = '3', 'Hepatite Fulminante'
        INCONCLUSIVO = '4', 'Inconclusivo'

    tp_forma_clinica = models.CharField(
        max_length=1,
        choices=FormaClinica.choices,
        null=True,
        blank=True,
        verbose_name="Forma clínica",
        help_text="Forma clínica da hepatite.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Classificação Etiológica
    # -------------------------------------------------------------------------

    class ClassificacaoEtiologica(models.TextChoices):
        VIRUS_A = '01', 'Vírus A'
        VIRUS_B = '02', 'Vírus B'
        VIRUS_C = '03', 'Vírus C'
        VIRUS_B_D = '04', 'Vírus B e D'
        VIRUS_E = '05', 'Vírus E'
        VIRUS_B_C = '06', 'Vírus B e C'
        VIRUS_A_B = '07', 'Vírus A e B'
        VIRUS_A_C = '08', 'Vírus A e C'
        OUTRAS_HEPATITES_VIRAIS = '09', 'Outras Hepatites virais'
        IGNORADO = '99', 'Ignorado'

    tp_classificacao_etiologica = models.CharField(
        max_length=2,
        choices=ClassificacaoEtiologica.choices,
        null=True,
        blank=True,
        verbose_name="Classificação etiológica",
        help_text="Agente(s) etiológico(s) do caso de acordo com resultado sorológico/virológico.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Provável Fonte/Mecanismo de infecção
    # -------------------------------------------------------------------------

    class ProvavelInfeccao(models.TextChoices):
        SEXUAL = '1', 'Sexual'
        TRANSFUSIONAL = '2', 'Transfusional'
        USO_DROGAS = '3', 'Uso de Drogas'
        VERTICAL = '4', 'Vertical'
        ACIDENTE_TRABALHO = '5', 'Acidente de Trabalho'
        HEMODIALISE = '6', 'Hemodiálise'
        DOMICILIAR = '7', 'Domiciliar'
        TRATAMENTO_CIRURGICO = '8', 'Tratamento cirúrgico'
        TRATAMENTO_DENTARIO = '9', 'Tratamento dentário'
        PESSOA_PESSOA = '10', 'Pessoa/pessoa'
        ALIMENTO_AGUA_CONTAMINADA = '11', 'Alimento/água contaminada'
        OUTROS = '12', 'Outros'
        IGNORADO = '99', 'Ignorado'

    tp_provavel_infeccao = models.CharField(
        max_length=2,
        choices=ProvavelInfeccao.choices,
        null=True,
        blank=True,
        verbose_name="Provável fonte/mecanismo de infecção",
        help_text="Provável fonte de infecção ou mecanismo de infecção.",
    )
    ds_provavel_infeccao_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outra fonte/mecanismo (especificar)",
        help_text="Descrição de outra fonte/mecanismo de infecção.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Data do encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento",
        help_text="Data do encerramento do caso. Deve ser >= data da investigação.",
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
        db_table = 'hepatites_virais'
        verbose_name = 'Hepatites Virais'
        verbose_name_plural = 'Hepatites Virais'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Hepatite Viral – {self.dt_investigacao}"