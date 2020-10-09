from django.contrib import admin
from .models import Livro


class ExibeLivro(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'ano_publicacao', 'isbn')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_filter = ('ano_publicacao',)
    list_per_page = 2


admin.site.register(Livro, ExibeLivro)
