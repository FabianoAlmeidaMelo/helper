# coding: utf-8
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from helper.core.models import Conta, User
from helper.core.forms import EnderecoForm

from helper.contabil.models import ContaMensagem, Mensagem, Setor

from helper.contabil.forms import (
    ClienteUserForm,
    ClienteUserSearchForm,
    ContadorForm,
    ContadorUserForm,
    ContadorUserSearchForm,
    MensagemForm,
    MensagensSearchForm,
    SetorForm,
    SetorListSearchForm,
)


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
    endereco = None
    if contador:
        endereco = contador.endereco
    if not contador.can_acess(request.user):
        raise Http404
    form = ContadorForm(request.POST or None, instance=contador, conta=conta)
    endereco_form = EnderecoForm(request.POST or None, instance=endereco)

    context = {}
    context['form'] = form
    context['endereco_form'] = endereco_form
    context['contador'] = contador
    context['conta'] = conta
    context['menu_administracao'] = "active"
 
    if request.method == 'POST':
        if form.is_valid() and endereco_form.is_valid():
            form.save()
            endereco_form.save()
            msg = u'cadastro alterado com sucesso.'
            messages.success(request, msg)
        else:
            msg = u'Falha na edição do cadastro: %s - %s' % (form.errors, endereco_form.errors)
            messages.warning(request, msg)
            return render(request, 'contabil/contador_form.html', context)
        return redirect(reverse('contador_read'))
    return render(request, 'contabil/contador_form.html', context)


@login_required
def contador_read(request):
    """
    acesso do contador
    """
    conta = request.user.conta
    contador = conta.contador
    if not contador.can_acess(request.user):
        raise Http404


    context = {}
    context['contador'] = contador
    context['conta'] = conta
    context['menu_administracao'] = "active"
    return render(request, 'contabil/contador_read.html', context)

@login_required
def setor_list(request):
    conta = request.user.conta
    contador = conta.contador
    if not contador.can_acess(request.user):
        raise Http404
    context = {}

    form = SetorListSearchForm(request.GET or None, contador=contador)
    object_list = form.get_queryset()

    # ### PAGINAÇÃO ####
    get_copy = request.GET.copy()
    context['parameters'] = get_copy.pop('page', True) and get_copy.urlencode()
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 15)
    try:
        setores = paginator.page(page)
    except PageNotAnInteger:
        setores = paginator.page(1)
    except EmptyPage:
        setores = paginator.page(paginator.num_pages)
    # ### paginação ####

    context['conta'] = conta
    context['object_list'] = setores
    context['form'] = form
    context['menu_administracao'] = "active"

    return render(request, 'contabil/setor_list.html', context)


@login_required
def setor_form(request, setor_pk=None):
    """
    acesso do contador
    """
    conta = request.user.conta
    contador = conta.contador
    setor = None
    if setor_pk:
        setor = get_object_or_404(Setor, pk=setor_pk)
    if not contador.can_acess(request.user):
        raise Http404
    form = SetorForm(request.POST or None, instance=setor, contador=contador)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg = u'Setor salvo com sucesso.'
            messages.success(request, msg)
        else:
            msg = u'Falha na edição do setor: %s ' % form.errors
            messages.warning(request, msg)
        return redirect(reverse('setor_list'))

    context = {}
    context['form'] = form
    context['contador'] = contador
    context['conta'] = conta
    context['menu_administracao'] = "active"
    return render(request, 'contabil/setor_form.html', context)


@login_required
def contador_users_list(request, conta_pk):
    """
    Lista os users DO contador
    tipo 1
    """
    conta = get_object_or_404(Conta, id=conta_pk)
    if not conta.can_acess(request.user):
        raise Http404
    context = {}

    form = ContadorUserSearchForm(request.GET or None, conta=conta)
    object_list = form.get_queryset()
    
    # ### PAGINAÇÃO ####
    get_copy = request.GET.copy()
    context['parameters'] = get_copy.pop('page', True) and get_copy.urlencode()
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 15)
    try:
        clientes_users = paginator.page(page)
    except PageNotAnInteger:
        clientes_users = paginator.page(1)
    except EmptyPage:
        clientes_users = paginator.page(paginator.num_pages)
    # ### paginação ####

    context['conta'] = conta
    context['object_list'] = clientes_users
    context['form'] = form
    context['menu_administracao'] = "active"

    return render(request, 'contabil/contador_user_list.html', context)


@login_required
def contador_user_form(request, user_pk=None):
    """
    acesso do contador
    cadastro e edição dos Users
    do Contador (funcionários e sócios)
    """
    user = request.user
    conta = user.conta
    contador = conta.contador
    if not contador.can_acess(user):
        raise Http404

    usuario_contador = None
    if user_pk:
        usuario_contador = get_object_or_404(User, pk=user_pk)
    form = ContadorUserForm(request.POST or None, instance=usuario_contador, conta=conta)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg = u'Usuário salvo com sucesso.'
            messages.success(request, msg)
        else:
            msg = u'Falha na edição do usuário: %s ' % form.errors
            messages.warning(request, msg)
        return redirect(reverse('contador_users_list', kwargs={'conta_pk': conta.pk}))

    context = {}
    context['form'] = form
    context['contador'] = contador
    context['conta'] = conta
    context['menu_administracao'] = "active"
    return render(request, 'contabil/usuario_contador_form.html', context)


