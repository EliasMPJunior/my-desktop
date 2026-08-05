# Índice Remissivo de Entidades e Paths

**Versão:** 1.0  
**Data:** 05/08/2026  
**Escopo:** localização canônica de documentos, dados e artefatos empresariais por entidade semântica.

Este índice complementa:

- `manual-organizacao-da-informacao-empresarial.md`;
- `AGENT.md`.

Em caso de conflito, prevalece o manual. O índice não substitui a análise do contexto: ele fornece o path padrão mais provável e as regras para resolver casos recorrentes.

---

## 1. Regra de leitura

A busca deve começar pela **entidade representada ou pelo processo ao qual o arquivo serve**, e não pela extensão, pelo aplicativo, pela pessoa que criou o arquivo ou pela pasta em que ele foi encontrado.

```text
Entidade ou processo → localização canônica → dossiê contextual → arquivo
```

Exemplo:

```text
Extrato bancário
→ 01_Financeiro
→ 06_Fluxo_de_Caixa_e_Tesouraria
→ Extratos_Bancarios
→ Banco/Conta/Ano
→ arquivo
```

### Convenções

- `<Empresa>` representa a raiz empresarial.
- `<AAAA>` representa o ano.
- `<ID_Projeto>`, `<ID_Oportunidade>`, `<ID_Contrato>` e equivalentes representam identificadores estáveis.
- Paths com `<...>` exigem substituição pelo valor real.
- A localização indicada é **canônica**. Outros contextos devem usar links, atalhos ou metadados, sem duplicação física.
- Arquivos pessoais, trabalhistas, bancários, jurídicos ou sigilosos devem herdar controles de acesso compatíveis com sua sensibilidade.

---

## 2. Resposta direta: extrato bancário

O path canônico é:

```text
<Empresa>/
└── 01_Financeiro/
    └── 06_Fluxo_de_Caixa_e_Tesouraria/
        └── Extratos_Bancarios/
            └── <Banco>/
                └── <Conta>/
                    └── <AAAA>/
                        └── <arquivo>
```

Exemplo:

```text
01_Financeiro/
└── 06_Fluxo_de_Caixa_e_Tesouraria/
    └── Extratos_Bancarios/
        └── Banco_Itau/
            └── Conta_1234-5/
                └── 2026/
                    └── Extrato_2026-07.pdf
```

**Não colocar em:**

```text
01_Financeiro/Extratos_Bancarios/
Documentos/PDF/
Banco/
2026/
Pasta_do_Elias/
```

O banco, a conta, o ano e o formato são facetas subordinadas. A função empresarial estável é **Financeiro** e o processo é **Fluxo de Caixa e Tesouraria**.

---

## 3. Índice alfabético por entidade

