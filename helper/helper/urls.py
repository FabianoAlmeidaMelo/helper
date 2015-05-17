from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    '',
    url(r'^$', 'helper.core.views.index', name='index'),
    url(r'^core/', include('helper.core.urls')),
)
