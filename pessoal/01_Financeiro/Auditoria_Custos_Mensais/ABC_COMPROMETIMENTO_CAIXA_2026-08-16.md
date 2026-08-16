# Curva ABC do comprometimento do caixa — 2026-08-16

## Objetivo

Esta análise mede **pressão sobre o caixa**, não apenas consumo. Ela agrega, sem duplicatas e sem transações canceladas:

1. consumo corrente efetivamente registrado nos cartões;
2. parcelas futuras conhecidas de cartão;
3. empréstimos futuros capturados nos prints;
4. plano de pagamento futuro capturado nos prints.

O `Pagamento recebido` do Nubank não é tratado como gasto.

## Base de comprometimento capturada

- Consumo corrente: **R$ 7.001,14**
- Parcelas futuras de cartão conhecidas: **R$ 3.033,64**
- Empréstimos futuros: **R$ 8.279,54**
- Plano de pagamento futuro: **R$ 6.352,34**

**Comprometimento nominal total capturado: R$ 24.666,66.**

> Atenção: este total é uma visão nominal/provisória. Os empréstimos, plano de pagamento e parcelas futuras de cartão foram somados como compromissos distintos porque aparecem como linhas distintas na base. Ainda é necessário confirmar se existe alguma sobreposição econômica entre eles antes de interpretar R$ 24.666,66 como “dívida líquida total”. Para gestão de caixa, porém, a visão é útil porque mostra onde estão as maiores pressões conhecidas.

## Curva ABC — comprometimento do caixa

| Ordem | Grupo | Valor | % do total | % acumulado | Classe |
|---:|---|---:|---:|---:|:---:|
| 1 | Empréstimos | R$ 8.279,54 | 33,6% | 33,6% | A |
| 2 | Plano de pagamento | R$ 6.352,34 | 25,8% | 59,3% | A |
| 3 | Parcelas futuras de cartão | R$ 3.033,64 | 12,3% | 71,6% | A |
| 4 | Não identificado — consumo corrente | R$ 2.052,40 | 8,3% | 79,9% | A |
| 5 | Supermercado | R$ 1.298,87 | 5,3% | 85,2% | B |
| 6 | Compras/Varejo | R$ 929,58 | 3,8% | 89,0% | B |
| 7 | Alimentação fora | R$ 925,30 | 3,8% | 92,7% | B |
| 8 | Combustível | R$ 536,51 | 2,2% | 94,9% | B |
| 9 | Pix no crédito já lançado | R$ 452,29 | 1,8% | 96,7% | C |
| 10 | Saúde/Farmácia | R$ 275,33 | 1,1% | 97,8% | C |
| 11 | Religioso/Doações | R$ 230,00 | 0,9% | 98,8% | C |
| 12 | Impostos | R$ 190,12 | 0,8% | 99,6% | C |
| 13 | Assinaturas/Digital | R$ 101,79 | 0,4% | 100,0% | C |
| 14 | Transporte | R$ 8,95 | <0,1% | 100,0% | C |

## O que compõe aproximadamente 80% da pressão sobre o caixa

Os quatro primeiros grupos chegam a **79,9%** do comprometimento capturado:

1. **Empréstimos — R$ 8.279,54**
2. **Plano de pagamento — R$ 6.352,34**
3. **Parcelas futuras de cartão — R$ 3.033,64**
4. **Consumo corrente ainda não identificado — R$ 2.052,40**

Somados: **R$ 19.717,92**, equivalentes a **79,9%** do comprometimento nominal capturado.

Se for usado o critério clássico de incluir o primeiro item que faz o acumulado ultrapassar 80%, entra também **Supermercado — R$ 1.298,87**, levando a Classe A ampliada para **R$ 21.016,79 (85,2%)**.

## Interpretação

A principal conclusão muda radicalmente em relação à ABC apenas de consumo: **o problema dominante não é supermercado nem alimentação; é endividamento/comprometimento futuro**.

Empréstimos + plano de pagamento + parcelas futuras de cartão somam **R$ 17.665,52**, cerca de **71,6% de toda a pressão de caixa conhecida**. Portanto, cortes de Netflix, alimentação fora ou pequenas compras ajudam, mas não resolvem estruturalmente o problema se novas dívidas e parcelamentos continuarem sendo criados.

O quarto maior grupo, `Não identificado`, ainda merece investigação porque representa **R$ 2.052,40** de consumo corrente. Classificá-lo pode mostrar oportunidades de corte rápido, mas ele é secundário diante do estoque financeiro já contratado.

## Prioridade operacional sugerida

1. **Bloquear crescimento do estoque de dívida:** evitar novos empréstimos, planos e parcelamentos salvo necessidade real.
2. **Mapear exatamente cada empréstimo/plano:** saldo, CET/taxa, parcelas restantes, possibilidade de antecipação ou refinanciamento.
3. **Montar fluxo mensal de obrigações:** setembro/2026 já aparece como o pico dos compromissos financeiros explícitos capturados.
4. **Identificar os R$ 2.052,40 ainda sem categoria:** é o principal espaço de consumo corrente ainda opaco.
5. **Depois atacar os gastos discricionários:** compras/varejo e alimentação fora são os primeiros candidatos conhecidos; supermercado deve ser otimizado, não simplesmente cortado.

## Limite desta ABC

Esta é uma ABC de **comprometimento nominal capturado**, não uma demonstração completa do patrimônio ou da dívida líquida familiar. Ainda faltam, se existirem, contas fora desses cartões, débito, PIX, boletos, financiamentos e demais despesas fixas. Também deve ser verificada eventual sobreposição entre plano de pagamento, empréstimos e parcelas futuras antes de qualquer decisão de quitação ou refinanciamento.