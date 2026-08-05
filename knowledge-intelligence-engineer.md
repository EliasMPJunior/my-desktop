# Knowledge Intelligence Engineer

## Registro conceitual, formação profissional e estratégia de implantação

> Documento de trabalho consolidado a partir das discussões de 4 e 5 de agosto de 2026.
>
> Este texto registra a ideia em seu estado atual, com suas premissas, contexto, fundamentos, possíveis parceiros, etapas e pontos ainda em aberto. O nome **Knowledge Intelligence Engineer** é provisório e secundário: o essencial é a função profissional descrita aqui.

---

## 1. Ponto de partida

A proposta nasce da percepção de que existe uma função profissional real, transversal e ainda mal definida pelo mercado.

Hoje, várias responsabilidades necessárias para produzir informação confiável ficam fragmentadas entre profissionais e áreas diferentes:

- engenharia de dados;
- engenharia de conhecimento;
- arquitetura da informação;
- ontologias e knowledge graphs;
- BI e visualização;
- desenvolvimento de software;
- infraestrutura de TI;
- inteligência artificial;
- gestão da informação;
- especialistas do domínio;
- gestão operacional.

Cada área cobre uma parte do problema, mas frequentemente ninguém assume a responsabilidade integrada de garantir que uma equipe obtenha, no momento necessário, a informação correta, contextualizada, rastreável e confiável para executar um processo real.

A proposta é reconhecer essa responsabilidade integrada como uma profissão própria.

---

## 2. Definição da profissão

### 2.1 Definição condensada

**Knowledge Intelligence Engineer é o profissional responsável por projetar e implementar os ambientes técnicos, semânticos e de interação necessários para que equipes produzam, integrem, recuperem e utilizem informação confiável, contextualizada, verificável e disponível no momento adequado aos seus processos.**

### 2.2 Formulação operacional

Esse profissional:

1. compreende o processo real da organização ou do projeto;
2. identifica quais informações serão necessárias para executar esse processo;
3. determina onde essas informações existem ou como devem ser produzidas;
4. estrutura dados, documentos, entidades, relações, regras e contextos;
5. define a infraestrutura necessária para captar, transportar, armazenar e disponibilizar os dados;
6. utiliza as melhores ferramentas disponíveis, incluindo software existente, programação, automação, IA, LLMs, RAG, ontologias, BI, sensores e infraestrutura;
7. valida as transformações e a qualidade dos resultados;
8. entrega a informação de forma compreensível e segura para pessoas, equipes ou máquinas;
9. preserva proveniência, contexto e critérios de confiança.

O objetivo não é simplesmente “encontrar documentos” ou “usar IA”. O objetivo é possibilitar que uma equipe obtenha **informação confiável just in time para um processo concreto**.

---

## 3. Objeto profissional

O objeto desse profissional é o **ambiente informacional operacional**.

Ele não trabalha apenas com dados já disponíveis. Pode precisar criar as condições para que os dados sejam gerados corretamente, circulem, ganhem significado e cheguem a quem precisa deles.

A profissão combina:

- conhecimento do domínio;
- engenharia da informação;
- semântica;
- infraestrutura;
- integração;
- automação;
- inteligência artificial;
- validação;
- apresentação e interação.

A programação é uma ferramenta importante, mas não é o centro da profissão. O centro é a engenharia da solução informacional.

---

## 4. As três camadas da atuação

Este é um conceito central e deve permanecer explícito na formação e na apresentação pública da profissão.

## 4.1 Camada de infraestrutura

É a camada que permite que o dado exista, seja captado, trafegue, seja armazenado e permaneça disponível.

Pode incluir:

- redes locais;
- switches;
- servidores locais;
- armazenamento;
- sincronização;
- dispositivos de campo;
- sensores;
- crachás e dispositivos BLE;
- conectividade temporária em canteiros;
- permissões e controle de acesso;
- serviços em nuvem quando adequados;
- computação local e offline;
- integração entre sistemas e dispositivos.

O profissional não atua como um técnico de infraestrutura genérico. Ele toma decisões de infraestrutura em função do processo informacional.

Exemplo: em um canteiro com conectividade ruim, pode projetar uma rede interna e um servidor local para permitir comunicação, coleta e consulta de informações sem depender continuamente da internet.

