from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Utilisateur(AbstractUser):
    class Role(models.TextChoices):
        ETUDIANT = 'etudiant', 'Étudiant'
        ADMINISTRATEUR = 'administrateur', 'Administrateur'
        AGENT_TECHNIQUE = 'agent_technique', 'Agent Technique'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.ETUDIANT,
    )
    telephone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"