| Entidade ou termos equivalentes | Path canônico | Regra de decisão |
|---|---|---|
| Ação corretiva | `<Empresa>/11_Qualidade_e_Seguranca/05_Acoes_Corretivas_e_Preventivas/<ID>/` | Manter evidência, responsável, prazo e verificação de eficácia no mesmo dossiê. |
| Ação preventiva | `<Empresa>/11_Qualidade_e_Seguranca/05_Acoes_Corretivas_e_Preventivas/<ID>/` | Não separar por status; registrar o estado em metadados. |
| Admissão | `<Empresa>/08_Pessoas/05_Admissao_e_Onboarding/<Pessoa>/` | Pasta restrita; separar materiais gerais de onboarding dos documentos pessoais. |
| Análise de mercado | `<Empresa>/03_Marketing_e_Comunicacao/07_Pesquisas_de_Mercado/` | Quando produzida para estratégia comercial específica, relacionar também a `02_Comercial/07_Inteligencia_Comercial/`. |
| Aprovação de pagamento | `<Empresa>/01_Financeiro/03_Contas_a_Pagar/02_Dossies_de_Pagamento/<AAAA>/<ID_Pagamento>/` | Integra o dossiê da obrigação; não criar uma coleção isolada de aprovações. |
| APR — Análise Preliminar de Risco, modelo | `<Empresa>/11_Qualidade_e_Seguranca/02_Procedimentos/Modelos/APR/` | Local do modelo corporativo reutilizável. |
| APR — Análise Preliminar de Risco, preenchida | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/04_Desenvolvimento/Seguranca/APR/` | O registro executado pertence ao projeto ou serviço onde foi aplicado; referenciar o modelo corporativo. |
| Arquitetura de sistemas | `<Empresa>/12_TI_e_Dados/01_Arquitetura_e_Padroes/` | Arquitetura de uma solução contratada também deve ser relacionada ao respectivo projeto. |
| Ata de reunião corporativa | `<Empresa>/00_Governanca_e_Estrategia/<Processo>/Reunioes_e_Decisoes/` | Classificar pelo processo decisório, não por uma pasta genérica `Reunioes`. |
| Ata de reunião de projeto | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/06_Reunioes_e_Decisoes/` | Manter decisões e encaminhamentos ligados à reunião. |
| Auditoria | `<Empresa>/11_Qualidade_e_Seguranca/03_Inspecoes_e_Auditorias/<ID_Auditoria>/` | Incluir plano, evidências, constatações e relatório no mesmo dossiê. |
| Avaliação de fornecedor | `<Empresa>/09_Compras_e_Fornecedores/06_Avaliacao_de_Fornecedores/<Fornecedor>/` | Relacionar ao cadastro canônico do fornecedor. |
| Avaliação de desempenho | `<Empresa>/08_Pessoas/07_Avaliacao_e_Desempenho/<Pessoa>/<Ciclo>/` | Conteúdo restrito; não misturar com indicadores gerais da empresa. |
| Backup e recuperação | `<Empresa>/12_TI_e_Dados/08_Continuidade_e_Recuperacao/` | Procedimentos, testes e evidências devem ser diferenciados por tipo documental. |
| Balanço patrimonial | `<Empresa>/01_Financeiro/07_Contabilidade_e_Tributos/Demonstracoes_Contabeis/<AAAA>/` | Preservar versão assinada ou oficialmente emitida. |
| Boleto a pagar | `<Empresa>/01_Financeiro/03_Contas_a_Pagar/02_Dossies_de_Pagamento/<AAAA>/<ID_Pagamento>/` | O boleto integra a obrigação, junto de nota fiscal, aprovação e comprovante. |
| Briefing de campanha | `<Empresa>/03_Marketing_e_Comunicacao/03_Campanhas/<ID_Campanha>/00_Briefing/` | Não armazenar separadamente da campanha que ele governa. |
| Cadastro de cliente | `<Empresa>/04_Clientes/00_Cadastro_e_Visao_Geral/<Cliente>/` | Informações comerciais, financeiras e de projeto permanecem em suas áreas canônicas e são apenas relacionadas ao cliente. |
| Cadastro de contatos e partes interessadas | `<Empresa>/00_Governanca_e_Estrategia/01_Cadastros_Corporativos/Partes_Interessadas_e_Contatos/` | Registro mestre corporativo; evitar listas paralelas por área. |
| Cadastro de fornecedor | `<Empresa>/09_Compras_e_Fornecedores/02_Cadastro_e_Homologacao/<Fornecedor>/` | Incluir documentação de homologação e relacionar contratos e avaliações. |
| Campanha de marketing | `<Empresa>/03_Marketing_e_Comunicacao/03_Campanhas/<ID_Campanha>/` | Reunir briefing, produção, aprovações, publicações, evidências e métricas. |
| Catálogo de fornecedor | `<Empresa>/09_Compras_e_Fornecedores/07_Catalogos_e_Referencias/<Fornecedor>/` | Catálogo usado exclusivamente por projeto pode ser referenciado nas entradas do projeto. |
| Certificado de treinamento | `<Empresa>/08_Pessoas/06_Desenvolvimento_e_Treinamento/Registros/<Pessoa>/` | Registros individuais restritos; material do curso fica em pasta própria de conteúdo. |
| Checklist operacional preenchido | `<Empresa>/05_Operacoes/04_Execucao_por_Servico/<Servico>/Registros/Checklists/` | O checklist executado é evidência operacional; o modelo fica em `08_Modelos_Checklists_e_Ferramentas`. |
| Código desenvolvido para demonstração comercial | `<Empresa>/02_Comercial/03_Pre_Venda/Oportunidades/<ID_Oportunidade>/02_Desenvolvimento_WIP/Codigo/` | A presença de código não torna o arquivo automaticamente pertencente a TI. |
| Código desenvolvido em projeto contratado | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/04_Desenvolvimento/Codigo/` | Manter requisitos, testes e versões relacionados ao projeto. |
| Código ou solução reutilizável | `<Empresa>/07_Engenharia_e_Tecnologia/06_Solucoes_Reutilizaveis/<Solucao>/` | Remover particularidades do cliente e preservar a proveniência do projeto ou oportunidade de origem. |
| Comprovante de pagamento | `<Empresa>/01_Financeiro/03_Contas_a_Pagar/02_Dossies_de_Pagamento/<AAAA>/<ID_Pagamento>/` | Pertence ao mesmo dossiê da obrigação quitada. |
| Comunicação relevante com cliente | Local canônico do processo ao qual a comunicação se refere | Contrato → Jurídico; oportunidade → Comercial; projeto → Projeto; cobrança → Financeiro. Não criar um arquivo universal de e-mails por cliente. |
| Conciliação bancária | `<Empresa>/01_Financeiro/06_Fluxo_de_Caixa_e_Tesouraria/Conciliacoes_Bancarias/<AAAA>/` | Relacionar aos extratos e aos lançamentos conciliados. |
| Conta a pagar | `<Empresa>/01_Financeiro/03_Contas_a_Pagar/02_Dossies_de_Pagamento/<AAAA>/<ID_Pagamento>/` | Uma obrigação corresponde a um dossiê estável. Status fica em metadados. |
| Conta a receber | `<Empresa>/01_Financeiro/04_Contas_a_Receber/02_Dossies_de_Recebimento/<AAAA>/<ID_Recebimento>/` | Reunir cobrança, evidências, recebimento e comunicações relevantes. |
| Contrato com cliente | `<Empresa>/10_Juridico_e_Compliance/02_Contratos/Clientes/<Cliente>/<ID_Contrato>/` | A oportunidade comercial e o projeto devem apontar para esta versão canônica. |
| Contrato de fornecedor | `<Empresa>/09_Compras_e_Fornecedores/05_Contratos_de_Fornecimento/<Fornecedor>/<ID_Contrato>/` | Quando o controle jurídico central for obrigatório, usar referência para `10_Juridico_e_Compliance/02_Contratos/`. |
| Contrato social e atos societários | `<Empresa>/00_Governanca_e_Estrategia/01_Cadastros_Corporativos/Documentos_Societarios/` | Tratar como documentação corporativa controlada e de acesso restrito. |
| Cotação de compra | `<Empresa>/09_Compras_e_Fornecedores/03_Cotacoes_e_Selecoes/<ID_Selecao>/` | Agrupar todas as propostas comparadas e a decisão de seleção. |
| Credencial, senha ou segredo | **Não armazenar como documento comum no Drive** | Usar cofre de segredos ou gerenciador de senhas aprovado. O Drive pode conter apenas instruções sem o segredo. |
| Currículo de candidato | `<Empresa>/08_Pessoas/04_Recrutamento_e_Selecao/<Vaga>/<Candidato>/` | Dado pessoal restrito; aplicar retenção e descarte adequados. |
| Decisão de projeto | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/06_Reunioes_e_Decisoes/Decisoes/` | Registrar contexto, autor, data, alternativas e impactos. |
| Demonstração comercial | `<Empresa>/02_Comercial/03_Pre_Venda/Oportunidades/<ID_Oportunidade>/03_Demonstracao/` | Guardar versão apresentada, roteiro, slides e evidências. |
| Desenho, prancha ou modelo técnico de projeto | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/04_Desenvolvimento/` | Organizar pela disciplina e entrega; padrões reutilizáveis ficam em Engenharia e Tecnologia. |
| DRE | `<Empresa>/01_Financeiro/07_Contabilidade_e_Tributos/Demonstracoes_Contabeis/<AAAA>/` | Manter competência, versão e aprovação identificáveis. |
| Documento fiscal recebido | `<Empresa>/01_Financeiro/03_Contas_a_Pagar/02_Dossies_de_Pagamento/<AAAA>/<ID_Pagamento>/` | Nota fiscal tomada deve integrar o dossiê da obrigação correspondente. |
| Documento fiscal emitido | `<Empresa>/01_Financeiro/05_Faturamento/Documentos_Fiscais_Emitidos/<AAAA>/` | Relacionar ao cliente, contrato, projeto e conta a receber. |
| Documento pessoal de colaborador | `<Empresa>/08_Pessoas/Registros_Restritos/<Pessoa>/Documentos_Pessoais/` | Acesso estritamente limitado; não armazenar em pastas compartilhadas gerais. |
| E-mail | Local canônico do assunto ou transação | E-mail não é função nem processo. Salvar junto ao contrato, pagamento, oportunidade, projeto, ocorrência ou decisão correspondente. |
| Entrega de projeto | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/05_Entregas/<ID_Entrega>/` | Preservar pacote emitido, protocolo, revisão e aceite. |
| Escopo de projeto | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/01_Contrato_e_Escopo/` | Relacionar à versão canônica do contrato. |
| Extrato bancário | `<Empresa>/01_Financeiro/06_Fluxo_de_Caixa_e_Tesouraria/Extratos_Bancarios/<Banco>/<Conta>/<AAAA>/` | Banco, conta e ano são níveis subordinados ao processo de tesouraria. |
| Fatura emitida | `<Empresa>/01_Financeiro/05_Faturamento/Faturas/<AAAA>/<ID_Fatura>/` | Relacionar à conta a receber e ao contrato ou projeto que originou a cobrança. |
| Feedback de cliente em oportunidade | `<Empresa>/02_Comercial/03_Pre_Venda/Oportunidades/<ID_Oportunidade>/04_Feedback_e_Decisoes/` | Não misturar com feedback de entrega contratada. |
| Feedback de cliente em projeto | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/06_Reunioes_e_Decisoes/Feedback/` | Relacionar à entrega, reunião ou decisão correspondente. |
| Fluxo de caixa | `<Empresa>/01_Financeiro/06_Fluxo_de_Caixa_e_Tesouraria/Fluxo_de_Caixa/<AAAA>/` | Diferenciar previsão, realizado e cenário. |
| Folha de pagamento | `<Empresa>/08_Pessoas/Registros_Restritos/Folha_de_Pagamento/<AAAA>/` | Registro altamente restrito; relatórios financeiros podem receber referência, não cópia. |
| Formulário reutilizável | Área responsável pelo processo, em `Modelos_e_Ferramentas` ou equivalente | O formulário preenchido pertence ao dossiê da operação em que foi usado. |
| Foto de execução de projeto | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/04_Desenvolvimento/Evidencias/Fotos/` | Registrar data, local, atividade, autor e relação com ocorrência ou entrega. |
| Guia ou obrigação tributária | `<Empresa>/01_Financeiro/07_Contabilidade_e_Tributos/Obrigacoes_Tributarias/<AAAA>/<Tributo>/` | Comprovante de pagamento pode ser relacionado ao respectivo dossiê financeiro. |
| Homologação de fornecedor | `<Empresa>/09_Compras_e_Fornecedores/02_Cadastro_e_Homologacao/<Fornecedor>/Homologacao/` | Manter documentos, critérios, aprovação e validade. |
| Incidente de segurança ou trabalho | `<Empresa>/11_Qualidade_e_Seguranca/06_Ocorrencias_e_Incidentes/<ID_Incidente>/` | Preservar comunicação, evidências, investigação, ações e encerramento. |
| Indicador corporativo | `<Empresa>/00_Governanca_e_Estrategia/Indicadores_Corporativos/` | Indicadores funcionais permanecem na área responsável e alimentam a visão corporativa por referência. |
| Inventário de ativos de TI | `<Empresa>/12_TI_e_Dados/03_Infraestrutura/Inventario_de_Ativos/` | Manter identificador, responsável, localização, estado e ciclo de vida. |
| Lição aprendida de projeto | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/09_Licoes_Aprendidas/` | Conhecimento generalizado pode ser promovido para Engenharia e Tecnologia sem remover o registro original. |
| Manual corporativo | `<Empresa>/00_Governanca_e_Estrategia/02_Gestao_da_Informacao/Manuais_Corporativos/` | O catálogo central deve apontar também para manuais específicos das áreas. |
| Manual de processo | Pasta do processo governado, em `00_Orientacoes_e_Procedimentos` ou equivalente | Não centralizar fisicamente todos os manuais e perder o contexto funcional. |
| Material de treinamento | `<Empresa>/08_Pessoas/06_Desenvolvimento_e_Treinamento/Conteudos/<Treinamento>/` | Certificados e presença individuais ficam em registros restritos ou controlados. |
| Modelo ou template de proposta | `<Empresa>/02_Comercial/03_Pre_Venda/Modelos/` | A proposta preenchida pertence à oportunidade ou ao dossiê de propostas. |
| Não conformidade | `<Empresa>/11_Qualidade_e_Seguranca/04_Nao_Conformidades/<ID_NC>/` | Relacionar inspeção, evidência, causa, ação corretiva e verificação. |
| NDA ou acordo de confidencialidade | `<Empresa>/10_Juridico_e_Compliance/02_Contratos/Acordos_de_Confidencialidade/<Organizacao>/<ID>/` | Relacionar à oportunidade, fornecedor, parceiro ou projeto correspondente. |
| Norma externa | `<Empresa>/07_Engenharia_e_Tecnologia/02_Normas_e_Requisitos/Normas_Externas/` | Respeitar licenciamento; preferir referência quando a cópia não puder ser redistribuída. |
| Nota fiscal emitida | `<Empresa>/01_Financeiro/05_Faturamento/Documentos_Fiscais_Emitidos/<AAAA>/` | Relacionar à fatura e à conta a receber. |
| Nota fiscal tomada | `<Empresa>/01_Financeiro/03_Contas_a_Pagar/02_Dossies_de_Pagamento/<AAAA>/<ID_Pagamento>/` | Não manter isolada em pasta por extensão ou apenas por mês. |
| Ocorrência operacional | `<Empresa>/05_Operacoes/06_Ocorrencias_e_Problemas/<ID_Ocorrencia>/` | Incidente de qualidade ou segurança deve usar o domínio específico de `11_Qualidade_e_Seguranca`. |
| Onboarding, material geral | `<Empresa>/08_Pessoas/05_Admissao_e_Onboarding/Conteudos_Gerais/` | Documentos individuais permanecem no dossiê restrito da pessoa. |
| Orçamento empresarial | `<Empresa>/01_Financeiro/02_Planejamento_Orcamentario/<AAAA>/` | Diferenciar orçamento aprovado, revisões, cenários e realizado. |
| Orçamento de projeto | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/02_Planejamento/Orcamento/` | Relacionar ao orçamento empresarial por centro de custo ou metadados. |
| Parecer jurídico | `<Empresa>/10_Juridico_e_Compliance/03_Pareceres_e_Consultas/<ID_Consulta>/` | Relacionar ao contrato, processo ou decisão que motivou a consulta. |
| Pedido de compra | `<Empresa>/09_Compras_e_Fornecedores/04_Pedidos_de_Compra/<AAAA>/<ID_Pedido>/` | Relacionar à seleção, fornecedor, contrato e pagamento. |
| Pesquisa ou artigo técnico | `<Empresa>/07_Engenharia_e_Tecnologia/09_Pesquisa_e_Inovacao/Referencias/` | Quando usado apenas como entrada de um projeto, criar referência em `03_Entradas_e_Referencias`. |
| Planejamento estratégico | `<Empresa>/00_Governanca_e_Estrategia/Planejamento_Estrategico/<Ciclo>/` | Reunir diagnóstico, objetivos, decisões, planos e acompanhamento. |
| Política corporativa | `<Empresa>/00_Governanca_e_Estrategia/Politicas_e_Diretrizes/` | Política específica pode ficar na área responsável, com entrada no catálogo corporativo. |
| Post ou conteúdo publicado | `<Empresa>/03_Marketing_e_Comunicacao/05_Conteudos/<Canal>/<AAAA>/` | Relacionar à campanha e preservar versão aprovada e evidência de publicação. |
| Procedimento operacional | `<Empresa>/05_Operacoes/02_Procedimentos_Operacionais/` | Se específico de qualidade, segurança, TI ou outra função, usar a área responsável. |
| Proposta comercial | `<Empresa>/02_Comercial/04_Propostas/<ID_Proposta>/` | Quando vinculada a oportunidade estruturada, pode permanecer dentro do dossiê da oportunidade e ser indexada aqui. |
| Proteção de dados e privacidade | `<Empresa>/10_Juridico_e_Compliance/06_Protecao_de_Dados/` | Controles técnicos relacionados permanecem em Segurança da Informação e são referenciados. |
| Recrutamento | `<Empresa>/08_Pessoas/04_Recrutamento_e_Selecao/<Vaga>/` | Separar divulgação, critérios, candidatos, entrevistas e decisão. |
| Relatório de projeto | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/08_Relatorios/` | Nomear por período, finalidade e revisão. |
| Relatório financeiro | `<Empresa>/01_Financeiro/08_Indicadores_e_Relatorios/` | Relatórios de um processo específico podem permanecer junto ao processo e ser indexados aqui. |
| Repositório de dados ou integração | `<Empresa>/12_TI_e_Dados/06_Dados_e_Integracoes/<Sistema_ou_Dominio>/` | Registrar esquema, origem, destino, responsável, atualização e regras de acesso. |
| Requisito técnico corporativo | `<Empresa>/07_Engenharia_e_Tecnologia/02_Normas_e_Requisitos/Requisitos_Internos/` | Requisito específico de projeto permanece nas entradas ou no desenvolvimento do projeto. |
| Risco de projeto | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/07_Riscos_e_Pendencias/` | Status, probabilidade, impacto e resposta ficam em metadados ou registro mestre. |
| RDO — Relatório Diário de Obra | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/08_Relatorios/RDO/<AAAA-MM>/` | Relacionar atividades, equipe, fotos, ocorrências e condições do dia. |
| Segurança da informação | `<Empresa>/12_TI_e_Dados/07_Seguranca_da_Informacao/` | Políticas corporativas gerais podem ter localização em Governança com referência técnica aqui. |
| Suporte de TI | `<Empresa>/12_TI_e_Dados/04_Suporte_e_Operacao/<Sistema_ou_Servico>/` | Chamados devem permanecer no sistema de suporte quando ele for o repositório oficial; guardar relatórios ou exportações, não cópias arbitrárias. |
| Termo de aceite de entrega | `<Empresa>/06_Projetos/01_Projetos_Ativos/<ID_Projeto>/05_Entregas/<ID_Entrega>/Aceite/` | Relacionar à versão exata do pacote aceito. |
| Treinamento realizado | `<Empresa>/08_Pessoas/06_Desenvolvimento_e_Treinamento/Registros/<Treinamento>/<Turma>/` | Incluir presença e avaliação; certificados individuais podem exigir acesso restrito. |
| Workstream ou frente de trabalho | Dossiê do projeto, operação, oportunidade ou estratégia que lhe dá contexto | `Workstream` é uma estrutura de execução, não uma área empresarial autônoma. |

