from django.contrib import admin
from .models import Docs, DocUser

@admin.register(Docs)
class DocsAdmin(admin.ModelAdmin):
	list_display = ('name','validate',)

@admin.register(DocUser)
class DocUserAdmin(admin.ModelAdmin):
    list_display = ('doc','type_doc','read',)