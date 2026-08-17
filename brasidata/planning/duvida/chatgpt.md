Worked for 10s

Você tem razão. O erro foi meu: o sistema me apresentou uma resposta anterior como se ela tivesse sido entregue, mas ela não apareceu para você. A única resposta que você recebeu foi a minha alegação incorreta de duplicidade. Segue agora a resposta completa.

VEREDITO PROVISÓRIO

O InfoBIM não vende hoje porque sua unidade tecnicamente demonstrável ainda não coincide com uma unidade econômica que alguém reconheça, orce e contrate. O código atual possui componentes reais e incomuns: projetos representados sobre datasets existentes, preservação dos arquivos originais, navegação de entidades IFC, parâmetros semânticos, linksets, contextos, WorkStreams, annotations e superfícies HTML offline. Mas a promessa comercial mais poderosa — selecionar um elemento, atividade ou assunto e reconstruir transversalmente sua história — ainda não aparece como um workflow completo, repetível e contratável na versão ativa.

O exemplo do perfil metálico é o teste decisivo. Hoje é possível localizar o elemento IFC pelo GlobalId, inspecionar propriedades e identificar datasets relacionados. O runtime OntoBDC fornece mecanismos genéricos para representar documentos, anotações, relações e contextos. Mas não encontrei na branch v0.6 uma experiência ativa que, partindo desse perfil, reúna automaticamente projeto, justificativas, threads, decisões, fornecedor, pedido, nota fiscal, atividade, fotografia, inspeção e alterações. Existem os blocos necessários em graus diferentes; ainda não existe o “dossiê do perfil” como uma entrega integrada.

Isso produz o primeiro mecanismo causal: o principal valor econômico imaginável do InfoBIM ainda resulta da combinação futura ou manual de componentes, e não de um resultado pronto que o comprador possa encomendar. Um responsável por commissioning não compra “linksets”; compra um pacote de evidências demonstrando que um sistema foi instalado, testado e aceito. Um gerente de contratos não compra “contexto semântico”; compra uma cronologia defensável de uma mudança. Um fiscal não compra “uma malha executável”; compra evidência rastreável de medição, execução e responsabilidade.

Mesmo com esse workflow completo, existiria um segundo problema: o valor da rastreabilidade é frequentemente posterior e distribuído. Alguém precisa identificar entidades, preservar versões e criar ou validar relações durante o trabalho normal; o benefício maior pode aparecer meses depois, para outra área, durante commissioning, auditoria, falha ou disputa. O Construction Industry Institute encontrou exatamente essa barreira em tracking e tracing de materiais: dificuldade de prever ROI, investimento inicial e necessidade de alinhar processos, apesar de organizações experientes relatarem retornos múltiplos quando a implementação é adequada. O CII também aponta o proprietário como patrocinador importante. Isso é evidência de um mecanismo aplicável ao InfoBIM — não prova direta sobre o produto. CII RT-384

O terceiro mecanismo é um cold start de densidade informacional. Uma relação entre um IFC e um PDF possui algum valor; uma rede suficientemente completa entre elemento, versão, atividade, fornecedor, teste, fotografia, decisão e responsável possui valor muito maior. Antes de essa densidade existir, a experiência pode parecer apenas uma busca mais sofisticada. Para chegar à densidade, alguém precisa configurar identificadores, proveniência, importações, regras e responsabilidades. O comprador encontra custo certo agora e benefício incerto ou posterior.

O quarto mecanismo é que o mercado já compra parcelas desse valor dentro de categorias maiores. Aconex vende um registro contratual auditável; Procore, Autodesk e ConstruCode ligam documentos, modelos, issues, campo e qualidade; Dalux liga objetos, fotos e histórico; Thinkproject vende contratos e handover; Catenda vende CDE openBIM e trilhas auditáveis. Isso não significa que sejam equivalentes ao InfoBIM. Significa que, para muitos compradores, grande parte da necessidade percebida já vem associada a um produto contratado para um workflow mais frequente. O InfoBIM teria de resolver a parcela transversal que permanece fragmentada, por um custo inferior ao trabalho de integração e manutenção da malha.

O quinto mecanismo é probatório. Manter as fontes nos ambientes originais é uma vantagem de interoperabilidade, soberania e implantação incremental. Porém, uma trilha usada em claims, auditoria ou fiscalização precisa demonstrar identidade, versão, timestamp, cadeia de custódia e resistência a alterações. Sistemas centralizados como o Aconex vendem explicitamente o fato de que decisões e comunicações são registradas prospectivamente e não podem ser apagadas ou alteradas. Uma camada federada pode ser mais aberta, mas precisa demonstrar que seus links continuam defensáveis quando o arquivo externo muda, desaparece ou perde permissão.