---

## 4. Índice por path principal

### `00_Governanca_e_Estrategia`

- cadastros corporativos;
- contatos e partes interessadas;
- documentos societários;
- políticas e diretrizes corporativas;
- planejamento estratégico;
- governança e manuais da informação;
- indicadores corporativos;
- decisões de governança.

### `01_Financeiro`

- planejamento orçamentário;
- contas a pagar;
- contas a receber;
- faturamento;
- notas fiscais emitidas;
- fluxo de caixa;
- tesouraria;
- extratos bancários;
- conciliações bancárias;
- contabilidade e tributos;
- demonstrações e relatórios financeiros.

### `02_Comercial`

- estratégia comercial;
- produtos e serviços;
- oportunidades;
- pré-venda;
- demonstrações;
- propostas;
- negociações;
- handover comercial;
- inteligência comercial.

### `03_Marketing_e_Comunicacao`

- marca e identidade;
- calendário editorial;
- campanhas;
- canais;
- conteúdo;
- eventos e imprensa;
- pesquisas de mercado;
- ativos de comunicação.

### `04_Clientes`

- cadastro e visão geral do cliente;
- índice de contratos, projetos, comunicações e decisões;
- histórico do relacionamento;
- links para informações canônicas mantidas em outras funções.

### `05_Operacoes`

