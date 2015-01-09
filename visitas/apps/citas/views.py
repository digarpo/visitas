from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from .models import Cita, Category
from apps.usuarios.models import User
from .forms import CitaForm

from django.core.urlresolvers import reverse, reverse_lazy

# def index(request):
#     events = Event.objects.all().order_by('-created')[:6]
#     categories = Category.objects.all()
#     return render(request, 'events/index.html', {'events' : events, 'categories':categories})
class IndexView(TemplateView):

    template_name = 'citas/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['citas'] = Cita.objects.all().order_by('-created')[:6]
        context['categories'] = Category.objects.all()
        return context

# def main_panel(request):
#     #organizer = request.user.username
#     events = Event.objects.filter(organizer__username='victorvillazon').order_by('is_free', '-created')
#     cantidad_eventos = events.count()
#     return render(request, 'events/panel/panel.html', {'events' : events, 'cantidad': cantidad_eventos})
class MainPanelView(TemplateView):

    template_name = 'citas/panel/panel.html'

    def get_context_data(self, **kwargs):
        context = super(MainPanelView, self).get_context_data(**kwargs)
        context['citas'] = Cita.objects.filter(organizer = self.request.user).order_by( '-created')
        context['cantidad'] = context['citas'].count()
        return context


# def detalle_evento(request, evento_id):
#     event = get_object_or_404(Event, pk=evento_id)
#     return render(request, 'events/panel/detalle_evento.html', {'event': event})

class DetailCita(DetailView):

    template_name = 'citas/panel/detalle_cita.html'
    model = Cita


# def crear_evento(request):
#     if request.method == "POST":
#         modelform = EventoForm(request.POST, request.FILES)
#         if modelform.is_valid():
#             organizador = User.objects.get(pk=3)
#             nuevo_evento = modelform.save()
#             nuevo_evento.organizer = organizador
#             nuevo_evento.save()
#             return redirect(reverse('events_app:panel'))
#     else:
#         modelform = EventoForm()

#     return render(request, "events/panel/crear_evento.html", {"form": modelform})

class CreateCita(CreateView):

    form_class = CitaForm
    template_name = 'citas/panel/crear_cita.html'
    success_url = reverse_lazy('citas_app:panel')

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super(CreateCita, self).form_valid(form)


# def editar_evento(request, evento_id):
#     event = get_object_or_404(Event, pk=evento_id)

#     if request.method == "POST":
#         modelform = EventoForm(request.POST, request.FILES, instance=event)
#         if modelform.is_valid():
#             modelform.save()
#             return redirect(reverse('events_app:panel'))
#     else:
#         modelform = EventoForm(instance=event)

#     return render(request, "events/panel/editar_evento.html", {"form": modelform, 'event': event})

class EditCita(UpdateView):

    template_name = 'citas/panel/editar_cita.html'
    success_url = reverse_lazy('citas_app:panel')
    model = Cita
    form_class = CitaForm

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super(EditCita, self).form_valid(form)


class DeleteCita(DeleteView):
    template_name = 'citas/panel/eliminar_cita.html'
    model = Cita
    success_url = reverse_lazy('citas_app:panel')
    #toma la cita a eliminar
    context_object_name = 'cita'


# def eliminar_evento(request, evento_id):
#     event = get_object_or_404(Event, pk=evento_id)

#     if request.method == "POST":
#         event.delete()
#         return redirect(reverse('events_app:panel'))

#     return render(request, "events/panel/eliminar_evento.html", {'event': event})


class CalendarView(TemplateView):

    template_name = 'citas/calendario/calendario.html'


class CordinateView(TemplateView):

    template_name='citas/coordinacion/coordinacion.html'