Portanto, o estado comercial é corretamente descrito como “não vende”. Não porque ontologia assuste, porque existe uma CLI ou porque ninguém conhece. Ele não vende porque ainda não há uma correspondência explícita entre gatilho urgente, comprador com orçamento, entrega end-to-end, custo aceitável de implantação, garantia de evidência e preço. Existe uma oportunidade plausível, mas provavelmente concentrada em nichos de alta consequência — commissioning, handover, claims, qualidade e ativos industriais — e inicialmente como serviço assistido, não como plataforma horizontal genérica.

1. O QUE O INFOBIM REALMENTE É

A principal referência analisada foi a branch v0.6 de EliasMPJunior/infobim-wip, complementada pelo repositório EliasMPJunior/ontobdc-wip.

O InfoBIM atual é uma camada BIM específica construída sobre o runtime genérico OntoBDC. A documentação o descreve como uma camada “thin, domain-specific” e atribui ao OntoBDC os mecanismos de contêiner, datasets, linksets, anotações, WorkStreams, páginas de assunto e superfícies HTML. README do InfoBIM v0.6

Ele não é um repositório central onde os objetos “vivem”. Um projeto é representado por uma estrutura contendo:

um dataset reservado para IfcProject;

um ou mais datasets com payloads IFC;

documentos complementares;

metadados, facades, bindings e linksets;

artefatos do OntoBDC em .__ontobdc__.


Os datasets permanecem fontes de verdade. O InfoBIM resolve entidades, classes e propriedades sobre esses datasets. No OntoBDC, PDFs, planilhas, imagens e documentos podem ser preservados como arquivos originais, acompanhados por metadados e facades. README do OntoBDC

Isso confirma a formulação central: o InfoBIM trabalha sobre informação existente e procura transformá-la em uma malha executável, sem exigir que toda informação seja criada dentro de uma aplicação única.

Mas quatro níveis precisam ser separados:

1. preservar um arquivo como dataset;


2. representar metadados ou entidades desse arquivo;


3. criar relações entre essas entidades;


4. reconstruir automaticamente uma história transversal.



Os três primeiros possuem suporte concreto em diferentes graus. O quarto ainda não constitui uma experiência completa na v0.6.

2. O QUE ELE REALMENTE FAZ HOJE

Implementado e testado na versão ativa

Capacidade	Situação verificada

Criar, listar, anexar, atualizar e excluir projetos	Implementado
Resolver projeto por IfcProject GlobalId, nome, caminho ou diretório atual	Implementado
Trabalhar com múltiplos datasets IFC no mesmo projeto	Implementado
Listar classes IFC e quantidades, deduplicando datasets	Implementado
Listar instâncias de determinada classe IFC	Implementado
Obter elemento por GlobalId em múltiplos datasets	Implementado
Ler propriedades e datasets associados ao elemento	Implementado
Definir ou remover parâmetro semântico em uma ocorrência ou em todas	Implementado
Aplicar parâmetros sobre XLSX sem pressupor que a instância seja IFC	Implementado e testado
Criar e consultar entidades de contexto	Implementado
Criar IfcWorkSchedule	Implementado
Gerar XLSX com IfcWorkSchedule, IfcTask e IfcTaskTime	Implementado
Gerar superfície HTML estática/offline	Implementado
Views de projeto, catálogo IFC, elementos, propriedades e WorkSchedule	Implementado


Referências diretas incluem o adaptador de catálogo IFC, os testes de parâmetros, os testes de cronograma e o tile HTML de navegação IFC.

Parcialmente implementado

Capacidade	O que existe	O que falta para a promessa comercial

Informação heterogênea	OntoBDC preserva e representa PDF, JPG, XLSX, DOCX e outros datasets	Extração e integração específica não estão completas para todas as fontes
Links entre entidades	Linksets baseados em ISO 21597/DirectedBinaryLink	Produção automática ou assistida de relações suficientemente densas
Anotações	Runtime possui Note, Issue, Classification, Location e Record	Experiência ativa no InfoBIM ligando anotações a qualquer elemento ou atividade
WorkStreams	Runtime possui Related, Suggested e Found, com persistência e auditoria	Workflow BIM completo ligando elemento, evidência, decisão e responsável
Contexto de elemento	Elemento IFC pode ser encontrado e suas propriedades exibidas	História envolvendo documentos, conversas, compras, execução e alterações
Cronograma	WorkSchedule, Task e TaskTime	Integração operacional com cronogramas reais e evidências de avanço
Operação local/offline	Contêiner e HTML estático	Atualização e governança multiempresa
Proveniência	Datasets, metadados e linksets	Cadeia de custódia demonstrada para claims e auditoria


