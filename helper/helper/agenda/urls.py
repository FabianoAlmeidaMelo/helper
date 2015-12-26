from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    '',
    url(
        r'^agenda_list/$',
        'helper.agenda.views.agenda_list', name='agenda_list'
        ),
    url(
        r'^agenda_form/$',
        'helper.agenda.views.agenda_form', name='agenda_add'
        ),
    url(
        r'^agenda_form/(?P<pk>\d+)/$',
        'helper.agenda.views.agenda_form', name='agenda_edit'
        ),
    url(
        r'^tarefa_list/$',
        'helper.agenda.views.tarefa_list', name='tarefa_list'
        ),
    url(
        r'^tarefa_form/$',
        'helper.agenda.views.tarefa_form', name='tarefa_add'
        ),
    url(
        r'^tarefa_form/(?P<pk>\d+)/$',
        'helper.agenda.views.tarefa_form', name='tarefa_edit'
        ),
)
