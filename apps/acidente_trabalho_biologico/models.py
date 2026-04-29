from django.db import models


class AcidenteTrabalhoBiologico(models.Model):
    """
    Ficha de Investigação - DRT Acidente Trabalho Biológico
    Dicionário de Dados SINAN NET - Versão 5.0
    Revisado em Julho/2010
    Campos 31 a 58 + campos de controle
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

    class SimNaoNaoSeAplicaIgnorado(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        NAO_SE_APLICA = '3', 'Não se aplica'
        IGNORADO = '9', 'Ignorado'

    # -------------------------------------------------------------------------
    # Campo 31 - Ocupação
    # -------------------------------------------------------------------------

    co_cbo_ocupacao = models.CharField(
        max_length=6,
        verbose_name="Ocupação (CBO)",
        help_text="Ocupação do indivíduo que sofreu o agravo.",
    )

    # -------------------------------------------------------------------------
    # Campo 32 - Situação no mercado de trabalho
    # -------------------------------------------------------------------------

    class SituacaoMercadoTrabalho(models.TextChoices):
        EMPREGADO_REGISTRADO = '1', 'Empregado registrado com carteira assinada'
        EMPREGADO_NAO_REGISTRADO = '2', 'Empregado não registrado'
        AUTONOMO = '3', 'Autônomo/conta própria'
        SERVIDOR_PUBLICO_ESTATUTARIO = '4', 'Servidor público estatutário'
        SERVIDOR_PUBLICO_CELETISTA = '5', 'Servidor público celetista'
        APOSENTADO = '6', 'Aposentado'
        DESEMPREGADO = '7', 'Desempregado'
        TRABALHO_TEMPORARIO = '8', 'Trabalho temporário'
        COOPERATIVADO = '9', 'Cooperativado'
        TRABALHADOR_AVULSO = '10', 'Trabalhador avulso'
        EMPREGADOR = '11', 'Empregador'
        OUTROS = '12', 'Outros'
        IGNORADO = '99', 'Ignorado'

    tp_mercado_trabalho = models.CharField(
        max_length=2,
        choices=SituacaoMercadoTrabalho.choices,
        null=True,
        blank=True,
        verbose_name="Situação no mercado de trabalho",
        help_text="Situação de trabalho do indivíduo que sofreu o agravo.",
    )

    # -------------------------------------------------------------------------
    # Campo 33 - Tempo de trabalho na ocupação
    # -------------------------------------------------------------------------

    nu_tempo_trabalho = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Tempo de trabalho na ocupação",
        help_text="Quantidade de tempo trabalhado na ocupação.",
    )

    class UnidadeTempoTrabalho(models.TextChoices):
        HORA = '1', 'Hora'
        DIAS = '2', 'Dias'
        MESES = '3', 'Meses'
        ANOS = '4', 'Anos'

    tp_tempo_trabalho = models.CharField(
        max_length=1,
        choices=UnidadeTempoTrabalho.choices,
        null=True,
        blank=True,
        verbose_name="Unidade de tempo",
        help_text="Unidade de medida do tempo de trabalho.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Registro/CNPJ/CPF
    # -------------------------------------------------------------------------

    nu_cnpj_cpf = models.CharField(
        max_length=18,
        null=True,
        blank=True,
        verbose_name="CNPJ/CPF do contratante",
        help_text="Número de registro/CNPJ ou CPF do contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Nome da empresa ou empregador
    # -------------------------------------------------------------------------

    no_empresa = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Nome da empresa ou empregador",
        help_text="Nome da empresa ou empregador contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Código da atividade Econômica (CNAE)
    # -------------------------------------------------------------------------

    co_cnae = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="CNAE",
        help_text="Classificação Nacional da Atividade Econômica do Contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - UF
    # -------------------------------------------------------------------------

    co_uf_empresa = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF da empresa",
        help_text="Unidade da Federação da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Município
    # -------------------------------------------------------------------------

    co_municipio_empresa = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município da empresa",
        help_text="Município da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Distrito
    # -------------------------------------------------------------------------

    co_distrito_empresa = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        verbose_name="Distrito da empresa",
        help_text="Código do distrito da empresa contratante.",
    )
    no_distrito_empresa = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Nome do distrito da empresa",
        help_text="Nome do distrito da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Bairro
    # -------------------------------------------------------------------------

    co_bairro_empresa = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name="Código do bairro da empresa",
        help_text="Código do bairro da empresa contratante.",
    )
    no_bairro_empresa = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Bairro da empresa",
        help_text="Nome do bairro da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Endereço
    # -------------------------------------------------------------------------

    co_endereco_empresa = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Código do endereço da empresa",
        help_text="Código do endereço da empresa contratante.",
    )
    no_endereco_empresa = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        verbose_name="Endereço da empresa",
        help_text="Endereço da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Número
    # -------------------------------------------------------------------------

    nu_numero_empresa = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name="Número da empresa",
        help_text="Número do lote da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Ponto de Referência
    # -------------------------------------------------------------------------

    no_referencia_empresa = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Ponto de referência da empresa",
        help_text="Ponto de referência da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - (DDD) Telefone
    # -------------------------------------------------------------------------

    ds_ddd_empresa = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name="DDD e telefone da empresa",
        help_text="DDD e telefone da empresa contratante.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - O empregador é empresa Terceirizada
    # -------------------------------------------------------------------------

    tp_empresa_terceirizada = models.CharField(
        max_length=2,
        choices=SimNaoNaoSeAplicaIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Empregador é empresa terceirizada",
        help_text="O empregador é de alguma empresa terceirizada.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Tipo de exposição (5 subcampos)
    # -------------------------------------------------------------------------

    st_exp_percutanea = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição percutânea",
        help_text="Se houve exposição percutânea.",
    )
    st_exp_mucosa = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição mucosa (oral/ocular)",
        help_text="Se houve exposição em mucosa (oral ou ocular).",
    )
    st_exp_pele_integra = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição pele íntegra",
        help_text="Se houve exposição em pele íntegra.",
    )
    st_exp_pele_nao_integra = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Exposição pele não íntegra",
        help_text="Se houve exposição em pele não íntegra.",
    )
    st_exp_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Outro tipo de exposição",
        help_text="Se houve outro tipo de exposição.",
    )
    ds_exp_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro tipo de exposição (especificar)",
        help_text="Especificação quando outro tipo de exposição = Sim.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Material orgânico
    # -------------------------------------------------------------------------

    class MaterialOrganico(models.TextChoices):
        SANGUE = '1', 'Sangue'
        LIQUOR = '2', 'Líquor'
        LIQUIDO_PLEURAL = '3', 'Líquido pleural'
        LIQUIDO_ASCITICO = '4', 'Líquido ascítico'
        LIQUIDO_AMNIOTICO = '5', 'Líquido amniótico'
        FLUIDO_COM_SANGUE = '6', 'Fluído com sangue'
        SORO_PLASMA = '7', 'Soro/plasma'
        OUTROS = '8', 'Outros'
        IGNORADO = '9', 'Ignorado'

    tp_material_organico = models.CharField(
        max_length=1,
        choices=MaterialOrganico.choices,
        null=True,
        blank=True,
        verbose_name="Material orgânico",
        help_text="Tipo de material orgânico envolvido no acidente.",
    )
    ds_material_organico_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro material orgânico (especificar)",
        help_text="Especificação quando material orgânico = 8 (Outros).",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Circunstância do Acidentado
    # -------------------------------------------------------------------------

    class CircunstanciaAcidente(models.TextChoices):
        ADMIN_MEDICACAO_EV = '01', 'Administração de medicação endovenosa'
        ADMIN_MEDICACAO_IM = '02', 'Administração de medicação intramuscular'
        ADMIN_MEDICACAO_SC = '03', 'Administração de medicação subcutânea'
        ADMIN_MEDICACAO_ID = '04', 'Administração de medicação intradérmica'
        PUNCAO_VENOSA_COLETA = '05', 'Punção venosa/arterial para coleta de sangue'
        PUNCAO_VENOSA_NAO_ESPEC = '06', 'Punção venosa/arterial não especificada'
        DESCARTE_INADEQUADO_LIXO = '07', 'Descarte inadequado de material perfuro/cortante em saco de lixo'
        DESCARTE_INADEQUADO_BANCADA = '08', 'Descarte inadequado de material perfuro/cortante em bancada, cama, chão, etc.'
        LAVANDERIA = '09', 'Lavanderia'
        LAVAGEM_MATERIAL = '10', 'Lavagem de material'
        MANIPULACAO_CAIXA = '11', 'Manipulação de caixa com material perfuro/cortante'
        PROCEDIMENTO_CIRURGICO = '12', 'Procedimento cirúrgico'
        PROCEDIMENTO_ODONTOLOGICO = '13', 'Procedimento odontológico'
        PROCEDIMENTO_LABORATORIAL = '14', 'Procedimento laboratorial'
        DEXTRO = '15', 'Dextro'
        REENCAPE = '16', 'Reencape'
        OUTROS = '98', 'Outros'
        IGNORADO = '99', 'Ignorado'

    tp_circunstancia_acidentado = models.CharField(
        max_length=2,
        choices=CircunstanciaAcidente.choices,
        null=True,
        blank=True,
        verbose_name="Circunstância do acidente",
        help_text="Circunstância em que ocorreu o acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Agente
    # -------------------------------------------------------------------------

    class Agente(models.TextChoices):
        AGULHA_COM_LUMEN = '1', 'Agulha com lúmen (luz)'
        AGULHA_SEM_LUMEN = '2', 'Agulha sem lúmen/maciça'
        INTRACATH = '3', 'Intracath'
        VIDROS = '4', 'Vidros'
        LAMINA_LANCETA = '5', 'Lâmina/lanceta (qualquer tipo)'
        OUTROS = '6', 'Outros'
        IGNORADO = '9', 'Ignorado'

    tp_agente = models.CharField(
        max_length=1,
        choices=Agente.choices,
        null=True,
        blank=True,
        verbose_name="Agente",
        help_text="Agente causador do acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Uso de EPI (6 subcampos)
    # -------------------------------------------------------------------------

    st_epi_luva = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="EPI - Luva",
        help_text="Se utilizou luva como EPI.",
    )
    st_epi_avental = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="EPI - Avental",
        help_text="Se utilizou avental como EPI.",
    )
    st_epi_oculos = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="EPI - Óculos",
        help_text="Se utilizou óculos de proteção como EPI.",
    )
    st_epi_mascara = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="EPI - Máscara",
        help_text="Se utilizou máscara como EPI.",
    )
    st_epi_protecao_facial = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="EPI - Proteção facial",
        help_text="Se utilizou proteção facial como EPI.",
    )
    st_epi_bota = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="EPI - Bota",
        help_text="Se utilizou bota como EPI.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Situação vacinal do acidentado em relação a hepatite B (3 Doses)
    # -------------------------------------------------------------------------

    class SituacaoVacinal(models.TextChoices):
        VACINADO = '1', 'Vacinado'
        NAO_VACINADO = '2', 'Não vacinado'
        IGNORADO = '9', 'Ignorado'

    st_situacao_vacinal = models.CharField(
        max_length=1,
        choices=SituacaoVacinal.choices,
        null=True,
        blank=True,
        verbose_name="Situação vacinal (Hepatite B - 3 doses)",
        help_text="Situação vacinal do acidentado em relação à hepatite B.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Resultados de exame do acidentado (Data Zero) - 4 subcampos
    # -------------------------------------------------------------------------

    class ResultadoExameZero(models.TextChoices):
        POSITIVO = '1', 'Positivo'
        NEGATIVO = '2', 'Negativo'
        INCONCLUSIVO = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'
        IGNORADO = '9', 'Ignorado'

    tp_resultado_acid_anti_hiv = models.CharField(
        max_length=1,
        choices=ResultadoExameZero.choices,
        null=True,
        blank=True,
        verbose_name="Exame acidentado (Data Zero) - Anti-HIV",
        help_text="Resultado do exame Anti-HIV no momento do acidente.",
    )
    tp_resultado_acid_hbs_ag = models.CharField(
        max_length=1,
        choices=ResultadoExameZero.choices,
        null=True,
        blank=True,
        verbose_name="Exame acidentado (Data Zero) - HbsAg",
        help_text="Resultado do exame HbsAg no momento do acidente.",
    )
    tp_resultado_acid_anti_hbs = models.CharField(
        max_length=1,
        choices=ResultadoExameZero.choices,
        null=True,
        blank=True,
        verbose_name="Exame acidentado (Data Zero) - Anti-HBs",
        help_text="Resultado do exame Anti-HBs no momento do acidente.",
    )
    tp_resultado_acid_anti_hcv = models.CharField(
        max_length=1,
        choices=ResultadoExameZero.choices,
        null=True,
        blank=True,
        verbose_name="Exame acidentado (Data Zero) - Anti-HCV",
        help_text="Resultado do exame Anti-HCV no momento do acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Paciente fonte conhecida
    # -------------------------------------------------------------------------

    st_dado_paciente = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Paciente fonte conhecida",
        help_text="Se o paciente fonte é conhecido.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Resultados dos testes sorológicos da fonte (4 subcampos)
    # -------------------------------------------------------------------------

    class ResultadoSoroFonte(models.TextChoices):
        POSITIVO = '1', 'Positivo'
        NEGATIVO = '2', 'Negativo'
        INCONCLUSIVO = '3', 'Inconclusivo'
        EM_ANDAMENTO = '4', 'Em andamento'
        NAO_REALIZADO = '5', 'Não realizado'
        IGNORADO = '9', 'Ignorado'

    tp_resultado_soro_hbs = models.CharField(
        max_length=1,
        choices=ResultadoSoroFonte.choices,
        null=True,
        blank=True,
        verbose_name="Teste sorológico fonte - HbsAg",
        help_text="Resultado do HbsAg da fonte.",
    )
    tp_resultado_soro_anti_hiv = models.CharField(
        max_length=1,
        choices=ResultadoSoroFonte.choices,
        null=True,
        blank=True,
        verbose_name="Teste sorológico fonte - Anti-HIV",
        help_text="Resultado do Anti-HIV da fonte.",
    )
    tp_resultado_soro_anti_hbs = models.CharField(
        max_length=1,
        choices=ResultadoSoroFonte.choices,
        null=True,
        blank=True,
        verbose_name="Teste sorológico fonte - Anti-HBs",
        help_text="Resultado do Anti-HBs da fonte.",
    )
    tp_resultado_soro_anti_hcv = models.CharField(
        max_length=1,
        choices=ResultadoSoroFonte.choices,
        null=True,
        blank=True,
        verbose_name="Teste sorológico fonte - Anti-HCV",
        help_text="Resultado do Anti-HCV da fonte.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Conduta no momento do acidente (9 subcampos)
    # -------------------------------------------------------------------------

    st_conduta_sem_quimio = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - Sem indicação de quimioprofilaxia",
        help_text="Se não houve indicação de quimioprofilaxia.",
    )
    st_conduta_recusa_quimio = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - Recusou quimioprofilaxia indicada",
        help_text="Se recusou quimioprofilaxia indicada.",
    )
    st_conduta_azt_3tc = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - AZT+3TC",
        help_text="Se utilizou esquema AZT+3TC.",
    )
    st_conduta_azt_3tc_indinavir = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - AZT+3TC+Indinavir",
        help_text="Se utilizou esquema AZT+3TC+Indinavir.",
    )
    st_conduta_azt_3tc_nelfinavir = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - AZT+3TC+Nelfinavir",
        help_text="Se utilizou esquema AZT+3TC+Nelfinavir.",
    )
    st_conduta_imunoglobulina = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - Imunoglobulina humana contra hepatite B (HBIG)",
        help_text="Se utilizou imunoglobulina contra hepatite B.",
    )
    st_conduta_vacina_hepatite_b = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - Vacina contra hepatite B",
        help_text="Se recebeu vacina contra hepatite B.",
    )
    st_conduta_outro_arv = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Conduta - Outro esquema de ARV",
        help_text="Se utilizou outro esquema de antirretroviral.",
    )
    ds_conduta_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro esquema de ARV (especificar)",
        help_text="Especificação quando outro esquema de ARV = Sim.",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - Evolução do caso
    # -------------------------------------------------------------------------

    class EvolucaoCaso(models.TextChoices):
        ALTA_CONVERSAO_SOROLOGICA = '1', 'Alta com conversão sorológica'
        ALTA_SEM_CONVERSAO_SOROLOGICA = '2', 'Alta sem conversão sorológica'
        ALTA_PACIENTE_FONTE_NEGATIVO = '3', 'Alta paciente fonte negativo'
        ABANDONO = '4', 'Abandono'
        OBITO_ACIDENTE_BIOLOGICO = '5', 'Óbito por acidente com exposição a material biológico'
        OBITO_OUTRA_CAUSA = '6', 'Óbito por outra causa'
        IGNORADO = '9', 'Ignorado'

    tp_evolucao_caso = models.CharField(
        max_length=1,
        choices=EvolucaoCaso.choices,
        null=True,
        blank=True,
        verbose_name="Evolução do caso",
        help_text="Evolução do acidentado.",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - Especificar vírus (se conversão sorológica)
    # -------------------------------------------------------------------------

    ds_evolucao_caso_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Especificar vírus",
        help_text="Especificação do vírus quando evolução = 1 (alta com conversão sorológica).",
    )

    # -------------------------------------------------------------------------
    # Campo 57 - Data do Óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do óbito",
        help_text="Data do óbito. Obrigatório se evolução = 5 ou 6. Deve ser >= data do acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 58 - Foi emitida a Comunicação de Acidente no Trabalho - CAT
    # -------------------------------------------------------------------------

    tp_comunicacao_cat = models.CharField(
        max_length=1,
        choices=SimNaoNaoSeAplicaIgnorado.choices,
        verbose_name="Comunicação de Acidente no Trabalho - CAT",
        help_text="Se foi emitida a Comunicação de Acidente no Trabalho (CAT).",
    )

    # -------------------------------------------------------------------------
    # Informações complementares e observações
    # -------------------------------------------------------------------------

    ds_observacao = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Observações",
        help_text="Descrição sumária de como ocorreu o acidente/atividades/causas/condições/objeto/agentes.",
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
        db_table = 'acidente_trabalho_biologico'
        verbose_name = 'Acidente de Trabalho Biológico'
        verbose_name_plural = 'Acidentes de Trabalho Biológico'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Acidente Trabalho Biológico – {self.co_cbo_ocupacao}"