# coding: utf-8
from django.db.models import Q, Sum
from datetime import date

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView  #, ListView # DeleteView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.contenttypes.models import ContentType

from django.shortcuts import get_object_or_404, redirect, render

from .models import (
    Agenda,
    CartaoCredito,
    Conta,
    Servico,
    Tarefa,
    )

from .forms import (
    AgendaForm,
    CartaoCreditoForm,
    CartaoCreditoBaseSearchForm,
    ServicoForm,
    TarefaForm,
    TarefaSearchForm,
    )

from helper.core.views import SearchFormListView

@login_required
def agenda_form(request, conta_pk, pk=None):
    '''
        #12
    '''
    conta = get_object_or_404(Conta, id=conta_pk)
    if pk:
        agenda = get_object_or_404(Agenda, pk=pk)
        msg = u'agenda alterada com sucesso.'
    else:
        agenda = None
        msg = u'agenda criada.'

    form = AgendaForm(request.POST or None, instance=agenda, user=request.user, conta=conta)
    context = {}
    context['conta'] = conta
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            agenda = form.save()
            messages.success(request, msg)

            return redirect(reverse('agenda_list', kwargs={'conta_pk': conta.pk}))
        else:
            messages.warning(request, u'Falha no cadastro de agenda')

    return render(request,'agenda/agenda_form.html', context)

@login_required
def agenda_list(request, conta_pk):
    conta = get_object_or_404(Conta, id=conta_pk)
    object_list = Agenda.objects.filter(conta=conta)

    context = {}
    context['conta'] = conta
    context['object_list'] = object_list
    return render(request, 'agenda/agenda_list.html', context)

@login_required
def servico_form(request, conta_pk, pk=None):
    '''
        #12
    '''
    conta = get_object_or_404(Conta, id=conta_pk)
    if pk:
        servico = get_object_or_404(Servico, pk=pk)
        msg = u'servico alterado com sucesso.'
    else:
        servico = None
        msg = u'servico criado.'

    form = ServicoForm(request.POST or None, instance=servico, conta=conta)

    context = {}
    context['conta'] = conta
    context['form'] = form
    
    if request.method == 'POST':
        if form.is_valid():
            servico = form.save()
            messages.success(request, msg)

            return redirect(reverse('servico_list', kwargs={'conta_pk': conta.pk}))
        else:
            messages.warning(request, u'Falha no cadastro de serviço')

    return render(request,'agenda/servico_form.html',context)


@login_required
def servico_list(request, conta_pk):
    conta = get_object_or_404(Conta, id=conta_pk)
    object_list = Servico.objects.filter(agenda__conta__id=conta_pk)
    # form = ServicoSearchForm(request.POST or None)
    context = {}
    context['conta'] = conta
    context['object_list'] = object_list
    # context['form'] = form

    return render(
        request, 'agenda/servico_list.html', context)

@login_required
def tarefa_form(request, conta_pk, pk=None):
    '''
        #12
    '''
    conta = get_object_or_404(Conta, id=conta_pk)
    if pk:
        tarefa = get_object_or_404(Tarefa, pk=pk)
        msg = u'Tarefa alterada com sucesso.'
    else:
        tarefa = None
        msg = u'Tarefa criada.'

    form = TarefaForm(request.POST or None, instance=tarefa, conta=conta)
    context = {}
    context['conta'] = conta
    context['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            tarefa = form.save()
            messages.success(request, msg)

            return redirect(reverse('tarefa_list', kwargs={'conta_pk': conta.pk}))
        else:
            messages.warning(request, u'Falha no cadastro de tarefa de Coleta')

    return render(request,'agenda/tarefa_form.html', context)


class TarefaFormListView(SearchFormListView):
    '''
    ref #19
    '''
    def get(self, request, *args, **kwargs):
        self.form = self.get_form(self.get_form_class())
        
        conta = None
        if 'conta_pk' in self.kwargs:
            conta_pk = self.kwargs['conta_pk']
            conta = get_object_or_404(Conta, id=conta_pk)

        if self.form.is_valid():
            self.object_list = self.form.get_result_queryset().filter(servico__agenda__conta=conta)
        else:
            self.object_list = []
        
        
        context = self.get_context_data(
            object_list=self.object_list,
            form=self.form,
            url_params=request.GET.urlencode(),
            conta=conta,)

        return self.render_to_response(context)

tarefa_list = (login_required(TarefaFormListView.as_view(
                                model=Tarefa,
                                form_class=TarefaSearchForm,
                                paginate_by=30,
                                )
                            )
                        )
#login_required(TemplateView.as_view(template_name='foo_index.html'))

# @login_required
# def tarefa_list(request, conta_pk):
#     conta = get_object_or_404(Conta, id=conta_pk)
#     object_list = Tarefa.objects.filter(servico__agenda__conta__id=conta_pk)

#     context = {}
#     context['conta'] = conta
#     context['object_list'] = object_list

#     return render(
#         request, 'agenda/tarefa_list.html', context)


@login_required
def cartao_form(request, conta_pk, pk=None):
    '''
    o cartao é o do dono da conta (um user)
    '''
    conta = get_object_or_404(Conta, id=conta_pk)
    context = {}
    context['conta'] = conta
    if pk:
        cartao = get_object_or_404(CartaoCredito, pk=pk)
        msg = u'Cartao de Crédito alterado com sucesso.'
    else:
        cartao = None
        msg = u'Cartao de Crédito criado.'

    form = CartaoCreditoForm(request.POST or None, instance=cartao, conta=conta)
    context['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            cartao = form.save()
            messages.success(request, msg)

            return redirect(reverse('cartao_list', kwargs={'conta_pk': conta.pk}))
        else:
            messages.warning(request, u'Falha no cadastro de Cartao Credito')

    return render(request, 'agenda/cartaocredito_form.html', context)


@login_required
def cartao_list(request, conta_pk):
    conta = get_object_or_404(Conta, id=conta_pk)
    object_list = CartaoCredito.objects.filter(usuario=conta.dono) # não tem relação: TODO vincular a conta e ou agenda
    form = CartaoCreditoBaseSearchForm(request.POST or None)
    context = {}
    context['conta'] = conta
    context['object_list'] = object_list
    context['form'] = form


    return render(
        request, 'agenda/cartaocredito_list.html', context)