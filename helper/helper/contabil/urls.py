# coding: utf-8
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    '',
    url(r'^contador/conta/(?P<conta_pk>\d+)/$',	'helper.contabil.views.contador_leitura', name='contador_leitura'),
    url(r'^contador/cadastro/$', 'helper.contabil.views.contador_read', name='contador_read'),
    url(r'^contador/formulario/$', 'helper.contabil.views.contador_form', name='contador_form'),
    url(r'^contador/setores/$', 'helper.contabil.views.setor_list', name='setor_list'),
    url(r'^contador/setor/novo/$', 'helper.contabil.views.setor_form', name='setor_form'),
    url(r'^contador/setor/(?P<setor_pk>\d+)/$', 'helper.contabil.views.setor_form', name='setor_edit'),
    url(r'^contador/conta/(?P<conta_pk>\d+)/usuarios/$', 'helper.contabil.views.contador_users_list', name='contador_users_list'),
    url(r'^contador/conta/(?P<conta_pk>\d+)/clientes/$', 'helper.contabil.views.cliente_list', name='cliente_list'),
)