Outro exemplo: pode implementar crachás ou dispositivos BLE para produzir dados de presença, localização aproximada, circulação, ferramentas ou frentes de serviço, quando isso fizer sentido para aquela operação.

## 4.2 Camada de inteligência e semântica

É a camada em que o dado ganha significado, relações, contexto, regras e critérios de confiança.

Pode incluir:

- ontologias;
- taxonomias;
- knowledge graphs;
- modelagem conceitual;
- metadados;
- proveniência;
- restrições e validações;
- SHACL e mecanismos equivalentes;
- integração de fontes heterogêneas;
- transformação de dados;
- vinculação entre documentos, atividades, pessoas, equipamentos e eventos;
- critérios de aceitação;
- auditoria;
- rastreabilidade;
- controle de estados;
- recuperação contextualizada;
- uso de LLMs e RAG com evidências e limites explícitos.

Ontologias são o coração dessa camada porque permitem representar não apenas dados isolados, mas o significado das entidades, suas relações, restrições e contexto.

## 4.3 Camada de interação e apresentação

Esta camada trata tanto de quem gera o dado quanto de quem o consome.

Ela cobre duas pontas:

### Origem

- como o dado é criado;
- quem o registra;
- quais interfaces, formulários, sensores, planilhas, arquivos ou máquinas participam da geração;
- quais erros podem ocorrer na captura;
- quais validações devem acontecer na entrada;
- como reduzir ambiguidade e perda de contexto.

### Consumo

- quem precisa da informação;
- em qual momento;
- com qual nível de detalhe;
- em qual linguagem;
- em qual meio;
- como apresentar proveniência, confiança e exceções;
- como permitir uma decisão segura.

O nome “apresentação” não deve ser interpretado apenas como dashboard. A camada inclui qualquer interação entre pessoas, máquinas e o ambiente informacional.

---

## 5. A tese principal: isso não é atribuição de um software

Muitas empresas tentaram vender essas responsabilidades como funcionalidades de um software ou de um SaaS:

- reduzir atraso;
- eliminar retrabalho;
- garantir rastreabilidade;
- integrar toda a informação;
- automatizar decisões;
- conectar todos os sistemas;
- entregar conhecimento confiável por assinatura.

A frustração recorrente decorre de uma premissa equivocada: essas responsabilidades não pertencem a uma ferramenta isolada. Elas pertencem a um profissional capaz de compreender o domínio, projetar a solução e combinar ferramentas.

Software pode:

- coletar;
- transformar;
- consultar;
- alertar;
- visualizar;
- registrar;
- validar partes do processo.

Mas alguém precisa decidir:

- quais dados importam;
- o que significam;
- como devem ser relacionados;
- como serão gerados;
- qual infraestrutura é necessária;
- quais critérios definem confiança;
- como o resultado será entregue;
- o que deve ser inspecionado;
- quando uma solução é adequada ao contexto.

Portanto, o software é instrumento. A responsabilidade integrada é profissional.

---

## 6. Analogia com o engenheiro calculista

A analogia com o engenheiro calculista é central.

O engenheiro calculista não vende “um software de cálculo”. Ele vende capacidade técnica aplicada a uma estrutura específica, usando normas, modelos, ferramentas e julgamento profissional.

Da mesma forma, o Knowledge Intelligence Engineer não vende simplesmente uma ontologia, um dashboard, um agente ou um software. Ele entrega uma estrutura informacional adequada a um processo concreto.

O cliente não precisa pedir:

- RDF;
- SHACL;
- ontologias;
- RAG;
- knowledge graph;
- proveniência formal.

Assim como o cliente de um calculista não precisa pedir “elementos finitos”, ele precisa de um resultado tecnicamente confiável.

O conhecimento do domínio é indispensável. Um especialista em semântica sem conhecimento da área pode produzir uma modelagem elegante e operacionalmente inútil. Um especialista do domínio sem conhecimentos de dados e semântica pode compreender o problema, mas não conseguir estruturá-lo de forma computável e interoperável.

A profissão existe justamente na combinação dessas competências.

---

## 7. O briefcase como artefato profissional

O **briefcase** é o artefato central da profissão.

