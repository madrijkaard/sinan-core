from django.db import models


class AidsCrianca(models.Model):
    """
    Ficha de Investigação - AIDS Criança
    Dicionário de Dados SINAN NET - Versão 5.0
    Revisado fevereiro/2012.
    Campos 31 a 51 + campos internos + campos de controle
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

    class ResultadoTesteAcido(models.TextChoices):
        DETECTAVEL    = '6', 'Detectável'
        INDETECTAVEL  = '7', 'Indetectável'
        NAO_REALIZADO = '4', 'Não realizado'
        IGNORADO      = '9', 'Ignorado'

    # -------------------------------------------------------------------------
    # Campo 31 - Idade da mãe
    # -------------------------------------------------------------------------

    nu_idade_mae = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Idade da mãe",
        help_text="Idade da mãe no momento do diagnóstico.",
    )

    # -------------------------------------------------------------------------
    # Campo 32 - Escolaridade da mãe
    # -------------------------------------------------------------------------

    class EscolaridadeMae(models.TextChoices):
        ANALFABETO              = '0', 'Analfabeto'
        EF_4_SERIE_INCOMPLETA   = '1', 'Até 4ª série incompleta do EF'
        EF_4_SERIE_COMPLETA     = '2', 'Até 4ª série completa do EF'
        EF_5_8_INCOMPLETA       = '3', '5ª a 8ª série incompleta do EF'
        EF_COMPLETO             = '4', 'Ensino fundamental completo'
        EM_INCOMPLETO           = '5', 'Ensino médio incompleto'
        EM_COMPLETO             = '6', 'Ensino médio completo'
        ES_INCOMPLETA           = '7', 'Educação superior incompleta'
        ES_COMPLETA             = '8', 'Educação superior completa'
        IGNORADA                = '9', 'Ignorada'

    tp_escolaridade_mae = models.CharField(
        max_length=1,
        choices=EscolaridadeMae.choices,
        verbose_name="Escolaridade da mãe",
        help_text="Escolaridade da mãe no momento da notificação do caso.",
    )

    # -------------------------------------------------------------------------
    # Campo 33 - Raça/cor da mãe
    # -------------------------------------------------------------------------

    class RacaMae(models.TextChoices):
        BRANCA   = '1', 'Branca'
        PRETA    = '2', 'Preta'
        AMARELA  = '3', 'Amarela'
        PARDA    = '4', 'Parda'
        INDIGENA = '5', 'Indígena'
        IGNORADO = '9', 'Ignorado'

    tp_raca_mae = models.CharField(
        max_length=1,
        choices=RacaMae.choices,
        verbose_name="Raça/cor da mãe",
        help_text="Cor ou raça declarada pela mãe.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Ocupação da mãe
    # -------------------------------------------------------------------------

    co_ocupacao_mae = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Ocupação da mãe",
        help_text="Código CBO da ocupação da mãe conforme tabela padronizada pelo Sinan.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Tipo de investigação
    # -------------------------------------------------------------------------

    class TipoInvestigacao(models.TextChoices):
        AIDS_MENORES_13 = '2', 'Aids em menores de 13 anos'

    tp_investigacao = models.CharField(
        max_length=1,
        choices=TipoInvestigacao.choices,
        verbose_name="Tipo de investigação",
        help_text="Caso de aids em menores de 13 anos de idade.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Transmissão vertical
    # -------------------------------------------------------------------------

    class TransmissaoVertical(models.TextChoices):
        SIM      = '1', 'Sim'
        NAO      = '2', 'Não foi transmissão vertical'
        IGNORADO = '9', 'Ignorado'

    tp_trans_vertical = models.CharField(
        max_length=1,
        choices=TransmissaoVertical.choices,
        verbose_name="Transmissão vertical",
        help_text="Registra se o provável modo de transmissão foi por transmissão vertical.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Transmissão sexual
    # -------------------------------------------------------------------------

    class TransmissaoSexual(models.TextChoices):
        SO_HOMENS       = '1', 'Relações sexuais só com homens'
        SO_MULHERES     = '2', 'Relações sexuais só com mulheres'
        HOMENS_MULHERES = '3', 'Relações sexuais com homens e mulheres'
        NAO_SEXUAL      = '4', 'Não foi transmissão sexual'
        IGNORADO        = '9', 'Ignorado'

    tp_trans_sexual = models.CharField(
        max_length=1,
        choices=TransmissaoSexual.choices,
        verbose_name="Transmissão sexual",
        help_text="Registra se o provável modo de transmissão foi sexual.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Transmissão sanguínea (4 subcampos)
    # -------------------------------------------------------------------------

    st_trans_sangue_droga = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Transmissão sanguínea – Uso de Drogas Injetáveis",
        help_text="Registra se o provável modo de transmissão foi o uso de drogas injetáveis.",
    )
    st_trans_sangue_hemofilia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Transmissão sanguínea – Tratamento para Hemofilia",
        help_text="Registra se o provável modo de transmissão foi tratamento/hemotransfusão para hemofilia.",
    )
    st_trans_sangue_transfusao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Transmissão sanguínea – Transfusão Sanguínea",
        help_text=(
            "Registra se o provável modo de transmissão foi transfusão sanguínea. "
            "Deve ser comprovada após cumprimento do algoritmo da investigação (RDC 153/ANVISA)."
        ),
    )
    st_trans_sangue_mat_biologico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Transmissão sanguínea – Acidente com Material Biológico com Posterior Soroconversão até 6 Meses",
        help_text=(
            "Registra se o provável modo de transmissão foi acidente com material biológico "
            "com soroconversão até 6 meses."
        ),
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Data da transfusão / acidente
    # -------------------------------------------------------------------------

    dt_evento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da Transfusão / Acidente",
        help_text=(
            "Obrigatório se transfusão sanguínea ou acidente com material biológico = 1."
        ),
    )

    # -------------------------------------------------------------------------
    # Campo 40 - UF da transfusão / acidente
    # -------------------------------------------------------------------------

    co_uf_transfusao = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF da Transfusão / Acidente",
        help_text="Obrigatório se transfusão sanguínea ou acidente com material biológico = 1.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Município onde ocorreu a transfusão / acidente
    # -------------------------------------------------------------------------

    co_municipio_transfusao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município da Transfusão / Acidente",
        help_text="Obrigatório se transfusão sanguínea ou acidente com material biológico = 1.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Instituição onde ocorreu a transfusão / acidente
    # -------------------------------------------------------------------------

    co_unidade_transfusao = models.DecimalField(
        max_digits=8,
        decimal_places=0,
        null=True,
        blank=True,
        verbose_name="Código da Instituição de Transfusão / Acidente",
        help_text="Obrigatório se transfusão sanguínea ou acidente com material biológico = 1.",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Após investigação, a transfusão/acidente foi causa da infecção?
    # -------------------------------------------------------------------------

    class TransfusaoCausa(models.TextChoices):
        SIM           = '1', 'Sim'
        NAO           = '2', 'Não'
        NAO_SE_APLICA = '3', 'Não se aplica'

    tp_transfusao_causa = models.CharField(
        max_length=1,
        choices=TransfusaoCausa.choices,
        null=True,
        blank=True,
        verbose_name="Transfusão/Acidente foi causa da infecção pelo HIV?",
        help_text=(
            "Obrigatório se transmissão sanguínea por transfusão ou acidente com material biológico = 1. "
            "Registra, após investigação conforme normas técnicas do Ministério da Saúde, "
            "se a transfusão ou acidente foi causa da infecção."
        ),
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Evidência laboratorial de infecção pelo HIV
    # -------------------------------------------------------------------------

    # Após 18 meses de vida
    tp_teste_triagem_1 = models.CharField(
        max_length=1,
        choices=ResultadoTeste.choices,
        null=True,
        blank=True,
        verbose_name="Teste de Triagem Anti-HIV (após 18 meses)",
        help_text=(
            "Resultado do teste de triagem Anti-HIV após os 18 meses de vida. "
            "Não habilitado se idade < 18 meses e transmissão vertical = 1."
        ),
    )
    dt_coleta_triagem_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da Coleta – Teste de Triagem",
        help_text="Obrigatório se teste de triagem = 1, 2 ou 3.",
    )
    tp_teste_confirmatorio_aids = models.CharField(
        max_length=1,
        choices=ResultadoTeste.choices,
        null=True,
        blank=True,
        verbose_name="Teste Confirmatório Anti-HIV (após 18 meses)",
        help_text=(
            "Resultado do teste confirmatório Anti-HIV após 18 meses de vida. "
            "Não habilitado se idade < 18 meses e transmissão vertical = 1."
        ),
    )
    dt_coleta_confirmatorio_aids = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da Coleta – Teste Confirmatório",
        help_text="Data da coleta do teste confirmatório.",
    )

    # Testes rápidos
    tp_teste_rapido_1 = models.CharField(
        max_length=1,
        choices=ResultadoTeste.choices,
        null=True,
        blank=True,
        verbose_name="Teste Rápido 1",
        help_text="Resultado do teste rápido 1 conforme algoritmo validado pelo MS (Portaria nº 34/SVS/MS, julho 2005).",
    )
    tp_teste_rapido_2 = models.CharField(
        max_length=1,
        choices=ResultadoTeste.choices,
        null=True,
        blank=True,
        verbose_name="Teste Rápido 2",
        help_text="Resultado do teste rápido 2.",
    )
    tp_teste_rapido_3 = models.CharField(
        max_length=1,
        choices=ResultadoTeste.choices,
        null=True,
        blank=True,
        verbose_name="Teste Rápido 3",
        help_text="Resultado do teste rápido 3.",
    )
    dt_coleta_rapido_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de Realização dos Testes Rápidos",
        help_text="Obrigatório se algum teste rápido for preenchido com 1, 2 ou 3.",
    )

    # Testes de detecção de ácido nucléico (antes dos 18 meses de vida)
    tp_teste_acido_1_aids = models.CharField(
        max_length=1,
        choices=ResultadoTesteAcido.choices,
        null=True,
        blank=True,
        verbose_name="1º Teste de Detecção de Ácido Nucléico",
        help_text="Evidência laboratorial de infecção pelo HIV: 1º teste de detecção de ácido nucléico.",
    )
    dt_coleta_acido_1_aids = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da Coleta – 1º Teste de Ácido Nucléico",
        help_text="Obrigatório se resultado do 1º teste de ácido nucléico = 6 ou 7.",
    )
    tp_teste_acido_2_aids = models.CharField(
        max_length=1,
        choices=ResultadoTesteAcido.choices,
        null=True,
        blank=True,
        verbose_name="2º Teste de Detecção de Ácido Nucléico",
        help_text="Evidência laboratorial de infecção pelo HIV: 2º teste de detecção de ácido nucléico.",
    )
    dt_coleta_acido_2_aids = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da Coleta – 2º Teste de Ácido Nucléico",
        help_text="Data da coleta do 2º teste de detecção de ácido nucléico.",
    )
    tp_teste_acido_3_aids = models.CharField(
        max_length=1,
        choices=ResultadoTesteAcido.choices,
        null=True,
        blank=True,
        verbose_name="3º Teste de Detecção de Ácido Nucléico",
        help_text="Evidência laboratorial de infecção pelo HIV: 3º teste de detecção de ácido nucléico.",
    )
    dt_coleta_acido_3_aids = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da Coleta – 3º Teste de Ácido Nucléico",
        help_text="Data da coleta do 3º teste de detecção de ácido nucléico.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Critério CDC Adaptado
    # Sinais/sintomas de caráter LEVE
    # -------------------------------------------------------------------------

    st_cdc_aumento_parotida = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Aumento Crônico de Parótida",
        help_text="Aumento crônico de parótida.",
    )
    st_cdc_dermatite = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Dermatite Persistente",
        help_text="Dermatite persistente.",
    )
    st_cdc_esplenomegalia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Esplenomegalia",
        help_text="Esplenomegalia.",
    )
    st_cdc_hepatomegalia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Hepatomegalia",
        help_text="Hepatomegalia.",
    )
    st_cdc_infeccao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Infecções Persistentes ou Recorrentes de VAS (Otite ou Sinusite)",
        help_text="Infecções persistentes ou recorrentes de vias aéreas superiores (otite ou sinusite).",
    )
    st_cdc_linfadenopatia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Linfadenopatia >= 0.5 cm em Mais de 2 Sítios",
        help_text="Linfadenopatia >= 0.5 cm em mais de 2 sítios.",
    )

    # Sinais/sintomas de caráter MODERADO/GRAVE
    st_cdc_anemia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Anemia por Mais de 30 Dias",
        help_text="Anemia por mais de 30 dias.",
    )
    st_cdc_candidose_esofago = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Candidose de Esôfago",
        help_text="Candidose de esôfago.",
    )
    st_cdc_candidose_traqueia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Candidose de Traquéia, Brônquios ou Pulmões",
        help_text="Candidose de traquéia, brônquios ou pulmões.",
    )
    st_cdc_candidose_oral = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Candidose Oral Resistente ao Tratamento",
        help_text="Candidose oral resistente ao tratamento.",
    )
    st_cdc_citomegalovirose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Citomegalovirose (qualquer local exceto fígado, baço ou linfonodo > 1 mês de idade)",
        help_text="Citomegalovirose em qualquer local que não fígado, baço ou linfonodo, em criança > 1 mês de idade.",
    )
    st_cdc_criptococose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Criptococose Extrapulmonar",
        help_text="Criptococose extrapulmonar.",
    )
    st_cdc_criptosporidiose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Criptosporidiose com Diarréia",
        help_text="Criptosporidiose com diarréia.",
    )
    st_cdc_diarreia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Diarréia Recorrente ou Crônica",
        help_text="Diarréia recorrente ou crônica.",
    )
    st_cdc_encefalopatia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Encefalopatia pelo HIV",
        help_text="Encefalopatia pelo HIV.",
    )
    st_cdc_febre = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Febre Persistente > 1 Mês",
        help_text="Febre persistente por mais de 1 mês.",
    )
    st_cdc_gengivoestomatite = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Gengivo-Estomatite Herpética Recorrente (> 2 episódios/ano)",
        help_text="Gengivo-estomatite herpética recorrente com mais de dois episódios em um ano.",
    )
    st_cdc_hepatite = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Hepatite por HIV",
        help_text="Hepatite por HIV.",
    )
    st_cdc_herpes_bronquios = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Herpes Simples em Brônquios, Pulmões ou Trato Gastrintestinal",
        help_text="Herpes simples em brônquios, pulmões ou trato gastrintestinal.",
    )
    st_cdc_herpes_mucocutaneo = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Herpes Simples Mucocutâneo > 1 Mês em Crianças > 1 Mês",
        help_text="Herpes simples mucocutâneo por mais de 1 mês em crianças com mais de 1 mês de idade.",
    )
    st_cdc_herpes_zoster = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Herpes Zoster (≥ 2 episódios distintos ou em > 1 dermátomo)",
        help_text="Herpes zoster com ao menos 2 episódios distintos ou em mais de um dermátomo.",
    )
    st_cdc_histoplasmose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Histoplasmose Disseminada",
        help_text="Histoplasmose disseminada.",
    )
    st_cdc_infec_bacteriana = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Infecções Bacterianas de Repetição/Múltiplas",
        help_text="Infecções bacterianas de repetição/múltiplas (pneumonia, abcessos em órgãos internos, infecções ósteo-articulares).",
    )
    st_cdc_infec_citomegalovirus = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Infecção por Citomegalovírus < 1 Mês de Idade",
        help_text="Infecção por citomegalovírus em criança com menos de 1 mês de idade.",
    )
    st_cdc_isosporidiose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Isosporidiose Intestinal Crônica > 1 Mês",
        help_text="Isosporidiose intestinal crônica por um período superior a 1 mês.",
    )
    st_cdc_leiomiosarcoma = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Leiomiossarcoma",
        help_text="Leiomiossarcoma.",
    )
    st_cdc_leucoencefalopatia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Leucoencefalopatia Multifocal Progressiva",
        help_text="Leucoencefalopatia multifocal progressiva.",
    )
    st_cdc_linfopenia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Linfopenia por Mais de 30 Dias",
        help_text="Linfopenia por mais de 30 dias.",
    )
    st_cdc_linfoma_hodgkin = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Linfoma Não Hodgkin e Outros Linfomas",
        help_text="Linfoma não Hodgkin e outros linfomas.",
    )
    st_cdc_linfoma_primario = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Linfoma Primário de Cérebro",
        help_text="Linfoma primário de cérebro.",
    )
    st_cdc_miocardiopatia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Miocardiopatia",
        help_text="Miocardiopatia.",
    )
    st_cdc_micobacteriose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Micobacteriose Disseminada (exceto tuberculose e hanseníase)",
        help_text="Micobacteriose disseminada, exceto tuberculose e hanseníase.",
    )
    st_cdc_meningite = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Meningite Bacteriana, Pneumonia ou Sepse (único episódio)",
        help_text="Meningite bacteriana, pneumonia ou sepse em único episódio.",
    )
    st_cdc_nefropatia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Nefropatia",
        help_text="Nefropatia.",
    )
    st_cdc_nocardiose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Norcardiose",
        help_text="Norcardiose.",
    )
    st_cdc_pneumonia_linfoide = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Pneumonia Linfóide Intersticial",
        help_text="Pneumonia linfóide intersticial.",
    )
    st_cdc_pneumonia_carinii = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Pneumonia por P. carinii",
        help_text="Pneumonia por Pneumocystis carinii.",
    )
    st_cdc_salmonelose = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Salmonelose (Sepse ou Septicemia Recorrente Não-Tifóide)",
        help_text="Salmonelose: sepse ou septicemia recorrente não-tifóide.",
    )
    st_cdc_sarcoma = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Sarcoma de Kaposi",
        help_text="Sarcoma de Kaposi.",
    )
    st_cdc_emaciacao = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Síndrome da Emaciação (AIDS Wasting Syndrome)",
        help_text="Síndrome da emaciação (AIDS Wasting Syndrome).",
    )
    st_cdc_toxoplasmose_cerebral = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Toxoplasmose Cerebral em Crianças > 1 Mês de Idade",
        help_text="Toxoplasmose cerebral em crianças com mais de 1 mês de idade.",
    )
    st_cdc_toxoplasmose_iniciada = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Toxoplasmose Iniciada antes de 1 Mês de Idade",
        help_text="Toxoplasmose iniciada antes de 1 mês de idade.",
    )
    st_cdc_trombocitopenia = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Trombocitopenia por Mais de 30 Dias",
        help_text="Trombocitopenia por mais de 30 dias.",
    )
    st_cdc_tuberculose_pulmonar = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Tuberculose Pulmonar",
        help_text="Tuberculose pulmonar.",
    )
    st_cdc_tuberculose_disseminada = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Tuberculose Disseminada ou Extrapulmonar",
        help_text="Tuberculose disseminada ou extrapulmonar.",
    )
    st_cdc_varicela_disseminada = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério CDC – Varicela Disseminada",
        help_text="Varicela disseminada.",
    )

    # Achados laboratoriais – Contagem de linfócitos T CD4+ por faixa etária
    st_achado_1500 = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Achado Laboratorial – CD4+ < 1500 células/mm³ (<25%)",
        help_text="< 1500 células por mm³ (<25%). Somente para crianças com idade inferior a 12 meses.",
    )
    st_achado_1000 = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Achado Laboratorial – CD4+ < 1000 células/mm³ (<25%)",
        help_text="< 1000 células por mm³ (<25%). Somente para crianças de 1 a 5 anos.",
    )
    st_achado_500 = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Achado Laboratorial – CD4+ < 500 células/mm³ (<25%)",
        help_text="< 500 células por mm³ (<25%). Somente para crianças de 6 a 12 anos.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Critério óbito
    # -------------------------------------------------------------------------

    st_criterio_obito = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Critério Óbito",
        help_text=(
            "Declaração de óbito com menção de aids, ou HIV e causa de morte associada à "
            "imunodeficiência, sem classificação por outro critério após investigação. "
            "Se = 1, campo Evolução do caso deve ser obrigatoriamente = 2 (óbito por aids)."
        ),
    )

    # -------------------------------------------------------------------------
    # Campo 47 - UF onde se realiza o tratamento
    # -------------------------------------------------------------------------

    co_uf_tratamento = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="UF onde se Realiza o Tratamento",
        help_text="Unidade federada onde se realiza o tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Município onde se realiza o tratamento
    # -------------------------------------------------------------------------

    co_municipio_tratamento = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Município onde se Realiza o Tratamento",
        help_text="Código do município onde se realiza o tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Unidade de saúde onde se realiza o tratamento
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
    # Campo 50 - Evolução do caso
    # -------------------------------------------------------------------------

    class EvolucaoCaso(models.TextChoices):
        VIVO         = '1', 'Vivo'
        OBITO_AIDS   = '2', 'Óbito por Aids'
        OBITO_OUTRAS = '3', 'Óbito por outras causas'
        IGNORADO     = '9', 'Ignorado'

    tp_evolucao_caso = models.CharField(
        max_length=1,
        choices=EvolucaoCaso.choices,
        null=True,
        blank=True,
        verbose_name="Evolução do Caso",
        help_text=(
            "Obrigatório se critério óbito = 1; nesse caso deve ser preenchido com 2 (Óbito por aids)."
        ),
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Data do óbito
    # -------------------------------------------------------------------------

    dt_obito = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do Óbito",
        help_text=(
            "Obrigatório se evolução = 2 ou 3. "
            "Se critério óbito = 1, a data do óbito deve ser obrigatoriamente igual à data de diagnóstico."
        ),
    )

    # -------------------------------------------------------------------------
    # Campos internos (atribuídos automaticamente pelo sistema)
    # -------------------------------------------------------------------------

    class CriterioDefinicao(models.TextChoices):
        CDC_ADAPTADO   = '100', 'CDC Adaptado'
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
            "Atribuído automaticamente pelo sistema. "
            "Hierarquia: 1º CDC Adaptado (100), 2º Óbito (600), 3º HIV+ (901), 4º Descartado (900)."
        ),
    )

    tp_categoria_exposicao = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        verbose_name="Categoria de Exposição (campo interno)",
        help_text=(
            "Categoria de exposição ao HIV atribuída automaticamente pelo sistema. "
            "Ex: 10-Homossexual, 30-Heterossexual, 60-Transfusão, 80-Perinatal, 90-Ignorado."
        ),
    )

    class Meta:
        db_table = 'aids_crianca'
        verbose_name = 'AIDS Criança'
        verbose_name_plural = 'AIDS Crianças'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] AIDS Criança – Critério {self.tp_criterio_definicao}"