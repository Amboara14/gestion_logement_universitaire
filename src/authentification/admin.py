from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur

# Register your models here.
class UtilisateurAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informations complémentaires', {'fields': ('role', 'telephone')}),
    )
    list_display = ('username', 'email', 'role', 'is_staff')

admin.site.register(Utilisateur, UtilisateurAdmin)