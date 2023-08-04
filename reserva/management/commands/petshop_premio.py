#Código para sortear um cliente (pet) para ganhar um banho gratis

from django.core.management.base import BaseCommand, CommandParser
from reserva.models import Petshop
import random

class Command (BaseCommand):
    def list_petshops(self):
        return Petshop.objects.all().values_list('pk', flat = True)
    
    def add_arguments(self, parser):
        parser.add_argument(
            'quantify',
            nargs='?',
            default=5,
            type=int,
            help='Quantas pessoas podem participar do sorteio?'
        )
        
        parser.add_argument(
            '-petshop',
            required=True,
            type=int,
            choices=self.list_petshops(),
            help = 'Digite o ID do petshop que vai realizar o  sorteio'
        )
    def escolher_reservas(self, banhos, quantidade):
        banhos_list = list(banhos)
        if quantidade > len(banhos_list):
            quantidade = len(banhos_list)
        return random.sample(banhos_list, quantidade)
    
    def imprimir_info_petshop(self, petshop):
        self.stdout.write(
            self.style.HTTP_INFO(
                'Dados do petshop que realizou o sorteio'
            )
        )
        self.stdout.write(f'Nome do Petshop: {petshop.nome}')
        self.stdout.write(f'Endereço: {petshop.rua}, {petshop.numero}')
        
    def handle(self,*args, **options):
        quantify = options['quantify']
        petshop_id = options['petshop']
        
        petshop = Petshop.objects.get(pk=petshop_id)
        reservas = petshop.reservas.all()
        
        banhos_escolhidos = self.escolher_reservas(reservas, quantify)
        
        self.stdout.write(
            self.style.SUCCESS('Sorteio realizado')
        )
        self.imprimir_info_petshop(petshop)
        for reserva in banhos_escolhidos:
            self.stdout.write(str(reserva))   
    