Arquiteturalmente suportado pelo OntoBDC

Subject Page com espaço, tempo e pessoas;

WorkStreams;

annotations;

linksets portáveis;

contêineres ICDD/ISO 21597;

facades sobre arquivos heterogêneos;

empacotamento local;

sugestão de recursos relacionados;

relações entre entidades de domínios diferentes.


Essas capacidades existem no substrato. Não é correto afirmar que a versão ativa do InfoBIM já as combina automaticamente em uma história completa de construção.

Planejado, legado ou não encontrado como capacidade ativa

consulta geral em linguagem natural sobre o projeto;

reconstrução automática da história completa de qualquer elemento;

integração pronta com e-mail ou WhatsApp;

ligação pronta entre IFC, fornecedor, pedido e nota fiscal;

linha do tempo completa de mudanças de um elemento;

ingestão semântica automática de todos os formatos citados;

pacote de evidências pronto para claims;

handover operacional completo por ativo.


O CHANGELOG mostra que a geração atual resultou de uma reconstrução seletiva. Recursos anteriores foram preservados em src/old, mas não estão ativos nem são descobertos pelo runtime atual.

O teste do perfil metálico

Hoje, o caminho comprovado é:

flowchart TD
    A["Selecionar GlobalId"] --> B["Encontrar elemento IFC"]
    B --> C["Ver propriedades"]
    B --> D["Identificar datasets"]
    D --> E["Navegar linksets e contextos"]
    E --> F["Reconstruir dossiê transversal"]

A–D estão implementados. E possui suporte parcial. F ainda não existe como workflow end-to-end.

3. QUAL VALOR ECONÔMICO CADA CAPACIDADE PODE GERAR

Capacidade	Valor econômico potencial	Condição necessária	Estado

Relacionar informação heterogênea	Menos procura, reconciliação e duplicação	Identificadores estáveis e relações atualizadas	Parcial
Rastrear história de uma entidade	Investigação, auditoria, causa-raiz, claims e manutenção mais rápidos	História temporal completa e defensável	Parcial
Recuperar decisões	Responsabilização e menor ambiguidade contratual	Captura prospectiva ou importação confiável	Integração incompleta
Relacionar IFC e documentos	Dossiê por componente ou sistema	Vínculos elemento–documento confiáveis	Parcial
Relacionar atividade e evidência	Validar avanço, medição e qualidade	Cronograma–campo–evidência integrado	Não end-to-end
Relacionar execução e financeiro	Medição, mudança e responsabilização	ERP, contratos, pedidos e evidências	Não pronto
Navegação contextual	Redução do esforço cognitivo para reunir informação	Contexto suficientemente denso	Parcial
HTML local/offline	Portabilidade, soberania e entrega permanente	Processo de atualização	Implementado tecnicamente
Preservar fontes originais	Menos migração e lock-in	Conectores, permissões e proveniência	Arquitetura favorável
Consulta em linguagem natural	Redução do trabalho de busca	Respostas verificáveis e controle de acesso	Não ativa
Parâmetros semânticos	Consistência, classificação e interoperabilidade	Aplicação a um processo econômico	Implementado


As capacidades com maior potencial econômico não são necessariamente as mais sofisticadas tecnicamente. São aquelas que podem:

reduzir tempo de commissioning;

demonstrar execução e responsabilidade;

preservar conhecimento depois de trocas de equipe;

diminuir o custo de montar um claim;

encontrar lacunas antes de um marco contratual;

entregar informação de ativos utilizável;

comprovar conformidade ou medição.


4. QUEM JÁ PAGA POR PROBLEMAS SEMELHANTES

Há pagamento comprovado, mas distribuído por categorias comerciais.

CDE e gestão documental

ConstruCode, Autodesk Construction Cloud, Procore, Aconex, ProjectWise, Catenda e Dalux vendem:

documentos aprovados;

versionamento;

workflows;

histórico;

distribuição;

auditoria.


Coordenação BIM e issues

Revizto, Autodesk, Dalux, Trimble Connect, Catenda e Aconex ligam:

modelo;

desenho;

issue;

localização;

responsável;

comentário;

resolução.


Field e qualidade

Procore, Dalux, Autodesk e ConstruCode vendem:

inspeções;

fotos;

RDO;

não conformidades;

punch lists;

histórico por serviço, unidade ou empreendimento.


Claims e contratos

Aconex e Thinkproject vendem registro contratual, correspondência, mudanças, obrigações, eventos e evidências. A alternativa é contratar consultores que reconstroem manualmente cronologias usando várias fontes.

Commissioning e handover

Thinkproject, Dalux FM, Autodesk e Aconex organizam:

dados de ativos;

certificados;

inspeções e testes;

O&M;

garantias;

