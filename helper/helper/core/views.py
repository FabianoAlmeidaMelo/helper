# coding: utf-8

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import (
    Developer,
)

from .forms import (
    DeveloperForm,
)


def index(request):
    return developer_list(request)


def developer_list(request):
    object_list = Developer.objects.all()

    return render(
        request, 'core/developer_list.html',
        {
            'object_list': object_list,
        }
    )


def developer_form(request, developer_pk=None):
    developer = get_object_or_404(Developer, pk=developer_pk) if developer_pk else None
    developer_form = DeveloperForm(request.POST or None, instance=developer)

    if request.method == 'POST':
        if developer_form.is_valid():
            developer_form.save()
            messages.success(request, u'Developer atualizado com sucesso')
            return redirect(reverse('developer_list'))
        else:
            messages.error(request, u'Falha ao salvar Developer')

    return render(
        request, 'core/developer_form.html',
        {
            'developer_form': developer_form,
        }
    )