- mapa de processos;
- procedimentos operacionais;
- planejamento operacional;
- execução por serviço;
- monitoramento;
- ocorrências operacionais;
- melhoria contínua;
- checklists e ferramentas;
- indicadores e lições aprendidas.

### `06_Projetos`

- metodologia e governança de projetos;
- contrato e escopo de cada projeto;
- planejamento;
- entradas e referências;
- desenvolvimento;
- entregas;
- reuniões e decisões;
- riscos e pendências;
- relatórios;
- lições aprendidas;
- projetos suspensos e encerrados.

### `07_Engenharia_e_Tecnologia`

- domínios técnicos;
- normas e requisitos;
- métodos e procedimentos;
- padrões técnicos;
- modelos e ferramentas;
- soluções reutilizáveis;
- problemas conhecidos;
- conhecimento e lições técnicas;
- pesquisa e inovação.

### `08_Pessoas`

- estrutura organizacional;
- funções e competências;
- recrutamento;
- admissão e onboarding;
- treinamento;
- avaliação de desempenho;
- comunicação interna;
- registros pessoais e trabalhistas restritos.

### `09_Compras_e_Fornecedores`

- cadastro e homologação;
- cotações e seleções;
- pedidos de compra;
- contratos de fornecimento;
- avaliação de fornecedores;
- catálogos e referências.

