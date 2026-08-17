# Análise Consolidada — Por que o InfoBIM não vende hoje?

> Consenso entre ChatGPT, Claude, Gemini e Perplexity (agosto/2026)

---

## 1. Veredito Central

**A capacidade é real. O valor é real. O formato comercial comprável não está sendo oferecido.**

O InfoBIM possui componentes técnicos incomuns (malha semântica sobre IFC + documentos heterogêneos, preservação de fontes originais, navegação contextual), mas ainda não os entrega como **uma unidade econômica que alguém reconheça, orce e contrate** — ou seja, um "produto de entrada" com gatilho, orçamento, comprador, prazo e critério de aceite explícitos.

---

## 2. Mecanismos Causais Consensuais

| Mecanismo | Explicação |
|---|---|
| **Valor retroativo e episódico** | O benefício aparece em eventos de exceção (claim, auditoria, handover, falha) — não no fluxo diário. A construção não tem categoria de compra para "capacidade preventiva que um dia pode valer". |
| **Traceability Benefit Problem** | Quem tem que capturar/manter os links (equipe de projeto, campo) não é quem colhe o benefício (jurídico, proprietário na operação, fiscal). Incentivo estrutural para minimizar esforço local. |
| **Cold start informacional** | O valor explode só depois de uma densidade mínima de relações. O custo de implantação (normalização, imports, validação) chega *antes* da evidência de retorno. |
| **Sem linha orçamentária** | "Malha semântica navegável" não é centro de custo em nenhuma empresa. Mercado compra CDE, field, quality, contracts, commissioning — categorias nomeadas com dono de orçamento. |
| **80% já resolvido em silos** | Histórico *dentro* de cada plataforma (ACC, ConstruCode, Aconex, Dalux) existe e é barato. O que falta é a costura *entre* silos — valor alto por evento, frequência baixa. |
| **Problema probatório da federação** | Vantagem arquitetural (não centralizar) vira risco em claims/auditoria: link que sobrevive mas fonte externa que muda/desaparece/perde permissão. Precisa demonstrar cadeia de custódia. |

---

## 3. Gatilhos de Compra — Rankeados

1. **Claim / disputa contratual / arbitragem ATIVA** — urgência processual, orçamento de litígio, resolvido hoje com humano + pasta. Chance mais alta.
2. **Handover / commissioning / as-built travado** — data marcada, dinheiro retido, multa diária por não entregar o dossiê.
3. **Auditoria / fiscalização / medição questionada** — obrigação regulatória, prazo certo.
4. **Não conformidade crítica / investigação de causa-raiz** — falha com risco de responsabilização.
5. **Troca de equipe / retomada de obra paralisada** — amnésia organizacional com custo imediato.

---

## 4. Segmentos Mais Aderentes

1. **O&G / EPC industrial / data centers** — equipamentos identificáveis, vendor data, commissioning formal, múltiplos fornecedores, alto custo de atraso.
2. **Infraestrutura / concessões / obras públicas complexas** — ciclos longos, múltiplas organizações, fiscalização, mudanças, memória de longo prazo.
3. **Consultorias de perícia, claims, commissioning, QA/QC** — já têm o problema, o cliente final, o orçamento por projeto e a competência técnica; podem ser clientes *e* canal.
4. **Proprietários / operadores de ativos críticos** — capturam benefício na operação, mas precisam exigir contratualmente a produção da informação.

**Aderência baixa:** Pequenas construtoras residenciais, edificações sem BIM avançado, mercado geral de incorporação padrão.

---

## 5. Diferenciação e Concorrência

- **Nenhum produto comercial** na construção reconstroi transversalmente a história de uma entidade arbitrária atravessando IFC, documentos, atividades, compras, execução e pessoas **sobre arquivos que já existem** sem exigir adoção prévia.
- Concorrentes parciais dentro de seus silos: ConstruCode, ACC, Dalux, Revizto, Aconex, Catenda, Thinkproject.
- **Substituto real do InfoBIM = um analista com uma pasta e 2–3 semanas.** Esse é o preço que você concorre, e ele é alto (bom para você).
- Em manufatura/PLM a categoria "digital thread / knowledge graph" já existe e é paga — prova que a capacidade tem preço *quando tem categoria*.

---

## 6. ConstruCode — A Lição (não copie, entenda)

- Wedge inicial **físico e visível**: QR Code no pilar resolvia uma falha com custo imediato (retrabalho por revisão errada no papel).
- **Distribuição alugada, não construída**: acesso ao canal da Vedacit foi o fator causal dominante (8x aumento de vendas na aceleração).
- Expansão modular sobre o **mesmo comprador**, do QR para Docs → Tasks → Field → Check.

> **Lição para o InfoBIM**: você provavelmente não precisa de um concorrente da ConstruCode. Precisa do seu **equivalente de Vedacit Labs** — canais já homologados (perícias, gerenciadoras, integradores O&G, consultorias BIM).