pacotes de entrega.


Isso demonstra que existe disposição de pagamento pelos problemas adjacentes. O mercado não parece comprar uma categoria abstrata chamada “malha semântica transversal”; compra CDE, quality, contracts, commissioning, handover ou asset information.

5. POR QUE ESSE VALOR PODE NÃO VIRAR COMPRA

5.1 Capacidade não é objeto de contratação

“Relacionar informação heterogênea” é uma capacidade.

“Entregar até Mechanical Completion o dossiê verificável de 200 equipamentos” é uma compra.

No estado atual, ainda não estão definidos de maneira comercial:

entrada mínima;

escopo padrão;

resultado verificável;

prazo;

responsabilidade do cliente;

garantia de proveniência;

preço;

critério de aceite.


5.2 Cold start informacional

Antes de receber valor, o projeto pode precisar pagar por:

levantamento de fontes;

normalização de identificadores;

definição de relações;

importação;

versionamento;

validação humana;

responsabilidades de captura.


O custo aparece antes do benefício.

5.3 O esforço e o benefício pertencem a atores diferentes

Um exemplo provável:

projetista identifica o elemento;

fornecedor entrega certificado;

obra registra instalação;

QA realiza inspeção;

empreiteiro paga parte da captura;

proprietário recebe o ativo;

jurídico usa a informação numa disputa.


Sem exigência contratual ou patrocínio do proprietário, cada participante tende a minimizar seu esforço local.

5.4 Alta severidade, baixa frequência percebida

Falhas graves, auditorias e claims podem ser caros, mas não são eventos diários para cada comprador. Durante a normalidade, o custo de manter rastreabilidade é visível e o benefício permanece latente.

O CII encontrou essa percepção de ROI duvidoso entre owners, contractors, vendors e suppliers, embora organizações experientes relatassem benefícios em recebimento, instalação, produtividade, commissioning, O&M e mitigação jurídica. CII RT-384

5.5 Paradoxo retrospectivo

Quando começa uma disputa, existe urgência e orçamento. Mas a informação que não foi preservada durante a execução pode já ter desaparecido.

Antes da disputa, a captura preventiva tem pouca urgência. Depois da disputa, parte do valor potencial tornou-se irrecuperável.

5.6 O valor já está incorporado a workflows mais frequentes

A ConstruCode não vende apenas rastreabilidade. Vende acesso ao documento correto, tarefas, field, RDO e qualidade. O histórico surge como subproduto do uso diário.

O Aconex vende audit trail junto com documentos, correspondência contratual, workflows, supplier documents e test plans. Oracle Aconex

Assim, o comprador pode considerar que sua necessidade já está parcialmente atendida pelo sistema contratado.

5.7 A federação cria um problema probatório específico

Se uma fotografia externa for substituída ou um documento perder permissão, o link pode sobreviver, mas a evidência pode não sobreviver.

Para uso em claims, auditoria ou fiscalização, o InfoBIM precisará demonstrar:

hash ou snapshot;

timestamp;

autor;

versão;

histórico de modificação;

origem;

distinção entre relação registrada e inferida;

pacote exportável e verificável.


5.8 A riqueza aumenta simultaneamente valor e custo

Cada novo domínio — cronograma, ERP, compras, notas fiscais, fotografias, mensagens — amplia o valor potencial e a superfície de integração.

A riqueza só gera valor econômico quando o custo marginal de adicionar uma nova fonte cai após as primeiras implantações.

5.9 Parte do mercado prefere criar o registro prospectivamente

Aconex e CDEs semelhantes obrigam o trabalho contratual a passar pelo sistema. Isso é centralizador, mas produz um registro consistente.

O InfoBIM aceita informação externa e heterogênea. Isso é mais aberto, mas também o obriga a tratar inconsistências que o CDE evita por construção.

6. QUAIS HIPÓTESES ANTERIORES DEVEM SER DESCARTADAS

“O problema é ontologia”

Descartada como explicação principal. Não existe divulgação comercial ampla falando de RDF, OWL ou SHACL que esteja afastando compradores.

A ontologia só seria comercialmente relevante se aumentasse comprovadamente o custo de implantação ou dependência de especialistas.

“O concorrente é Excel, e-mail ou WhatsApp”

Incorreta sem qualificação. Esses meios podem ser fontes compatíveis.

O substituto real é o processo pelo qual document controllers, engenheiros, BIM coordinators e consultores reconstroem contexto manualmente utilizando esses meios e sistemas existentes.

“É o sétimo sistema”

Não descreve corretamente o InfoBIM. Ele pode funcionar sobre fontes existentes.

O problema pertinente é se a camada adicional exige novos conectores, responsabilidades e governança.

“A CLI ou o pip impedem a venda”