### `10_Juridico_e_Compliance`

- contratos;
- acordos de confidencialidade;
- pareceres e consultas;
- obrigações legais;
- contencioso;
- proteção de dados;
- compliance e integridade.

### `11_Qualidade_e_Seguranca`

- sistema de gestão;
- procedimentos;
- inspeções e auditorias;
- não conformidades;
- ações corretivas e preventivas;
- ocorrências e incidentes;
- indicadores e lições aprendidas.

### `12_TI_e_Dados`

- arquitetura e padrões;
- sistemas e aplicações;
- infraestrutura;
- suporte e operação;
- desenvolvimento interno;
- dados e integrações;
- segurança da informação;
- continuidade e recuperação;
- conhecimento técnico de TI.

### `90_Arquivo_Corporativo`

- informação encerrada ou substituída que perdeu o contexto operacional imediato;
- conjuntos preservados por valor histórico, administrativo ou legal;
- conteúdo acompanhado de metadados de origem, retenção e motivo do arquivamento.

`90_Arquivo_Corporativo` não é lixeira nem destino para arquivos cuja classificação não foi compreendida.

---

## 5. Regras para entidades ambíguas

### 5.1 O mesmo tipo documental pode ter paths diferentes

A entidade aparente deve ser interpretada pelo processo:

