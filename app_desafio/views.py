from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from app_desafio.models import Familiar

# Create your views here.

def listar_familiares(request):
    context = {}
    context["familiares"] = Familiar.objects.all()
    return render(request, "app_desafio/familia.html", context)
