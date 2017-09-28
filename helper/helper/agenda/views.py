# coding: utf-8
from django.db.models import Q, Sum
from datetime import date

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView  #, ListView # DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.contenttypes.models import ContentType
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.context import RequestContext

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
    TarefaStatusForm,
    ServicoForm,
    ServicoSearchForm,
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
    if not conta.can_acess(request.user):
        raise Http404
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
    context['menu_administracao'] = "active"

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
    if not conta.can_acess(request.user):
        raise Http404
    object_list = Agenda.objects.filter(conta=conta)

    context = {}
    context['conta'] = conta
    context['object_list'] = object_list
    context['menu_administracao'] = "active"
    return render(request, 'agenda/agenda_list.html', context)

@login_required
def servico_form(request, conta_pk, pk=None):
    '''
        #12
    '''
    conta = get_object_or_404(Conta, id=conta_pk)
    if not conta.can_acess(request.user):
        raise Http404
    if pk:
        servico = get_object_or_404(Servico, pk=pk)
        msg = u'Serviço alterado com sucesso.'
    else:
        servico = None
        msg = u'Serviço criado.'

    form = ServicoForm(request.POST or None, instance=servico, conta=conta)

    context = {}
    context['conta'] = conta
    context['form'] = form
    context['menu_administracao'] = "active"
    
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
    if not conta.can_acess(request.user):
        raise Http404
    form = ServicoSearchForm(request.GET or None, conta=conta)
    object_list = form.get_result_queryset()
    context = {}
    context['conta'] = conta
    context['object_list'] = object_list
    context['form'] = form
    context['menu_administracao'] = "active"

    return render(
        request, 'agenda/servico_list.html', context)

@login_required
def tarefa_form(request, conta_pk, agenda_pk=None, pk=None):
    '''
        #12
    '''
    conta = get_object_or_404(Conta, id=conta_pk)
    if not conta.can_acess(request.user):
        raise Http404
    agenda = None
    if agenda_pk:
        agenda = get_object_or_404(Agenda, id=agenda_pk)
    if pk:
        tarefa = get_object_or_404(Tarefa, pk=pk)
        msg = u'Tarefa alterada com sucesso.'
    else:
        tarefa = None
        msg = u'Tarefa criada.'

    form = TarefaForm(request.POST or None, instance=tarefa, conta=conta, agenda=agenda)
    context = {}
    context['conta'] = conta
    context['agenda'] = agenda
    context['form'] = form
    context['menu_tarefas'] = "active"
    if request.method == 'POST':
        if form.is_valid():
            tarefa = form.save()
            messages.success(request, msg)
            if agenda:
                return redirect(reverse('agenda_tarefa_list', kwargs={'conta_pk': conta.pk, 'agenda_pk':agenda.pk}))
            else:
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
            if not conta.can_acess(request.user):
                raise Http404

        total_pos = total_neg = total = 0
        data_ini = self.form.ini
        data_fim = self.form.fim
        if self.form.is_valid():
            self.object_list = self.form.get_result_queryset().filter(servico__agenda__conta=conta)
            total_pos = sum(self.object_list.filter(tipo=1).values_list('valor', flat=True))
            total_neg = sum(self.object_list.filter(tipo=2).values_list('valor', flat=True))
            total = total_pos - total_neg
            if self.form.__dict__['cleaned_data']['data_ini'] is None:
                self.form.__dict__['cleaned_data']['data_ini'] = data_ini
            else:
                data_ini = self.form.__dict__['cleaned_data']['data_ini']
            if self.form.__dict__['cleaned_data']['data_fim'] is None:
                self.form.__dict__['cleaned_data']['data_fim'] = data_fim
            else:
                data_fim = self.form.__dict__['cleaned_data']['data_fim']
        else:
            self.object_list = []

        get_ = "?data_ini=%s&data_fim=%s" % (
            request.GET.get('data_ini', data_ini),
            request.GET.get('data_fim', data_fim),
            )

        # Marca o Menu 'Tarefas'
        # Nav BAR
        menu_tarefas = "active"
      
        context = self.get_context_data(
            object_list=self.object_list,
            form=self.form,
            url_params=request.GET.urlencode(),
            conta=conta,
            data_ini=data_ini,
            data_fim=data_fim,
            menu_tarefas=menu_tarefas,
            total=total,
            get_=get_,
            entradas=int(total_pos),
            saidas=int(total_neg))

        return self.render_to_response(context)