```text
Apresentacao
├── para oportunidade comercial → 02_Comercial/03_Pre_Venda/...
├── para reunião de projeto     → 06_Projetos/.../06_Reunioes_e_Decisoes/...
├── institucional publicada     → 03_Marketing_e_Comunicacao/05_Conteudos/...
└── material de treinamento     → 08_Pessoas/06_Desenvolvimento_e_Treinamento/...
```

```text
Planilha
├── controle de contas a pagar  → 01_Financeiro/03_Contas_a_Pagar/01_Controle/
├── cronograma de projeto       → 06_Projetos/.../02_Planejamento/
├── cadastro de contatos        → 00_Governanca_e_Estrategia/01_Cadastros_Corporativos/...
└── inventário de ativos de TI  → 12_TI_e_Dados/03_Infraestrutura/Inventario_de_Ativos/
```

### 5.2 Distinguir modelo de registro preenchido

```text
Modelo reutilizável
→ área responsável pelo processo / Modelos_e_Ferramentas

Registro preenchido
→ dossiê da transação, projeto, serviço ou pessoa em que foi usado
```

### 5.3 Distinguir referência de evidência produzida

```text
Norma ou artigo consultado
→ Engenharia e Tecnologia / Normas ou Pesquisa

Cópia ou link usado em um projeto
→ Projeto / Entradas_e_Referencias
```

