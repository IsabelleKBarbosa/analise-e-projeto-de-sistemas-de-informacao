"""Testes simples do prototipo para ajudar a dupla na homologacao."""

import unittest
from decimal import Decimal

from turma import Turma
from parcela import Parcela
from antecipacao import Antecipacao
from antecipacao_simples import AntecipacaoSimples
from antecipacao_composta import AntecipacaoComposta


class TestesFormaFlux(unittest.TestCase):
    def setUp(self):
        self.turma = Turma("BSI 2026", 2026)
        self.parcela = Parcela("P01", Decimal("1000"), 3)
        self.turma.adicionar_parcela(self.parcela)

    def test_valores_documento(self):
        simples = AntecipacaoSimples(Decimal("0.02"), Decimal("10"))
        composta = AntecipacaoComposta(Decimal("0.02"), Decimal("10"))
        self.assertEqual(simples.calcular_valor_liquido(self.parcela), Decimal("930.00"))
        self.assertEqual(composta.calcular_valor_liquido(self.parcela), Decimal("932.32"))

    def test_heranca_e_polimorfismo(self):
        modelos: list[Antecipacao] = [
            AntecipacaoSimples(Decimal("0.02"), Decimal("10")),
            AntecipacaoComposta(Decimal("0.02"), Decimal("10")),
        ]
        resultados = [modelo.calcular_valor_liquido(self.parcela) for modelo in modelos]
        self.assertNotEqual(resultados[0], resultados[1])

    def test_parcela_duplicada(self):
        with self.assertRaises(ValueError):
            self.turma.adicionar_parcela(Parcela("p01", Decimal("200"), 1))

    def test_id_imutavel(self):
        with self.assertRaises(AttributeError):
            self.parcela.id_parcela = "OUTRO"

    def test_setters_impedem_valores_invalidos(self):
        with self.assertRaises(ValueError):
            self.parcela.valor_nominal = Decimal("-50")
        with self.assertRaises(ValueError):
            self.parcela.prazo_meses = 0
        self.assertEqual(self.parcela.valor_nominal, Decimal("1000"))

    def test_sem_parcela(self):
        self.assertIsNone(self.turma.buscar_parcela("P02"))

    def test_antecipacao_inviavel(self):
        simples = AntecipacaoSimples(Decimal("0.4"), Decimal("0"))
        with self.assertRaises(ValueError):
            simples.calcular_valor_liquido(self.parcela)

    def test_nao_instanciar_classe_abstrata(self):
        with self.assertRaises(TypeError):
            Antecipacao(Decimal("0.02"), Decimal("10"))


if __name__ == "__main__":
    unittest.main()
