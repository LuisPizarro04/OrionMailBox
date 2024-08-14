from django.contrib import admin
from .models import Faena, Solicitud, Documento, SolicitudDocumento


class FaenaAdmin(admin.ModelAdmin):
    list_display = ('id_faena', 'nombre_faena')
    search_fields = ('nombre_faena',)
    ordering = ('id_faena',)


class DocumentoInline(admin.TabularInline):
    model = SolicitudDocumento
    extra = 1


class SolicitudAdmin(admin.ModelAdmin):
    list_display = (
        'id_solicitud', 'nombre_solicitante', 'apellido_solicitante', 'rut_solicitante', 'faena', 'fecha_solicitud',
        'estado_solicitud')
    list_filter = ('estado_solicitud', 'fecha_solicitud', 'faena')
    search_fields = ('nombre_solicitante', 'apellido_solicitante', 'rut_solicitante')
    ordering = ('-fecha_solicitud',)
    inlines = [DocumentoInline]


class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id_documento', 'archivo')
    search_fields = ('id_documento',)
    ordering = ('id_documento',)


class SolicitudDocumentoAdmin(admin.ModelAdmin):
    list_display = ('id_solicitud_documento', 'solicitud', 'documento')
    search_fields = ('solicitud__nombre_solicitante', 'documento__id_documento')
    ordering = ('id_solicitud_documento',)


admin.site.register(Faena, FaenaAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(SolicitudDocumento, SolicitudDocumentoAdmin)