Não demonstrado. Existem superfícies HTML e artefatos offline. Uma consultoria pode operar a CLI sem expô-la ao usuário final.

A CLI só seria obstáculo se um workflow comercial exigisse que usuários de campo a utilizassem diretamente.

“Falta distribuição”

Verdadeiro, mas insuficiente. Mais divulgação não corrige ausência de gatilho, comprador e entrega.

“Falta prova social”

Ajuda a reduzir risco, mas não explica o que deve ser comprado. O ciclo inicial pode ser rompido por pilotos delimitados, implantação assistida e parceiros.

“Falta prova econômica”

Genérico demais. A prova precisa ser ligada ao evento:

pacote de commissioning aceito;

lacuna documental encontrada antes do handover;

cronologia produzida para um claim;

medição sustentada por evidências;

dossiê de ativo entregue sem reconciliação manual.


“A riqueza precisa ser simplificada”

Não necessariamente. A arquitetura pode continuar rica. O que precisa ser delimitado é a oferta comercial, não o motor.

7. GATILHOS DE COMPRA

Não encontrei base brasileira confiável para atribuir uma taxa universal de ocorrência a claims, falhas ou problemas de handover. Relatórios como o CRUX da HKA analisam projetos já problemáticos, não a prevalência sobre todos os projetos. Eles demonstram severidade, não frequência geral. HKA CRUX

Ordem	Gatilho	Frequência	Custo e urgência	Quem sente/decide	Solução atual	Aderência InfoBIM	Chance

1	Commissioning/handover de sistemas e ativos	Inevitável por fase	Alta perto do marco	Owner, EPC, commissioning manager	Aconex, Thinkproject, Dalux, ACC, equipes documentais	Alta conceitualmente; parcial hoje	Alta
2	Claim ou investigação de atraso/mudança	Episódica	Muito alta quando ocorre	Contratos, jurídico, project controls	Aconex, Thinkproject, consultoria forense	Boa como serviço	Média-alta
3	Não conformidade, falha ou causa-raiz	Recorrente em projetos complexos	Média a muito alta	QA/QC, engenharia, owner	Procore, Dalux, ACC, ConstruCode	Boa se ligar elemento–atividade–evidência	Média-alta
4	Auditoria ou fiscalização	Periódica/obrigatória	Alta por prazo e compliance	Fiscal, owner, gestor público	CDE, relatórios, document control	Boa, principalmente com pacote local	Média-alta
5	Material ou equipamento crítico	Por pacote/equipamento	Alta em industrial	Suprimentos, QA, commissioning	ERP, material tracking, CDE	Forte aderência ao problema do CII	Média-alta
6	As-built e informação de ativos	Uma vez por projeto	Alta no encerramento	Owner, FM, BIM manager	Handover software e consultoria BIM	Alta se houver template por ativo	Média
7	Troca de equipe/perda de memória	Comum	Urgência variável	Project director, owner	CDE, busca manual, entrevistas	Boa, mas gatilho fraco	Média-baixa
8	Integração cotidiana projeto–campo	Diária	Custo acumulado	Engenharia de obra	ConstruCode, Procore, Dalux	Mercado grande, porém concorrido	Baixa agora
9	O&M genérica	Contínua	Valor difuso e tardio	Owner/FM	CMMS, IWMS, Dalux FM	Depende do handover	Baixa inicialmente
10	Consulta em linguagem natural	Frequente	Baixa isoladamente	Diversos usuários	Busca e copilots	Não é gatilho sozinho	Baixa


O gatilho mais plausível é:

> “Tenho um marco de handover ou commissioning e não consigo demonstrar que cada ativo possui desenho, versão, fornecedor, teste, certificado, instalação, foto, aprovação e responsável.”



8. SEGMENTOS DE MERCADO

1. EPC, industrial, energia, óleo e gás e data centers

Maior aderência porque possuem:

equipamentos identificáveis;

vendor data;

certificados;

inspection and test plans;

commissioning formal;

múltiplos fornecedores;

alto custo de atraso;

operação posterior.


É o contexto mais próximo dos componentes e módulos estudados pelo CII.

2. Infraestrutura, concessões e obras públicas complexas

Projetos longos, múltiplas organizações, fiscalização, mudanças, medições e necessidade de memória de longo prazo.

Na PAIC 2024, infraestrutura representou aproximadamente R$ 200,9 bilhões — 38,4% do valor de obras e serviços. IBGE, PAIC 2024

3. Consultorias de commissioning, claims, qualidade e fiscalização

Podem ser clientes, usuários ou canais. Já possuem:

problema;

cliente final;

orçamento por projeto;

competência para operar ferramenta técnica;

incentivo para transformar o InfoBIM em entrega profissional.


