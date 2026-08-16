# Auditoria de Custos Mensais

## Objetivo

Esta pasta existe para consolidar e auditar os gastos mensais pessoais e familiares a partir de faturas, extratos, comprovantes e outras fontes de despesas.

O trabalho realizado aqui deve permitir:

- registrar e normalizar os lançamentos mensais;
- identificar despesas recorrentes, eventuais e extraordinárias;
- classificar os gastos por categoria e favorecido/estabelecimento;
- consolidar valores por mês, categoria e origem;
- produzir Curva ABC dos gastos;
- identificar os itens com maior impacto financeiro;
- detectar aumentos, recorrências desnecessárias, duplicidades e gastos potencialmente evitáveis;
- comparar meses sucessivos;
- propor um planejamento objetivo de redução de despesas, preservando gastos necessários e priorizando cortes pelo impacto financeiro.

## Fonte inicial

A primeira fonte prevista é o levantamento de lançamentos do cartão de crédito da esposa de Elias, obtido a partir de capturas de tela fornecidas na conversa com o ChatGPT.

Os valores só devem ser registrados quando forem legíveis na fonte. Não inferir ou completar lançamentos duvidosos. Quando houver incerteza, registrar a observação explicitamente para revisão.

## Arquivo principal

`gastos_mensais.csv` é a base tabular consolidada desta pasta.

Cada lançamento deve ocupar uma linha independente. Sempre que a fonte permitir, registrar data, descrição original, valor, parcela, cartão/origem e demais campos úteis para auditoria.

## Análises esperadas

1. Total mensal de despesas.
2. Totais por categoria.
3. Totais por estabelecimento/favorecido.
4. Despesas recorrentes.
5. Curva ABC por valor acumulado.
6. Maiores variações entre meses.
7. Gastos candidatos a redução, renegociação, substituição ou eliminação.
8. Cenários de economia mensal e anual.

## Princípio de auditoria

Preservar sempre o dado bruto extraído da fonte. Classificações e interpretações podem evoluir; o lançamento original não deve ser silenciosamente reescrito.