A ideia é promover o conceito de briefcase, originalmente desenvolvido no contexto do InfoBIM e do dBriefcase, para um conceito acadêmico e profissional geral.

Assim como hoje se diz:

- “vou gerar um dashboard para a diretoria”;
- “vou montar um cockpit gerencial”;
- “vou criar um modelo BIM para o projeto”;
- “vou emitir um parecer técnico”;

pretende-se que seja possível dizer:

- “vou gerar um briefcase para esta equipe”;
- “vou montar um briefcase para este processo”;
- “este projeto precisa de um briefcase operacional”.

## 7.1 O que é o briefcase

Um briefcase é um artefato informacional contextualizado, autossuficiente ou suficientemente autônomo, que reúne conforme a necessidade:

- dados;
- documentos;
- metadados;
- ontologias;
- relações;
- regras;
- proveniência;
- critérios de validação;
- transformações;
- evidências;
- visualizações;
- mecanismos de consulta;
- capacidades de execução;
- interfaces para pessoas ou máquinas.

Ele é produzido para uma equipe, processo, projeto ou operação específicos.

## 7.2 O briefcase como porto seguro dos dados

A solução técnica pode mudar:

- um script pode ser substituído;
- uma interface pode ser refeita;
- um agente pode ser trocado;
- um aplicativo gerado por IA pode ser descartável;
- uma tecnologia pode deixar de existir.

O briefcase deve preservar:

- o estado de entrada;
- o significado dos dados;
- as relações;
- as regras;
- o estado de saída esperado;
- a proveniência;
- os critérios de aceitação;
- as evidências de validação.

Ele funciona como porto seguro do dado e do conhecimento do processo.

## 7.3 Confiança em soluções geradas por IA

A IA pode ser delegada para produzir software ou realizar transformações, assim como um profissional delega a execução de uma tarefa a alguém competente.

A confiança não precisa vir da leitura manual de cada linha de código. Ela pode ser estabelecida por:

- estado de entrada conhecido;
- estado de saída esperado;
- regras explícitas;
- critérios de aceitação;
- testes;
- inspeção de pontos críticos;
- conferência de perdas ou alterações indevidas;
- preservação da proveniência;
- auditoria do processo.

A analogia é a execução de obra: o engenheiro não acompanha cada movimento da colher do pedreiro. Ele define critérios, inspeciona aspectos relevantes, verifica o resultado e aceita ou rejeita a entrega.

A IA pode ser mão de obra técnica delegada. A responsabilidade continua com o profissional que especifica, verifica e aceita.

---

## 8. Soluções específicas e o “bacalhau de engenheiro”

Uma forma informal de resumir a proposta é:

> **oficializar, organizar e dar método aos famosos bacalhaus de engenheiro.**

“Bacalhau”, aqui, não significa necessariamente gambiarra ruim. Muitas vezes é uma solução específica, local e adequada para uma necessidade que não possui mercado suficiente para justificar um produto comercial genérico.

A proposta reconhece que:

- uma ideia pode ser tecnicamente excelente;
- pode resolver um problema real;
- pode valer a pena para um projeto;
- e ainda assim não sustentar uma startup, um SaaS ou um produto de massa.

Isso não torna a ideia inválida. Ela pode ser implementada como projeto específico.

O problema não é a solução ser sob medida. O problema seria ela ser:

- opaca;
- sem documentação;
- sem validação;
- sem proveniência;
- sem critérios de aceitação;
- impossível de manter;
- dependente de conhecimento que desaparece com uma pessoa.

O Knowledge Intelligence Engineer transforma a solução específica em um projeto técnico controlado, compreensível e verificável.

---

## 9. Redução da dependência de software de mercado

A proposta não pretende eliminar softwares existentes.

O profissional continuará usando:

- aplicações comerciais;
- sistemas corporativos;
- ferramentas open source;
- serviços em nuvem;
- bancos de dados;
- plataformas de BI;
- ferramentas de modelagem;
- aplicações de IA;
- qualquer tecnologia que seja adequada.

A mudança é reduzir a dependência de que um fornecedor de software decida criar exatamente a solução necessária.

Antes, muitas necessidades morriam assim:

1. não existe software pronto;
2. desenvolver do zero custa caro;
3. o mercado é pequeno demais para sustentar um produto;
4. portanto, a solução não existe.

