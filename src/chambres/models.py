from typing import Any

from django.db import models

class Chambre(models.Model):
    def __init__(self, id, nbrlit, mobilierdispo, prix, statut):
        self.id = id
        self.nbrlit = nbrlit
        self.mobilierdispo = mobilierdispo
        self.prix = prix
        self.statut = statut

# Create your models here.
