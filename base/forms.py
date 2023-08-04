from django import forms 
from base.models import Contato


class contatoForm(forms.ModelForm):
    
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']
        
        

       