Com programação assistida por IA, agentes generativos, ferramentas open source e profissionais com visão integrada, torna-se possível montar soluções específicas com custo e prazo menores.

A organização não precisa esperar Autodesk, AltoQi, Microsoft ou outro fornecedor reconhecer comercialmente aquele nicho.

A pergunta deixa de ser:

> “Existe um software comercial para isso?”

E passa a ser:

> “É possível projetar e implementar uma solução confiável para este contexto?”

Isso é uma forma de soberania técnica local: não independência absoluta de fornecedores, mas capacidade de resolver problemas mesmo quando as condições de mercado não justificam a existência de um produto genérico.

---

## 10. Relação com programação generativa

O avanço de LLMs e agentes de desenvolvimento reduz o custo operacional de produzir software específico.

Há relatos de equipes em que a programação manual deixou de ser a atividade principal: o profissional descreve, orienta, revisa e aceita aplicações geradas por ferramentas como Claude Code e equivalentes.

Isso não elimina a engenharia da solução. Desloca o gargalo.

O gargalo passa a ser:

- compreender o processo;
- definir corretamente o problema;
- identificar dados e fontes;
- modelar o conhecimento;
- escolher arquitetura e infraestrutura;
- especificar estados e regras;
- avaliar o que foi gerado;
- validar o resultado;
- garantir confiança e manutenção.

Essas são precisamente competências do profissional proposto.

---

## 11. Relação com InfoBIM, OntoBDC e dBriefcase

A formação não deve ser um curso de InfoBIM.

O InfoBIM é:

- uma aplicação de referência para engenharia;
- um caso concreto;
- um laboratório;
- uma demonstração da prática.

O OntoBDC é:

- uma infraestrutura técnica possível;
- um runtime semântico;
- uma base para criação e execução de containers e briefcases.

O dBriefcase é:

- a implementação e formulação inicial do conceito de briefcase;
- uma referência de arquitetura e artefato.

A pós-graduação deve ensinar o conceito geral de briefcase e as competências necessárias para produzi-lo, não apenas o uso de uma ferramenta específica.

Outras ferramentas, padrões e arquiteturas devem ser estudados e aceitos. O profissional deve sair capaz de escolher e combinar tecnologias, não dependente de uma única implementação.

---

## 12. Formação proposta: pós-graduação

A proposta concreta é criar uma pós-graduação para formar esse profissional.

A pós-graduação é o mecanismo inicial de existência prática da profissão:

- organiza o corpo de conhecimentos;
- forma profissionais;
- cria uma linguagem comum;
- define competências;
- produz projetos aplicados;
- cria os primeiros briefcases acadêmicos e profissionais;
- estabelece uma comunidade inicial de prática.

## 12.1 Eixos preliminares da formação

O currículo ainda deverá ser desenvolvido em momento próprio, mas deverá incluir, no mínimo:

### Fundamentos de dados e informação

- dado, informação e conhecimento;
- qualidade de dados;
- estruturas de dados;
- bancos de dados;
- integração;
- ETL/ELT;
- metadados;
- governança;
- proveniência.

### Programação e automação

- lógica e programação;
- scripting;
- APIs;
- integração de ferramentas;
- automação de processos;
- geração de aplicações;
- revisão e validação de código gerado por IA.

### Inteligência artificial

- fundamentos de IA;
- funcionamento de LLMs;
- limites e alucinação;
- RAG;
- agentes;
- avaliação;
- uso seguro e verificável;
- automação assistida por IA.

### Semântica e ontologias

- modelagem conceitual;
- taxonomias;
- ontologias;
- RDF e tecnologias correlatas;
- knowledge graphs;
- inferência;
- restrições;
- validação;
- alinhamento e interoperabilidade;
- ontologias de domínio.

### BI, visualização e interação

- dashboards;
- cockpits;
- visualização de informação;
- design de interação;
- comunicação de incerteza;
- apresentação contextual;
- interfaces para usuários técnicos;
- interfaces para máquinas.

### Infraestrutura aplicada

- redes;
- servidores;
- armazenamento;
- computação local e em nuvem;
- offline-first;
- sensores e dispositivos;
- IoT e BLE;
- segurança;
- arquitetura aplicada ao processo informacional.

