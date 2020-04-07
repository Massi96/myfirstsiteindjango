from django.shortcuts import render

# Create your views here. Descrive quali dati vediamo

def contatti(request):
    return render(request,"contatti.html")
