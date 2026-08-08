from typing import Any

from django.db import models

class Etudiant(models.Model):
    def __init__(self, numero, nom, prenom, niveau):
        self.numero = numero
        self.nom = nom
        self.prenom = prenom
        self.niveau = niveau
        self.save()




# Create your models here.