### Conhecimento do domínio

A formação deve reconhecer que o profissional precisa conhecer ou aprender profundamente o domínio em que atua.

Pode haver trilhas ou especializações, por exemplo:

- engenharia e construção;
- indústria;
- operação de ativos;
- saúde;
- administração pública;
- finanças;
- jurídico;
- pesquisa científica.

### Briefcases

- conceito;
- arquitetura;
- levantamento de necessidades;
- definição de fontes;
- modelagem;
- integração;
- validação;
- entrega;
- manutenção;
- auditoria;
- projeto final aplicado.

## 12.2 Perfil do egresso

O egresso deverá ser capaz de:

1. analisar um processo real;
2. identificar necessidades informacionais;
3. mapear fontes e lacunas;
4. definir infraestrutura adequada;
5. modelar dados e conhecimento;
6. selecionar ferramentas;
7. usar IA e programação como instrumentos;
8. implementar ou coordenar uma solução específica;
9. construir um briefcase;
10. validar confiança, qualidade e proveniência;
11. apresentar a informação para decisão segura;
12. documentar e manter o ambiente criado.

---

## 13. Ideia, estratégia e plano

A proposta contém três níveis diferentes.

### 13.1 Ideia

Reconhecer e nomear uma função profissional transversal centrada em ambientes informacionais confiáveis e briefcases.

### 13.2 Estratégia

Criar a profissão na prática por meio de:

1. definição conceitual;
2. formação de pós-graduação;
3. articulação institucional;
4. projetos aplicados;
5. conscientização contínua;
6. certificação posterior;
7. expansão para diferentes domínios e países.

### 13.3 Plano

O plano ainda precisa ser detalhado com responsáveis, prazos, recursos, instituições e entregáveis. Este documento registra a estratégia conceitual que deve orientar esse planejamento.

---

## 14. Articulação institucional

A proposta não depende de uma única instituição.

A TYLKO é a primeira parceira considerada porque existe forte sinergia temática e boa relação pessoal e profissional.

A TYLKO já atua com:

- treinamentos;
- certificações;
- inteligência artificial;
- ontologias;
- temas próximos ao núcleo da formação.

A proposta é lançar a pós-graduação em colaboração com a TYLKO, possivelmente agregando uma instituição universitária para chancela acadêmica.

## 14.1 Possível participação da PUC-Rio

A PUC-Rio pode ser procurada para:

- chancela acadêmica;
- estrutura de pós-graduação;
- professores;
- laboratórios;
- articulação com engenharia e informática;
- credibilidade no mercado brasileiro.

Contatos pessoais mencionados:

- **Tadeu** — posição de direção ou alta gestão no Departamento de Informática; cargo exato a confirmar;
- **Marcelo Congro** — ligado ao Departamento de Engenharia; cargo exato a confirmar.

A relação é direta. A abordagem não precisa ser tratada como prospecção fria: é possível telefonar e conversar sobre a proposta.

## 14.2 Universidade de Barcelona

**Professor Daniel Nascimento** é um contato central.

Contexto da relação:

- foi chefe de Elias no Tecgraf/PUC-Rio;
- trabalharam juntos com temas relacionados;
- foi chefe de Elias na CERTI;
- o desenvolvimento do CDE ocorreu sob sua gestão;
- existe confiança profissional e experiência compartilhada;
- há possibilidade de conversa presencial em Barcelona, inclusive de maneira informal.

A conversa com Daniel não é um pitch para um desconhecido. Pode ser apresentada como a organização conceitual e acadêmica de práticas que ambos já conhecem.

Possíveis contribuições:

- interlocução acadêmica;
- desenho curricular;
- participação docente;
- coautoria conceitual;
- articulação com a Universidade de Barcelona;
- internacionalização da formação;
- conexão entre engenharia, operações e informação.

## 14.3 buildingSMART International

Foi mencionado **Aidan Mercer** — nome e cargo atual a confirmar — como contato direto relacionado à buildingSMART International.

Há previsão de encontro presencial no mês seguinte à elaboração deste documento.

Possíveis contribuições:

- padrões e interoperabilidade;
- OpenBIM;
- reconhecimento internacional;
- eventos;
- palestras;
- conexão com indústria e comunidades técnicas;
- possível apoio institucional futuro.

