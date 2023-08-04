from django.contrib import admin
from reserva.models import Reserva

@admin.register(Reserva)
class ReservaAdmin (admin.ModelAdmin):
    list_display = ['nome', 'email', 'nome_pet', 'data_agendamento', 'horario', 'petshop',] 
    search_fields = ['nome', 'email', 'nome_pet','data_agendamento','petshop']
    list_display = ['data_agendamento', 'horario', 'tamanho','petshop']




