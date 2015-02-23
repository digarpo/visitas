from django.conf.urls import patterns, url
from .views import EditUser, DetailUser

urlpatterns = patterns('',
            url(r'^login/$', 'apps.usuarios.views.userlogin', name="login"),
            url(r'^salir/$', 'apps.usuarios.views.LogOut', name="logout"),
             url(r'^usuario/editar/(?P<pk>\d+)/$', EditUser.as_view(), name = 'editar'),
              url(r'^usuario/informacion/(?P<pk>\d+)/$', DetailUser.as_view(), name = 'detalle')
)