## 14.4 Parlamento Europeu

Foi mencionado **Claudio Bessi [sobrenome exato a confirmar]**, ligado à direção ou área de tecnologia do Parlamento Europeu.

Contexto:

- mantém contato frequente com Elias;
- demonstra interesse em realizar iniciativas conjuntas;
- pode ser procurado diretamente por telefone.

Possíveis contribuições:

- diálogo sobre tecnologia, informação e instituições;
- dimensão europeia;
- eventos;
- articulação institucional;
- reflexão sobre aplicação no setor público.

## 14.5 Natureza da rede

Essas pessoas não são “leads” frios.

São contatos que:

- já trabalharam com Elias;
- conhecem sua capacidade;
- mantêm relação direta;
- podem ser contatados por telefone;
- podem receber a proposta em conversas pessoais e profissionais já existentes.

A estratégia deve aproveitar esse capital relacional real, sem converter relações existentes em um processo artificial de prospecção.

---

## 15. Sequência lógica e temporal proposta

## Fase 1 — Consolidação conceitual

Objetivo: definir claramente a profissão antes de estruturar a formação.

Entregáveis:

- definição da função;
- objeto profissional;
- três camadas de atuação;
- competências;
- limites e interfaces com outras profissões;
- conceito de briefcase;
- exemplos de aplicação;
- justificativa histórica e tecnológica;
- possíveis nomes.

Estado atual: iniciado e parcialmente consolidado neste documento.

## Fase 2 — Conversas exploratórias com parceiros próximos

Objetivo: discutir a proposta com pessoas que já conhecem Elias, o campo e parte da trajetória que originou a ideia.

Conversas prioritárias:

1. TYLKO;
2. Daniel Nascimento;
3. Tadeu;
4. Marcelo Congro;
5. Aidan Mercer;
6. Claudio Bessi [nome a confirmar];
7. outros interlocutores acadêmicos, industriais e institucionais que surgirem.

Essas conversas devem servir para:

- criticar a definição;
- ampliar ou reduzir o escopo;
- identificar competências ausentes;
- entender modelos acadêmicos possíveis;
- identificar instituições interessadas;
- compor um grupo inicial;
- verificar possibilidades de pós-graduação nacional e internacional.

Não se trata de vender uma ideia a desconhecidos, mas de organizar uma proposta com pessoas que possuem experiência, relação e peças complementares.

## Fase 3 — Desenho da pós-graduação

Objetivo: transformar a função profissional em formação acadêmica.

Entregáveis:

- perfil do egresso;
- competências;
- matriz curricular;
- disciplinas;
- carga horária;
- corpo docente;
- metodologia;
- critérios de avaliação;
- projeto final de briefcase;
- trilhas de domínio;
- formato presencial, híbrido ou remoto;
- modelo institucional e jurídico;
- possíveis instituições certificadoras.

## Fase 4 — Formação do núcleo institucional

Objetivo: definir o arranjo entre parceiros.

Possibilidades:

- TYLKO como parceira técnica e de formação;
- PUC-Rio como chancela acadêmica no Brasil;
- Universidade de Barcelona como parceira acadêmica internacional;
- buildingSMART International como parceira de padrões, interoperabilidade e conscientização;
- outros parceiros conforme o desenho amadurecer.

A proposta não deve ficar presa a uma única instituição. A rede pode ser composta por competências complementares.

## Fase 5 — Curso piloto ou primeira turma

Objetivo: formar os primeiros profissionais e testar o currículo.

Características desejáveis:

- turma pequena;
- participantes com diferentes formações;
- projetos aplicados reais;
- briefcase como trabalho final;
- avaliação de competências, não apenas presença;
- documentação dos casos;
- revisão curricular após a primeira edição.

## Fase 6 — Conscientização contínua

A conscientização não é uma fase que termina. Deve ocorrer continuamente.

Ações possíveis:

- palestras;
- eventos;
- congressos;
- artigos;
- mesas-redondas;
- webinars;
- demonstrações;
- publicações acadêmicas;
- conteúdos institucionais;
- apresentação de casos;
- participação em comunidades de engenharia, dados, IA, BIM, ontologias e gestão;
- explicação sobre a profissão;
- explicação sobre como se formar;
- explicação sobre como organizações podem usar esse profissional.

