Vou primeiro tentar acessar os repositórios, porque a regra final do seu prompt depende disso.

# BLOQUEIO DE VERIFICAÇÃO (leia antes do veredito)

Sua REGRA FINAL me obriga a começar por aqui: **não consegui acessar `EliasMPJunior/infobim-wip` (v0.6) nem `EliasMPJunior/ontobdc-wip`.** Não estão indexados nem publicamente legíveis; minha sandbox está sem rede. `infobim.org` e `InfoBIM-Community/infobim-core` também não retornaram conteúdo.

Consequência honesta: **as seções 1, 2 e 3 do formato que você pediu eu não posso entregar como investigação — só como leitura da sua própria descrição.** Vou marcar tudo que vem de você como `[declarado, não verificado]`. Se você subir um zip do repo (ou colar README, `--help` da CLI, lista de comandos, lista de testes, uma view HTML gerada e um exemplo de linkset), eu refaço as seções 1–3 de verdade. Sem isso, a análise abaixo é sobre **a capacidade tal como você a descreve** — o que ainda é suficiente para a pergunta central, porque a pergunta central é sobre mercado, não sobre código.

O que **eu** verifiquei: ConstruCode (números, produto, precificação, história de canal), literatura do *traceability benefit problem*, categoria comercial de "digital thread", dados setoriais brasileiros (CBIC/IBGE). Isso está citado.

---

# VEREDITO PROVISÓRIO

**1.** O InfoBIM não vende hoje porque a capacidade central que ele oferece — reconstruir transversalmente a história de uma entidade a partir de informação que já existe — é **retroativa e episódica**, e o mercado de construção não tem nenhum mecanismo de compra para capacidades retroativas e episódicas. Ele tem mecanismos de compra para *operação recorrente* (GED, CDE, campo, qualidade) e mecanismos de compra para *evento crítico* (perícia, claim, advogado, consultoria). O InfoBIM entrega valor no segundo caso mas está embalado como o primeiro. Não existe assinatura para "quando der problema".

