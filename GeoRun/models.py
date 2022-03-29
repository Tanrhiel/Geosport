from django.db import models

# Create your models here.

class Runner(models.Model):
    pseudo = models.CharField(max_length=50,unique=True)
    mail = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)

class Defi(models.Model):
    nom = models.CharField(max_length=254)
    createur = models.ForeignKey(Runner, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_debut = models.DateTimeField()
    type = models.CharField(max_length=50)
    duree = models.IntegerField()
    description = models.TextField(max_length=50)

class Participation(models.Model):
    participant=models.ForeignKey(Runner, on_delete=models.CASCADE)
    defi=models.ForeignKey(Defi, on_delete=models.CASCADE)
    score=models.FloatField(default=0.0)

    class Meta:
        unique_together = ('participant', 'defi',)
