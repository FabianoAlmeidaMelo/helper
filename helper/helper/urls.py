from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name="base.html")),
    url(r'^core/', include('helper.core.urls')),
    url(r'^agenda/', include('helper.agenda.urls')),
)