**2.** A literatura confirma o mecanismo, e de forma mais dura do que você formulou. O artigo original de Arkley & Riddle sobre o *traceability benefit problem* diz que a causa da rastreabilidade mal registrada é a falta de benefício direto percebido pelo processo principal de desenvolvimento, e a consequência é informação incompleta, imprecisa e desatualizada. [nih](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8802773/) A revisão de NLP para rastreabilidade acrescenta o dado comercialmente decisivo: na prática o custo de criar e manter links é percebido como excessivamente alto, e as equipes tendem a evitar o overhead a menos que seja exigido por regulação. [ThreadMoat](https://threadmoat.com/es/categories/digital-thread-startups) Ou seja: **rastreabilidade é historicamente comprada por obrigação, não por benefício.** Isso não é clichê de startup — é um resultado replicado em engenharia de requisitos por 20 anos.

**3.** Isso divide o pagador do beneficiário, e a divisão é estrutural na construção. Quem teria que manter a malha (equipe de projeto, coordenação, campo, durante a obra) não é quem colhe (jurídico em claim, cliente/proprietário na operação, seguradora, órgão fiscalizador, equipe de manutenção anos depois). Numa obra com prazo apertado, o time de execução não gasta esforço para melhorar o dia de outra pessoa em 2029. Isso não é falta de educação de mercado; é incentivo.

**4.** Mas há uma assimetria a seu favor que muda tudo — e é a coisa mais importante deste documento. **Se o InfoBIM realmente opera sobre arquivos existentes sem exigir adoção prévia, ele é uma das pouquíssimas ferramentas de rastreabilidade que pode ser vendida *depois* do gatilho.** Aconex, ACC e ConstruCode só sabem o que foi criado dentro delas — se a obra não usou, não há história. Um mecanismo que reconstrói a partir de IFC, PDFs, planilhas e pastas *post hoc* não sofre do problema de cold start que mata o resto da categoria. Isso não é uma feature: é o único caminho comercial claro que eu consigo enxergar aqui, e ele **não é venda de produto — é venda de serviço com margem anômala.**

**5.** Segundo mecanismo, verificável e não-óbvio: **não existe linha orçamentária.** Olhe a estrutura de preços da ConstruCode: planos por empreendimento, com teto de documentos e de pessoas, e módulos com nome de dor conhecida — Docs (GED), Tasks (apontamentos), Field (times de campo), Check (qualidade e vistorias de entrega), [IEEE Xplore](https://ieeexplore.ieee.org/document/1531058/) mais um Enterprise personalizado. Todos os botões são "Quero contratar" levando a formulário de contato: **venda consultiva, sem preço público, sem self-service.** Esse é o formato de compra real do mercado brasileiro. "Malha semântica navegável" não é módulo, não é dor nomeada, não é por empreendimento e não pertence a nenhum centro de custo existente. Sem linha orçamentária, a compra não tem onde acontecer, mesmo com o comprador convencido.

**6.** Terceiro mecanismo: **não existe categoria comercial de "digital thread" na construção.** Ela existe e está madura em manufatura/PLM — os relatórios de 2026 descrevem a migração de fluxos documento-cêntricos para engenharia dado-cêntrica, ligando requisitos, BOM, planos de processo, resultados de teste e registros de qualidade por identificadores consistentes e modelos semânticos, especialmente em indústrias reguladas onde rastreabilidade e auditabilidade afetam compliance, [DemystifyingPLM](https://www.demystifyingplm.com/best-plm-software-2026) e há vendedores explicitamente vendendo grafo de conhecimento de produto. Na construção esse vocabulário está em papers, não em ordens de compra. Compradores compram de categorias; quando não há categoria, o vendedor precisa (a) alugar o nome de outra categoria ou (b) vender resultado, não ferramenta.

**7.** Quarto mecanismo, e é o que pode matar a demo: **a densidade da fonte pode ser insuficiente exatamente no elo mais valioso.** Você pode reconstruir *o quê*, *quando* e *quem assinou* a partir de IFC, revisões e planilhas. Mas *por que foi projetado daquela forma* mora em WhatsApp não arquivado, reunião sem ata e decisão verbal. Se o "por quê" não estiver em nenhum artefato, o InfoBIM devolve um grafo tecnicamente correto e comercialmente morno. Isso é falseável em uma tarde com os arquivos de um cliente real, e é o teste que eu rodaria primeiro.

**8.** Quinto mecanismo, parcialmente verdadeiro e que você deve conceder: **80% da necessidade *cotidiana* já está resolvida dentro dos silos.** A própria ConstruCode lista controle de revisões, controle automático de obsoletos, versionamento automático com histórico completo, logs auditáveis de aprovações, rastreio de cópias impressas com quem imprimiu e qual versão, e histórico completo por unidade, serviço ou empreendimento. [IEEE Xplore](https://ieeexplore.ieee.org/document/1531058/) História *dentro de cada silo* existe e é barata. O que não existe é a costura *entre* silos. Logo: valor alto por evento, frequência baixa por semana — e isso produz baixíssima disposição a pagar antecipadamente, exatamente como você formulou na sua hipótese-exemplo. A conclusão correta não é "melhore o produto"; é "mude a unidade de cobrança do tempo para o evento".

**9.** Sexto: o segmento com a dor mais aguda é o mais fechado a você. EPC, óleo e gás, infraestrutura concedida e data center têm claims de milhões, commissioning e exigência contratual de evidência — e compram por homologação de fornecedor, due diligence de segurança da informação e ciclo de 6–18 meses. Fundador solo com software open source não passa nesse crivo **como fornecedor de software**; passa como **prestador de serviço técnico especializado**, especialmente subcontratado por quem já está homologado. Você está dentro desse mundo hoje via Brasidata/TechnipFMC — esse acesso vale mais do que qualquer campanha de marketing que você pudesse pagar.

**10.** Resumindo o veredito: não é "faltou marketing", não é ontologia, não é CLI. É que **a capacidade é real, o valor é real, e o formato comercial em que ela é comprável não está sendo oferecido.** Há oportunidade comercial real, mas ela é estreita: prática boutique de reconstituição de informação, disparada por evento, precificada por escopo, com o software como vantagem de margem e não como produto vendido. Se você insistir em vender ferramenta recorrente, minha previsão é que não vende.

---

## 1–3. O QUE ELE É, O QUE FAZ, E ONDE ESTÁ O VALOR ECONÔMICO

Não verifiquei o repo. O que segue é `[declarado]` por você, com meu julgamento sobre **onde cada capacidade tem preço**:

| Capacidade `[declarada]` | Vale dinheiro? | Onde |
|---|---|---|
| Reconstruir história de entidade cruzando fontes | **Sim, alto** | Claim, perícia, arbitragem, auditoria, handover |
| Operar sobre arquivos existentes, sem adoção prévia | **Sim — é o diferencial comercial** | Permite venda pós-gatilho, que ninguém mais oferece |
| Relacionar IFC ↔ documentos ↔ evidência de campo | Sim, médio | As-built, commissioning, informação de ativo |
| Relacionar projeto ↔ execução ↔ financeiro | Sim, alto, mas politicamente sensível | Medição, glosa, aditivo |
| Consulta em linguagem natural | Baixo isolado, alto como demo | Vende a reunião, não o contrato |
| Local/offline, sem sistema centralizador | Sim, em O&G/infra/público | Requisito de segurança da informação |
| WorkStreams / 5W2H / threads / annotations | Provavelmente baixo | Compete com o que já existe e é barato |
| RDF/SHACL/ICDD/RO-Crate | Zero para o comprador | Vantagem de custo/margem sua, interna |

O ponto que você pediu em §11: **a riqueza que produz valor econômico é a que reduz o custo de reconstituir o passado.** A riqueza que descreve o presente do projeto compete com produtos maduros e baratos, e ali a sofisticação não é remunerada.

## 4. QUEM JÁ PAGA POR PROBLEMAS PARECIDOS

- **Perícia e claims de engenharia** — consultorias de *delay analysis*/quantum cobram por hora ou por escopo, e a maior parte do orçamento é *reconstruir o que aconteceu a partir de acervo documental*. É literalmente o seu caso de uso, feito hoje por humanos.
- **Gerenciadoras e fiscalização** — vendem controle de evidência como serviço, embutido em taxa de gerenciamento.
- **Consultoria BIM / ISO 19650** — vendem estruturação de informação por empreendimento.
- **PLM/digital thread em manufatura** — a categoria paga por exatamente essa capacidade, com vendedores estabelecidos; prova de que a capacidade tem preço quando tem categoria.
- **CDEs** — pagam por custódia e distribuição, não por reconstituição.

## 5. HIPÓTESES A DESCARTAR

- **Ontologia/SHACL/RDF assustam o cliente** — descartada por ausência de exposição. É mecanismo interno; não interfere numa venda que não aconteceu.
- **Excel/e-mail/WhatsApp são concorrentes** — descartada. São fontes. Ressalva legítima: quando a decisão *só* existe no WhatsApp, ela não é fonte legível, e isso limita o produto (mecanismo 7) — mas isso é problema de densidade, não competição.
- **"Sétimo sistema"** — descartada na forma ingênua. Substituo por algo verificável e menor: mesmo sem centralizar, você precisa de **acesso concedido** às pastas, ao CDE e aos arquivos — e liberação de acervo é um obstáculo de confiança e jurídico, não de TI. É o obstáculo que o experimento 1 abaixo mede.
- **CLI/pip é fatal** — descartada, e por um motivo estrutural: **no modelo de serviço, quem operou a CLI foi você.** O cliente recebe HTML e conclusão. A superfície técnica deixa de ser problema comercial quando o operador é o vendedor.
- **Falta distribuição / falta prova social** — verdadeiras, irrelevantes como explicação. Como novas empresas rompem o ciclo: alugando canal de terceiro (foi exatamente o que a ConstruCode fez — ver §10) ou entregando o primeiro caso como serviço pago sob NDA, que não exige prova social pública.

## 7. GATILHOS, ORDENADOS POR PLAUSIBILIDADE DE COMPRA

1. **Claim / arbitragem / disputa contratual ativa** — frequência baixa por empresa, alta no agregado; custo em milhões; urgência com prazo processual; sente o jurídico e o diretor de contratos; paga o orçamento de litígio (que é grande e não é orçamento de TI); resolvido hoje com estagiário + pasta + perito; nenhum concorrente de software atende; InfoBIM resolve muito; **chance de compra: a mais alta que existe.**
2. **Handover / as-built / commissioning com aceitação travada** — data marcada, dinheiro retido, dor concreta; paga a construtora ou o EPC para liberar recebimento.
3. **Auditoria / fiscalização / obra pública com questionamento de medição** — obrigação regulatória, que é o mecanismo histórico de compra de rastreabilidade.
4. **Troca de equipe / retomada de obra paralisada** — perda de memória organizacional com custo imediato de reaprendizado.
5. **Não conformidade grave / falha em serviço com risco de responsabilização.**
6. **Exigência contratual ISO 19650 imposta pelo cliente** — compra por conformidade, geralmente atendida pela consultoria já contratada.
7. **Integração BIM ↔ campo em regime normal** — aqui o mercado compra ConstruCode/ACC, não você.

## 8. SEGMENTOS, POR ADERÊNCIA

O&G / EPC industrial → infraestrutura e concessões → data center → obra pública sob fiscalização → grandes construtoras em disputa → escritórios de perícia e advocacia de construção (como *canal*, não usuário) → incorporação residencial (aderência baixa: aqui a ConstruCode ganha).

## 9. CONCORRENTES REAIS

Respondendo sua pergunta central: **não encontrei nenhum produto comercial na construção que permita selecionar uma entidade e reconstruir sua história transversalmente entre múltiplas fontes.** O que existe: histórico *dentro* de cada plataforma (ACC, Aconex, Dalux, Revizto, Trimble, Catenda, ConstruCode — todos com audit trail e versionamento robustos, e todos cegos ao que não passou por eles); a categoria *digital thread / knowledge graph* resolvida e vendida em manufatura/PLM; e humanos fazendo o trabalho manualmente em perícia. Substituto real do InfoBIM = **um analista com uma pasta e três semanas.** Esse é o preço que você concorre, e ele é alto — o que é bom.

## 10. CONSTRUCODE — o que realmente aconteceu

Números confirmados: fundada em 2018, aporte anjo inicial de cerca de R$ 200 mil pela rede Anjos do Brasil, primeira investida do núcleo da Bahia; [Negociosbrasil](https://negociosbrasil.com.br/quanto-vale-uma-empresa-de-engenharia/) em 2020 a Vedacit assumiu o controle — com R$ 5 milhões na criação da Vedacit Soluções Tecnológicas, tendo então mais de 500 obras digitalizadas, 100 mil etiquetas acessadas, 50 mil projetos e mais de 50 construtoras; [Thórus Engenharia](https://thorusengenharia.com.br/seu-canteiro-de-obras-digitalizado-conheca-a-construcode/) segunda rodada de R$ 8 milhões com valor de mercado de R$ 45 milhões, depois mais R$ 2,6 milhões, e previsão de ~R$ 4 milhões de faturamento em 2022; [PR Newswire](https://www.prnewswire.com/news-releases/construcode-transforma-a-gestao-das-obras-com-tecnologia-de-alta-performance-na-construcao-civil-867771470.html) mais de 1.400 obras e presença em seis das dez maiores construtoras do ranking INTEC em fev/2022; [PitchBook](https://pitchbook.com/profiles/company/522559-99) hoje mais de 6 mil empreendimentos e mais de 50 mil profissionais, com reposicionamento IA-driven e anúncio de expansão global. [cbinsights](https://www.cbinsights.com/company/construcode/financials) Seus dados estavam corretos.

Os mecanismos reais, sem hindsight bias:

- **O wedge tinha um objeto físico e uma falha com custo visível.** Não era "QR Code é genial". Era: existe uma prancha impressa no canteiro, alguém executa pela revisão errada, e isso custa retrabalho hoje. O produto se prendeu a um artefato que **já tinha dono, já tinha fluxo e já tinha fracasso conhecido.** Simplicidade não foi virtude — foi consequência de ancorar num objeto existente.
- **Eles não resolveram distribuição: alugaram.** Durante a aceleração do Vedacit Labs o volume de vendas aumentou cerca de oito vezes, permitindo os primeiros retornos aos anjos, e depois Diego foi convidado para o time da Vedacit. [Sienge](https://www.sienge.com.br/blog/vedacit-labs-startups-investimentos/) Uma fabricante de 85 anos com faturamento recorde de R$ 542,3 milhões em 2020 [Anfacer](https://www.anfacer.org.br/noticias/como-serao-os-imoveis-do-futuro-construtechs-e-proptechs-crescem-no-brasil-e-dao-a-resposta) emprestou relacionamento com construtoras. **Esse é o fator causal dominante, e é o que "clonar o marketing" não clona.** Copiar o tom de voz deles sem canal equivalente reproduz a parte irrelevante.
- **Expansão modular sobre o mesmo comprador**, do QR Code para GED/CDE/Tasks/Field/Check — cada módulo é uma dor nomeada e um upsell, nunca uma capacidade abstrata.

Sua metáfora do submarino artesanal está certa quanto a *apresentar*. Mas a conclusão que eu tiro é diferente da sua: o aprendizado não é "criar um concorrente pequeno e barato" — é **encontrar seu equivalente de Vedacit Labs.** No seu caso os candidatos são gerenciadoras, escritórios de perícia/advocacia de construção, consultorias BIM, seguradoras de risco de engenharia e integradores homologados em O&G. Competir de frente com a ConstruCode em GED por empreendimento é a única estratégia aqui que eu diria com confiança que falha.

## 11. TAM / SAM / SOM (premissas explícitas, precisão baixa)

Dado publicado: o PIB da construção cresceu 0,5% em 2025, segundo ano consecutivo de alta; [CBIC](https://cbic.org.br/construcao-cresce-29-no-primeiro-trimestre-de-2026/) a construção cresceu 1,7% até o 3º trimestre de 2025 e os investimentos em infraestrutura estimados pela ABDIB alcançaram cerca de R$ 280 bilhões em 2025, com 84% de capital privado. [CBIC](https://cbic.org.br/construcao-civil-cresce-43-em-2024-e-impulsiona-economia-nacional/)

Estimativa **minha**, não publicada: VAB da construção na ordem de R$ 250–300 bi/ano; gasto com software de gestão de obra historicamente na casa de 0,1–0,3% do valor da obra em empresas digitalizadas. Isso põe o **TAM brasileiro de software de gestão/informação de obra em algo como R$ 0,5–1,5 bi/ano** — ordem de grandeza, não número. Sanity check: a ConstruCode, líder de mind share da categoria com presença em 6 das 10 maiores, projetava R$ 4 mi de faturamento em 2022. **Isso é o dado mais importante desta seção inteira:** a categoria em que você pensou competir é pequena. Um líder faz dezenas de milhões, não centenas.

- **SAM** (reconstituição de informação em segmentos com dor contratual — O&G, infra, EPC, público, data center, mais claims): estimo **R$ 50–150 mi/ano**, hoje capturado majoritariamente por consultoria e perícia humana, não por software.
- **SOM realista, fundador solo, 24 meses:** 4 a 12 engajamentos, R$ 40k–150k cada → **R$ 300k–1,5 mi/ano.** Alta margem, sem funcionários, sem VC.

Diga-se com clareza: **o prêmio realista é uma prática boutique de alto valor por hora, não uma empresa de software.** Se esse prêmio não te interessa, essa é uma razão legítima para parar — e é uma decisão sua, não uma conclusão de mercado.

## 12. MODELO COMERCIAL MAIS PLAUSÍVEL

**Primário — serviço de reconstituição de informação disparado por evento, com InfoBIM como infraestrutura interna.** Preço por escopo (R$ 30k–150k), entrega em HTML/relatório navegável + laudo. Você não vende licença, não vende assinatura, não pede adoção, não pede mudança de processo, e não sofre cold start. O open source funciona como prova de competência e gerador de demanda, não como produto.

**Secundário — capacidade subcontratada por canal:** perícia, gerenciadora, consultoria BIM, integrador homologado. Eles têm o gatilho e o contrato; você tem a ferramenta que os torna 5x mais rápidos. Split de receita ou hora técnica.

**Terciário, só depois de 3+ casos pagos — assinatura de manutenção da malha** para o cliente que já sentiu o valor retroativamente. Essa é a única sequência em que a assinatura fica vendável: **primeiro o evento, depois a prevenção.** Nunca o contrário.

**Descartar por ora:** SaaS self-service, freemium, licença enterprise, PLG.

## 13. CRITÉRIOS PARA MATAR COMERCIALMENTE

- Após **12 conversas** com donos de gatilho ativo (jurídico de construtora, perito, gerente de contrato de EPC, gerenciadora), **nenhum** aceita entregar acervo real de um projeto encerrado, nem sob NDA → a dor não é contratável por um terceiro; mate.
- Em **3 acervos reais**, o grafo reconstruído não recupera o *porquê* de nenhuma decisão relevante e nenhum entrevistado consegue nomear uma pergunta que ele não conseguia responder antes → o mecanismo 7 é dominante; mate ou reduza a as-built/handover.
- Após **5 propostas com preço fechado** para gatilhos ativos e reais, **zero PO assinado** e nenhuma objeção de preço (só silêncio) → não é preço, é ausência de dor; mate.
- Se um incumbente lançar reconstituição cross-source de fontes externas → sua janela específica fecha.

## 14. CRITÉRIOS PARA CONTINUAR

- ≥3 dos 12 entregam acervo real espontaneamente na primeira conversa.
- **1 PO assinado** por ≥R$ 30k dentro de 90 dias, disparado por evento real.
- Alguém pergunta "quanto custa fazer isso todo mês" **sem você sugerir** — sinal de que a assinatura existe do outro lado.
- Um canal (perito, gerenciadora, integrador) pede para usar a capacidade num contrato dele.
- Um segundo cliente vem por indicação do primeiro.

## 15. EXPERIMENTOS QUE DISCRIMINAM (três)

1. **Autópsia gratuita, escopo fechado.** Peça a 5 empresas o acervo de **um empreendimento já encerrado ou paralisado** (risco político baixo) e devolva a reconstituição de 10 entidades em uma semana. Discrimina simultaneamente: a dor é real? o acervo é liberável? a densidade da fonte sustenta o "porquê"? Custo: seu tempo. É o experimento com maior valor informacional por real gasto.
2. **Proposta precificada em gatilho vivo.** Encontre 5 situações ativas (claim, handover travado, auditoria) e mande proposta de preço fechado sem nenhum trial. Discrimina "acham interessante" de "compram". A objeção que vier já é o dado.
3. **Teste de canal.** Apresente a 5 peritos/gerenciadoras/advogados de construção como **capacidade subcontratável**, não como software. Discrimina se sua rota é venda direta ou alavancagem de canal — a variável em que a ConstruCode foi decidida.

Nada disso exige marca, site, funil ou CNPJ novo. Todos os três cabem em 60 dias.

## 16. RESPOSTA FINAL EM UMA FRASE

> **"Hoje, o InfoBIM não vende principalmente porque sua capacidade mais valiosa é retroativa e episódica — não existe categoria de compra nem linha orçamentária para ela no fluxo normal da obra, e o único formato em que ela é comprável (serviço especializado disparado por um evento contratual, com o software como vantagem de margem interna) ainda não está sendo oferecido a ninguém."**

Duas ressalvas de honestidade: essa frase é sobre o mercado, e o mercado eu investiguei. A parte que eu **não** verifiquei é se o InfoBIM, rodando sobre um acervo real e sujo de obra brasileira, entrega a reconstituição que você descreve — e essa é a variável que decide se a frase acima é um problema de embalagem (solúvel) ou de substância (não solúvel). O experimento 1 responde isso em uma semana, e é o único que eu rodaria antes de qualquer outra coisa.

Se você subir o repo, eu volto e faço as seções 1–3 como investigação de verdade.