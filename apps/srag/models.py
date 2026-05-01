from django.db import models


class Srag(models.Model):
    """
    Ficha de Investigação - Síndrome Respiratória Aguda Grave (SRAG)
    Dicionário de Dados SINAN Influenza WEB (Ficha versão 8)
    Revisado em Março/2013
    Campos 1 a 52 + campos de controle
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

    class ResultadoDiagnostico(models.TextChoices):
        POSITIVO = '1', 'Positivo'
        NEGATIVO = '2', 'Negativo'
        INCONCLUSIVO = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'

    # -------------------------------------------------------------------------
    # Número da Notificação
    # -------------------------------------------------------------------------

    nu_notificacao = models.CharField(
        max_length=7,
        verbose_name="Número da notificação",
        help_text="Número da notificação - chave para identificação do registro no sistema.",
    )

    # -------------------------------------------------------------------------
    # Campo 1 - Data do preenchimento
    # -------------------------------------------------------------------------

    dt_notificacao = models.DateField(
        verbose_name="Data do preenchimento",
        help_text="Data de preenchimento da ficha de notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 2 - UF do Registro do caso
    # -------------------------------------------------------------------------

    sg_uf_not = models.CharField(
        max_length=2,
        verbose_name="UF do registro do caso",
        help_text="Sigla da UF onde está localizada a unidade de saúde que realizou a notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 3 - Município de Registro do caso
    # -------------------------------------------------------------------------

    id_municipio = models.CharField(
        max_length=6,
        verbose_name="Município de registro do caso",
        help_text="Código do município onde está localizada a unidade de saúde que realizou a notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 4 - Unidade de saúde de identificação do caso
    # -------------------------------------------------------------------------

    id_unidade = models.CharField(
        max_length=8,
        verbose_name="Unidade de saúde (CNES)",
        help_text="Código CNES da unidade de saúde que realizou o atendimento e notificação do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 5 - Data dos primeiros sintomas / Diagnóstico
    # -------------------------------------------------------------------------

    dt_sin_pri = models.DateField(
        verbose_name="Data dos primeiros sintomas",
        help_text="Data dos primeiros sintomas do caso. Deve ser <= data de preenchimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 6 - Nome
    # -------------------------------------------------------------------------

    nm_paciente = models.CharField(
        max_length=70,
        verbose_name="Nome do paciente",
        help_text="Nome completo do paciente (sem abreviações).",
    )

    # -------------------------------------------------------------------------
    # Campo 7 - Nº Cartão SUS
    # -------------------------------------------------------------------------

    id_cns_sus = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name="Nº Cartão SUS",
        help_text="Número do cartão do Sistema Único de Saúde (SUS) do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 8 - Data de nascimento
    # -------------------------------------------------------------------------

    dt_nasc = models.DateField(
        verbose_name="Data de nascimento",
        help_text="Data de nascimento do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 9 - Idade (campo composto)
    # -------------------------------------------------------------------------

    nu_idade_n = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="Idade",
        help_text="Campo composto: 1o dígito (1-hora,2-dia,3-mês,4-ano) + 3 dígitos do número.",
    )

    # -------------------------------------------------------------------------
    # Campo 10 - Sexo
    # -------------------------------------------------------------------------

    cs_sexo = models.CharField(
        max_length=1,
        choices=[
            ('M', 'Masculino'),
            ('F', 'Feminino'),
            ('I', 'Ignorado'),
        ],
        verbose_name="Sexo",
        help_text="Sexo do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 11 - Gestante
    # -------------------------------------------------------------------------

    cs_gestante = models.CharField(
        max_length=1,
        choices=[
            ('1', '1º Trimestre'),
            ('2', '2º Trimestre'),
            ('3', '3º Trimestre'),
            ('4', 'Idade gestacional ignorada'),
            ('5', 'Não'),
            ('6', 'Não se aplica'),
            ('9', 'Ignorado'),
        ],
        null=True,
        blank=True,
        verbose_name="Gestante",
        help_text="Idade gestacional da paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 12 - Raça/Cor
    # -------------------------------------------------------------------------

    cs_raca = models.CharField(
        max_length=1,
        choices=[
            ('1', 'Branca'),
            ('2', 'Preta'),
            ('3', 'Amarela'),
            ('4', 'Parda'),
            ('5', 'Indígena'),
            ('9', 'Ignorado'),
        ],
        null=True,
        blank=True,
        verbose_name="Raça/Cor",
        help_text="Cor ou raça declarada pela pessoa.",
    )

    # -------------------------------------------------------------------------
    # Campo 13 - Escolaridade
    # -------------------------------------------------------------------------

    cs_escol_n = models.CharField(
        max_length=2,
        choices=[
            ('0', 'Analfabeto'),
            ('1', 'Fundamental (1-9 anos)'),
            ('2', 'Médio (1-3 anos)'),
            ('3', 'Superior'),
            ('9', 'Ignorado'),
            ('10', 'Não se aplica'),
        ],
        null=True,
        blank=True,
        verbose_name="Escolaridade",
        help_text="Grau de instrução do paciente por ocasião da notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 14 - Nome da mãe
    # -------------------------------------------------------------------------

    nm_mae_pac = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Nome da mãe",
        help_text="Nome completo da mãe do paciente (sem abreviações).",
    )

    # -------------------------------------------------------------------------
    # Campo 15 - UF de residência
    # -------------------------------------------------------------------------

    sg_uf = models.CharField(
        max_length=2,
        verbose_name="UF de residência",
        help_text="Sigla da UF de residência do paciente por ocasião da notificação.",
    )

    # -------------------------------------------------------------------------
    # Campo 16 - Município de residência
    # -------------------------------------------------------------------------

    id_mn_resi = models.CharField(
        max_length=6,
        verbose_name="Município de residência",
        help_text="Código do município de residência do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 17 - Distrito
    # -------------------------------------------------------------------------

    id_distrit = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Distrito",
        help_text="Código do distrito de residência do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 18 - Bairro
    # -------------------------------------------------------------------------

    nm_bairro = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Bairro",
        help_text="Nome do bairro de residência.",
    )

    # -------------------------------------------------------------------------
    # Campo 19 - Logradouro
    # -------------------------------------------------------------------------

    nm_logradouro = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Logradouro",
        help_text="Nome do logradouro (rua, avenida, etc.).",
    )

    # -------------------------------------------------------------------------
    # Campo 20 - Número do logradouro
    # -------------------------------------------------------------------------

    nu_numero = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Número",
        help_text="Número do logradouro.",
    )

    # -------------------------------------------------------------------------
    # Campo 21 - Complemento do logradouro
    # -------------------------------------------------------------------------

    nm_complem = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Complemento",
        help_text="Complemento do logradouro (bloco, apto, etc.).",
    )

    # -------------------------------------------------------------------------
    # Campo 22 - Ponto de referência
    # -------------------------------------------------------------------------

    nm_referen = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Ponto de referência",
        help_text="Ponto de referência para facilitar a localização.",
    )

    # -------------------------------------------------------------------------
    # Campo 23 - CEP de residência
    # -------------------------------------------------------------------------

    nu_cep = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name="CEP",
        help_text="CEP de residência do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 24 - (DDD) Telefone
    # -------------------------------------------------------------------------

    nu_ddd_tel = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="DDD",
        help_text="DDD do telefone de residência.",
    )
    nu_telefone = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Telefone",
        help_text="Telefone de residência do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 25 - Zona
    # -------------------------------------------------------------------------

    cs_zona = models.CharField(
        max_length=1,
        choices=[
            ('1', 'Urbana'),
            ('2', 'Rural'),
            ('3', 'Periurbana'),
            ('9', 'Ignorado'),
        ],
        null=True,
        blank=True,
        verbose_name="Zona",
        help_text="Zona de residência do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 26 - País
    # -------------------------------------------------------------------------

    id_pais = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        verbose_name="País",
        help_text="País onde residia o paciente (se residente fora do Brasil).",
    )

    # -------------------------------------------------------------------------
    # Campo 27 - Recebeu vacina contra gripe
    # -------------------------------------------------------------------------

    st_vacina_gripe = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Recebeu vacina contra gripe",
        help_text="Se o paciente foi vacinado contra gripe.",
    )

    # -------------------------------------------------------------------------
    # Campo 28 - Data da última dose da vacina contra gripe
    # -------------------------------------------------------------------------

    dt_ut_dose = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da última dose da vacina",
        help_text="Data da última dose de vacina contra gripe.",
    )

    # -------------------------------------------------------------------------
    # Campo 29 - Sinais e sintomas (8 subcampos)
    # -------------------------------------------------------------------------

    st_sintoma_febre = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Febre",
        help_text="Paciente apresentou febre.",
    )
    st_sintoma_tosse = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Tosse",
        help_text="Paciente apresentou tosse.",
    )
    st_sintoma_garganta = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Dor de garganta",
        help_text="Paciente apresentou dor de garganta.",
    )
    st_sintoma_dispneia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Dispnéia",
        help_text="Paciente apresentou dispneia.",
    )
    st_sintoma_mialgia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Mialgia",
        help_text="Paciente apresentou mialgia (dor muscular).",
    )
    st_sintoma_saturacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Saturação de O2 < 95%",
        help_text="Paciente apresentou saturação de O2 < 95%.",
    )
    st_sintoma_desc_resp = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Desconforto respiratório",
        help_text="Paciente apresentou desconforto respiratório.",
    )
    st_sintoma_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outros sintomas",
        help_text="Paciente apresentou outros sintomas.",
    )
    ds_sintoma_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outros sintomas (especificar)",
        help_text="Especificação de outros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 30 - Fatores de risco (12 subcampos)
    # -------------------------------------------------------------------------

    st_comorb_pneumopatia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Pneumopatia Crônica",
        help_text="Paciente possui pneumopatia crônica.",
    )
    st_comorb_cardiopatia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Doença Cardiovascular Crônica",
        help_text="Paciente possui cardiopatia crônica.",
    )
    st_comorb_imunodeprimido = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Imunodeficiência/Imunodepressão",
        help_text="Paciente possui imunodepressão.",
    )
    st_comorb_hepatica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Doença Hepática Crônica",
        help_text="Paciente possui doença hepática crônica.",
    )
    st_comorb_neurologica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Doença Neurológica Crônica",
        help_text="Paciente possui doença neurológica crônica.",
    )
    st_comorb_renal = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Doença Renal Crônica",
        help_text="Paciente possui doença renal crônica.",
    )
    st_comorb_sind_down = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Síndrome de Down",
        help_text="Paciente possui Síndrome de Down.",
    )
    st_comorb_metabolica = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Diabetes mellitus",
        help_text="Paciente possui diabetes mellitus.",
    )
    st_comorb_puerpera = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Puerpério",
        help_text="Paciente é puérpera ou parturiente.",
    )
    st_comorb_obesidade = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Obesidade",
        help_text="Paciente possui obesidade.",
    )
    st_comorb_obes_imc = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="IMC (Obesidade)",
        help_text="Especificar o IMC do paciente com obesidade.",
    )
    st_comorb_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outros fatores de risco",
        help_text="Paciente possui outra morbidade associada.",
    )
    ds_comorb_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outros fatores de risco (especificar)",
        help_text="Descrição da morbidade associada.",
    )

    # -------------------------------------------------------------------------
    # Campo 31 - Uso de antiviral
    # -------------------------------------------------------------------------

    class Antiviral(models.TextChoices):
        NAO = '1', 'Não'
        OSELTAMIVIR = '2', 'Oseltamivir'
        ZANAMIVIR = '3', 'Zanamivir'
        OUTRO = '4', 'Outro'
        IGNORADO = '9', 'Ignorado'

    tp_antiviral = models.CharField(
        max_length=1,
        choices=Antiviral.choices,
        null=True,
        blank=True,
        verbose_name="Uso de antiviral",
        help_text="Fez uso de antiviral para tratamento da doença.",
    )
    ds_antiviral_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro antiviral (especificar)",
        help_text="Especificação do antiviral utilizado quando opção = 4 (Outro).",
    )

    # -------------------------------------------------------------------------
    # Campo 32 - Data do início do tratamento
    # -------------------------------------------------------------------------

    dt_antiviral = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do início do tratamento antiviral",
        help_text="Data em que foi iniciado o tratamento com antiviral.",
    )

    # -------------------------------------------------------------------------
    # Campo 33 - Ocorreu internação?
    # -------------------------------------------------------------------------

    st_hospitalizacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Ocorreu internação",
        help_text="Se o paciente foi hospitalizado em decorrência da influenza.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Data da internação
    # -------------------------------------------------------------------------

    dt_internacao = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da internação",
        help_text="Data da internação.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - UF da internação
    # -------------------------------------------------------------------------

    co_uf_internacao = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF da internação",
        help_text="Sigla da UF da hospitalização.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Município da Unidade de saúde de internação
    # -------------------------------------------------------------------------

    co_mu_internacao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município da internação",
        help_text="Município onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Nome da Unidade de Saúde de internação
    # -------------------------------------------------------------------------

    co_un_internacao = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Unidade de saúde de internação (CNES)",
        help_text="Código CNES da unidade de saúde onde o paciente foi internado.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - RX de Tórax
    # -------------------------------------------------------------------------

    class RaioXResultado(models.TextChoices):
        NORMAL = '1', 'Normal'
        INFILTRADO_INTERSTICIAL = '2', 'Infiltrado intersticial'
        CONSOLIDACAO = '3', 'Consolidação'
        MISTO = '4', 'Misto'
        OUTRO = '5', 'Outro'
        NAO_REALIZADO = '6', 'Não realizado'
        IGNORADO = '9', 'Ignorado'

    tp_raiox = models.CharField(
        max_length=1,
        choices=RaioXResultado.choices,
        null=True,
        blank=True,
        verbose_name="RX de Tórax",
        help_text="Resultado do Raio X de tórax.",
    )
    ds_raiox_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="RX de Tórax - Outro (especificar)",
        help_text="Especificação quando resultado = 5 (Outro).",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Data do Raio X
    # -------------------------------------------------------------------------

    dt_raiox = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do Raio X",
        help_text="Data do exame de Raio X de tórax.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Fez uso de suporte ventilatório?
    # -------------------------------------------------------------------------

    class SuporteVentilatorio(models.TextChoices):
        NAO_USOU = '1', 'Não usou'
        SIM_INVASIVO = '2', 'Sim, invasivo'
        SIM_NAO_INVASIVO = '3', 'Sim, não invasivo'
        IGNORADO = '9', 'Ignorado'

    tp_suporte_ven = models.CharField(
        max_length=1,
        choices=SuporteVentilatorio.choices,
        null=True,
        blank=True,
        verbose_name="Suporte ventilatório",
        help_text="Se o paciente fez uso de suporte ventilatório.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Foi internado em UTI?
    # -------------------------------------------------------------------------

    st_uti = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Internado em UTI",
        help_text="Se o paciente foi internado em Unidade de Terapia Intensiva (UTI).",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Data de entrada na UTI
    # -------------------------------------------------------------------------

    dt_entuti = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de entrada na UTI",
        help_text="Data da entrada na UTI.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Data de saída da UTI
    # -------------------------------------------------------------------------

    dt_saiduti = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de saída da UTI",
        help_text="Data da saída da UTI.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Coletou que tipo de amostra?
    # -------------------------------------------------------------------------

    class TipoAmostra(models.TextChoices):
        NAO_COLETOU = '1', 'Não coletou'
        SECRECAO_ORO_NASO = '2', 'Secreção de Oro e Nasofaringe'
        TECIDO_POST_MORTEM = '3', 'Tecido post-mortem'
        LAVADO_BRONCO_ALVEOLAR = '4', 'Lavado Bronco-alveolar'
        OUTRA = '5', 'Outra'
        IGNORADO = '9', 'Ignorado'

    tp_amostra = models.CharField(
        max_length=1,
        choices=TipoAmostra.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de amostra coletada",
        help_text="Tipo de amostra clínica coletada para diagnóstico laboratorial.",
    )
    ds_amostra_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outra amostra (especificar)",
        help_text="Especificação do tipo de amostra quando opção = 5 (Outra).",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Data da Coleta
    # -------------------------------------------------------------------------

    dt_coleta = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da coleta",
        help_text="Data da coleta da amostra para realização do teste diagnóstico.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Metodologia Realizada
    # -------------------------------------------------------------------------

    st_ifi = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="IFI realizada",
        help_text="Se o diagnóstico foi efetuado por IFI.",
    )
    dt_ifi = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do resultado - IFI",
        help_text="Data do resultado diagnóstico da IFI.",
    )
    st_pcr = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="PCR realizada",
        help_text="Se o diagnóstico foi efetuado por PCR.",
    )
    tp_pcr = models.CharField(
        max_length=1,
        choices=[
            ('1', 'Convencional'),
            ('2', 'Em tempo real'),
        ],
        null=True,
        blank=True,
        verbose_name="Tipo de PCR",
        help_text="Tipo de PCR realizado.",
    )
    dt_pcr = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do resultado - PCR",
        help_text="Data do resultado diagnóstico do PCR.",
    )
    st_out_metodo = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outra metodologia",
        help_text="Se foi utilizada outra metodologia para diagnóstico.",
    )
    ds_out_metodo = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outra metodologia (descrição)",
        help_text="Nome da outra metodologia realizada.",
    )
    dt_out_metodo = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do resultado - Outra metodologia",
        help_text="Data do resultado diagnóstico da outra metodologia.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Diagnóstico Etiológico (10 subcampos)
    # -------------------------------------------------------------------------

    tp_res_flua = models.CharField(
        max_length=1,
        choices=ResultadoDiagnostico.choices,
        null=True,
        blank=True,
        verbose_name="Influenza A",
        help_text="Resultado diagnóstico para Influenza A.",
    )
    tp_res_fluasu = models.CharField(
        max_length=1,
        choices=[
            ('1', 'Influenza A(H1N1)pdm09'),
            ('2', 'Influenza A(H1) Sazonal'),
            ('3', 'Influenza A(H3) Sazonal'),
            ('4', 'Influenza A não subtipado'),
            ('5', 'Influenza A/H3N2v'),
            ('6', 'Outro subtipo de Influenza A'),
        ],
        null=True,
        blank=True,
        verbose_name="Subtipo de Influenza A",
        help_text="Subtipo identificado se positivo para Influenza A.",
    )
    ds_outsub = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro subtipo (especificar)",
        help_text="Especificação de outro subtipo de Influenza A.",
    )
    tp_res_flub = models.CharField(
        max_length=1,
        choices=ResultadoDiagnostico.choices,
        null=True,
        blank=True,
        verbose_name="Influenza B",
        help_text="Resultado diagnóstico para Influenza B.",
    )
    tp_res_vrs = models.CharField(
        max_length=1,
        choices=ResultadoDiagnostico.choices,
        null=True,
        blank=True,
        verbose_name="VRS",
        help_text="Resultado diagnóstico para VRS.",
    )
    tp_res_para1 = models.CharField(
        max_length=1,
        choices=ResultadoDiagnostico.choices,
        null=True,
        blank=True,
        verbose_name="Parainfluenza 1",
        help_text="Resultado diagnóstico para Parainfluenza 1.",
    )
    tp_res_para2 = models.CharField(
        max_length=1,
        choices=ResultadoDiagnostico.choices,
        null=True,
        blank=True,
        verbose_name="Parainfluenza 2",
        help_text="Resultado diagnóstico para Parainfluenza 2.",
    )
    tp_res_para3 = models.CharField(
        max_length=1,
        choices=ResultadoDiagnostico.choices,
        null=True,
        blank=True,
        verbose_name="Parainfluenza 3",
        help_text="Resultado diagnóstico para Parainfluenza 3.",
    )
    tp_res_adno = models.CharField(
        max_length=1,
        choices=ResultadoDiagnostico.choices,
        null=True,
        blank=True,
        verbose_name="Adenovírus",
        help_text="Resultado diagnóstico para Adenovírus.",
    )
    tp_res_outro = models.CharField(
        max_length=1,
        choices=ResultadoDiagnostico.choices,
        null=True,
        blank=True,
        verbose_name="Outro agente etiológico",
        help_text="Resultado diagnóstico para outros agentes etiológicos.",
    )
    ds_oageeti = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro agente etiológico (especificar)",
        help_text="Nome do outro agente etiológico identificado.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Classificação final da SRAG
    # -------------------------------------------------------------------------

    class ClassificacaoFinal(models.TextChoices):
        SRAG_INFLUENZA = '1', 'SRAG por Influenza'
        SRAG_OUTROS_VIRUS = '2', 'SRAG por outros vírus respiratórios'
        SRAG_OUTROS_AGENTES = '3', 'SRAG por outros agentes etiológicos'
        SRAG_NAO_ESPECIFICADO = '4', 'SRAG não especificado'

    tp_classificacao_final = models.CharField(
        max_length=1,
        choices=ClassificacaoFinal.choices,
        null=True,
        blank=True,
        verbose_name="Classificação final da SRAG",
        help_text="Diagnóstico final do caso suspeito.",
    )
    ds_classificacao_outroae = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro agente etiológico (classificação final)",
        help_text="Specification quando classificação = 3 (SRAG por outros agentes).",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Critério de confirmação
    # -------------------------------------------------------------------------

    class CriterioConfirmacao(models.TextChoices):
        LABORATORIAL = '1', 'Laboratorial'
        CLINICO_EPIDEMIOLOGICO = '2', 'Clínico-Epidemiológico'
        CLINICO = '3', 'Clínico'

    tp_criterio_confirmacao = models.CharField(
        max_length=1,
        choices=CriterioConfirmacao.choices,
        null=True,
        blank=True,
        verbose_name="Critério de confirmação",
        help_text="Critério de confirmação do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Evolução clínica
    # -------------------------------------------------------------------------

    class EvolucaoClinica(models.TextChoices):
        ALTA_CURA = '1', 'Recebeu alta por cura'
        EVOLUIU_OBITO = '2', 'Evoluiu para óbito'
        IGNORADO = '9', 'Ignorado'

    tp_evolucao_caso = models.CharField(
        max_length=1,
        choices=EvolucaoClinica.choices,
        null=True,
        blank=True,
        verbose_name="Evolução clínica",
        help_text="Evolução do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Data da alta ou do óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da alta ou do óbito",
        help_text="Data da alta hospitalar ou do óbito. Deve ser >= data dos primeiros sintomas.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Data do encerramento
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento",
        help_text="Data do encerramento da investigação. Deve ser >= data de preenchimento.",
    )

    # -------------------------------------------------------------------------
    # Anotações / Observações
    # -------------------------------------------------------------------------

    ds_observacao = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Observações",
        help_text="Anotações adicionais sobre o caso.",
    )

    # -------------------------------------------------------------------------
    # Campos internos
    # -------------------------------------------------------------------------

    st_srag2012 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        editable=False,
        verbose_name="SRAG 2012 (campo interno)",
        help_text="Campo de controle interno do GT-SINAN.",
    )
    st_sraghosp2009 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        editable=False,
        verbose_name="SRAG 2009 (campo interno)",
        help_text="Campo de controle interno do GT-SINAN.",
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
        db_table = 'srag'
        verbose_name = 'SRAG - Síndrome Respiratória Aguda Grave'
        verbose_name_plural = 'SRAG - Síndrome Respiratória Aguda Grave'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.nu_notificacao}] SRAG – {self.nm_paciente}"