---

## 7. Modelo Comercial Recomendado (Unânime)

### ❌ NÃO FAZER AGORA
- SaaS self-service / PLG / freemium horizontal
- Cobrança por usuário
- Contrato enterprise de serviço ou implantação antes de provar repetibilidade de projeto para projeto
- Competição de frente com ConstruCode/ACC em GED/field/RDO

### ✅ FAZER PRIMEIRO
**Open source + Serviço de Reconstituição de Informação disparado por evento, com o InfoBIM como infraestrutura interna.**

- Entrega: HTML navegável + relatório/lacuna por ativo, sistema ou evento.
- Preço **por escopo fechado**: R$ 30k–R$ 150k (piloto R$ 15k–R$ 30k).
- Você opera a CLI; cliente recebe o resultado. O motor técnico fica invisível.
- O open source funciona como **prova de competência** e reduz medo de lock-in — não como produto vendido.
- **Canal secundário**: subcontratação por perícias, gerenciadoras, consultorias BIM, integradores homologados. Split de receita ou hora técnica.
- Assinatura de manutenção/atualização **só depois** do cliente sentir o valor retroativamente e perguntar "quanto custa pra manter?". Nunca antes.

### TAM / SAM / SOM realista
- **SAM**: R$ 50–150 mi/ano (reconstituição de informação em O&G, infra, EPC, público + claims) — hoje capturado por humanos, não software.
- **SOM fundador solo em 24 meses**: 4–12 engajamentos → **R$ 300k–R$ 1,5 mi/ano** (alta margem, sem equipe, sem VC).
- O prêmio realista é uma **boutique de alto valor por hora**, não uma empresa de software VC-backed. Se esse prêmio não interessa, essa é uma razão legítima para parar.

---

## 8. Hipóteses Oficialmente Descartadas

| Hipótese | Veredito |
|---|---|
| "Ontologia/SHACL assusta o cliente" | ❌ Descartada. É mecanismo interno, nunca foi exposto comercialmente. |
| "Concorrente é Excel/e-mail/WhatsApp" | ❌ Descartada. São *fontes*, não substitutos. Substituto real = humano montando dossiê. |
| "É o sétimo sistema" | ❌ Descartada na forma ingênua. Ele não centraliza. Obstáculo real é acesso concedido aos acervos, não quantidade de sistemas. |
| "CLI/pip é fatal" | ❌ Descartada. No modelo de serviço, quem opera a CLI é você. O cliente vê HTML. |
| "Falta distribuição / prova social" | Irrelevante como explicação. Rompe-se via canal alugado ou serviço pago sob NDA. |

---

## 9. Três Experimentos Que Discriminam (60 dias, orçamento próximo de zero)

1. **Autópsia gratuita, escopo fechado**  
   Pegar acervo de 1 projeto já encerrado/paralisado de 5 empresas (risco político baixo) → devolver reconstituição de 10 entidades em 1 semana. Mede: dor é real? acervo é liberável? densidade sustenta o "por quê"?

2. **Proposta precificada em gatilho vivo**  
   5 situações ATIVAS (claim, handover travado, auditoria) → proposta de preço fechado, sem trial. A objeção que vier já é o dado. Mede: "acham interessante" ≠ "compram".

3. **Teste de canal como subcontratado**  
   Apresentar para 5 peritos/gerenciadoras/advogados de construção como *capacidade subcontratável*, não como software. Mede: rota é venda direta ou alavancagem de canal?

---

## 10. Critérios de Kill / Continue

### MATA (empiricamente) se:
- 12 conversas com donos de gatilho → nenhum entrega acervo real nem sob NDA.
- 3 acervos reais → o grafo não recupera o *porquê* de nenhuma decisão relevante.
- 5 propostas fechadas em gatilhos vivos → zero PO assinado e nenhuma objeção de preço (só silêncio).

### CONTINUA se:
- ≥3 dos 12 entregam acervo espontaneamente na 1ª conversa.
- **1 PO ≥ R$ 30k assinado em 90 dias** disparado por evento real.
- Alguém pergunta "quanto custa pra fazer isso todo mês" *sem você sugerir*.
- Um canal pede para usar a capacidade no contrato deles.
- 2º cliente vem por indicação do 1º.

---

## 11. Resposta Final em Uma Frase (Consenso)

> **Hoje, o InfoBIM não vende principalmente porque sua capacidade mais valiosa é retroativa, episódica e transversal — não existe categoria de compra, linha orçamentária nem gatilho de adoção preventiva para ela no fluxo normal da obra, e o único formato em que ela é comprável (serviço especializado disparado por evento contratual, com o software como vantagem de margem interna) ainda não está sendo oferecido a ninguém.**
