from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    # url(r'^$', 'helper.core.views.home', name='home'),
    # url(r'^developer_list/$', 'helper.core.views.developer_list', name='developer_list'),
    # url(r'^developer_form/$', 'helper.core.views.developer_form', name='developer_add'),
    # url(r'^developer_form/(?P<developer_pk>\d+)/$', 'helper.core.views.developer_form', name='developer_edit'),
)
