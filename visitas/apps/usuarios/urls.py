from django.conf.urls import patterns, url, include
from .views import EditUser, DetailUser, EditCompanyDocs

urlpatterns = patterns('',
            url(r'^login/$', 'apps.usuarios.views.userlogin', name="login"),
            url(r'^registro/$', 'apps.usuarios.views.userregister', name="registro"),
            url(r'^salir/$', 'apps.usuarios.views.LogOut', name="logout"),
            url(r'^usuario/password/reset/$','django.contrib.auth.views.password_reset',
                {'post_reset_redirect' : '/usario/password/reset/done/'},name="password_reset"),
                (r'^usuario/password/reset/done/$',
                    'django.contrib.auth.views.password_reset_done'),
                (r'^usuario/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                    'django.contrib.auth.views.password_reset_confirm',
                    {'post_reset_redirect' : '/usuario/password/done/'}),
                (r'^usuario/password/done/$',
                    'django.contrib.auth.views.password_reset_complete'),
            url(r'^usuario/password_change/$',
                'django.contrib.auth.views.password_change',
                {'post_change_redirect' : '/usuario/password_change/done/'},
                name="password_change"),
                (r'^usuario/password_change/done/$',
                'django.contrib.auth.views.password_change_done'),
            url(r'^login/$', include('django.contrib.auth.urls')),
            url(r'^registro/recuperar_contrasena/$', include('django.contrib.auth.urls')),
            url(r'^salir/$', 'apps.usuarios.views.LogOut', name="logout"),

            url(r'^usuario/editar/(?P<pk>\d+)/$', EditUser.as_view(), name = 'editar'),
            url(r'^usuario/informacion/(?P<pk>\d+)/$', DetailUser.as_view(), name = 'detalle'),
         #   url(r'^usuario/editar/(?P<pk>\d+)/$', EditCompanyDocs.as_view(), name = 'editar_company')

)


