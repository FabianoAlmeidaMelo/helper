from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.views import logout, login
from helper.core.forms import AuthenticationForm
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'helper.core.views.home', name='home'),

    url(r'^core/', include('helper.core.urls')),
    url(r'^agenda/', include('helper.agenda.urls')),
    url(r'^contabil/', include('helper.contabil.urls')),

    # Logins
    url(r'^logout/$', logout, {"next_page": "/"}, name="logout"),
    url(r'^login/$',login,{'template_name': 'login.html',
                           'authentication_form': AuthenticationForm}, name="login"),

    # password Reset
    url(r'^user/password/reset/$', 'django.contrib.auth.views.password_reset',
        {'post_reset_redirect': '/user/password/reset/done/'},
        name="password_reset"),
    url(r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect': '/user/password/done/'}),
    url(r'^user/password/done/$',
        'django.contrib.auth.views.password_reset_complete'),
    url(r'^municipios_app/', include('municipios.urls')),
    url(r'^admin/', include(admin.site.urls)),)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
