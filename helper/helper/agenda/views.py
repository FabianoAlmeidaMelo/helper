# coding: utf-8
from django.db.models import Q, Sum
from datetime import date

from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView  #, ListView # DeleteView
from django.core.urlresolvers import reverse
from django.contrib import messages
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.contenttypes.models import ContentType

from django.shortcuts import get_object_or_404, redirect, render

from .models import (
    Agenda,
    CartaoCredito,
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


def agenda_form(request, pk=None):
    '''
        #12
    '''
    if pk:
        agenda = get_object_or_404(Agenda, pk=pk)
        msg = u'agenda alterada com sucesso.'
    else:
        agenda = None
        msg = u'agenda criada.'

    form = AgendaForm(request.POST or None, instance=agenda, user=request.user)

    if request.method == 'POST':
        if form.is_valid():
            agenda = form.save()
            messages.success(request, msg)

            return redirect(reverse('agenda_list'))
        else:
            messages.warning(request, u'Falha no cadastro de agenda')

    return render(
        request,
        'agenda/agenda_form.html',
        {
            'form': form,
        }
    )


def agenda_list(request):
    object_list = Agenda.objects.all()
    # object_list = AgendaSearchForm(request.POST or None)

    return render(
        request, 'agenda/agenda_list.html', {
                                            'object_list': object_list,
                                            # 'form': form,
                                            }
    )


def servico_form(request, pk=None):
    '''
        #12
    '''
    if pk:
        servico = get_object_or_404(Servico, pk=pk)
        msg = u'servico alterado com sucesso.'
    else:
        servico = None
        msg = u'servico criado.'

    form = ServicoForm(request.POST or None, instance=servico)

    if request.method == 'POST':
        if form.is_valid():
            servico = form.save()
            messages.success(request, msg)

            return redirect(reverse('servico_list'))
        else:
            messages.warning(request, u'Falha no cadastro de serviço')

    return render(
        request,
        'agenda/servico_form.html',
        {
            'form': form,
        }
    )


def servico_list(request):
    object_list = Servico.objects.all()
    # form = ServicoSearchForm(request.POST or None)

    return render(
        request, 'agenda/servico_list.html', {
                                            'object_list': object_list,
                                            # 'form': form,
                                            }
    )


def tarefa_form(request, pk=None):
    '''
        #12
    '''
    if pk:
        tarefa = get_object_or_404(Tarefa, pk=pk)
        msg = u'Tarefa alterada com sucesso.'
    else:
        tarefa = None
        msg = u'Tarefa criada.'

    form = TarefaForm(request.POST or None, instance=tarefa, )

    if request.method == 'POST':
        if form.is_valid():
            tarefa = form.save()
            messages.success(request, msg)

            return redirect(reverse('tarefa_list'))
        else:
            messages.warning(request, u'Falha no cadastro de tarefa de Coleta')

    return render(
        request,
        'agenda/tarefa_form.html',
        {
            'form': form,
        }
    )


# class TarefaFormListView(SearchFormListView):
#     '''
#     ref #19
#     datas anteriores a data corrente,
#         devem encabeçar a listagem, quando:
#         Tiverem valor e não estiverem marcadas como PAGO
#     '''
#     def get(self, request, *args, **kwargs):
#         self.form = self.get_form(self.get_form_class())
#         if self.form.is_valid():
#             self.object_list = self.form.get_result_queryset()
#         else:
#             self.object_list = []

#         context = self.get_context_data(
#             object_list=self.object_list,
#             form=self.form,
#             url_params=request.GET.urlencode(),
#         )

#         return self.render_to_response(context)

tarefa_list = (
    SearchFormListView.as_view(
                                model=Tarefa,
                                form_class=TarefaSearchForm,
                                paginate_by=30
                                )
                            )


# class CartaoCreditoCreate(CreateView):
#     '''Funciona só para Novo '''

#     form_class = CartaoCreditoForm
#     template_name = 'agenda/cartaocredito_form.html'

#     def get_success_url(self):
#         return reverse_lazy('carato_list')


# cartao_form = CartaoCreditoCreate.as_view()


def cartao_form(request, pk=None):
    if pk:
        cartao = get_object_or_404(CartaoCredito, pk=pk)
        msg = u'Cartao de Crédito alterado com sucesso.'
    else:
        cartao = None
        msg = u'Cartao de Crédito criado.'

    form = CartaoCreditoForm(request.POST or None, instance=cartao)

    if request.method == 'POST':
        if form.is_valid():
            cartao = form.save()
            messages.success(request, msg)

            return redirect(reverse('cartao_list'))
        else:
            messages.warning(request, u'Falha no cadastro de Cartao Credito')

    return render(
        request,
        'agenda/cartaocredito_form.html',
        {
            'form': form,
        }
    )


cartao_list = (
    SearchFormListView.as_view(
                                model=CartaoCredito,
                                form_class=CartaoCreditoBaseSearchForm,
                                paginate_by=30
                                )
                            )
