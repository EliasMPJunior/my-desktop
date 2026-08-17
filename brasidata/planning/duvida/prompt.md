Quero que você faça uma investigação séria, profunda e baseada em evidências para responder a uma pergunta central:

Por que o InfoBIM, com as capacidades que já possui hoje, não apresenta um mecanismo comercial claro de venda?

Não quero uma resposta genérica sobre startups, SaaS, marketing, product-market fit ou adoção tecnológica. Quero que você investigue o InfoBIM real, o mercado real de construção e as alternativas reais existentes.

A condição inicial deve ser tratada desta forma:

«Se ninguém fizer nada, o InfoBIM não vende.
Portanto, se não conseguimos explicar concretamente quem compra, por quê, em qual circunstância, por quanto, como chega até ele e o que dispara a compra, então comercialmente o estado atual é "não vende".»

Não quero que você tente suavizar isso dizendo coisas como "ainda não provamos que não vende". Isso é irrelevante para a pergunta prática.

---

1. PRIMEIRO: ENTENDA O INFOBIM REAL

Antes de analisar mercado, marketing, concorrentes ou possíveis compradores, examine diretamente os repositórios atuais do projeto.

Use principalmente:

- "EliasMPJunior/infobim-wip"
- branch atual relevante, especialmente "v0.6"
- "EliasMPJunior/ontobdc-wip"
- documentação, README, código ativo, comandos, ontologias, capabilities, views, exemplos e testes

Não analise o InfoBIM com base em memória, descrição genérica ou analogia com SaaS/CDE.

Algumas características já conhecidas que você deve CONFIRMAR no repositório

O InfoBIM não deve ser tratado como um repositório central no qual os objetos "vivem".

Ele trabalha sobre informação existente.

A documentação atual afirma explicitamente que ele transforma informação comum de projeto em uma malha semântica executável enquanto mantém arquivos nos formatos e ambientes onde já estão.

Ele pode trabalhar com coisas como:

- IFC;
- PDF;
- planilhas;
- documentos;
- imagens;
- datasets;
- informação relacionada por OntoBDC;
- WorkStreams;
- threads;
- annotations;
- links entre entidades;
- contextos;
- informação de projeto;
- informação de execução.

Confirme o que está realmente implementado hoje.

Não diga "se o InfoBIM consegue ingerir X" quando isso puder ser verificado diretamente.

---

2. ENTENDA A CAPACIDADE DE RASTREABILIDADE

Uma das capacidades que considero particularmente importantes é a possibilidade de reconstruir o contexto/história de algo da construção.

Exemplo conceitual:

Tenho um perfil metálico instalado.

Quero poder chegar a esse perfil e encontrar, conforme os dados existentes no projeto:

- quem projetou;
- de qual projeto veio;
- por que foi projetado daquela forma;
- comentários e discussões;
- threads relacionadas;
- decisões;
- documentos;
- desenhos;
- elemento IFC;
- alterações;
- responsável;
- fornecedor;
- pedido;
- nota fiscal;
- evidências da execução;
- fotos;
- datas;
- atividades relacionadas;
- cronograma;
- demais registros relevantes.

Não assuma que exatamente todos esses itens estão implementados agora.

INVESTIGUE o que já existe e diferencie claramente:

- já implementado;
- parcialmente implementado;
- arquiteturalmente suportado;
- ainda planejado.

O ponto importante é entender a natureza da ferramenta:

«informação heterogênea relacionada e navegável por contexto, sem exigir que tudo seja criado dentro de uma única aplicação.»

---

3. NÃO REPITA ESTES ERROS DE ANÁLISE

Durante uma discussão anterior surgiram várias hipóteses ruins. Não quero que sejam recicladas sem evidência.

Não diga que o problema é "ontologia"

Não faça uma longa dissertação dizendo:

- "o cliente não entende ontologia";
- "semântica assusta";
- "runtime é técnico";
- "ninguém quer ouvir falar de SHACL";
- "precisa esconder a ontologia".

O InfoBIM não está atualmente sendo amplamente anunciado ao mercado usando essas palavras.

Portanto isso seria criticar campanhas publicitárias imaginárias.

Ontologia, RDF, SHACL, OntoBDC etc. podem ser mecanismos internos da solução. Só discuta sua influência comercial se houver evidência concreta de que estão interferindo na venda.

Não trate e-mail, Excel, PDF ou WhatsApp automaticamente como concorrentes

