from datetime import date
from django import forms 
from reserva.models import Reserva

class ReservaForm(forms.ModelForm):
    def clean_data (self):
        data_1 = self.cleaned_data['data_agendamento']
        hoje_1 = date.today()
        if data_1 < hoje_1 :
            raise forms.ValidationError ('Não é possivel realizar uma reserva para o passado!')
 
    
    class Meta:
        model = Reserva
        fields = [ 'nome', 'nome_pet', 'telefone', 'email','data_agendamento',
                  'horario', 'tamanho','levaetraz','petshop','observacao']

        