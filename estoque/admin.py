from django.contrib import admin
from .models import Categoria, LocalArmazenamento, Produto

admin.site.register(Categoria)
admin.site.register(LocalArmazenamento)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'categoria', 'quantidade_atual', 'unidade_medida', 'ativo')
    search_fields = ('nome', 'codigo')