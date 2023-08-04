from django.shortcuts import render
from base.forms import contatoForm


def inicio(request):
    return render (request, 'index.html')

def contato(request):
    sucesso = False 
    form = contatoForm (request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
                              
    contexto = {
        'telefone': '(14)9.9824.6259',
        'responsavel': 'Rafael Malaquias', 
        'form':form,
        'sucesso':sucesso
    }

    return render(request, 'contato.html',contexto)
