from decimal import Decimal
from django.test import TestCase
from .models import Produto

class ProdutoModelTest(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(
            nome="Produto de Teste",
            preco=Decimal('49.99'),
            descricao="Descrição do produto de teste",
            categoria="Categoria de Teste",
            sku="TESTE123",
            quantidade_estoque=100,
            fornecedor="Fornecedor Teste",
            unidade_medida="unidade",
            status="ativo"
        )

    def test_criacao_produto(self):
        produto = Produto.objects.get(sku="TESTE123")
        self.assertEqual(produto.nome, "Produto de Teste")
        self.assertEqual(produto.preco, Decimal('49.99'))
        self.assertEqual(produto.quantidade_estoque, 100)

    def test_str_method(self):
        produto = Produto.objects.get(sku="TESTE123")
        self.assertEqual(str(produto), "Produto de Teste")