O InfoBIM pode justamente relacionar informação proveniente de ferramentas e formatos já existentes.

Se o usuário continua usando Excel, PDF, e-mail, WhatsApp ou IFC, isso pode ser perfeitamente compatível com o InfoBIM.

Portanto não escreva coisas como:

«"O concorrente do InfoBIM é e-mail + Excel + WhatsApp."»

sem demonstrar por que seria verdade.

Eles podem ser fontes de informação, não substitutos.

Não trate o InfoBIM como "mais um sistema"

Não use automaticamente o argumento:

«"A empresa já tem seis sistemas e não quer instalar o sétimo."»

Primeiro verifique como o InfoBIM funciona.

Ele não é simplesmente outro sistema vertical centralizador.

Não diga que "os objetos vivem no InfoBIM"

Isso está conceitualmente errado.

Não invente problema de interface

O fato de existir CLI ou instalação por "pip" não demonstra, sozinho, que o produto seja comercialmente inviável ou inutilizável.

Não diga automaticamente:

«"A superfície é técnica demais."»

Só faça essa afirmação se você conseguir mostrar concretamente que a experiência atual impede ou prejudica um workflow comercial importante.

Lembre-se de que o InfoBIM também gera superfícies HTML, visualizações, arquivos e outros artefatos consumíveis sem o usuário necessariamente operar diretamente a CLI.

Não transforme "não tem distribuição" em grande descoberta

Atualmente a divulgação comercial brasileira do InfoBIM praticamente não aconteceu.

As apresentações realizadas foram poucas, incluindo apresentações para a Tylko Advisors, da Polônia.

Portanto escrever:

«"Pouca gente conhece porque houve pouca divulgação."»

é verdade, mas é Capitão Óbvio.

Isso não responde à pergunta central.

Não use "falta de prova social" como explicação final

Toda empresa começa sem clientes.

Dizer:

«"Não vende porque não tem clientes; não tem clientes porque não vende."»

é apenas o problema do ovo e da galinha.

Se prova social for relevante, explique COMO empresas novas rompem esse ciclo e se isso é aplicável aqui.

Não diga simplesmente "falta prova econômica"

Frases como:

«"Você precisa mostrar que algo levava 90 minutos e agora leva 20 segundos."»

não são automaticamente uma análise.

Pode ser verdade em determinado caso, mas demonstre por que esse seria um mecanismo comercial relevante para este produto e este mercado.

Não invente "aquisição empresarial autônoma"

Nunca foi estabelecido que o InfoBIM precise ser vendido como SaaS self-service.

Não suponha:

- self-service;
- PLG;
- assinatura online;
- trial;
- checkout;
- aquisição autônoma;
- venture capital;
- crescimento exponencial;
- modelo SaaS.

Descubra qual modelo comercial faria sentido em vez de impor um.

---

4. CONTEXTO DA CONSTRUCODE

Um amigo sugeriu que eu apresentasse o InfoBIM para a ConstruCode.

Minha avaliação é que isso provavelmente seria ignorado e que não existe motivo relevante para abordá-los hoje.

A metáfora utilizada foi:

«apresentar o InfoBIM para a ConstruCode seria como alguém com um submarino artesanal indo apresentá-lo à Marinha.»

A ideia que surgiu depois foi outra:

«em vez de falar com a ConstruCode, estudar a ConstruCode e usar seu marketing e sua trajetória como referência para criar um concorrente pequeno, barato e inicialmente muito menor.»

Não quero copiar marca, identidade visual ou propriedade intelectual deles.

"Clonar marketing" significa estudar e adaptar:

- posicionamento;
- linguagem;
- aquisição;
- canais;
- ofertas;
- estrutura comercial;
- conteúdo;
- crescimento;
- mecanismo de entrada;
- evolução da oferta;
- abordagem ao mercado brasileiro.

---

5. DADOS JÁ LEVANTADOS SOBRE A CONSTRUCODE

Confirme e atualize estes dados.

A ConstruCode:

