from django.shortcuts import render
from django.http import HttpResponse
from .models import Superhero

# Create your views here.
def index(request):
    all_heros = Superhero.objects.all()
    context ={
        'all_heros': all_heros
    }
    return render(request, 'superheros/index.html', context)