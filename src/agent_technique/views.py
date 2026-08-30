from django.shortcuts import render

def agent_view(request):
    return render(request, "agent_technique/agent_tech.html")
