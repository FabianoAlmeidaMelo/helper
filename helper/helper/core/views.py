# coding: utf-8

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from .models import (
    Developer,
)

from .forms import (
    DeveloperForm,
)


class SearchFormListView(FormMixin, ListView):

    '''
    example:
    class UserSearchView(SearchFormListView):
        # initial = {}
        # success_url = None
        # paginate_by = 20
        form_class = UserSearchForm
        model = User
    user_list = login_required(UserSearchView.as_view())
    '''

    def get_form_kwargs(self):
        return {'initial': self.get_initial(), 'data': self.request.GET}

    def get(self, request, *args, **kwargs):
        self.form = self.get_form(self.get_form_class())
        self.object_list = self.form.get_result_queryset()
        context = self.get_context_data(
            object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

# View home para usuário deslogado
home_anonymous = TemplateView.as_view(template_name='base.html')


def index(request):
    pass
    # return developer_list(request)


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