É particularmente compatível com fundador solo.

4. Proprietários e operadores de ativos críticos

Capturam o benefício durante operação. Precisam, contudo, exigir contratualmente a produção da informação.

5. Construtoras e incorporadoras grandes com BIM

Há aderência, mas o mercado de documentos, field e qualidade já é concorrido.

6. Consultorias BIM e projetistas

Mais promissores como parceiros de implantação do que como pagadores finais.

7. Pequenas construtoras residenciais

Aderência inicial baixa: menor consequência absoluta, menor orçamento e menor disponibilidade para integração.

9. CONCORRENTES E SUBSTITUTOS REAIS

Solução	Categoria e benefício vendido	Reconstrução de contexto	Preço

ConstruCode	GED/CDE, BIM, QR, field, RDO, qualidade	Histórico de documentos, acesso, issues e qualidade	Não publicado; por plano/empreendimento
Procore	Project management, RFIs, documentos, field, qualidade, custos	Audit trail de RFIs, decisões e registros	Cotação anual, associada ao volume de construção
Autodesk Construction Cloud	Docs, Build, BIM Collaborate, Takeoff	Modelos, documentos, issues, campo e custos	Assinaturas/pacotes e cotação
Dalux	Field, Box, BIM e FM	Fotos, issues, object history e dados de ativo	Field Basic gratuito; demais por cotação
Revizto	Coordenação 2D/3D e issues	Issue ligada a objeto/local, chat e anexos	Cotação
Trimble Connect	CDE, modelos, tarefas e dados de objetos	Propriedades, comentários, to-dos e BCF	Assinatura por usuário/região
Bentley ProjectWise/iTwin	Engenharia, CDE e digital twin	Mudanças, modelos e contexto de ativos	Cotação empresarial
Oracle Aconex	Registro contratual, documentos e workflows	Registro imutável de comunicações, decisões e ações	Cotação empresarial
Catenda Hub/Duo	CDE openBIM, IFC/BCF, documentos e ativos	Modelos, issues, documentos e histórico	€400/mês em projeto de €10 mi; €1.100 em €50 mi
Thinkproject	CDE, Contracts e Handover	Obrigações, mudanças, riscos, evidências e ativos	Cotação


A Catenda é importante porque combina openBIM, IFC/BCF, ausência de lock-in e preço por valor do projeto. Catenda Pricing

O Aconex é o concorrente mais próximo no aspecto “história de projeto”, mas usa estratégia oposta: concentra as transações no sistema para construir um registro imutável. Oracle Aconex

Existe equivalente direto?

Não encontrei uma solução comercial pública que simultaneamente:

parta de uma entidade arbitrária;

atravesse IFC, documentos, atividades, pessoas, financeiro e execução;

preserve fontes nos ambientes originais;

funcione localmente;

produza uma história contextual navegável;

seja vendida como capacidade transversal independente.


Existem equivalentes parciais:

Dalux: histórico de objeto e ativo;

Revizto: issue centrada em objeto;

iTwin: mudanças e contexto do modelo;

Aconex: decisões e comunicações;

Thinkproject: contratos e handover;

Catenda: modelos, documentos, issues e ativos em openBIM.


A combinação arquitetural do InfoBIM parece incomum. O problema é que a versão ativa ainda não entrega a combinação completa que constituiria essa diferenciação.

Substituto principal

O substituto não é o Excel isolado. É a combinação de:

CDE já contratado;

document controller;

BIM coordinator;

QA/QC;

commissioning manager;

project controls;

consultoria de claims;

montagem manual de dossiês e cronologias.


10. CONSTRUCODE

Os principais dados foram confirmados:

fundada em 2018;

11–50 funcionários;

LinkedIn mostra 32 pessoas associadas; LinkedIn

investimento-anjo reportado de R$ 200 mil;

rodada de R$ 8 milhões;

valuation reportado de R$ 45 milhões;

captação adicional de R$ 2,6 milhões;

previsão de faturamento de R$ 4 milhões em 2022; Forbes Brasil

controle assumido pela Vedacit Soluções Tecnológicas em 2020;

naquele momento, mais de 500 obras, 100 mil etiquetas, 50 mil projetos e 50 construtoras;

aceleração com aumento reportado de 50% no faturamento. Vedacit


Os números atuais de milhares de empreendimentos e dezenas de milhares de profissionais aparecem em comunicação empresarial e matérias promocionais, não em demonstrações financeiras auditadas.

O mecanismo do wedge inicial

O QR Code resolvia um evento cotidiano:

1. alguém precisava do desenho correto;


2. estava fisicamente no local;


3. havia risco de acessar versão obsoleta;


4. o QR conduzia ao documento liberado.



