from django.db import models


class AtendimentoAntirabico(models.Model):
    """
    Ficha de Investigação - Atendimento Anti-rábico
    Dicionário de Dados SINAN NET - Versão 5.0
    Campos 31 a 60 + campos de controle
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

    class SimNaoDesconhecido(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'
        DESCONHECIDA = '3', 'Desconhecida'

    # -------------------------------------------------------------------------
    # Campo 31 - Ocupação
    # -------------------------------------------------------------------------

    co_cbo_ocupacao = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        verbose_name="Ocupação (CBO)",
        help_text="Código CBO da ocupação exercida pelo paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 32 - Tipo de exposição ao vírus rábico (5 subcampos)
    # -------------------------------------------------------------------------

    st_exp_virusrabico_indireto = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Tipo de exposição - Contato Indireto",
        help_text="Informa se a exposição foi por contato indireto.",
    )
    st_exp_virusrabico_arranhadura = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Tipo de exposição - Arranhadura",
        help_text="Informa se a exposição foi por arranhadura.",
    )
    st_exp_virusrabico_lambedura = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Tipo de exposição - Lambedura",
        help_text="Informa se a exposição foi por lambedura.",
    )
    st_exp_virusrabico_mordedura = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Tipo de exposição - Mordedura",
        help_text="Informa se a exposição foi por mordedura.",
    )
    st_exp_virusrabico_outro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        verbose_name="Tipo de exposição - Outros",
        help_text="Informa se houve outro modo de exposição ao vírus rábico.",
    )
    ds_exp_virusrabico_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Tipo de exposição - Outros (especificar)",
        help_text="Especificação de outro modo de exposição ao vírus rábico.",
    )

    # -------------------------------------------------------------------------
    # Campo 33 - Localização do ferimento (6 subcampos)
    # -------------------------------------------------------------------------

    tp_localizacao_mucosa = models.CharField(
        max_length=1,
        choices=SimNaoDesconhecido.choices,
        verbose_name="Localização - Mucosa",
        help_text="Informa se o ferimento foi em mucosa.",
    )
    tp_localizacao_cabeca_pescoco = models.CharField(
        max_length=1,
        choices=SimNaoDesconhecido.choices,
        verbose_name="Localização - Cabeça/Pescoço",
        help_text="Informa se o ferimento foi em cabeça ou pescoço.",
    )
    tp_localizacao_maos_pes = models.CharField(
        max_length=1,
        choices=SimNaoDesconhecido.choices,
        verbose_name="Localização - Mãos/Pés",
        help_text="Informa se o ferimento foi em mãos ou pés.",
    )
    tp_localizacao_tronco = models.CharField(
        max_length=1,
        choices=SimNaoDesconhecido.choices,
        verbose_name="Localização - Tronco",
        help_text="Informa se o ferimento foi em tronco.",
    )
    tp_localizacao_membro_superior = models.CharField(
        max_length=1,
        choices=SimNaoDesconhecido.choices,
        verbose_name="Localização - Membros Superiores",
        help_text="Informa se o ferimento foi em membros superiores.",
    )
    tp_localizacao_membro_inferior = models.CharField(
        max_length=1,
        choices=SimNaoDesconhecido.choices,
        verbose_name="Localização - Membros Inferiores",
        help_text="Informa se o ferimento foi em membros inferiores.",
    )

    # -------------------------------------------------------------------------
    # Campo 34 - Ferimento
    # -------------------------------------------------------------------------

    class TipoFerimentoGeral(models.TextChoices):
        UNICO = '1', 'Único'
        MULTIPLO = '2', 'Múltiplo'
        SEM_FERIMENTO = '3', 'Sem ferimento'
        IGNORADO = '9', 'Ignorado'

    tp_ferimento = models.CharField(
        max_length=1,
        choices=TipoFerimentoGeral.choices,
        verbose_name="Ferimento",
        help_text="Informa se o ferimento é único, múltiplo, inexistente ou ignorado.",
    )

    # -------------------------------------------------------------------------
    # Campo 35 - Tipo de ferimento (3 subcampos)
    # -------------------------------------------------------------------------

    st_tipo_ferimento_profundo = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de ferimento - Profundo",
        help_text="Informa se o ferimento é profundo.",
    )
    st_tipo_ferimento_superficial = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de ferimento - Superficial",
        help_text="Informa se o ferimento é superficial.",
    )
    st_tipo_ferimento_desconhecido = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de ferimento - Desconhecido",
        help_text="Informa se o tipo de ferimento é desconhecido.",
    )

    # -------------------------------------------------------------------------
    # Campo 36 - Data da exposição
    # -------------------------------------------------------------------------

    dt_exposicao = models.DateField(
        verbose_name="Data da exposição",
        help_text="Data da ocorrência da agressão. Deve ser <= data de atendimento.",
    )

    # -------------------------------------------------------------------------
    # Campo 37 - Antecedentes de tratamento anti-rábico
    # -------------------------------------------------------------------------

    st_ante_trat_antirabico_pre_exp = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Antecedente - Pré-exposição",
        help_text="Informa se houve tratamento anti-rábico pré-exposição.",
    )
    st_ante_trat_antirabico_pos_exp = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Antecedente - Pós-exposição completo",
        help_text="Informa se houve tratamento anti-rábico pós-exposição completo.",
    )

    # -------------------------------------------------------------------------
    # Campo 38 - Quando foi concluído
    # -------------------------------------------------------------------------

    class PeriodoConclusao(models.TextChoices):
        ATE_90_DIAS = '1', 'Até 90 dias'
        APOS_90_DIAS = '2', 'Após 90 dias'

    st_concluido = models.CharField(
        max_length=1,
        choices=PeriodoConclusao.choices,
        null=True,
        blank=True,
        verbose_name="Quando foi concluído",
        help_text="Período de conclusão do tratamento antecedente.",
    )

    # -------------------------------------------------------------------------
    # Campo 39 - Número de doses aplicadas
    # -------------------------------------------------------------------------

    nu_dose_aplicada = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Número de doses aplicadas",
        help_text="Número de doses aplicadas no tratamento antecedente.",
    )

    # -------------------------------------------------------------------------
    # Campo 40 - Espécie do animal agressor
    # -------------------------------------------------------------------------

    class EspecieAnimal(models.TextChoices):
        CANINA = '1', 'Canina'
        FELINA = '2', 'Felina'
        QUIROPTERA = '3', 'Quiróptera (morcego)'
        PRIMATA = '4', 'Primata (macaco)'
        RAPOSA = '5', 'Raposa'
        HERBIVORO_DOMESTICO = '6', 'Herbívoro doméstico'
        OUTRA = '7', 'Outra'

    tp_animal_agressor = models.CharField(
        max_length=1,
        choices=EspecieAnimal.choices,
        verbose_name="Espécie do animal agressor",
        help_text="Espécie do animal responsável pela agressão.",
    )
    ds_animal_agressor_herbivoro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Herbívoro doméstico (especificar)",
        help_text="Especificar o herbívoro doméstico agressor.",
    )
    ds_animal_agressor_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outra espécie (especificar)",
        help_text="Especificar outra espécie de animal agressor.",
    )

    # -------------------------------------------------------------------------
    # Campo 41 - Condição do animal para fins de conduta do tratamento
    # -------------------------------------------------------------------------

    class CondicaoAnimalTratamento(models.TextChoices):
        SADIO = '1', 'Sadio'
        SUSPEITO = '2', 'Suspeito'
        RAIOSO = '3', 'Raivoso'
        MORTO_DESAPARECIDO = '4', 'Morto/desaparecido'

    tp_condicao_animal_tratamento = models.CharField(
        max_length=1,
        choices=CondicaoAnimalTratamento.choices,
        null=True,
        blank=True,
        verbose_name="Condição do animal",
        help_text="Condição do animal após a agressão para fins de conduta do tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 42 - Animal passível de observação (somente cão ou gato)
    # -------------------------------------------------------------------------

    class AnimalPassivelObservacao(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'

    tp_animal_passivel_obs = models.CharField(
        max_length=1,
        choices=AnimalPassivelObservacao.choices,
        null=True,
        blank=True,
        verbose_name="Animal passível de observação",
        help_text="Informa se o animal pode ser observado (somente para cão ou gato).",
    )

    # -------------------------------------------------------------------------
    # Campo 43 - Tratamento indicado
    # -------------------------------------------------------------------------

    class TratamentoIndicado(models.TextChoices):
        PRE_EXPOSICAO = '1', 'Pré-exposição'
        DISPENSA_TRATAMENTO = '2', 'Dispensa de tratamento'
        OBSERVACAO_ANIMAL = '3', 'Observação do animal (se cão ou gato)'
        OBSERVACAO_VACINA = '4', 'Observação + vacina'
        VACINA = '5', 'Vacina'
        SORO_VACINA = '6', 'Soro + vacina'
        ESQUEMA_REEXXPOSICAO = '7', 'Esquema de Reexposição'

    tp_tratamento_indicado = models.CharField(
        max_length=1,
        choices=TratamentoIndicado.choices,
        null=True,
        blank=True,
        verbose_name="Tratamento indicado",
        help_text="Tipo de tratamento atualmente indicado.",
    )

    # -------------------------------------------------------------------------
    # Campo 44 - Laboratório produtor da vacina
    # -------------------------------------------------------------------------

    class ProdutorVacina(models.TextChoices):
        BUTANTAN = '1', 'Instituto Butantan'
        VITAL_BRASIL = '2', 'Instituto Vital Brasil'
        AVENTIS_PASTEUR = '3', 'Aventis Pasteur'
        OUTRO = '4', 'Outro'

    tp_produtor_vacina = models.CharField(
        max_length=1,
        choices=ProdutorVacina.choices,
        null=True,
        blank=True,
        verbose_name="Laboratório produtor da vacina",
        help_text="Laboratório produtor da vacina utilizada.",
    )
    ds_produtor_vacina_outro = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro produtor de vacina (especificar)",
        help_text="Especificar outro laboratório produtor da vacina.",
    )

    # -------------------------------------------------------------------------
    # Campo 45 - Número do lote
    # -------------------------------------------------------------------------

    nu_lote = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Número do lote",
        help_text="Número do lote da primeira vacina.",
    )

    # -------------------------------------------------------------------------
    # Campo 46 - Data do vencimento
    # -------------------------------------------------------------------------

    dt_vencimento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do vencimento",
        help_text="Data do vencimento da primeira vacina.",
    )

    # -------------------------------------------------------------------------
    # Campo 47 - Datas das aplicações da vacina (5 doses)
    # -------------------------------------------------------------------------

    dt_vacina_dose_1 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da 1ª dose da vacina",
        help_text="Data da aplicação da primeira dose.",
    )
    dt_vacina_dose_2 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da 2ª dose da vacina",
        help_text="Data da aplicação da segunda dose.",
    )
    dt_vacina_dose_3 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da 3ª dose da vacina",
        help_text="Data da aplicação da terceira dose.",
    )
    dt_vacina_dose_4 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da 4ª dose da vacina",
        help_text="Data da aplicação da quarta dose.",
    )
    dt_vacina_dose_5 = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da 5ª dose da vacina",
        help_text="Data da aplicação da quinta dose.",
    )

    # -------------------------------------------------------------------------
    # Campo 48 - Condição final do animal
    # -------------------------------------------------------------------------

    class CondicaoFinalAnimal(models.TextChoices):
        NEGATIVO_CLINICA = '1', 'Negativo para raiva (clínica)'
        NEGATIVO_LAB = '2', 'Negativo para raiva (laboratório)'
        POSITIVO_CLINICA = '3', 'Positivo para raiva (clínica)'
        POSITIVO_LAB = '4', 'Positivo para raiva (laboratório)'
        MORTO_SEM_DIAG = '5', 'Morto/sacrificado/sem diagnóstico'
        IGNORADO = '9', 'Ignorado'

    tp_condicao_animal = models.CharField(
        max_length=1,
        choices=CondicaoFinalAnimal.choices,
        null=True,
        blank=True,
        verbose_name="Condição final do animal",
        help_text="Condição final do animal após período de observação.",
    )

    # -------------------------------------------------------------------------
    # Campo 49 - Houve interrupção do tratamento
    # -------------------------------------------------------------------------

    class InterrupcaoTratamento(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'

    tp_interrupcao_tratamento = models.CharField(
        max_length=1,
        choices=InterrupcaoTratamento.choices,
        null=True,
        blank=True,
        verbose_name="Houve interrupção do tratamento",
        help_text="Informa se o tratamento foi interrompido.",
    )

    # -------------------------------------------------------------------------
    # Campo 50 - Motivo da interrupção
    # -------------------------------------------------------------------------

    class MotivoInterrupcao(models.TextChoices):
        INDICACAO_US = '1', 'Indicação da Unidade de saúde'
        ABANDONO = '2', 'Abandono'
        TRANSFERENCIA = '3', 'Transferência'

    tp_motivo_interrupcao = models.CharField(
        max_length=1,
        choices=MotivoInterrupcao.choices,
        null=True,
        blank=True,
        verbose_name="Motivo da interrupção",
        help_text="Motivo da interrupção do tratamento.",
    )

    # -------------------------------------------------------------------------
    # Campo 51 - Busca ativa em caso de abandono
    # -------------------------------------------------------------------------

    class BuscaAtiva(models.TextChoices):
        SIM = '1', 'Sim'
        NAO = '2', 'Não'

    tp_abandono_tratamento = models.CharField(
        max_length=1,
        choices=BuscaAtiva.choices,
        null=True,
        blank=True,
        verbose_name="Unidade procurou o paciente",
        help_text="Informa se a unidade de saúde, em caso de abandono, fez busca-ativa do paciente.",
    )

    # -------------------------------------------------------------------------
    # Campo 52 - Evento adverso à vacina
    # -------------------------------------------------------------------------

    st_adverso_vacina = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Evento adverso à vacina",
        help_text="Informa se houve reação adversa à vacina.",
    )

    # -------------------------------------------------------------------------
    # Campo 53 - Indicação do soro anti-rábico
    # -------------------------------------------------------------------------

    st_soro_antirabico = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Indicação do soro anti-rábico",
        help_text="Informa se houve indicação da aplicação do soro anti-rábico.",
    )

    # -------------------------------------------------------------------------
    # Campo 54 - Peso do paciente
    # -------------------------------------------------------------------------

    nu_peso_paciente = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Peso do paciente (kg)",
        help_text="Peso do paciente em quilogramas.",
    )

    # -------------------------------------------------------------------------
    # Campo 55 - Quantidade e tipo de soro aplicado
    # -------------------------------------------------------------------------

    qt_soro = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Quantidade de soro aplicada (ml)",
        help_text="Quantidade de soro aplicada em mililitros.",
    )

    class TipoSoro(models.TextChoices):
        HETEROLOGO = '1', 'Heterólogo'
        HOMOLOGO = '2', 'Homólogo'

    tp_soro = models.CharField(
        max_length=1,
        choices=TipoSoro.choices,
        null=True,
        blank=True,
        verbose_name="Tipo de soro",
        help_text="Tipo de soro aplicado (heterólogo ou homólogo).",
    )

    # -------------------------------------------------------------------------
    # Campo 56 - Infiltração de soro nos ferimentos
    # -------------------------------------------------------------------------

    tp_infiltracao_soro_total = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Infiltração de soro - Total",
        help_text="Informa se houve infiltração total do soro nos ferimentos.",
    )
    tp_infiltracao_soro_parcial = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Infiltração de soro - Parcial",
        help_text="Informa se houve infiltração parcial do soro nos ferimentos.",
    )

    # -------------------------------------------------------------------------
    # Campo 57 - Laboratório produtor do soro anti-rábico
    # -------------------------------------------------------------------------

    class ProdutorSoro(models.TextChoices):
        BUTANTAN = '1', 'Instituto Butantan'
        VITAL_BRASIL = '2', 'Instituto Vital Brasil'
        AVENTIS_PASTEUR = '3', 'Aventis Pasteur'
        OUTRO = '4', 'Outro'

    tp_produtor_soro_antibico = models.CharField(
        max_length=1,
        choices=ProdutorSoro.choices,
        null=True,
        blank=True,
        verbose_name="Laboratório produtor do soro",
        help_text="Laboratório produtor do soro anti-rábico utilizado.",
    )
    ds_produtor_soro_antibico = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Outro produtor de soro (especificar)",
        help_text="Especificar outro laboratório produtor do soro anti-rábico.",
    )

    # -------------------------------------------------------------------------
    # Campo 58 - Número da partida / lote do soro
    # -------------------------------------------------------------------------

    nu_partida = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Número da partida/lote do soro",
        help_text="Número da partida ou lote do soro anti-rábico utilizado.",
    )

    # -------------------------------------------------------------------------
    # Campo 59 - Evento adverso ao soro
    # -------------------------------------------------------------------------

    st_adverso_soro = models.CharField(
        max_length=1,
        choices=SimNaoIgnorado.choices,
        null=True,
        blank=True,
        verbose_name="Evento adverso ao soro",
        help_text="Informa se houve reação adversa ao soro anti-rábico.",
    )

    # -------------------------------------------------------------------------
    # Campo 60 - Data do encerramento do caso
    # -------------------------------------------------------------------------

    dt_encerramento = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data do encerramento do caso",
        help_text="Data do encerramento do caso. Deve ser >= data de atendimento e <= data atual.",
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
        db_table = 'atendimento_antirabico'
        verbose_name = 'Atendimento Anti-rábico'
        verbose_name_plural = 'Atendimentos Anti-rábico'
        ordering = ['-created_date']

    def __str__(self):
        return f"[{self.code}] Atendimento Anti-rábico – {self.dt_exposicao}"