from django.db import models
from django.apps import apps

class DatosGlobales(models.Model):
    id = models.AutoField(primary_key=True)
    variable =  models.CharField(max_length=100)
    anio =  models.IntegerField()
    valor =  models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"Variable:{self.variable}, Año:{self.anio}, Valor:{self.valor}"