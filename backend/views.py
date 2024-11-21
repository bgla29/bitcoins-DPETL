from django.shortcuts import render
from .models import Criptomonedas

#Se crea la vista la obtener todas las criptomonedas
def index(request):
    bitcoins = Criptomonedas.objects.all()
    return render(request, 'backend/bitcoin_list.html', {'bitcoins': bitcoins})