@login_required
def cliente_list(request, conta_pk):
    """
    Lista usuários Clientes do Contador
    """
    conta = get_object_or_404(Conta, id=conta_pk)
    if not conta.can_acess(request.user):
        raise Http404

    context = {}
    form = ClienteUserSearchForm(request.GET or None, conta=conta)
    object_list = form.get_queryset()
    
    # ### PAGINAÇÃO ####
    get_copy = request.GET.copy()
    context['parameters'] = get_copy.pop('page', True) and get_copy.urlencode()
    paginator = Paginator(object_list, 15)
    page = request.GET.get('page', 1)
    try:
        clientes_users = paginator.page(page)
    except PageNotAnInteger:
        clientes_users = paginator.page(1)
    except EmptyPage:
        clientes_users = paginator.page(paginator.num_pages)
    # ### paginação ####

    context['conta'] = conta
    context['object_list'] = clientes_users
    context['form'] = form
    context['menu_clientes'] = "active"

    return render(request, 'contabil/cliente_list.html', context)



@login_required
def cliente_user_form(request, user_pk=None):
    """
    acesso do contador
    cadastro e edição dos Users Clientes
    do Contador 
    """
    user_contador = request.user
    conta_contador = user_contador.conta
    contador = conta_contador.contador
    if not contador.can_acess(user_contador):
        raise Http404

    usuario_cliente = None
    if user_pk:
        usuario_cliente = get_object_or_404(User, pk=user_pk)
    form = ClienteUserForm(request.POST or None, instance=usuario_cliente, contador=contador)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg = u'Usuário salvo com sucesso.'
            messages.success(request, msg)
        else:
            msg = u'Falha na edição do usuário: %s ' % form.errors
            messages.warning(request, msg)
        return redirect(reverse('cliente_list', kwargs={'conta_pk': conta_contador.pk}))

    context = {}
    context['form'] = form
    context['contador'] = contador
    if usuario_cliente:
        context['conta'] = usuario_cliente.conta
    context['menu_clientes'] = "active"
    context['tab_cliente_cadastro'] = "active"
    return render(request, 'contabil/usuario_cliente_form.html', context)


@login_required
def mensagens_list(request, conta_pk):
    """
    Lista as menmsagens enviadas e recebidas de um Contador
    para um cliente específico
    """
    conta = get_object_or_404(Conta, id=conta_pk)
    if not conta.can_acess(request.user):
        raise Http404
    context = {}

    form = MensagensSearchForm(request.GET or None, conta=conta)
    object_list = form.get_queryset()
    
    # ### PAGINAÇÃO ####
    get_copy = request.GET.copy()
    context['parameters'] = get_copy.pop('page', True) and get_copy.urlencode()
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 12)
    try:
        mensagens = paginator.page(page)
    except PageNotAnInteger:
        mensagens = paginator.page(1)
    except EmptyPage:
        mensagens = paginator.page(paginator.num_pages)
    # ### paginação ####

    context['conta'] = conta
    context['object_list'] = mensagens
    context['form'] = form
    context['menu_clientes'] = "active"  # usado no acesso do contador
    context['tab_mensagens'] = "active"

    return render(request, 'contabil/mensagens_list.html', context)


@login_required
def mensagem_form(request, conta_pk, mensagem_pk=None):
    """
    #51
    cadastro e edição de mensagem
    """
    conta_redirect = get_object_or_404(Conta, pk=conta_pk)
    contador = conta_redirect.contador
    user = request.user

    if user.conta.tipo == 1:
        conta = conta_redirect # conta do user 'Cliente'
        contador = conta.contador
        conta_mensagem_conta = user.conta
    else:
        conta_mensagem_conta = conta_redirect
        conta = user.conta.contador.conta_core.filter(tipo=1).first()  # conta do 'contador'

    can_edit = True
    mensagem = None
    if mensagem_pk:
        mensagem = get_object_or_404(Mensagem, pk=mensagem_pk)
        can_edit = mensagem.can_edit(user)
    form = MensagemForm(request.POST or None, request.FILES or None, instance=mensagem, conta=conta, user=user)

    if request.method == 'POST':
        if form.is_valid():
            mensagem = form.save()
            msg = u'Mensagem salva com sucesso.'
            messages.success(request, msg)
        else:
            msg = u'Falha na edição da mensagem: %s ' % form.errors
            messages.warning(request, msg)
        return redirect(reverse('mensagens_list', kwargs={'conta_pk': conta_redirect.pk}))

    elif request.method == 'GET' and not can_edit and mensagem and mensagem.user_add.conta != user.conta:
        conta_mensagem = ContaMensagem.objects.get(mensagem=mensagem, conta=conta_mensagem_conta) #, conta=conta_redirect.pk)
        # TODO: transformar em método do model
        if conta_mensagem.can_edit():
            conta_mensagem.data = timezone.now()
            conta_mensagem.user = user
            conta_mensagem.save()

    context = {}
    context['form'] = form
    context['can_edit'] = can_edit
    context['contador'] = contador
    context['conta'] = conta_redirect
    context['menu_clientes'] = "active"  # usado no acesso do contador
    context['tab_mensagens'] = "active"
    return render(request, 'contabil/mensagem_form.html', context)