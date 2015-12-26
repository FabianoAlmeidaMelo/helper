# coding: utf-8

# from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib import messages
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect, render

from .models import (
    Agenda,
    Tarefa,
    )
from helper.core.views import SearchFormListView
from .forms import (
    AgendaForm,
    TarefaForm,
    TarefaSearchForm,
    )


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

    form = AgendaForm(request.POST or None, instance=agenda)

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
    # form = AgendaSearchForm(request.POST or None)

    return render(
        request, 'agenda/agenda_list.html', {
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

    form = TarefaForm(request.POST or None, instance=tarefa)

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


# tarefa_list = (
#     SearchFormListView.as_view(
#                                 model=Tarefa,
#                                 form_class=TarefaSearchForm,
#                                 paginate_by=15
#                                 )
#                             )


def tarefa_list(request):
    object_list = Tarefa.objects.all()
    form = TarefaSearchForm(request.POST or None)

    return render(
        request, 'agenda/tarefa_list.html', {
                                            'object_list': object_list,
                                            'form': form,
                                            }
    )
