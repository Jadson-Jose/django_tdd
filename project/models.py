from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    quantidade_estoque = models.PositiveIntegerField()
    fornecedor = models.CharField(max_length=255)  # Podemos criar uma relação com outro modelo se desejar
    data_validade = models.DateField(blank=True, null=True)
    unidade_medida = models.CharField(max_length=50, default='unidade')  # Ex.: unidade, kg, litro
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('ativo', 'Ativo'), ('inativo', 'Inativo'), ('esgotado', 'Esgotado')], default='ativo')

    def __str__(self):
        return self.nome

