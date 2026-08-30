from django.contrib import admin
from django.urls import path
from src.authentification.views import login_view, register_view
from src.etudiants.views import etudiant_view
from src.admin.views import admin_view
from src.agent_technique.views import agent_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('etudiant/', etudiant_view, name='etudiant'),
    path('espace-admin/', admin_view, name='espace_admin'),
    path('agent-technique/', agent_view, name='agent_technique'),
]