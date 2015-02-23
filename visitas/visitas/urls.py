
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'citas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.citas.urls', namespace="citas_app")),
    url(r'^', include('apps.usuarios.urls', namespace="usuarios_app")),
     #url(r'^calendario/', include('django_bootstrap_calendar.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns("",
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,}
        ),
    )