A mensagem não deve ser:

> “Inventamos um nome; adotem.”

Deve ser:

> “Existe uma função profissional estruturada para projetar ambientes informacionais confiáveis. Há formação, competências, métodos e artefatos concretos para exercê-la.”

## Fase 7 — Certificação

Após o amadurecimento inicial da formação, pode ser criada uma certificação nacional ou internacional.

A certificação deve servir para sinalizar que o profissional foi formado e avaliado nas competências definidas.

Pode envolver:

- prova teórica;
- avaliação de projeto;
- briefcase aplicado;
- defesa técnica;
- requisitos de experiência;
- recertificação;
- níveis de competência;
- especializações por domínio.

O certificado não cria a profissão nem substitui competência. Ele facilita o reconhecimento pelo mercado e por instituições.

## Fase 8 — Expansão

Possíveis caminhos:

- novas turmas;
- outros países;
- novas universidades;
- trilhas setoriais;
- comunidade profissional;
- eventos recorrentes;
- repositório de casos e padrões;
- pesquisa acadêmica;
- evolução do conceito de briefcase;
- certificações especializadas;
- reconhecimento em empresas e projetos.

---

## 16. Conscientização: mensagem central

Uma mensagem possível para eventos e apresentações:

> A transformação digital e a IA reduziram o custo de criar soluções específicas, mas aumentaram a necessidade de profissionais capazes de estruturar dados, modelar conhecimento, projetar a infraestrutura e garantir que a informação certa chegue, com confiança, ao processo certo.

Outra formulação:

> Recuperar texto ficou barato. Produzir informação contextualizada, verificável e adequada para decisão continua sendo trabalho profissional.

E uma formulação centrada no briefcase:

> O Knowledge Intelligence Engineer transforma dados dispersos, processos e conhecimento de domínio em briefcases confiáveis para equipes, projetos e operações.

---

## 17. Diferença entre profissão, ferramenta e produto

É essencial evitar confusão entre esses níveis.

### Profissão

Knowledge Intelligence Engineer: quem assume a responsabilidade integrada.

### Artefato

Briefcase: o ambiente informacional contextualizado entregue à equipe, projeto ou processo.

### Ferramentas

OntoBDC, InfoBIM, dBriefcase, bancos de dados, LLMs, RAG, BI, software comercial, scripts, sensores, redes e demais tecnologias.

### Serviço

Análise, modelagem, implantação, integração, validação, infraestrutura, entrega e manutenção de briefcases.

### Produto

Pode ou não existir. Algumas soluções podem virar produtos, mas isso não é requisito para a profissão nem para a utilidade do trabalho.

---

## 18. Escalabilidade não é requisito central

A profissão não depende de um modelo escalável de software.

O trabalho pode ser:

- específico;
- artesanal;
- técnico;
- adaptado ao domínio;
- dependente de julgamento profissional;
- executado como projeto ou serviço.

A dependência de um operador especializado não é automaticamente fraqueza. Em serviços de engenharia, direito, medicina, arquitetura, auditoria e cálculo, o especialista é parte da entrega.

O objetivo é aumentar a capacidade, qualidade e confiança do profissional, não necessariamente eliminar o profissional.

---

## 19. Origem autobiográfica e relevância coletiva

A proposta nasce também de uma constatação pessoal:

Elias atua de forma transversal entre engenharia civil, software, BIM, dados, ontologias, IA, gestão da informação e operação. Essa combinação é difícil de encaixar em títulos existentes e pode contribuir para dificuldades de absorção pelo mercado.

Uma forma informal de descrever o movimento é:

> “Pegar o que eu sei fazer, dar um rótulo de profissão e criar um monte de gente capaz de fazer também.”

Isso não deve ser entendido como criação de uma profissão para glorificação pessoal. A proposta ganha legitimidade justamente quando:

- é ensinável;
- outras pessoas podem exercê-la;
- o nome pode mudar;
- diferentes ferramentas podem ser usadas;
- instituições podem compartilhar autoria;
- os alunos podem ampliar e superar o método inicial;
- a profissão serve a organizações, processos e equipes reais.