A localização canônica permanece no acervo técnico; o projeto registra a relação.

### 5.4 Distinguir entidade de status

Não criar como pastas principais:

```text
Pendente
Em andamento
Aprovado
Pago
Cancelado
Finalizado
```

Esses termos descrevem estado variável e devem ser metadados, campos de controle ou filtros.

---

## 6. Regra de extensão do índice

Quando uma entidade não estiver listada:

1. identificar a função empresarial para a qual a informação existe;
2. identificar o processo, atividade ou assunto;
3. identificar se o item é dossiê, registro, modelo, referência, relatório ou ativo reutilizável;
4. localizar a área e o processo mais próximos no manual;
5. propor um path semanticamente verdadeiro;
6. verificar se já existe localização canônica equivalente;
7. adicionar a nova entidade a este índice em ordem alfabética;
8. registrar sinônimos usados nas buscas;
9. não criar novas funções principais sem evidência de uma responsabilidade empresarial estável;
10. encaminhar para triagem quando a confiança for insuficiente.

Formato recomendado para nova entrada:

```text
| Entidade; sinônimo; abreviação | <path canônico> | Regra que diferencia os contextos possíveis. |
```

---

## 7. Critério de qualidade

Uma entrada é adequada quando uma pessoa consegue responder, sem conhecer quem criou o arquivo:

- qual função empresarial o produz ou utiliza;
- a qual processo ele pertence;
- qual entidade, transação, projeto ou obrigação lhe dá contexto;
- onde está a versão oficial;
- quais outros contextos apenas apontam para ela;
- quais metadados explicam seu estado e suas relações.

Uma árvore bem organizada deve explicar o negócio. Se ela só explica que um arquivo é PDF, Excel ou “do João”, o armário digital venceu a semântica.