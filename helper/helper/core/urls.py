from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    # url(r'^$', TemplateView.as_view(template_name="home.html")),
    # url(r'^$', 'helper.core.views.home', name='home'),
)