A origem pessoal ajuda a identificar a prática. A finalidade é coletiva: formar profissionais capazes de resolver esse tipo de problema em diferentes contextos.

---

## 20. Princípios orientadores

1. **O nome é secundário.** A função profissional vem primeiro.
2. **O domínio importa.** Sem conhecimento do contexto, a semântica pode se tornar elegante e inútil.
3. **Ontologias são centrais.** Elas estruturam significado, relações, restrições e interoperabilidade.
4. **A IA é ferramenta, não autoridade.** O resultado precisa ser especificado, verificado e auditável.
5. **O briefcase é o porto seguro.** Ferramentas mudam; dados, contexto, proveniência e critérios devem permanecer.
6. **Infraestrutura também é informação.** Redes, dispositivos e servidores podem ser parte da solução.
7. **A interação começa na origem.** Qualidade depende de como o dado é produzido, não apenas de como é exibido.
8. **Soluções sob medida são legítimas.** Nem toda boa ideia precisa se tornar SaaS.
9. **Software não substitui responsabilidade profissional.** Ele executa partes da solução.
10. **A formação deve criar autonomia.** O profissional não pode ficar preso ao InfoBIM, OntoBDC ou a qualquer fornecedor.
11. **Confiança precisa ser verificável.** Proveniência, regras e critérios de aceitação devem ser explícitos.
12. **A conscientização é contínua.** A profissão será explicada, demonstrada e refinada ao longo do tempo.
13. **A rede é relacional, não uma lista de leads.** Os primeiros parceiros são pessoas com história e confiança compartilhadas.
14. **A profissão deve permanecer aberta à crítica.** O conceito será aprimorado por professores, alunos, profissionais e instituições.

---

## 21. Pontos ainda em aberto

- nome definitivo da profissão;
- tradução e uso em português;
- limites entre “engineer”, “architect”, “specialist” e outras denominações;
- matriz curricular detalhada;
- carga horária;
- pré-requisitos dos alunos;
- necessidade de trilhas por domínio;
- instituição responsável pela titulação;
- modelo de parceria com a TYLKO;
- participação da PUC-Rio;
- participação da Universidade de Barcelona;
- participação de buildingSMART International;
- formato da certificação;
- propriedade intelectual e governança do conceito de briefcase;
- ferramentas obrigatórias ou apenas referenciais;
- critérios objetivos de confiança e validação;
- escopo de atuação em infraestrutura;
- modelo de projeto final;
- reconhecimento acadêmico internacional;
- financiamento e operação da primeira turma.

---

## 22. Próximos passos imediatos

1. revisar este documento e corrigir lacunas;
2. escrever uma definição de uma página da profissão;
3. preparar uma apresentação curta para conversas iniciais;
4. conversar com a TYLKO;
5. conversar informalmente com Daniel Nascimento;
6. ligar para Tadeu e Marcelo Congro;
7. conversar com Aidan Mercer no encontro previsto;
8. confirmar o nome e o cargo de Claudio Bessi e apresentar a proposta;
9. formar um pequeno grupo de discussão;
10. esboçar a matriz curricular;
11. definir um modelo de briefcase como projeto final;
12. mapear caminhos de pós-graduação no Brasil e na Europa;
13. planejar a primeira ação pública de conscientização somente depois de haver uma proposta formativa minimamente estruturada.

---

## 23. Síntese final

A proposta não é publicar um novo nome no LinkedIn e esperar que o mercado o adote.

A proposta é:

1. reconhecer uma função profissional que já existe de forma fragmentada;
2. defini-la com clareza;
3. organizar suas competências;
4. criar uma pós-graduação para formar profissionais;
5. estabelecer o briefcase como artefato central da prática;
6. articular instituições e pessoas com competências complementares;
7. formar as primeiras turmas;
8. conscientizar continuamente empresas, profissionais e academia;
9. criar certificação quando houver maturidade suficiente;
10. ampliar a capacidade de organizações criarem soluções adequadas independentemente de existir um produto comercial para cada necessidade.

Em sua formulação mais direta:

> **Trata-se de formar profissionais capazes de estruturar dados, conhecimento, infraestrutura e interação para entregar informação confiável, just in time, por meio de briefcases aplicados a processos reais.**
