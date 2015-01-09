from django.contrib import admin
from .models import Cita, Category, Assistant, Comments

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
	list_display = ('name','category','start','finish','organizer',)

admin.site.register(Category)
admin.site.register(Assistant)
admin.site.register(Comments)