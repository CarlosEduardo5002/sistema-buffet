from django.db import models

class Categoria(models.Model):
    TIPO_COMPORTAMENTO = [
        ('consumivel', 'Consumível'),
        ('reutilizavel', 'Reutilizável'),
        ('descartavel', 'Descartável'),
        ('perecivel', 'Alimento Perecível'),
        ('equipamento', 'Equipamento'),
    ]
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome da Categoria")
    comportamento = models.CharField(max_length=30, choices=TIPO_COMPORTAMENTO, default='consumivel', verbose_name="Comportamento")

    def __str__(self):
        return f"{self.nome} ({self.get_comportamento_display()})"

class LocalArmazenamento(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Local (Ex: Geladeira, Depósito)")

    def __str__(self):
        return self.nome

class Produto(models.Model):
    UNIDADES_MEDIDA = [
        ('un', 'Unidade'),
        ('kg', 'Quilograma (kg)'),
        ('g', 'Grama (g)'),
        ('l', 'Litro (L)'),
        ('pct', 'Pacote'),
        ('cx', 'Caixa'),
    ]
    nome = models.CharField(max_length=150, verbose_name="Nome do Produto")
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código / Identificador")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name="Categoria")
    localizacao = models.ForeignKey(LocalArmazenamento, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Local")
    unidade_medida = models.CharField(max_length=10, choices=UNIDADES_MEDIDA, default='un', verbose_name="Unidade")
    quantidade_atual = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Qtd Atual")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    def __str__(self):
        return f"{self.codigo} - {self.nome}"