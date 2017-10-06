# coding: utf-8

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from helper.agenda.models import (
    Conta,
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
home_anonymous = TemplateView.as_view(template_name='home.html')

# class HomeView(TemplateView):
#     template_name = 'base.html'

#     def get_context_data(self, **kwargs):
#         context = {}
#         if request.user.is_authenticated:
#             context = super(HomeView, self).get_context_data(**kwargs)
#             context['conta'] = Conta.objects.filter(dono=request.user)
#         return context

def home(request):
    user = request.user
    conta = None
    context = {}
    if user.is_authenticated() and user.conta_set.count():
        conta = get_object_or_404(Conta, dono=request.user)
    context['conta'] = conta
    context['menu_home'] = "active"
    return render(request, 'home.html', context)