tarefa_list = (login_required(TarefaFormListView.as_view(
                                model=Tarefa,
                                form_class=TarefaSearchForm,
                                paginate_by=15,
                                template_name='agenda/tarefa_list.html'
                                )
                            )
                        )

class AgendaTarefaFormListView(SearchFormListView):
    '''
    ref #**
    listagem de Tarefas, por agenda
    '''
    def get(self, request, *args, **kwargs):
        self.form = self.get_form(self.get_form_class())
        
        conta = None
        agenda = None
        if 'conta_pk' in self.kwargs:
            conta_pk = self.kwargs['conta_pk']
            conta = get_object_or_404(Conta, id=conta_pk)
            if not conta.can_acess(request.user):
                raise Http404
        if 'agenda_pk' in self.kwargs:
            agenda_pk = self.kwargs['agenda_pk']
            agenda = get_object_or_404(Agenda, id=agenda_pk)
        
        data_ini = self.form.ini
        data_fim = self.form.fim
        total_pos = total_neg = total = 0

        if self.form.is_valid():
            self.object_list = self.form.get_result_queryset().filter(servico__agenda=agenda)
            total_pos = sum(self.object_list.filter(tipo=1).values_list('valor', flat=True))
            total_neg = sum(self.object_list.filter(tipo=2).values_list('valor', flat=True))
            total = total_pos - total_neg
            if self.form.__dict__['cleaned_data']['data_ini'] is None:
                self.form.__dict__['cleaned_data']['data_ini'] = data_ini
            else:
                data_ini = self.form.__dict__['cleaned_data']['data_ini']
            if self.form.__dict__['cleaned_data']['data_fim'] is None:
                self.form.__dict__['cleaned_data']['data_fim'] = data_fim
            else:
                data_fim = self.form.__dict__['cleaned_data']['data_fim']
        else:
            self.object_list = []

        get_ = "?data_ini=%s&data_fim=%s" % (
            request.GET.get('data_ini', data_ini),
            request.GET.get('data_fim', data_fim),
            )

        menu_tarefas_agenda = "active"

        context = self.get_context_data(
            object_list=self.object_list,
            form=self.form,
            url_params=request.GET.urlencode(),
            conta=conta,
            agenda=agenda,
            data_ini=data_ini,
            data_fim=data_fim,
            menu_tarefas_agenda=menu_tarefas_agenda,
            total=total,
            get_=get_,
            entradas=int(total_pos),
            saidas=int(total_neg))

        return self.render_to_response(context)

agenda_tarefa_list = (login_required(AgendaTarefaFormListView.as_view(
                                model=Tarefa,
                                form_class=TarefaSearchForm,
                                paginate_by=15,
                                template_name='agenda/tarefa_list.html'
                                )
                            )
                        )

@login_required
def set_tarefa_status(request, tarefa_pk):
    '''
    ref #38 - ajax
    altera tarefa.pago
        para: True ou False
    '''
    tarefa = get_object_or_404(Tarefa, id=tarefa_pk)
    # if not conta.can_acess(request.user):
    #     raise Http404
    if tarefa.pago is True:
        tarefa.pago = False
    else:
        tarefa.pago = True
    tarefa.save()

    return HttpResponse('Ok')

@login_required
def cartao_form(request, conta_pk, pk=None):
    '''
    o cartao é o do dono da conta (um user)
    '''
    conta = get_object_or_404(Conta, id=conta_pk)
    if not conta.can_acess(request.user):
        raise Http404
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
    context['menu_administracao'] = "active"
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
    if not conta.can_acess(request.user):
        raise Http404
    object_list = CartaoCredito.objects.filter(usuario=conta.dono) # não tem relação: TODO vincular a conta e ou agenda
    form = CartaoCreditoBaseSearchForm(request.POST or None)
    context = {}
    context['conta'] = conta
    context['object_list'] = object_list
    context['form'] = form
    context['menu_administracao'] = "active"

    return render(
        request, 'agenda/cartaocredito_list.html', context)