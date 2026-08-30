from django.shortcuts import render

def etudiant_view(request):
    return render(request, "etudiant/etudiant.html")
