from django.shortcuts import render
from helper.core.models import Conta
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404

from helper.contabil.forms import ClienteUserSearchForm
from helper.core.views import SearchFormListView


@login_required
def contador_leitura(request, conta_pk):
    conta = get_object_or_404(Conta, id=conta_pk)
    if not conta.contador:
        raise Http404
    contador = conta.contador

    context = {}
    context['contador'] = contador
    context['conta'] = conta
    context['menu_contador'] = "active"
    return render(request, 'contabil/contador_leitura.html', context)


@login_required
def cliente_list(request, conta_pk):
    conta = get_object_or_404(Conta, id=conta_pk)
    if not conta.can_acess(request.user):
        raise Http404
    # form = PrestacaoContasItensSearchForm(request.GET or None, prestacoes_conta=prestacoes_conta)
    form = ClienteUserSearchForm(request.GET or None, conta=conta)
    object_list = form.get_queryset()
    context = {}
    context['conta'] = conta
    context['object_list'] = object_list
    context['form'] = form
    context['menu_clientes'] = "active"

    return render(
        request, 'contabil/cliente_list.html', context)