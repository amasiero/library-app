from django.shortcuts import render, get_object_or_404
from .models import Livro

def index(request):
    dados = {
        'livros': Livro.objects.all()
    }
    return render(request, 'index.html', dados)


def livro(request, livro_id):
    livro = {
        'livro': get_object_or_404(Livro, pk=livro_id)
    }
    return render(request, 'livro.html', livro)
