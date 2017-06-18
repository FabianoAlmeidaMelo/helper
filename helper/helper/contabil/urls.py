# coding: utf-8
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    '',
    url(r'^contador/conta/(?P<conta_pk>\d+)/$',
	'helper.contabil.views.contador_leitura', name='contador_leitura'
    ),
)
