# Curva ABC do comprometimento do caixa — por competência

## Correção metodológica

A versão anterior estava conceitualmente errada para fluxo de caixa: ela somava o estoque nominal de obrigações de vários meses e produzia uma única ABC. Isso mede estoque de compromissos, não comprometimento mensal do caixa.

Para gestão de caixa, a unidade correta é a **competência de pagamento/vencimento**. Portanto:

- uma parcela de empréstimo que vence em setembro entra em setembro, não no total acumulado de todos os meses;
- parcelas futuras entram apenas no mês em que forem exigíveis;
- consumo no cartão só entra como obrigação do mês quando a fatura correspondente for identificada;
- transações canceladas e duplicadas continuam excluídas;
- `Pagamento recebido` não é gasto.

## O que a base permite afirmar hoje

### Agosto/2026

A base contém a **fatura de agosto do Nubank**, formada por compras datadas em julho. O valor bruto de compras importado dessa fatura é R$ 4.223,45, separado do registro `Pagamento recebido` de R$ 4.589,16.

O FREE MASTERCARD contém transações até 15/08, mas a base não identifica com segurança em qual fatura/data de vencimento cada uma será paga. Portanto elas não devem ser automaticamente tratadas como saída de caixa de agosto.

**Importante:** nos dados capturados até agora não existe uma linha de empréstimo identificada como efetivamente paga/vencida em agosto. Logo, não é correto inventar um valor de empréstimo para agosto. Se houver parcela paga em agosto, falta o documento/lançamento correspondente na base.

### Setembro/2026 — obrigações de empréstimo explicitamente capturadas

A base contém quatro obrigações de empréstimo com vencimento em setembro:

| Data | Obrigação | Parcela | Valor |
|---|---|---:|---:|
| 01/09/2026 | Empréstimo | 6/6 | R$ 315,11 |
| 09/09/2026 | Empréstimo | 3/12 | R$ 737,39 |
| 11/09/2026 | Empréstimo pessoal | 8/10 | R$ 393,15 |
| 11/09/2026 | Empréstimo pessoal | 2/12 | R$ 197,41 |

**Total de empréstimos explicitamente exigíveis em setembro: R$ 1.643,06.**

Além disso, aparece um `Plano de pagamento` com vencimento em 08/09/2026 de **R$ 1.048,51**.

Assim, considerando apenas obrigações financeiras com vencimento explícito já capturadas:

**Setembro/2026 = R$ 2.691,57**

- Empréstimos: R$ 1.643,06 — 61,0%
- Plano de pagamento: R$ 1.048,51 — 39,0%

Essa é uma ABC mensal válida para as obrigações financeiras explícitas conhecidas de setembro.

## Fluxo financeiro explícito conhecido por mês

| Competência | Empréstimos | Plano de pagamento | Total explícito |
|---|---:|---:|---:|
| ago/2026 | não identificado na base | não identificado na base | incompleto |
| set/2026 | R$ 1.643,06 | R$ 1.048,51 | **R$ 2.691,57** |
| out/2026 | R$ 737,39 | R$ 1.048,51 | **R$ 1.785,90** |
| nov/2026 | R$ 737,39 | R$ 709,22 | **R$ 1.446,61** |
| dez/2026 | R$ 737,39 | R$ 709,22 | **R$ 1.446,61** |
| jan/2027 | R$ 737,39 | R$ 709,22 | **R$ 1.446,61** |
| fev/2027 | R$ 737,39 | R$ 709,22 | **R$ 1.446,61** |
| mar/2027 | R$ 737,39 | R$ 709,22 | **R$ 1.446,61** |
| abr/2027 | R$ 737,39 | R$ 709,22 | **R$ 1.446,61** |
| mai/2027 | R$ 737,39 | — | **R$ 737,39** |
| jun/2027 | R$ 737,36 | — | **R$ 737,36** |

## Como deve ser feita a ABC de comprometimento do caixa

A ABC deve ser recalculada **mês a mês**, juntando somente valores que efetivamente pressionam aquele mês:

1. faturas de cartão que vencem no mês;
2. parcelas de empréstimos com vencimento no mês;
3. plano de pagamento com vencimento no mês;
4. demais boletos, débitos e despesas fixas do mês;
5. excluindo duplicidades, cancelamentos e transferências que não representem despesa.

Portanto não há uma única “ABC de comprometimento do caixa” de R$ 24 mil. Esse número era apenas a soma nominal do estoque futuro e foi descartado como métrica de caixa.

## Situação atual

A competência mais completa para obrigações financeiras futuras é **setembro/2026**, com R$ 2.691,57 explicitamente mapeados antes de acrescentar faturas de cartão e outras contas do mês.

Para agosto, a fatura Nubank é conhecida, mas ainda falta fechar corretamente:

- o que já foi efetivamente pago;
- eventual parcela de empréstimo de agosto;
- a competência de pagamento do FREE MASTERCARD;
- outras despesas fixas fora dos cartões.

Sem esses dados, uma ABC completa de agosto seria falsa precisão.