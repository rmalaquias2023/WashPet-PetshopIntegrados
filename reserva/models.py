from django.db import models

class Reserva (models.Model):
    turno_opcoes=(
        ('Indiferente','Indiferente'),('Manhã','Manhã'),
        ('Tarde','Tarde'))
    
    TAMANHO_OPCOES=(('Pequeno','Pequeno'),('Pequeno','Medio'),('Grande','Grande'))
    
    levaetraz_opcao = (('Sim', 'Sim'), ('Não','Não'))
           
    nome = models.CharField(verbose_name = 'Nome', max_length=50, default = None, blank=True)
    nome_pet = models.CharField(verbose_name = 'Nome do Pet:', max_length=50, default = None, blank=True)
    telefone = models.CharField(verbose_name = 'Telefone', max_length=11,default = None, blank=True)
    email = models.CharField(verbose_name = 'E-mail', max_length=50, default = None, blank=True)
    data_agendamento = models.DateField(verbose_name ='Data', help_text='dd/mm/aaaa', default = None, blank=True)
    horario = models.CharField(verbose_name = 'Horário:', max_length=30, choices=turno_opcoes, default='Indiferente', blank=True)
    tamanho = models.CharField(verbose_name="Tamanho: ", max_length=10, choices=TAMANHO_OPCOES, default=None, blank=True)
    levaetraz = models.CharField (verbose_name= 'Precisa de Transtorte? ',max_length=3,choices=levaetraz_opcao, default=None, blank=True)
    petshop = models.ForeignKey('Petshop', related_name = 'reservas', on_delete=models.CASCADE, blank=True, null= True, default = None)
    observacao = models.TextField(blank=True)
    
    
    def __str__(self):
        return f'{self.nome}: {self.data_agendamento} - {self.horario}'
    
    class Meta:
        verbose_name='Reserva de Banho'
        verbose_name_plural='Reservas de Banhos'

class Petshop (models.Model):
    nome = models.CharField(verbose_name='Petshop', max_length=50)
    rua = models.CharField(verbose_name='Endereço', max_length=100)
    numero = models.CharField(verbose_name='Número', max_length=10)
    bairro = models.CharField(verbose_name='Bairro', max_length=50)
    
    
