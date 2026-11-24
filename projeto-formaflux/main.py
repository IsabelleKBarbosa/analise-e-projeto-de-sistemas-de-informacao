"""FormaFlux: simulador de antecipacao de recebiveis para formaturas.

Interface via terminal (CLI), com dados ficticios mantidos apenas em memoria.
"""

from decimal import Decimal, InvalidOperation

from antecipacao_composta import AntecipacaoComposta
from antecipacao_simples import AntecipacaoSimples
from parcela import Parcela
from turma import Turma


def moeda(valor: Decimal) -> str:
    numero = f"{valor:,.2f}"
    return "R$ " + numero.replace(",", "X").replace(".", ",").replace("X", ".")


def ler_decimal(mensagem: str) -> Decimal:
    entrada = input(mensagem).strip().replace("R$", "").strip()
    if "," in entrada:
        entrada = entrada.replace(".", "").replace(",", ".")
    try:
        numero = Decimal(entrada)
        if not numero.is_finite():
            raise InvalidOperation
        return numero
    except InvalidOperation:
        raise ValueError("Digite um numero valido (ex.: 1000,00).") from None


def ler_inteiro(mensagem: str) -> int:
    try:
        return int(input(mensagem).strip())
    except ValueError:
        raise ValueError("Digite um numero inteiro valido.") from None


def exigir_turma(turma: Turma | None) -> Turma:
    if turma is None:
        raise ValueError("Cadastre a turma primeiro (opcao 1).")
    return turma


def escolher_parcela(turma: Turma) -> Parcela:
    if not turma.listar_parcelas():
        raise ValueError("Cadastre uma parcela primeiro (opcao 2).")
    codigo = input("Identificador da parcela: ")
    parcela = turma.buscar_parcela(codigo)
    if parcela is None:
        raise ValueError("Parcela nao encontrada.")
    return parcela


def ler_parametros() -> tuple[Decimal, Decimal]:
    taxa_percentual = ler_decimal("Taxa mensal (%): ")
    tarifa = ler_decimal("Tarifa fixa (R$): ")
    # Taxa digitada como 2 representa 2% ao mes.
    taxa_decimal = taxa_percentual / 100
    if not (Decimal("0") <= taxa_decimal < Decimal("1")):
        raise ValueError("A taxa deve estar entre 0% e menos de 100%.")
    if tarifa < 0:
        raise ValueError("A tarifa nao pode ser negativa.")
    return taxa_decimal, tarifa


def exibir_resultado(nome: str, parcela: Parcela, valor_liquido: Decimal) -> None:
    custo_total = parcela.valor_nominal - valor_liquido
    print(f"\n{nome}")
    print(f"  Valor nominal: {moeda(parcela.valor_nominal)}")
    print(f"  Valor liquido: {moeda(valor_liquido)}")
    print(f"  Custo total:   {moeda(custo_total)}")


def comparar_modalidades(parcela: Parcela, taxa: Decimal, tarifa: Decimal) -> None:
    """CSU05: pode ser acessado pelo menu ou apos uma simulacao."""
    print("\n=== COMPARACAO DAS MODALIDADES ===")
    modalidades = [
        ("Desconto comercial simples", AntecipacaoSimples(taxa, tarifa)),
        ("Valor presente composto", AntecipacaoComposta(taxa, tarifa)),
    ]
    for nome, modalidade in modalidades:
        try:
            valor = modalidade.calcular_valor_liquido(parcela)
            exibir_resultado(nome, parcela, valor)
        except ValueError as erro:
            print(f"\n{nome}: nao foi possivel calcular. Motivo: {erro}")


def mostrar_menu() -> None:
    print("\n=== FORMAFLUX ===")
    print("1 - Cadastrar turma")
    print("2 - Cadastrar parcela")
    print("3 - Consultar parcelas")
    print("4 - Simular antecipacao")
    print("5 - Comparar modalidades")
    print("0 - Sair")


def executar() -> None:
    turma: Turma | None = None
    while True:
        mostrar_menu()
        opcao = input("Escolha: ").strip()
        if opcao == "0":
            print("Encerrando o FormaFlux. Cadastros nao sao salvos.")
            break
        try:
            if opcao == "1":
                if turma is not None:
                    confirmar = input("Substituir turma e perder parcelas atuais? (s/n): ")
                    if confirmar.strip().lower() != "s":
                        continue
                nome = input("Nome da turma: ")
                ano = ler_inteiro("Ano da formatura: ")
                turma = Turma(nome, ano)
                print("Turma cadastrada com sucesso.")

            elif opcao == "2":
                turma_atual = exigir_turma(turma)
                identificador = input("Identificador (ex.: P01): ")
                valor = ler_decimal("Valor nominal (R$): ")
                meses = ler_inteiro("Prazo em meses: ")
                turma_atual.adicionar_parcela(Parcela(identificador, valor, meses))
                print("Parcela cadastrada com sucesso.")

            elif opcao == "3":
                turma_atual = exigir_turma(turma)
                parcelas = turma_atual.listar_parcelas()
                if not parcelas:
                    print("Nenhuma parcela cadastrada.")
                else:
                    print(f"\nTurma: {turma_atual.nome} ({turma_atual.ano})")
                    for parcela in parcelas:
                        print(f"{parcela.id_parcela} | {moeda(parcela.valor_nominal)} | "
                              f"prazo: {parcela.prazo_meses} mes(es)")

            elif opcao == "4":
                parcela = escolher_parcela(exigir_turma(turma))
                taxa, tarifa = ler_parametros()
                print("\n1 - Desconto comercial simples")
                print("2 - Valor presente composto")
                escolha = input("Modalidade: ").strip()
                if escolha == "1":
                    modelo = AntecipacaoSimples(taxa, tarifa)
                    nome = "Desconto comercial simples"
                elif escolha == "2":
                    modelo = AntecipacaoComposta(taxa, tarifa)
                    nome = "Valor presente composto"
                else:
                    raise ValueError("Modalidade inexistente.")
                valor = modelo.calcular_valor_liquido(parcela)
                exibir_resultado(nome, parcela, valor)
                # CSU05 pode estender CSU04 se o usuario quiser comparar.
                comparar = input("Deseja comparar as duas modalidades? (s/n): ")
                if comparar.strip().lower() == "s":
                    comparar_modalidades(parcela, taxa, tarifa)

            elif opcao == "5":
                parcela = escolher_parcela(exigir_turma(turma))
                taxa, tarifa = ler_parametros()
                comparar_modalidades(parcela, taxa, tarifa)

            else:
                print("Opcao desconhecida. Tente novamente.")
        except ValueError as erro:
            print(f"Atencao: {erro}")


if __name__ == "__main__":
    try:
        executar()
    except (KeyboardInterrupt, EOFError):
        print("\nExecucao encerrada.")
