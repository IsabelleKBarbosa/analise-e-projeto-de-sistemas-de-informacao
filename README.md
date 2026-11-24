# Análise e Projeto de Sistemas de Informação

Repositório destinado ao registro dos projetos e atividades desenvolvidos durante a disciplina de **Análise e Projeto de Sistemas de Informação**, do curso de **Bacharelado em Sistemas de Informação da Universidade Federal Rural de Pernambuco (UFRPE)**, semestre **2026.2**.

O conteúdo está organizado por projeto, preservando o contexto acadêmico e as decisões de modelagem adotadas ao longo da disciplina.

## Projetos

### [FormaFlux — Simulador de antecipação de recebíveis](./projeto-formaflux/)

Projeto da **2ª Verificação de Aprendizagem (2ª VA)**, desenvolvido em dupla, voltado à simulação de antecipação de parcelas previstas por comissões de formatura.

O sistema é implementado em **Python** e demonstra encapsulamento, herança, polimorfismo, abstração e relacionamento entre objetos. Conta com menu interativo no terminal (CLI) e interface gráfica complementar em CustomTkinter.

As operações são **fictícias e exclusivamente educacionais**. Não há integração com instituições financeiras nem movimentação de recursos reais.

## Organização

```text
analise-e-projeto-de-sistemas-de-informacao/
├── projeto-formaflux/
│   ├── main.py
│   ├── interface.py
│   ├── turma.py
│   ├── parcela.py
│   ├── antecipacao.py
│   ├── antecipacao_simples.py
│   ├── antecipacao_composta.py
│   ├── testes/
│   ├── requirements.txt
│   └── README.md
├── .gitignore
├── .gitattributes
└── README.md
```

O funcionamento, os testes e as decisões do projeto estão documentados no README da pasta `projeto-formaflux`.
