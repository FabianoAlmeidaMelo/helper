# coding: utf-8
from django.shortcuts import render
from helper.core.models import Conta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404

from helper.contabil.forms import (
    ClienteUserSearchForm,
    ContadorForm,
)
from helper.core.views import SearchFormListView


@login_required
def contador_leitura(request, conta_pk):
    """
    acesso do cliente
    """
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
def contador_form(request):
    """
    acesso do contador
    """
    conta = request.user.conta
    contador = conta.contador
    if not contador.can_acess(request.user):
        raise Http404
    form = ContadorForm(request.POST or None, instance=contador, conta=conta)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg = u'cadastro alterado com sucesso.'
            messages.success(request, msg)
        else:
            msg = u'Falha na edição do cadastro: %s ' % form.errors
            messages.warning(request, msg)

    context = {}
    context['form'] = form
    context['contador'] = contador
    context['conta'] = conta
    context['menu_cadastro'] = "active"
    return render(request, 'contabil/contador_form.html', context)


@login_required
def cliente_list(request, conta_pk):
    conta = get_object_or_404(Conta, id=conta_pk)
    page = request.GET.get('page', 1)
    if not conta.can_acess(request.user):
        raise Http404

    form = ClienteUserSearchForm(request.GET or None, conta=conta)
    object_list = form.get_queryset()
   
    paginator = Paginator(object_list, 15)
    try:
        clientes_users = paginator.page(page)
    except PageNotAnInteger:
        clientes_users = paginator.page(1)
    except EmptyPage:
        clientes_users = paginator.page(paginator.num_pages)

    context = {}
    context['conta'] = conta
    context['object_list'] = clientes_users
    context['form'] = form
    context['menu_clientes'] = "active"

    return render(request, 'contabil/cliente_list.html', context)