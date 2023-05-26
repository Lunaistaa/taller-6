from django.db import models

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=500)

    class Meta:
        app_label = 'nombre_de_la_app'

class Ciudad(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=500)

    class Meta:
        app_label = 'nombre_de_la_app'

class Persona(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    tipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    documento = models.CharField(max_length=255)
    lugarresidencia = models.CharField(max_length=255)
    fechanacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        app_label = 'nombre_de_la_app'