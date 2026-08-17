# Estratégia de Venda Recorrente — InfoBIM

> Complemento ao [resumo_consolidado.md](file:///Users/eliasmpjunior/Brasidata/07_Engenharia_e_Tecnologia/06_Solucoes_Reutilizaveis/OntoBDC/my-desktop/brasidata/planning/duvida/resumo_consolidado.md)
> Objetivo: ter uma oferta recorrente "deixada lá de exposição" — mesmo que a receita principal continue vindo de serviços pontuais por evento.

---

## Premissa Não Negociável (das 4 análises)

A receita **principal** continua sendo o serviço de reconstituição por evento (R$ 30k–150k por escopo fechado). O modelo recorrente NÃO é o produto principal; é **isca de lead + retenção + faturamento de margem complementar + artefato de exposição**.

Inventar SaaS self-service PLG horizontal agora = erro confirmado por 4 LLMs independentes. Não fazemos isso.

---

## Arquitetura de 3 Tiers Recorrentes

```
┌──────────────────────────────────────────────────────────────────────┐
│  Tier 3 — Parceria White-Label (Boutiques Especializadas)            │
│  R$ 4.997/mês base + R$ 2.997/projeto  →  receita recorrente +      │
│  alavancagem. InfoBIM é open-source gratuito; o cobrado é            │
│  OPERAÇÃO + SUPORTE + ENTREGA de resultados com marca do parceiro.   │
├──────────────────────────────────────────────────────────────────────┤
│  Tier 2 — Manutenção da Malha (follow-up de serviço pontual)         │
│  R$ 2.997 / mês por projeto  →  receita recorrente REAL              │
├──────────────────────────────────────────────────────────────────────┤
│  Tier 1 — InfoBIM Watch (porta de entrada / exposição)               │
│  R$ 497 / mês por projeto  →  barato, baixo atrito, gerador de       │
│                                 leads para Tier 2 e serviço          │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Tier 1 — InfoBIM Watch (o "deixar lá de exposição")

### O que é (na prática, não no slide)
Uma assinatura de **monitoramento passivo de 1 projeto**, sem exigir mudança de processo do cliente. Você (ou um script/CLI agendado) faz:

1. **Acesso SOMENTE LEITURA** a uma pasta ou CDE do cliente (IFC + documentos). Nenhuma modificação, nenhuma exigência de nova ferramenta para a equipe do cliente.
2. **Snapshot quinzenal/mensal** dos arquivos + ingestão no InfoBIM.
3. **Geração automática** de:
   - 1 surface HTML estática do projeto (atualizada)
   - 1 relatório PDF curto (1 página) com **3–4 itens concretos**:
     - "3 novas classes IFC sem nenhum documento vinculado → risco de lacuna em handover"
     - "2 PDFs de certificado novos adicionados → vinculamos automaticamente aos 5 elementos correspondentes"
     - "1 versão de IFC antiga ainda está sendo referenciada em 8 relatórios"
   - 1 alerta por e-mail quando algo **crítico** aparece (ex: "o certificado do transformador expirou no sistema de arquivos — o link do Watch quebrou")
4. **1 call de 15 minutos por mês** (opcional, mas recomendado) para revisar o relatório.

### Preço
- **Mensal:** R$ 497 / mês por projeto
- **Anual (recomendado no pitch):** R$ 4.970 / ano → 2 meses grátis + 1 "check-up de handover readiness" no 6º mês

### Por que esse tier existe
- **Exposição**: é barato o suficiente para um engenheiro sênior/BIM manager aprovar sem subir para CFO. Aprovação rápida → "deixa lá rodando".
- **Lead magnet**: cliente que tem Watch rodando há 6 meses tem **5x mais chance** de comprar o serviço pontual quando o gatilho (claim/handover/auditoria) aparecer — você já tem os dados, já conhece o projeto, já tem credibilidade.
- **Artefato visível**: todo mês o cliente vê um relatório seu na caixa de entrada. Não é "esqueci que você existe".
- **Sem automação total inicial**: nos primeiros 20 clientes, você opera o Watch manualmente (roda CLI, gera relatório, envia email). A recorrência é do **contrato e do valor percebido**, não da automação perfeitamente acabada. Automatiza só quando ficar repetitivo.

### Perfil de cliente alvo para Tier 1
- Construtoras/EPCs com 1 projeto industrial ou de infraestrutura em andamento (≥ R$ 50MM)
- Que já usam BIM mas têm documentação espalhada em 3+ lugares
- BIM manager ou coordenador que você já conhece de algum evento/conversa anterior
- Pitch de 1 frase: *"Por menos do que você paga de celular por mês, eu deixo um robô rodando no seu projeto que te avisa todo mês quais lacunas de rastreabilidade vão te dar dor de cabeça no handover. Se nada aparecer, paz; se aparecer, você já sabe antes do marco."*

---

## Tier 2 — Manutenção da Malha (receita recorrente REAL)

### Quando oferecer
**SOMENTE DEPOIS** que o cliente já comprou e recebeu o serviço pontual de reconstituição (R$ 30k–150k). Nunca ofereça Tier 2 antes. O cliente precisa ter **sentido o valor** primeiro.

### O que é
- "Você me pagou R$ 60k para montar o dossiê de handover do sistema de refrigeração com 42 ativos. Agora, por R$ 2.997/mês, eu **mantenho esse dossiê vivo**:
  - Atualizo toda vez que entra nova versão de IFC, novo certificado, nova foto de inspeção, nova nota fiscal
  - Re-rodo as vinculações automaticamente
  - Te entrego o pacote de evidência atualizado em qualquer dia útil, em até 4h, se o fiscal ou o cliente pedir
  - Todo mês envio um relatório de 'saúde da malha' e 1 sugestão de melhoria de processo pra reduzir risco de lacuna"

### Preço
- **R$ 2.997 / mês por projeto / sistema**
- Desconto para 3+ sistemas no mesmo projeto: R$ 7.997 / mês
- Anual: 10x o valor mensal (2 meses grátis)

### Por que esse tier funciona
- **Alta conversão**: cliente que acabou de pagar R$ 60k e viu o resultado entende que a informação azeda se não for mantida. A recorrência se vende sozinha.
- **Baixo esforço incremental**: o grosso do trabalho foi na reconstituição inicial. A manutenção mensal custa ~10% do esforço do pontual, mas gera ~5–10% do valor do pontual **todos os meses**. Margem excelente.
- **Retenção**: cliente com Manutenção da Malha raramente volta para o processo manual. O custo de troca é alto.

### Meta
- ≥ 60% dos clientes de serviço pontual aceitam Tier 2 no follow-up
- Tempo de vida médio (LTV): ≥ 8 meses

---

## Tier 3 — Parceria White-Label (Serviço de Operação Assistida)

> InfoBIM é gratuito e open-source — NÃO HÁ venda de licença, de assento ou de direito de uso de software. O que o parceiro paga é exclusivamente pela **OPERAÇÃO HUMANA + SUPORTE + ENTREGA** de resultados finais white-label. O motor InfoBIM (open-source) é o instrumento que você usa para prestar o serviço; não é um produto vendido ou licenciado.

### O problema real que esse tier resolve (para o PARCEIRO, não pra você)

Toda boutique especializada (perícia, claims, commissioning, QA/QC de handover) tem os mesmos 3 pesadelos:

1. **Faturamento cravado por hora**: parceiro cobra R$ 300/h de engenheiro. Um trabalho de reconstituição de histórico demora 3 semanas (120h) → fatura R$ 36k, mas só lucra R$ 10k porque é mão de obra cara. Não escala sem contratar mais gente.
2. **Submete a trabalho braçal repetitivo**: 2 analistas juniores passam 2 semanas abrindo pasta, cruzando planilha, copiando GlobalId do IFC pra planilha do Excel. Atividade de baixo valor que a equipe técnica odeia.
3. **Perde pitch para concorrente maior**: concorrente apresenta uma entrega visual bonita (surface navegável, QR em elemento, timeline) e o cliente acha "mais profissional", mesmo que a qualidade da análise seja igual ou pior.

O Tier 3 resolve exatamente esses 3.

---

### Como funciona NA PRÁTICA (fluxo completo)

```
1. Parceiro fecha com CLIENTE FINAL um serviço de:
   → Reconstituição de claim de atraso        (R$ 80k–R$ 150k)
   → Dossiê de handover de sistema crítico   (R$ 60k–R$ 120k)
   → Pacote de evidências de commissioning   (R$ 50k–R$ 90k)
   → Perícia de causa-raiz em falha          (R$ 40k–R$ 100k)

2. Parceiro envia PRA VOCÊ os arquivos brutos (IFC + PDFs + planilhas +
   fotos + etc.) via pasta zipada, OneDrive, CDE — qualquer formato.
   Parceiro NÃO toca no InfoBIM. Parceiro não precisa saber Python.
   Parceiro não instala NADA.

3. VOCÊ roda a CLI, configura os bindings, gera:
   → Surface HTML navegável white-label (só marca do PARCEIRO,
     nenhuma menção a InfoBIM/Brasidata)
   → Pacote de evidências estruturado por ativo/evento
   → Índice de lacunas de prova automático
   → Timeline visual de decisões e alterações

4. Você entrega tudo pronto pro parceiro em até 3 DIAS ÚTEIS.
   Parceiro revisa, adiciona sua análise técnica / laudo pericial
   (a parte intelectual que realmente justifica o preço dele),
   e entrega ao cliente final com a marca dele.

5. Paralelamente, o parceiro tem direito a:
   → 2 dias de "envolvimento pré-venda" por mês: você entra numa
     reunião de pitch com prospect DO PARCEIRO, faz uma demo
     customizada usando dados públicos do prospect, e sai.
   → Suporte técnico ilimitado por e-mail/WhatsApp.
   → Templates customizados de relatório alinhados ao
     layout gráfico do parceiro.
   → Taxa preferencial em projetos com escopo extraordinário
     (>200 ativos ou >500 documentos).
```

---

### Preço e modelos de remuneração (3 opções, parceiro escolhe)

#### Modelo A — Contrato Base + Taxa por Projeto (recomendado para validação inicial)
- **R$ 4.997 / mês** por contrato de parceiro ativo (inclui suporte, templates customizados e dias de pré-venda)
- **+ R$ 2.997 POR PROJETO** entregue (qualquer escopo até 200 ativos / 500 documentos)
- Projetos maiores (acima do limite): orçamento separado, 20% de desconto sobre a tabela de serviço direto.
- Fidelidade mínima: 3 meses (reduz atrito)

**ROI do parceiro em 1 projeto só:**
- Parceiro fecha claim de atraso: R$ 90k
- Custo Tier 3: R$ 4.997 (mês) + R$ 2.997 (projeto) = R$ 7.994
- Antes custava R$ 36k de mão de obra interna (120h × R$ 300/h)
- **Economia do parceiro: ~R$ 28k em 1 projeto.**
- E o contrato mensal de ~R$ 5k já se pagou 6x no primeiro mês.

#### Modelo B — Operação Ilimitada Mensal (parceiro com pipeline comprovado)
- **R$ 9.997 / mês** fixo
- Projetos ilimitados durante o mês (até 4 projetos/parceiro/mês — fair use razoável)
- Ideal para parceiro que fecha ≥2 serviços de reconstituição por mês com recorrência
- Fidelidade mínima: 6 meses
- Workshop de onboarding de 8h incluso no 1º mês

#### Modelo C — Participação em Projeto (para parceiros casuais, sem mensalidade)
- **Sem valor mensal fixo**
- **30% do valor do contrato final do parceiro** (você recebe 30%, parceiro fica com 70%)
- Ex: parceiro fecha projeto de R$ 80k → você recebe R$ 24k, sem custo fixo mensal
- Prazo de entrega acordado caso a caso
- Nenhum direito a dias de pré-venda inclusos

---

### Perfil de parceiro (CLAREZA CIRÚRGICA — se não bater, não perde tempo)

#### ✅ PERFIL IDEAL — 5/5
1. **Carteira ativa de pelo menos 3 clientes de O&G, infraestrutura concedida, data center ou obra pública federal** (São Paulo, Rio, Bahia, Brasilia)
2. **Já vende serviços com valor de contrato ≥ R$ 40k** (não é consultoria de R$ 5k por diagnóstico)
3. **Tem pelo menos 1 profissional sênior com cargo de Engenheiro Especialista, Perito Judicial ou Gerente de Commissioning** que assina laudos/relatórios tecnicamente
4. **Opera com 3–15 funcionários** (tamanho boutique: tem dores de escala mas ainda é ágil)
5. **Histórico de pelo menos 2 disputas contratuais, auditorias ou processos de handover complexos nos últimos 12 meses**

#### ❌ NÃO É PARCEIRO AGORA — não persegue
- Startup nova sem clientes pagantes
- Consultoria geral de transformação digital / BIM genérico
- Escritório pequeno de projeto arquitetônico ou estrutura
- Software house / integrador que quer "customizar o produto"
- Grande empresa de auditoria multinacional (ciclo de homologação é 1 ano+)

---

### 3 Tipos de Parceiro (por atividade) — do mais promissor ao menos

| # | Tipo | Por que é top | Pitch do parceiro |
|---|---|---|---|
| 1 | **Perícia de Engenharia / Escritório de Arbitragem** | Já trabalha EXATAMENTE com reconstrução de histórico. Tem cliente com claim ATIVO e orçamento de litígio. Orçamento é o de menos — prazo e qualidade da evidência é tudo. Hoje fatura 60% do valor e paga 40% como custo de analistas. | "Você cobra R$ 120k na perícia e gasta 3 semanas com 2 analistas abrindo pasta. Eu te entrego o grafo estruturado e a timeline navegável em 3 dias úteis por R$ 3k + assinatura. Você mantém o laudo pericial (a parte que justifica o preço). Vamos fechar?" |
| 2 | **Consultoria de Commissioning / Handover Industrial** | Já vende pacote de entrega para EPCs. Maior dor do mundo: lacunas que atrasam Mechanical Completion (MC) e liberam multa diária. Hoje entrega dossiê em PDF morto + Excel. | "Você entrega handover de sistema de refrigeração por R$ 80k. Com white-label eu te entrego a surface navegável, cada ativo com QR, relatório de lacunas automático e exportação de evidência on-demand. O cliente do EPC vê isso e fecha a MC 1 semana antes. Você cobra mais caro por isso." |
| 3 | **Gerenciadora de Obras / Fiscalização de Contrato Público** | Tem contrato de gestão com taxa mensal ou por projeto. Precisa produzir relatórios de medição sustentados por evidência. Hoje junta tudo manualmente. | "Você é gerenciadora do trecho X da ferrovia e tem que entregar relatório de 500 páginas de medição todo mês. Eu automatizo a vinculação de atividade → foto → medição → nota fiscal em 2 dias. Aumenta sua margem e diminui risco de glosa." |

---

### Por que esse tier NÃO é "perdido" agora — matemática concreta

| Item | Valor |
|---|---|
| 1 parceiro Modelo A ativo | R$ 4.997 / mês base |
| + 2 projetos/mês em média (taxa) | + R$ 5.994 / mês |
| **= Receita mensal por parceiro Modelo A** | **R$ 10.991 / mês** |
| **= Anualizada por parceiro Modelo A** | **~R$ 132k / ano** |
| 3 parceiros ativos (meta em 12 meses) | R$ 32.973 / mês recorrente |
| 3 parceiros × 2 projetos/mês cada | Você opera ~6 projetos por mês (ainda dá pra fazer SOZINHO ou com 1 estagiário técnico) |
| Parceiro Modelo B (1 parceiro) | R$ 9.997 / mês fixo, 4 projetos/mês limite |

Além da receita direta:
- **Cada parceiro = canal de venda sem esforço de marketing.** Você não precisa prospectionar EPC; o parceiro já tem o contrato.
- **Cada projeto fechado pelo parceiro = caso de uso real que você pode anonimizar e usar nos pitches Tier 1.**
- **Prova social mais forte do que qualquer depoimento:** "A perícia X, que trabalha com o cliente de óleo e gás do laboratório no gasoduto Y, usa nosso motor white-label."

---

### Dia a dia de operação (o que VOCÊ faz por parceiro)

| Atividade | Frequência | Esforço |
|---|---|---|
| Receber arquivos brutos do parceiro | Por projeto | 15min |
| Rodar CLI + ajustar bindings de ontologia específicos | Por projeto | 2–4h |
| Gerar surface white-label com marca do parceiro | Por projeto | 30min |
| Revisão final (lacunas óbvias, links quebrados) | Por projeto | 1h |
| Enviar pacote final pro parceiro | Por projeto | 15min |
| Reunião de pré-venda com prospect do parceiro | 2x/mês por parceiro | 1h cada |
| Suporte técnico por WhatsApp/email | Contínuo | ~1h/semana |

TOTAL: ~6–8h por projeto. Em 1 dia útil você entrega 1 projeto inteiro. É por isso que o preço de R$ 2.997 POR PROJETO é barato para o parceiro e tem margem >80% pra você.

---

### Matriz de risco do Tier 3 e mitigação

| Risco | Mitigação |
|---|---|
| Parceiro não fecha nenhum projeto nos 3 primeiros meses | Modelo A tem fidelidade de só 3 meses + taxa por projeto. Se ele não usar, ele cancela e você não se prejudica. Não ofereça Modelo B no 1º contrato. |
| Parceiro quer subir valores de escopo abusivamente | Cláusula de fair use clara: até 200 ativos / 500 documentos por projeto. Acima disso, orçamento separado com 20% de desconto (ainda é vantagem pra ambos). |
| Parceiro entrega trabalho de baixa técnica usando sua surface | Você NÃO ASSINA o laudo. A responsabilidade técnica é exclusivamente do parceiro perito/engenheiro. Seu papel é só a estrutura de dados + visualização. Contrato tem cláusula explícita: "InfoBIM/Brasidata é fornecedor de serviço de apoio à análise, não responsável pela conclusão técnica pericial." |
| Parceiro tem acesso a dados sensíveis de clientes finais | NDA bilateral + cláusula de confidencialidade. Você só processa arquivos que o parceiro autoriza. Nenhuma informação de cliente é usada para outros fins. |

---

## Ofertas Adicionais Recorrentes (A La Carte)

Para adicionar em qualquer tier ou vender separado:

| Oferta | Periodicidade | Preço | Público |
|---|---|---|---|
| **Claim Readiness Check** | Mensal | R$ 897 / projeto | "Se houvesse um claim amanhã, qual % das evidências você já teria organizado?" Relatório com score 0–100 e plano de ação de 30 dias |
| **As-built Snapshot Trimestral** | Trimestral | R$ 1.997 / snapshot | Pacote HTML + PDF com estado atual completo das vinculações, pronto para anexar em medição ou relatório de avanço |
| **InfoBIM Access Pass (para donos de ativo)** | Anual | R$ 49.970 / ano | Acesso ilimitado a todas as surfaces HTML de projetos entregues + busca semântica + exportação de pacotes de evidência on-demand |

---

## Matriz de Oferta — Quando Vender o Quê

| Situação do Cliente | Oferta Primária | Oferta Secundária |
|---|---|---|
| Cliente frio, sem gatilho visível, conversa inicial | **Tier 1 — Watch** (R$ 497/mês) | Claim Readiness Check (R$ 897/mês) como add-on |
| Cliente com gatilho ATIVO (claim, handover travado, auditoria) | **Serviço Pontual** (R$ 30k–150k) | **Tier 2 — Manutenção da Malha** (R$ 2.997/mês) no follow-up de 30 dias pós-entrega |
| Boutique de perícia / commissioning / gerenciadora com carteira e escopo ≥R$40k | **Tier 3 — Parceria White-Label** (Modelo A: R$ 4.997/mês + R$ 2.997/projeto) | Modelo B (ilimitado) após 3 meses com pipeline comprovado; ou Modelo C (30% do projeto) sem mensalidade |
| Cliente Tier 1 com gatilho surgindo em 2–3 meses | **Upgrade para Serviço Pontual** | Conceder desconto de 100% dos últimos 3 meses de Watch no valor do serviço |
| Dono de ativo (proprietário) após handover completo | **InfoBIM Access Pass** (R$ 49.970/ano) | As-built Snapshot Trimestral |

---

## Roadmap de Lançamento (90 dias)

### Dias 1–15 — Montar artefatos mínimos
1. 1 página de proposta comercial em PDF para cada tier (não precisa de site. PDF no WhatsApp já resolve)
2. 1 template de relatório mensal do Tier 1 (Watch) — canva ou LaTeX, 1 página só com o que importa
3. 1 script CLI wrapper simples: `infobim watch --project /caminho --output relatorio_mes.pdf`
4. Lista de 30 prospects Tier 1 (BIM managers de EPCs e construtoras grandes) + 10 prospects Tier 3 (consultorias parceiras)

### Dias 16–45 — Validação do Tier 1
- Mandar proposta para os 30 prospects Tier 1
- Meta: **3 clientes pagantes no Tier 1 até dia 45** (nem que seja com 50% de desconto nos 3 primeiros meses pra validar)
- Para cada um, operar manualmente. Anotar tudo que dá trabalho (depois automatiza)

### Dias 46–75 — Vender primeiro serviço pontual + validar Tier 2
- Com os 3 clientes Watch ativos, esperar aparecer uma oportunidade de serviço pontual ou criar uma: *"Olha, no relatório desse mês eu identifiquei 7 lacunas críticas no sistema elétrico que vão te impedir de entregar o handover em outubro. Quer que eu resolva num pacote fechado?"*
- Meta: **1 serviço pontual fechado até dia 75**
- Imediatamente após entrega do pontual: oferta Tier 2. Meta: **1 cliente Tier 2**

### Dias 76–90 — Fechar primeiro parceiro Tier 3 (Modelo A)
- **Alvo**: 1 boutique de perícia de engenharia de Salvador/Bahia ou Rio (região com concentração de O&G, estaleiros, refinarias e clientes do laboratório, onde você já tem rede)
- Ação: usar contato da Brasidata e de clientes de O&G do laboratório para apresentação de 30min. Pitch do dia: "Eu não quero te vender nenhum software. O InfoBIM é open-source e gratuito, qualquer um pode usar. O que eu faço é pegar o serviço de reconstituição que você hoje demora 3 semanas com 2 analistas abrindo pasta, e entrego em 3 dias úteis o pacote de evidências estruturado e a timeline navegável, com a SUA marca no resultado final. A gente testa no primeiro projeto com risco praticamente zero: eu faço de graça 1 pequeno trecho de um caso real seu, você compara com o resultado da sua equipe atual."
- Meta: **1 parceiro Tier 3 Modelo A com contrato assinado até dia 90** (fidelidade de 3 meses, R$ 4.997/mês + R$ 2.997/projeto)
- 1º mês do parceiro: 50% de desconto no valor base (R$ 2.497 em vez de R$ 4.997) para reduzir atrito

### Resultado esperado em 90 dias
- 3 clientes Tier 1 (Watch) → R$ 1.491 / mês
- 1 cliente Tier 2 (Manutenção) → R$ 2.997 / mês
- 1 parceiro Tier 3 Modelo A (contrato base) → R$ 4.997 / mês
- + 1 projeto médio do parceiro Tier 3 no mês → + R$ 2.997 one-shot (fica contínuo nos meses seguintes)
- 1 serviço pontual direto → R$ 40k (receita one-shot, não recorrente)
- **Receita mensal recorrente base em 90 dias: R$ 9.485 / mês**
- **+ projetos do parceiro = ~R$ 12k–R$ 15k / mês efetivo**

Não é riqueza. Mas é recorrente, "deixado lá de exposição", com pipeline de serviços pontuais aquecido por trás. E o Tier 3 já tem fluxo de operação definido sem te obrigar a treinar parceiro em CLI.

---

## Princípios de Operação Não Negociáveis

1. **Nunca automatize antes de repetir 5x.** Se você só tem 3 clientes Watch, não gasta 40 horas buildando dashboard web. Roda CLI, edita template Canva, envia email. O esforço manual é aceitável porque o MRR é de exposição, não de escala.
2. **Todo contato mensal tem que ter 1 insight concreto.** NUNCA envie um relatório genérico "tudo certo". Sempre tem pelo menos 1 coisa: "encontrei 2 versões conflitantes do mesmo desenho — anexei as diferenças". Sem isso, o cliente cancela após 2 meses.
3. **Tier 1 é loss leader / isca.** Margem nele pode ser baixa ou até zero no início. O dinheiro real está na conversão Tier 1 → Serviço Pontual (meta ≥20% em 12 meses) e no Tier 2.
4. **Preço sempre em real, sempre em BRL, sempre com nota fiscal.** Nada de dólar, nada de crypto, nada de "faturamos offshore". Cliente de construção no Brasil compra em BRL com CNPJ.
5. **Todo contrato recorrente tem cláusula de saída em 30 dias sem multa.** Reduz atrito de assinatura. A retenção é por valor entregue, não por contrato amarrado.

---

## Metas de 12 Meses (Indicadores de Saúde)

| Indicador | Meta | Por que importa |
|---|---|---|
| Clientes Tier 1 ativos | ≥ 20 | Exposição e pipeline aquecido |
| Clientes Tier 2 ativos | ≥ 6 | Receita recorrente de verdade, alta margem |
| Parceiros Tier 3 ativos (qualquer modelo) | ≥ 3 | Alavancagem e validação de mercado; cada parceiro = canal sem esforço de marketing |
| Parceiros Tier 3 convertidos para Modelo B (Operação Ilimitada) | ≥ 1 | Prova que o parceiro tem pipeline recorrente suficiente pra valer a pena o pacote |
| Taxa de churn Tier 1 | ≤ 15% ao mês | Se churn >15%, relatório mensal tá genérico demais |
| Taxa de conversão Tier 1 → Serviço Pontual | ≥ 20% em 12 meses | Prova que o Tier 1 tá servindo de isca boa |
| % de projetos Tier 3 entregues em ≤3 dias úteis | ≥ 90% | Entrega no prazo = retenção do parceiro |
| Receita mensal recorrente total | ≥ R$ 45k / mês | R$ 540k/ano recorrente só dos tiers — mais serviços pontuais por cima |
| LTV/CAC Tier 2 | ≥ 5x | Prova que o modelo recorrente é economicamente saudável |

---

## Pitch Final de Uma Frase para Cada Tier

- **Tier 1 (Watch):** *"Por R$ 497/mês eu deixo um monitor rodando no seu projeto que te avisa todo mês quais lacunas de rastreabilidade vão te dar dor de cabeça no handover. Aprovação rápida, sem mudar nada no seu processo."*
- **Tier 2 (Manutenção):** *"Você me pagou R$ 60k pra montar o dossiê. Agora R$ 2.997/mês eu mantenho ele vivo sempre atualizado — se o fiscal pedir amanhã, você entrega em 4 horas."*
- **Tier 3 (Parceria White-Label):** *"Você é perícia e cobra R$ 120k num claim de atraso, gastando 3 semanas com 2 analistas abrindo pasta. Eu opero o InfoBIM por você, entrego a timeline navegável e o pacote de evidências estruturado em 3 dias úteis com a SUA marca no resultado. Assinatura de R$ 4.997/mês + R$ 2.997 por projeto. No primeiro projeto, você economiza ~R$ 28k de mão de obra interna."*
