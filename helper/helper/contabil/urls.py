# coding: utf-8
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    '',
    url(r'^contador/conta/(?P<conta_pk>\d+)/$',	'helper.contabil.views.contador_leitura', name='contador_leitura'),
    url(r'^contador/cadastro/$', 'helper.contabil.views.contador_read', name='contador_read'),
    url(r'^contador/formulario/$', 'helper.contabil.views.contador_form', name='contador_form'),
    url(r'^contador/conta/(?P<conta_pk>\d+)/clientes/$', 'helper.contabil.views.cliente_list', name='cliente_list'),
)

#contador_read
