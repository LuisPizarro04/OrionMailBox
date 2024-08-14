from django.db import models
from django.core.validators import FileExtensionValidator

# Define your choices here
pendiente = 'Pendiente'
enproceso = 'En Proceso'
cerrado = 'Cerrado'
rechazado = 'Rechazado'

ESTADOS_CHOICES = [
    (pendiente, 'Pendiente'),
    (enproceso, 'En Proceso'),
    (cerrado, 'Cerrado'),
    (rechazado, 'Rechazado')
]


class Faena(models.Model):
    id_faena = models.AutoField(primary_key=True)
    nombre_faena = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_faena

    class Meta:
        db_table = 'faena'


class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    nombre_solicitante = models.CharField(max_length=50)
    apellido_solicitante = models.CharField(max_length=50)
    rut_solicitante = models.CharField(max_length=50)
    faena = models.ForeignKey(Faena, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now=True)
    estado_solicitud = models.CharField(choices=ESTADOS_CHOICES, default=pendiente, max_length=50)

    def __str__(self):
        return f'{self.nombre_solicitante} {self.apellido_solicitante} - {self.estado_solicitud}'

    class Meta:
        db_table = 'solicitud'


def user_directory_path(instance, filename):
    # Archivos se subirán a MEDIA_ROOT/archivos/documento_<id>/<filename>
    return f'archivos/documento_{instance.id_documento}/{filename}'


class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    archivo = models.FileField(
        upload_to=user_directory_path,
        max_length=255,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])],
        blank=True,
        null=True,
        verbose_name='User File',
        help_text='Upload a PDF or DOC/DOCX file.',
    )

    def __str__(self):
        return f'Documento {self.id_documento}'

    class Meta:
        db_table = 'documento'


class SolicitudDocumento(models.Model):
    id_solicitud_documento = models.AutoField(primary_key=True)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)

    def __str__(self):
        return f'Solicitud {self.solicitud.id_solicitud} - Documento {self.documento.id_documento}'

    class Meta:
        db_table = 'solicituddocumento'
