from django.conf.urls import patterns, url
from .views import IndexView, MainPanelView, CreateCita, DetailCita, EditCita, DeleteCita, CalendarView,CordinateView


urlpatterns = patterns('',

  # url(r'^$', 'apps.citas.views.index', name='index'),



   url(r'^calendario/$',CalendarView.as_view(), name = 'calendario'),
   url(r'^coordinacion/$',CordinateView.as_view(), name = 'coordinacion'),

url(r'^empresas/editar/(?P<pk>\d+)$', EditCita.as_view(), name='editar_usuario'),
  #
  #   url(r'^panel/$', 'apps.citas.views.main_panel', name='panel'),
  #   url(r'^panel/cita/nuevo/$', 'apps.citas.views.crear_cita', name='nuevo'),
  #   url(r'^panel/citas/(?P<cita_id>\d+)/$', 'apps.citas.views.detalle_cita', name='detalle'),
  #   url(r'^panel/citas/editar/(?P<pk>\d+)$', 'apps.citas.views.editar_cita', name='editar'),
  #   url(r'^panel/citas/eliminar/(?P<cita_id>\d+)$', 'apps.citas.views.eliminar_cita', name='eliminar'),

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^panel/$', MainPanelView.as_view(), name='panel'),
    url(r'^panel/cita/nuevo/$', CreateCita.as_view(), name='nuevo'),
    url(r'^panel/citas/(?P<pk>\d+)/$', DetailCita.as_view(), name='detalle'),
    url(r'^panel/citas/editar/(?P<pk>\d+)$', EditCita.as_view(), name='editar'),
    url(r'^panel/citas/eliminar/(?P<pk>\d+)$', DeleteCita.as_view(), name='eliminar'),
)
