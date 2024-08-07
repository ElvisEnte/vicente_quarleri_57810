from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    altura = models.IntegerField()
    timbre = models.CharField(max_length=50, default='Sin timbre')
    barrio = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50, default='Sin nombre')
    telefono = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.calle} {self.altura}"
    
    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"
    
class Favorito(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=250)
    anio = models.IntegerField()
    genero = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.titulo}"
    
class LibroCatalogo(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    anio = models.IntegerField()
    genero = models.CharField(max_length=100)
    portada = models.ImageField(upload_to='portadas/',null=True, blank=True)
    
    def __str__(self):
        return f"{self.titulo}"
    
    class Meta:
        ordering = ["titulo", "autor"]

class LibroUsuario(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    anio = models.IntegerField()
    genero = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.titulo}"
    
    class Meta:
        ordering = ["titulo", "autor"]

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} {self.imagen}'
