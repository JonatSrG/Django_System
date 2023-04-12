from django.db import models

from django.contrib.auth.models import User

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTiemField(auto_now_add=True)
    fm = models.DateTiemField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntergerField(blank=True,null=True)

    class Meta:
        abstract=True
