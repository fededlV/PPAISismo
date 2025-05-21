from django.shortcuts import render

# Create your views here.

def buscarventosSismicos(request):
    return render(request, 'buscarventosSismicos.html')