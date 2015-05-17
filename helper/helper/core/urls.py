from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    '',
    url(r'^developer_list/$', 'helper.core.views.developer_list', name='developer_list'),
    url(r'^developer_form/$', 'helper.core.views.developer_form', name='developer_add'),
    url(r'^developer_form/(?P<developer_pk>\d+)/$', 'helper.core.views.developer_form', name='developer_edit'),
)
