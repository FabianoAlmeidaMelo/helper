from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    '',
    url(r'^tarefa_list/$', 'helper.agenda.views.tarefa_list', name='tarefa_list'),
    url(r'^tarefa_form/$', 'helper.agenda.views.tarefa_form', name='tarefa_add'),
    url(r'^tarefa_form/(?P<pk>\d+)/$', 'helper.agenda.views.tarefa_form', name='tarefa_edit'),
)