Os mecanismos de crescimento foram:

alta frequência;

ponto de uso óbvio;

benefício imediatamente observável;

artefato visível no canteiro;

baixa necessidade de explicar a tecnologia;

escolha de empresas já digitalizadas, mas mal atendidas;

venda B2B assistida;

capital e canal da Vedacit;

expansão posterior para documentos, tarefas, BIM, field, qualidade e RDO.


A empresa atual oferece Multi, Multi PRO e Build PRO, com limites por empreendimento, documentos e participantes. Planos da ConstruCode

Não há razão para hindsight bias. O QR Code poderia ter permanecido uma funcionalidade pequena. O crescimento decorreu da execução comercial, capital, distribuição, escolha do segmento e expansão da oferta — não de uma inevitabilidade técnica.

O que pode ser adaptado

um wedge único;

um momento concreto de uso;

um artefato demonstrável;

preço por empreendimento;

escolha de cliente já digitalizado;

casos operacionais;

expansão somente depois da primeira compra.


Para o InfoBIM, o equivalente funcional poderia ser um dossiê contextual de ativo, sistema ou evento, acessível por link ou QR, contendo fontes, cronologia, evidências e lacunas.

Apresentar à ConstruCode hoje?

Uma apresentação genérica tem baixo valor esperado. Eles já anunciam documentos, BIM, issues, histórico, field e qualidade.

Uma abordagem só teria motivo concreto depois de existir algo complementar, como:

pacote aberto/local de handover;

dossiê de ativo atravessando fontes externas;

reconstrução de evidências para claims;

integração com informação que não reside na plataforma.


11. TAM / SAM / SOM

Dados publicados

A PAIC 2024 registrou:

191 mil empresas;

2,5 milhões de pessoas ocupadas;

R$ 522,5 bilhões em obras, incorporações e serviços;

R$ 95,6 bilhões em salários e remunerações. IBGE


A FGV IBRE encontrou uso de BIM em 20,6% das empresas pesquisadas em março de 2024, ante 9,2% em 2018. Em edificações residenciais, 37,2%. FGV IBRE

Não encontrei fonte pública robusta para o gasto brasileiro em construction software, CDE ou BIM.

Os relatórios globais divergem conforme a categoria:

Grand View: US$ 11 bilhões em construction and design software em 2024; Grand View Research

Fortune: US$ 11,72 bilhões em construction management software em 2025; Fortune Business Insights

Future Market Insights: US$ 7,5 bilhões em 2025. FMI


Essa variação impede usar um único relatório como TAM do InfoBIM.

TAM — teto hipotético

Aplicar 20,6% a 191 mil empresas produziria aproximadamente 39 mil organizações. Os universos das pesquisas não são idênticos; portanto, é apenas um cenário.

A R$ 24 mil–R$ 120 mil por ano:

aproximadamente R$ 940 milhões;

até R$ 4,7 bilhões.


Isso é um teto BIM-adjacente, não TAM comercial demonstrado.

SAM — estimativa própria

Premissas:

1.000–5.000 organizações ou projetos;

médias/grandes construtoras, EPCs, owners, órgãos, concessões e consultorias;

BIM ou ativos identificáveis;

múltiplas fontes;

problema de handover, fiscalização, qualidade ou claims;

gasto de R$ 30 mil–R$ 150 mil por projeto/fase.


Resultado:

R$ 30 milhões–R$ 750 milhões anuais.


A faixa larga reflete a ausência de dados brasileiros específicos.

SOM — fundador solo em 24 meses

Capacidade operacional plausível:

4–12 projetos;

R$ 25 mil–R$ 80 mil por projeto;

R$ 100 mil–R$ 960 mil acumulados.


Caso-base: seis projetos a R$ 40 mil, totalizando R$ 240 mil.

Esse SOM é limitado pela capacidade de implantação, não por uma porcentagem arbitrária do mercado.

12. MODELO COMERCIAL MAIS PLAUSÍVEL

Open source + serviço de evidência contextual por projeto

A recomendação não é vender inicialmente “InfoBIM Enterprise”. É vender uma entrega produzida com o InfoBIM.

Oferta A — Commissioning Evidence Thread

Escopo experimental:

um sistema ou 20–50 ativos;

IFC;

datasheets;

certificados;

inspeções e testes;

fotografias;

aprovações;

O&M;

dossiê HTML/local por ativo;

relatório de lacunas.


Faixa de teste, não preço de mercado comprovado:

piloto: R$ 15 mil–R$ 30 mil;

fase ampliada: R$ 40 mil–R$ 100 mil.


Oferta B — reconstrução de contexto para claim ou mudança

Entrega:

cronologia;

documentos relacionados;

atividades afetadas;

decisões;

versões;

