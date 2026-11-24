# FormaFlux

**Simulador de antecipação de recebíveis para comissões de formatura.**

Projeto acadêmico desenvolvido em dupla para a 2ª Verificação de Aprendizagem da disciplina de Análise e Projeto de Sistemas de Informação (UFRPE — 2026.2).

## Sobre o projeto

Uma comissão de formatura pode precisar de recursos antes da data prevista para receber uma parcela. O FormaFlux permite cadastrar uma turma e parcelas previstas, simular o valor líquido de uma antecipação e comparar dois modelos financeiros ilustrativos.

**Escopo:** uma turma por execução, dados fictícios e armazenamento somente em memória. O FormaFlux não realiza pagamentos, antecipações reais ou consultas bancárias.

## Funcionalidades

| Código | Funcionalidade |
|---|---|
| CSU01 | Cadastrar turma |
| CSU02 | Cadastrar parcela |
| CSU03 | Consultar parcelas |
| CSU04 | Simular antecipação |
| CSU05 | Comparar modalidades |
| CSU06 | Validar parâmetros da simulação (operação interna) |

## Como executar

Requer **Python 3.10 ou superior**.

No terminal, entre na pasta `projeto-formaflux`.

### Menu CLI (requisito da avaliação)

```powershell
py main.py
```

O menu CLI utiliza apenas a biblioteca padrão do Python.

### Interface gráfica complementar

Instale a dependência:

```powershell
py -m pip install -r requirements.txt
py interface.py
```

O CustomTkinter é usado apenas na interface gráfica; as fórmulas são implementadas nas classes de domínio.

## Estrutura de classes

- `Turma`: identifica a turma e administra a lista de parcelas.
- `Parcela`: representa um valor previsto, com identificador, valor nominal e prazo.
- `Antecipacao`: classe abstrata que reúne taxa e tarifa e define a operação de cálculo.
- `AntecipacaoSimples`: especializa o cálculo pelo desconto comercial simples.
- `AntecipacaoComposta`: especializa o cálculo pelo valor presente composto.

As subclasses usam `super()` e sobrescrevem `calcular_valor_liquido(parcela)`. O código adota encapsulamento e validações de valores e prazos.

## Exemplo de simulação

Parcela `P01`: **R$ 1.000,00**, prazo de **3 meses**, taxa de **2% ao mês** e tarifa fixa de **R$ 10,00**.

| Modelo | Valor líquido | Custo total |
|---|---:|---:|
| Desconto comercial simples | R$ 930,00 | R$ 70,00 |
| Valor presente composto | R$ 932,32 | R$ 67,68 |

Esses valores são calculados por modelos didáticos; não representam oferta de uma instituição financeira.

## Testes

Na pasta do projeto, execute:

```powershell
py -m unittest discover -s testes -v
```

Os testes abrangem resultados das fórmulas, herança, polimorfismo, validação de atributos, parcela duplicada e situações inválidas.

## Modelagem UML

A implementação é acompanhada, na atividade acadêmica, de diagramas de **casos de uso, classes, sequência e atividades**, que devem ser coerentes com os métodos do programa. A documentação final poderá ser adicionada à pasta do projeto após a revisão da equipe.

## Colaboração

Projeto desenvolvido por **Luana Luzia Ferreira de Medeiros e Isabelle Karoline de Oliveira Barbosa**. As contribuições podem ser acompanhadas pelo histórico de commits e revisões do repositório.

## Observação

Projeto acadêmico de demonstração. Sem persistência de dados ou movimentação financeira real.