- foi fundada em 2018;
- aparece publicamente como empresa de aproximadamente 11–50 funcionários;
- LinkedIn mostrava cerca de 32 pessoas vinculadas;
- recebeu investimento inicial;
- houve rodada reportada de cerca de R$ 8 milhões;
- foi reportado valuation de aproximadamente R$ 45 milhões em 2022;
- houve outra captação reportada de cerca de R$ 2,6 milhões;
- havia previsão de aproximadamente R$ 4 milhões de faturamento em 2022;
- a Vedacit adquiriu/assumiu controle da empresa em 2020;
- em 2020 havia algo como 50 construtoras e 500 obras digitalizadas;
- hoje a comunicação pública fala em milhares de empreendimentos e dezenas de milhares de profissionais/usuários;
- o produto começou com algo relativamente simples: QR Code no canteiro levando ao projeto correto/atualizado;
- posteriormente expandiu para gestão documental, BIM, tarefas, field, qualidade, RDO, vistorias etc.

Isso é importante porque eu conheci a ConstruCode aproximadamente no final de 2019 ou início de 2020.

Na época, eu e meu então sócio achamos a ideia do QR Code apontando para projeto bastante simples e pouco impressionante.

Anos depois, a empresa cresceu significativamente.

Não faça hindsight bias.

Não diga:

«"Eles eram gênios porque começaram simples."»

Se eu tivesse apresentado a mesma ideia em 2019, provavelmente muita gente teria dito que era simples demais.

A pergunta interessante é:

«Quais mecanismos permitiram que uma ideia tecnicamente simples se transformasse em uma empresa relevante?»

---

6. MERCADO

Levante dados atuais e confiáveis sobre:

- tamanho do setor de construção no Brasil;
- número de empresas;
- maturidade digital;
- adoção BIM;
- gastos com software;
- mercado de construction technology;
- construction management software;
- BIM software;
- CDE;
- project controls;
- field management;
- information management;
- document management;
- digital thread;
- handover;
- asset information;
- claims;
- quality;
- traceability.

Quero TAM, SAM e SOM quando for possível construir estimativas razoáveis.

Mas:

- não invente precisão;
- mostre premissas;
- diferencie dado publicado de estimativa própria.

Quero especialmente entender:

«qual parte desse mercado poderia economicamente se interessar pelas capacidades atuais do InfoBIM?»

---

7. CONCORRENTES E ALTERNATIVAS

Analise pelo menos:

- ConstruCode;
- Procore;
- Autodesk Construction Cloud;
- Dalux;
- Revizto;
- Trimble Connect;
- Bentley;
- Oracle Aconex;
- Catenda;

e procure outras empresas relevantes, especialmente:

- Brasil;
- América Latina;
- ferramentas menores;
- startups;
- openBIM;
- rastreabilidade;
- digital thread;
- knowledge graph aplicado à construção;
- semantic BIM;
- project information graph;
- handover;
- claims;
- evidence management;
- construction intelligence.

Não faça apenas tabela de features.

A pergunta principal é:

«Existe atualmente alguma solução que permita selecionar uma entidade, elemento, atividade ou assunto e reconstruir transversalmente sua história/contexto através de múltiplas fontes de informação?»

Se sim:

- quem;
- como faz;
- quanto cobra;
- para quem vende;
- qual benefício anuncia;
- em qual categoria comercial se posiciona.

Se não houver equivalente claro, diga isso.

---

8. A PERGUNTA MAIS IMPORTANTE

Quero que você tente explicar causalmente:

Por que capacidades como estas não gerariam compra?

Exemplos:

- relacionar informação heterogênea;
- rastrear história de uma entidade;
- recuperar decisões;
- navegar contexto;
- relacionar IFC com documentos;
- relacionar atividade com evidências;
- relacionar projeto, execução e informação financeira;
- consulta em linguagem natural;
- visualizar informação contextualizada;
- manter fontes originais em seus ambientes;
- trabalhar offline/local quando aplicável;
- evitar dependência de um sistema centralizador.

Não responda apenas:

- ninguém conhece;
- não tem marketing;
- não tem clientes;
- não tem distribuição;
- falta prova social;
- é novo;
- é técnico;
- precisa de UX;
- precisa de PMF.

Essas podem ser condições verdadeiras, mas não são a explicação que estou procurando.

Quero mecanismos do tipo:

«"A capacidade possui alto valor eventual, mas baixa frequência percebida; por isso existe baixa disposição de pagamento antecipado."»

Isso é uma hipótese causal.

Outro exemplo:

«"O benefício é capturado por um departamento diferente daquele que teria de pagar."»

Também é uma hipótese causal, mas precisa de evidência.

Outro:

