from django.db import models


class AidsAdulto(models.Model):
    """
    Ficha de Investigação - AIDS Adulto
    Dicionário de Dados SINAN NET - Versão 5.0
    Revisado fevereiro/2012.
    Campos 31 a 48 + campos internos + campos de controle
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
        SIM      = '1', 'Sim'
        NAO      = '2', 'Não'
        IGNORADO = '9', 'Ignorado'

    class ResultadoTeste(models.TextChoices):
        POSITIVO      = '1', 'Positivo / Reagente'
        NEGATIVO      = '2', 'Negativo / Não reagente'
        INCONCLUSIVO  = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'
        IGNORADO      = '9', 'Ignorado'

    class ResultadoTesteComIndeterminado(models.TextChoices):
        POSITIVO      = '1', 'Positivo / Reagente'
        NEGATIVO      = '2', 'Negativo / Não reagente'
        INCONCLUSIVO  = '3', 'Inconclusivo'
        NAO_REALIZADO = '4', 'Não realizado'
        INDETERMINADO = '5', 'Indeterminado'
        IGNORADO      = '9', 'Ignorado'

    # -------------------------------------------------------------------------
    # Campo 31 - Ocupação / Ramo de Atividade Econômica
    # -------------------------------------------------------------------------

    co_cbo_ocupacao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Ocupação / Ramo de Atividade Econômica",
        help_text="Código CBO da ocupação do paciente conforme Portaria nº 3.947/GM de 25/11/1998.",
    )

    # -------------------------------------------------------------------------
    # Campo 32 - Transmissão Vertical
    # -------------------------------------------------------------------------

    class TransmissaoVertical(models.TextChoices):
        SIM      = '1', 'Sim'
        NAO      = '2', 'Não foi transmissão vertical'
        IGNORADO = '9', 'Ignorado'

    st_transmissao_vertical = models.CharField(
        max_length=1,
        choices=TransmissaoVertical.choices,
        verbose_name="Transmissão Vertical",
        help_text="Provável modo de transmissão do HIV: de mãe para filho.",
    )

    # -------------------------------------------------------------------------
    # Campo 33 - Sexual
    # -------------------------------------------------------------------------

    class TransmissaoSexual(models.TextChoices):
        HOMENS         = '1', 'Relações sexuais com Homens'
        MULHERES       = '2', 'Relações sexuais com Mulheres'
        HOMENS_MULHERES = '3', 'Relações sexuais com homens e mulheres'
        NAO_SEXUAL     = '4', 'Não foi transmissão sexual'
        IGNORADO       = '9', 'Ignorado'

    tp_sexual = models.CharField(
        max_length=1,
        choices=TransmissaoSexual.choices,
        verbose_name="Sexual",
        help_text="Provável modo de transmissão do HIV: sexual.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Sanguínea (4 subcampos)
    # -------------------------------------------------------------------------

    st_sanguinea_droga = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Sanguínea – Uso de Droga Injetável",
        help_text="Provável modo de transmissão do HIV: uso de drogas injetáveis.",
    )

    class SimNaoIgnoradoHemofilia(models.TextChoices):
        SIM      = '1', 'Sim'
        NAO      = '2', 'Não'
        IGNORADO = '3', 'Ignorado'

    st_sanguinea_hemofilia = models.CharField(
        max_length=1,
        choices=SimNaoIgnoradoHemofilia.choices,
        verbose_name="Sanguínea – Tratamento/Hemotransfusão para Hemofilia",
        help_text=(
            "Provável modo de transmissão do HIV: tratamento para hemofilia/hemotransfusão. "
            "Para pacientes do sexo feminino, preenchido automaticamente com 2 (Não)."
        ),
    )

    st_sanguinea_transfusao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Sanguínea – Transfusão Sanguínea",
        help_text=(
            "Provável modo de transmissão: transfusão sanguínea. "
            "Se = 1, exige preenchimento de data do evento, UF e município de transfusão."
        ),
    )

    st_sanguinea_acidente = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Sanguínea – Acidente com Material Biológico com Posterior Soroconversão até 6 meses",
        help_text=(
            "Provável modo de transmissão: acidente com material biológico com soroconversão até 6 meses. "
            "Se = 1, exige preenchimento de data do evento, UF e município."
        ),
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Data da transfusão/acidente
    # -------------------------------------------------------------------------

    dt_evento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da Transfusão / Acidente",
        help_text=(
            "Obrigatório quando Transfusão Sanguínea = 1 "
            "ou Acidente com Material Biológico com Posterior Soroconversão = 1."
        ),
    )

    # -------------------------------------------------------------------------
    # Campo 36 - UF de transfusão/acidente
    # -------------------------------------------------------------------------

    co_uf_transfusao = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF da Transfusão / Acidente",
        help_text="Obrigatório quando transfusão sanguínea = 1 ou acidente com material biológico = 1.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Município da transfusão/acidente
    # -------------------------------------------------------------------------

    co_municipio_transfusao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município da Transfusão / Acidente",
        help_text="Código IBGE do município onde foi realizada a transfusão/acidente.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Instituição onde foi realizada a transfusão/acidente
    # -------------------------------------------------------------------------

    co_unidade_transfusao = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        verbose_name="Código da Instituição de Transfusão / Acidente",
        help_text="Código da instituição onde foi realizada a transfusão ou acidente com material biológico.",
    )
    no_unidade_transfusao = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Nome da Instituição de Transfusão / Acidente",
        help_text="Nome da instituição onde foi realizada a transfusão ou acidente com material biológico.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Após investigação, a transfusão/acidente foi causa da infecção?
    # -------------------------------------------------------------------------

    class CategoriaExposicaoInvestigacao(models.TextChoices):
        SIM          = '1', 'Sim'
        NAO          = '2', 'Não'
        NAO_SE_APLICA = '3', 'Não se aplica'

    tp_categoria_exposicao = models.CharField(
        max_length=2,
        choices=CategoriaExposicaoInvestigacao.choices,
        null=True,
        blank=True,
        verbose_name="Transfusão/Acidente foi causa da infecção pelo HIV?",
        help_text=(
            "Após investigação conforme algoritmo do PN DST/AIDS, "
            "a transfusão/acidente com material biológico foi considerada causa da infecção. "
            "Obrigatório se transfusão sanguínea = 1 ou acidente material biológico = 1."
        ),
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Evidência laboratorial de infecção pelo HIV
    # -------------------------------------------------------------------------

    tp_teste_triagem_1 = models.CharField(
        max_length=1,
        choices=ResultadoTeste.choices,
        verbose_name="Teste de Triagem Anti-HIV",
        help_text="Evidência laboratorial de infecção pelo HIV (teste de triagem). Não aceita categoria 5-indeterminado.",
    )

    dt_coleta_triagem_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da Coleta – Teste de Triagem",
        help_text="Data da coleta do teste de triagem.",
    )

    tp_teste_confirmatorio = models.CharField(
        max_length=1,
        choices=ResultadoTesteComIndeterminado.choices,
        verbose_name="Teste Confirmatório Anti-HIV",
        help_text="Evidência laboratorial de infecção pelo HIV (teste confirmatório).",
    )

    tp_teste_rapido_1 = models.CharField(
        max_length=1,
        choices=ResultadoTeste.choices,
        null=True,
        blank=True,
        verbose_name="Teste Rápido 1",
        help_text="Resultado do teste rápido 1. Não aceita categoria 5-indeterminado.",
    )

    tp_teste_rapido_2 = models.CharField(
        max_length=1,
        choices=ResultadoTeste.choices,
        null=True,
        blank=True,
        verbose_name="Teste Rápido 2",
        help_text="Resultado do teste rápido 2. Não aceita categoria 5-indeterminado.",
    )

    tp_teste_rapido_3 = models.CharField(
        max_length=1,
        choices=ResultadoTeste.choices,
        null=True,
        blank=True,
        verbose_name="Teste Rápido 3",
        help_text="Resultado do teste rápido 3. Não aceita categoria 5-indeterminado.",
    )

    dt_coleta_rapido_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da Coleta – Testes Rápidos",
        help_text="Data de realização dos testes rápidos.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Critério Rio de Janeiro / Caracas
    # -------------------------------------------------------------------------

    st_sarcoma = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério RJ/Caracas – Sarcoma de Kaposi (10 pts)",
        help_text="Sarcoma de Kaposi. Pontuação 10.",
    )
    st_tuberculose_disseminada = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério RJ/Caracas – Tuberculose Disseminada/Extrapulmonar/Não Cavitária (10 pts)",
        help_text="Tuberculose disseminada/extrapulmonar/não cavitária. Pontuação 10.",
    )
    st_candidose_oral = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério RJ/Caracas – Candidose Oral ou Leucoplasia Pilosa (5 pts)",
        help_text="Candidíase oral ou leucoplasia pilosa. Pontuação 5.",
    )
    st_tuberculose_pulmonar = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério RJ/Caracas – Tuberculose Pulmonar Cavitária ou Não Especificada (5 pts)",
        help_text="Tuberculose pulmonar cavitária ou não especificada. Pontuação 5.",
    )
    st_herpes_zoster = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério RJ/Caracas – Herpes Zoster em Indivíduo ≤ 60 Anos (5 pts)",
        help_text="Herpes Zoster em indivíduo menor ou igual a 60 anos. Pontuação 5.",
    )
    st_disfuncao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério RJ/Caracas – Disfunção do Sistema Nervoso Central (5 pts)",
        help_text="Disfunção do sistema nervoso central. Pontuação 5.",
    )
    st_diarreia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério RJ/Caracas – Diarréia ≥ 1 Mês (2 pts)",
        help_text="Diarréia igual ou maior a 1 mês. Pontuação 2.",
    )
    st_febre = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério RJ/Caracas – Febre ≥ 38ºC por ≥ 1 Mês (2 pts)",
        help_text="Febre maior ou igual a 38ºC por tempo maior ou igual a 1 mês. Excluída tuberculose como causa. Pontuação 2.",
    )
    st_caquexia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério RJ/Caracas – Caquexia ou Perda de Peso > 10% (2 pts)",
        help_text="Caquexia ou perda de peso maior que 10%. Excluída tuberculose como causa. Pontuação 2.",
    )
    st_astenia_mes_1 = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério RJ/Caracas – Astenia ≥ 1 Mês (2 pts)",
        help_text="Astenia maior ou igual a 1 mês. Excluída tuberculose como causa. Pontuação 2.",
    )
    st_dermatite = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério RJ/Caracas – Dermatite Persistente (2 pts)",
        help_text="Dermatite persistente. Pontuação 2.",
    )
    st_anemia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério RJ/Caracas – Anemia e/ou Linfopenia e/ou Trombocitopenia (2 pts)",
        help_text="Anemia e/ou linfopenia e/ou trombocitopenia. Pontuação 2.",
    )
    st_tosse = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério RJ/Caracas – Tosse Persistente ou Qualquer Pneumonia (2 pts)",
        help_text="Tosse persistente ou qualquer pneumonia. Excluída tuberculose como causa. Pontuação 2.",
    )
    st_linfadenopatia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério RJ/Caracas – Linfadenopatia ≥ 1 cm, ≥ 2 Sítios Extra-Inguinais por ≥ 1 Mês (2 pts)",
        help_text="Linfadenopatia maior ou igual a 1 cm, maior ou igual a 2 sítios extra-inguinais por tempo maior ou igual a 1 mês. Pontuação 2.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Critério CDC Adaptado
    # -------------------------------------------------------------------------

    st_cancer = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Câncer Cervical Invasivo",
        help_text="Câncer cervical invasivo. Para pacientes do sexo masculino, preenchido automaticamente com 2.",
    )
    st_candidose_esofago = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Candidose de Esôfago",
        help_text="Candidose de esôfago, traquéia, brônquios ou pulmão.",
    )
    st_candidose_traqueia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Candidose de Traquéia, Brônquio, Pulmão",
        help_text="Candidose de traquéia, brônquios ou pulmão.",
    )
    st_citomegalovirose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Citomegalovirose (exceto fígado, baço ou linfonodos)",
        help_text="Citomegalovirose, exceto fígado, baço ou linfonodos.",
    )
    st_criptococose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Criptococose Extrapulmonar",
        help_text="Criptococose extrapulmonar.",
    )
    st_criptosporidiose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Criptosporidiose Intestinal Crônica > 1 Mês",
        help_text="Criptosporidiose intestinal crônica por mais de 1 mês.",
    )
    st_herpes_simples = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Herpes Simples Mucocutâneo > 1 Mês",
        help_text="Herpes simples mucocutâneo por mais de 1 mês, esôfago, brônquios ou pulmão.",
    )
    st_histoplasmose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Histoplasmose Disseminada",
        help_text="Histoplasmose disseminada.",
    )
    st_isosporidiose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Isosporidiose Intestinal Crônica > 1 Mês",
        help_text="Isosporíase intestinal crônica por mais de 1 mês.",
    )
    st_leucoencefalopatia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Leucoencefalopatia Multifocal Progressiva",
        help_text="Leucoencefalopatia multifocal progressiva.",
    )
    st_linfoma_hodgkin = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Linfoma Não Hodgkin e Outros Linfomas",
        help_text="Linfoma não Hodgkin e outros linfomas.",
    )
    st_linfoma_primario = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Linfoma Primário do Cérebro",
        help_text="Linfoma primário do cérebro.",
    )
    st_micobacteriose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Micobacteriose Disseminada (exceto tuberculose e hanseníase)",
        help_text="Micobacteriose disseminada, exceto tuberculose e hanseníase.",
    )
    st_pneumonia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Pneumonia por Pneumocystis carinii",
        help_text="Pneumonia por Pneumocystis carinii.",
    )
    st_reativacao_chagas = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Reativação de Doença de Chagas (meningoencefalite e/ou miocardite)",
        help_text="Reativação de doença de Chagas (meningoencefalite e/ou miocardite).",
    )
    st_salmonelose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Salmonelose (Septicemia Recorrente Não-Tifóide)",
        help_text="Salmonelose: septicemia recorrente não-tifóide.",
    )
    st_toxoplasmose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Toxoplasmose Cerebral",
        help_text="Toxoplasmose cerebral.",
    )
    st_contagem_lifocitos = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Contagem de Linfócitos T CD4+ < 350 cel/mm³",
        help_text="Contagem de linfócitos T CD4+ menor que 350 cel/mm³.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Critério Óbito
    # -------------------------------------------------------------------------

    st_criterio_obito = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério Óbito",
        help_text=(
            "Declaração de óbito com menção de aids, ou HIV e causa de morte associada à "
            "imunodeficiência, sem classificação por outro critério após investigação. "
            "Se = 1, campo Evolução do caso deve ser preenchido com 2 (Óbito por aids)."
        ),
    )

    # -------------------------------------------------------------------------
    # Campo 44 - UF onde se realiza o tratamento
    # -------------------------------------------------------------------------

    co_uf_tratamento = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF onde se Realiza o Tratamento",
        help_text="Unidade federada onde se realiza o tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Município onde se realiza o tratamento
    # -------------------------------------------------------------------------

    co_municipio_tratamento = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município onde se Realiza o Tratamento",
        help_text="Código do município onde se realiza o tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Unidade de saúde onde se realiza o tratamento
    # -------------------------------------------------------------------------

    co_unidade_tratamento = models.DecimalField(
        max_digits=8,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Código da Unidade de Saúde de Tratamento",
        help_text="Código da unidade de saúde onde se realiza o tratamento.",
    )
    no_unidade_tratamento = models.CharField(
        max_length=70,
        null=True,
        blank=True,
        verbose_name="Nome da Unidade de Saúde de Tratamento",
        help_text="Nome da unidade de saúde onde se realiza o tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Evolução do caso
    # -------------------------------------------------------------------------

    class EvolucaoCaso(models.TextChoices):
        VIVO               = '1', 'Vivo'
        OBITO_AIDS         = '2', 'Óbito por Aids'
        OBITO_OUTRAS       = '3', 'Óbito por outras causas'
        IGNORADO           = '9', 'Ignorado'

    tp_evolucao_caso = models.CharField(
        max_length=1,
        choices=EvolucaoCaso.choices,
        null=True,
        blank=True,
        verbose_name="Evolução do Caso",
        help_text=(
            "Obrigatório se Critério óbito = 1; nesse caso deve ser preenchido com 2 (Óbito por aids)."
        ),
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Data do óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do Óbito",
        help_text=(
            "Obrigatório se Evolução do caso = 2 ou 3. "
            "Se Critério óbito = 1, a data do óbito deve ser menor ou igual à data de notificação."
        ),
    )

    # -------------------------------------------------------------------------
    # Campos internos (atribuídos automaticamente pelo sistema)
    # -------------------------------------------------------------------------

    class CriterioDefinicao(models.TextChoices):
        CDC_ADAPTADO   = '100', 'CDC Adaptado'
        RIO_CARACAS    = '300', 'Rio de Janeiro / Caracas'
        CRITERIO_OBITO = '600', 'Critério Óbito'
        DESCARTADO     = '900', 'Descartado'
        HIV_POSITIVO   = '901', 'HIV+'

    tp_criterio_definicao = models.CharField(
        max_length=3,
        choices=CriterioDefinicao.choices,
        null=True,
        blank=True,
        verbose_name="Critério de Definição de Caso (campo interno)",
        help_text=(
            "Atribuído automaticamente pelo sistema com base na hierarquia: "
            "1º CDC Adaptado (100), 2º Rio/Caracas (300), 3º Óbito (600), 5º HIV+ (901), 6º Descartado (900)."
        ),
    )

    tp_categoria_exposicao_calculada = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Categoria de Exposição (campo interno)",
        help_text=(
            "Categoria de exposição ao HIV atribuída automaticamente pelo sistema "
            "com base na hierarquia e combinação dos campos de transmissão. "
            "Ex: 10-Homossexual, 30-Heterossexual, 60-Transfusão, 80-Perinatal, 90-Ignorado."
        ),
    )

    # -------------------------------------------------------------------------
    # Campo de lote - Transferência vertical da investigação
    # -------------------------------------------------------------------------

    nu_lote_vertical = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        verbose_name="Lote de Transferência Vertical",
        help_text="Identificador do lote de transferência vertical da investigação entre níveis do sistema.",
    )

    class Meta:
        db_table = 'aids_adulto'
        verbose_name = 'AIDS Adulto'
        verbose_name_plural = 'AIDS Adulto'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] AIDS Adulto – Critério {self.tp_criterio_definicao}"