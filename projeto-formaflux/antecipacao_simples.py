"""Antecipacao usando desconto comercial simples."""

from decimal import Decimal

from antecipacao import Antecipacao
from parcela import Parcela


class AntecipacaoSimples(Antecipacao):
    def __init__(self, taxa_mensal: Decimal, tarifa_fixa: Decimal):
        super().__init__(taxa_mensal, tarifa_fixa)

    def calcular_valor_liquido(self, parcela: Parcela) -> Decimal:
        # Desconto simples: VP = valor nominal * (1 - taxa * prazo).
        valor_presente = parcela.valor_nominal * (
            1 - self._taxa_mensal * parcela.prazo_meses
        )
        return self._finalizar_calculo(valor_presente)