«"O valor só surge depois de acumular determinada densidade de informação, gerando um cold-start operacional."»

Também é causal, se for verdadeiro.

Outro:

«"O mercado resolve 80% da necessidade com ferramentas existentes por custo marginal quase zero."»

Também é causal.

Quero descobrir QUAIS mecanismos realmente se aplicam ao InfoBIM.

---

9. INVESTIGUE O "TRACEABILITY BENEFIT PROBLEM"

Foi encontrada uma pista interessante chamada "traceability benefit problem".

A ideia geral é que quem precisa criar/manter rastreabilidade pode perceber pouco benefício imediato durante o trabalho normal, enquanto o valor aparece fortemente quando surge necessidade de:

- auditoria;
- investigação;
- mudança;
- disputa;
- claim;
- responsabilização;
- commissioning;
- handover;
- falha;
- não conformidade;
- manutenção.

Também foi encontrado material do Construction Industry Institute relacionado a tracking/tracing e digital information threads indicando que algumas organizações têm dificuldade de enxergar ROI antes da adoção, enquanto organizações com experiência relatam benefícios maiores.

Investigue isso profundamente.

Pergunte:

- isso realmente se aplica às capacidades do InfoBIM?
- em quais situações?
- qual a frequência dessas situações?
- quem sofre economicamente?
- quanto custa hoje não ter rastreabilidade?
- existem setores da construção onde isso é mais crítico?
- fiscalização?
- infraestrutura?
- EPC?
- óleo e gás?
- data centers?
- indústria?
- edificações?
- commissioning?
- claims?
- quality assurance?
- handover?

Não assuma que essa é a resposta. Teste-a.

---

10. INVESTIGUE POSSÍVEIS GATILHOS REAIS DE COMPRA

Quero descobrir situações concretas nas quais alguém pensaria:

«"Preciso disso agora."»

Por exemplo:

- disputa contratual;
- claim;
- investigação de atraso;
- não conformidade;
- falha de execução;
- auditoria;
- handover;
- commissioning;
- fiscalização;
- rastreamento de material;
- investigação de responsabilidade;
- troca de equipe;
- projeto longo;
- perda de memória organizacional;
- integração entre projetista e obra;
- integração de BIM e campo;
- entrega de as-built;
- operação/manutenção;
- compliance;
- ISO 19650;
- requisitos contratuais;
- controle de evidências.

Para cada gatilho:

1. frequência;
2. custo;
3. urgência;
4. quem sente;
5. quem decide;
6. quem paga;
7. como resolve hoje;
8. qual concorrente atende;
9. o quanto InfoBIM poderia resolver;
10. chance de compra.

---

11. NÃO CONFUNDA RIQUEZA COM COMPLEXIDADE

Uma das minhas percepções é que o InfoBIM possui uma proposta funcional rica.

Isso não significa necessariamente que seja comercialmente bom.

Mas não quero que você caia no erro de:

«"é rico/sofisticado, portanto precisa ser simplificado."»

Nem no inverso:

«"é sofisticado, portanto é superior."»

Quero saber:

«qual parte dessa riqueza produz valor econômico?»

---

12. MODELOS COMERCIAIS POSSÍVEIS

Não assuma SaaS.

Analise possibilidades como:

- open source + serviços;
- consultoria;
- implantação;
- licença;
- assinatura;
- por projeto;
- por empreendimento;
- por empresa;
- freemium;
- enterprise;
- suporte;
- treinamento;
- integração;
- managed service;
- auditoria;
- solução embarcada em serviço BIM;
- produto gratuito como gerador de demanda para serviços;
- produto como infraestrutura de outro serviço;
- parceria com consultorias;
- uso em fiscalização;
- uso em commissioning;
- uso em claims;
- uso em informação de ativos.

Quero saber qual modelo combina melhor com as capacidades e estágio atual.

---

13. MINHA SITUAÇÃO REAL

Isso importa porque não estou tentando construir uma startup financiada por VC.

Sou engenheiro civil, engenheiro de software e especialista em BIM.

O InfoBIM é essencialmente um projeto autoral/open source.

Tenho capacidade técnica alta, mas recursos financeiros e comerciais limitados.

Não tenho equipe grande de vendas ou marketing.

Não quero montar uma empresa de 100 funcionários antes de descobrir se alguém paga.

Portanto procure estratégias compatíveis com:

