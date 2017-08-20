from django.shortcuts import render
from helper.agenda.models import Conta
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404

@login_required
def contador_leitura(request, conta_pk):
    conta = get_object_or_404(Conta, id=conta_pk)
    if not conta.contador:
    	raise Http404
    contador = conta.contador

    context = {}
    context['contador'] = contador
    context['conta'] = conta
    return render(request, 'contador_leitura.html', context)