responsáveis;

contradições;

lacunas de evidência.


O serviço organiza evidência; não oferece conclusão jurídica.

Oferta C — handover aberto por ativo

normalização da informação existente;

vínculos por ativo;

verificação de completude;

pacote portátil;

ausência de lock-in;

preservação de fontes e proveniência.


Por que serviço primeiro

o trabalho de implantação ainda varia;

permite descobrir quais relações realmente têm valor;

gera receita antes de construir produto horizontal;

é compatível com fundador solo;

converte CLI e engine em infraestrutura invisível;

o open source reduz medo de lock-in;

produz casos reais.


Evolução possível

1. serviço assistido;


2. templates por segmento;


3. managed service por projeto;


4. licença e suporte para consultorias;


5. integrações pagas;


6. assinatura de atualização/manutenção.



Modelos menos aderentes agora:

freemium horizontal;

self-service;

cobrança por usuário;

suíte ampla concorrendo com ConstruCode;

enterprise antes de repetibilidade;

produto gratuito sem serviço ou canal associado.


13. O QUE FARIA EU MATAR COMERCIALMENTE O PROJETO

Eu abandonaria a tese comercial, preservando o open source como projeto técnico, se em 90–120 dias:

1. fossem realizadas 12–15 entrevistas com commissioning, QA/QC, contratos, fiscalização e owners;


2. ocorressem cinco demonstrações usando dados reais, ainda que anonimizados;


3. menos de três pessoas identificassem problema atual superior a 40 horas ou R$ 50 mil de exposição;


4. ninguém aceitasse pagar pelo menos R$ 15 mil por um piloto delimitado;


5. todos exigissem primeiro um CDE, aplicativo de campo ou suíte completa;


6. nenhum sponsor aceitasse fornecer dados e um responsável pela validação;


7. cada projeto exigisse mais de cinco dias de modelagem manual sem redução nos projetos seguintes;


8. após três pilotos, menos de 50% do trabalho pudesse ser reutilizado;


9. o artefato não fosse aceito em commissioning, auditoria, fiscalização ou análise contratual;


10. as respostas permanecessem em “interessante”, “inovador” e “poderia ser útil”.



14. O QUE FARIA EU CONTINUAR

Eu continuaria se:

dois de cinco prospects com dados próprios comprassem piloto de R$ 15 mil–R$ 30 mil;

um deles expandisse para outro sistema ou projeto;

o mesmo perfil de comprador se repetisse;

um dossiê pudesse ser produzido em menos de um dia após configuração;

ao menos 70% das relações fossem importadas, derivadas ou reutilizadas;

o resultado fosse usado num marco real;

uma consultoria aceitasse revendê-lo ou incorporá-lo ao próprio serviço;

o segundo e o terceiro projeto apresentassem margem crescente;

o cliente considerasse custoso retornar ao processo manual.


15. EXPERIMENTOS DE MERCADO

Experimento 1 — dossiê de um ativo real

Escolher um ativo ou sistema real e reunir:

IFC;

desenho;

especificação;

fornecedor;

pedido ou submittal;

certificado;

inspeção;

foto;

atividade;

decisão;

pendências.


Produzir uma página HTML local com fontes e lacunas. Demonstrar para cinco profissionais de commissioning, QA ou contratos.

Pergunta discriminante:

> “Você pagaria para receber isto para vinte ativos antes do próximo marco?”



Experimento 2 — piloto pago acionado por evento

Oferecer apenas uma entrega:

vinte ativos prontos para handover em três semanas; ou

cronologia e pacote de evidência de um evento de mudança.


Preço fixo experimental: R$ 15 mil–R$ 30 mil.

O pagamento diferencia curiosidade técnica de demanda.

Experimento 3 — canal com consultorias

Procurar três consultorias pequenas de:

commissioning;

claims;

fiscalização;

QA/QC;

asset information.


Propor que vendam a entrega ao cliente usando o InfoBIM como infraestrutura, por participação na receita ou suporte licenciado.

Isso testa aquisição compatível com fundador solo.

O que não testar ainda

tráfego pago amplo;

landing page genérica;

freemium;

dezenas de entrevistas sem dados reais;

apresentação geral para ConstruCode;

construção de módulos de CDE, RDO ou field;

precificação complexa antes de uma entrega ser aceita.


16. RESPOSTA FINAL EM UMA FRASE

Hoje, o InfoBIM não vende principalmente porque o código já fornece parte substancial da infraestrutura para relacionar informação, mas ainda não a transforma em um workflow end-to-end, acionado por um evento orçamentário concreto e capaz de entregar uma trilha de evidência confiável sem exigir do comprador um investimento prévio de integração e manutenção maior que o valor percebido antes desse evento.