- fundador solo ou equipe mínima;
- orçamento muito pequeno;
- mercado brasileiro;
- capacidade de prestar serviços;
- autoridade técnica;
- possibilidade de demonstrar tecnologia;
- software open source.

---

14. UMA COISA MUITO IMPORTANTE: NÃO PARTA DA CONCLUSÃO DE QUE O INFOBIM VAI DAR CERTO

Pode ser que a resposta correta seja:

«"essas funcionalidades são tecnicamente interessantes, mas não possuem valor comercial suficiente."»

Se as evidências apontarem para isso, diga.

Pode ser:

«"o problema existe, mas compradores não pagam por prevenção."»

Diga.

Pode ser:

«"só existe mercado em nichos muito específicos."»

Diga.

Pode ser:

«"o mercado quer exatamente isso, mas compra dentro de produtos maiores."»

Diga.

Pode ser:

«"há oportunidade comercial real."»

Diga.

Quero resposta, não motivação.

---

15. TAMBÉM NÃO PARTA DA CONCLUSÃO DE QUE VAI DAR ERRADO

Não procure evidências apenas para enterrar o projeto.

A investigação precisa ser simétrica.

---

16. FORMATO FINAL DA RESPOSTA

Quero uma resposta longa e substancial.

Comece com:

VEREDITO PROVISÓRIO

Em 5–10 parágrafos, responda diretamente:

«Por que o InfoBIM não vende hoje?»

Depois:

1. O QUE O INFOBIM REALMENTE É

Baseado no repositório.

2. O QUE ELE REALMENTE FAZ HOJE

Separando implementado, parcial e planejado.

3. QUAL VALOR ECONÔMICO CADA CAPACIDADE PODE GERAR

Não apenas funcionalidade.

4. QUEM JÁ PAGA POR PROBLEMAS SEMELHANTES

Empresas, produtos e categorias.

5. POR QUE ESSE VALOR PODE NÃO VIRAR COMPRA

Somente mecanismos causais bem fundamentados.

6. QUAIS HIPÓTESES ANTERIORES DEVEM SER DESCARTADAS

Incluindo as hipóteses genéricas ruins descritas neste prompt.

7. GATILHOS DE COMPRA

Ordenados por plausibilidade.

8. SEGMENTOS DE MERCADO

Ordenados por aderência.

9. CONCORRENTES E SUBSTITUTOS REAIS

Sem chamar automaticamente Excel/e-mail de concorrentes.

10. CONSTRUCODE

Explique seu crescimento, seu wedge inicial, seu marketing e o que realmente pode ser aprendido.

11. TAM / SAM / SOM

Com números, premissas e incerteza.

12. MODELO COMERCIAL MAIS PLAUSÍVEL PARA O INFOBIM

Incluindo alternativas não-SaaS.

13. O QUE FARIA EU MATAR COMERCIALMENTE O PROJETO

Defina critérios objetivos.

Exemplo:

«"Se após X entrevistas/demo para empresas com característica Y ninguém demonstrar Z, a hipótese comercial fica enfraquecida."»

14. O QUE FARIA EU CONTINUAR

Também com critérios objetivos.

15. EXPERIMENTOS DE MERCADO

Poucos, baratos e capazes de produzir informação real.

Não quero uma lista de 47 tarefas de marketing.

Quero os experimentos que realmente discriminem entre as hipóteses.

16. RESPOSTA FINAL EM UMA FRASE

Termine completando:

«"Hoje, o InfoBIM não vende principalmente porque __________________________."»

Se a evidência não permitir completar essa frase com segurança, diga:

«"Ainda não há evidência suficiente para identificar a causa principal; as hipóteses mais fortes são A, B e C, e o experimento X distingue entre elas."»

Isso é preferível a inventar certeza.

---

REGRA FINAL

Toda vez que você escrever alguma afirmação sobre o InfoBIM, pergunte:

«"Eu verifiquei isso no InfoBIM ou estou imaginando?"»

Toda vez que escrever algo sobre o mercado:

«"Tenho evidência ou estou repetindo clichê de startup?"»

Toda vez que escrever uma causa:

«"Isso realmente explica o fenômeno, ou é só uma forma mais elegante de dizer que ele não vende?"»

Não quero consultoria genérica.

Quero uma investigação quase forense sobre por que uma ferramenta que parece possuir capacidades incomuns e potencialmente valiosas não possui hoje um mecanismo comercial claro de venda.