from django.db import models

# Create your models here.

class cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField(blank=True,null=True)
    pontuacao= models.IntegerField(blank=True,null=True)
    habilicado= models.BooleanField(blank=True,null=True)
    observacao= models.TextField(blank=True,null=True)
    
    def __str__(self) -> str:
        return self.nome