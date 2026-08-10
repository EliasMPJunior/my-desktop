# Manual de Organização da Informação Empresarial

**Versão:** 1.1  
**Data:** 10/08/2026  
**Objetivo:** estabelecer uma estrutura empresarial simples de navegar, semanticamente coerente e sustentável para organizar documentos, dados e conhecimento.

---

## 1. Princípio de organização

A informação deve ser classificada prioritariamente pelo **contexto empresarial para o qual ela existe**, seguindo esta hierarquia:

```text
Empresa
└── Função ou área de informação
    └── Processo, atividade ou assunto
        └── Dossiê, tipo de informação ou ativo de conhecimento
            └── Documento, dado ou artefato
```

Exemplo:

```text
Empresa
└── Financeiro
    └── Contas a pagar
        └── Pagamento CP-2026-0001
            ├── Nota fiscal
            ├── Aprovação
            └── Comprovante
```

A estrutura deve permitir que uma pessoa que não participou da criação da informação consiga prever onde procurá-la.

**Fundamentação:**

- **ISO/TR 26122:2008:** análise funcional, decompondo funções em processos, e análise sequencial do fluxo de transações.
- **ISO 15489-1:2016:** classificação e gestão dos registros segundo seu contexto de negócio.
- **DIRKS / Business Classification Scheme:** organização hierárquica por função, atividade e transação.
- **Arquitetura da Informação:** organização e rotulagem orientadas à usabilidade e à encontrabilidade.

---

## 2. Estrutura principal recomendada

```text
Empresa/
├── 00_Governanca_e_Estrategia/
├── 01_Financeiro/
├── 02_Comercial/
├── 03_Marketing_e_Comunicacao/
├── 04_Clientes/
├── 05_Operacoes/
├── 06_Projetos/
├── 07_Engenharia_e_Tecnologia/
├── 08_Pessoas/
├── 09_Compras_e_Fornecedores/
├── 10_Juridico_e_Compliance/
├── 11_Qualidade_e_Seguranca/
├── 12_TI_e_Dados/
└── 90_Arquivo_Corporativo/
```

Essas categorias representam **funções ou domínios de informação estáveis**, não necessariamente departamentos do organograma. A empresa pode alterar cargos, diretorias e responsáveis sem precisar reconstruir toda a classificação.

**Fundamentação:**

- **DIRKS / Business Classification Scheme:** funções como primeiro nível de classificação e atividades como segundo nível.
- **ISO/TR 26122:2008:** identificação das funções e processos reais da organização.
- **ISO 15489-1:2016:** análise recorrente do contexto empresarial e dos requisitos dos registros.
- **National Archives of Australia — Business Classification Scheme:** funções são áreas de responsabilidade; atividades são os principais processos executados para cumpri-las.

---

## 3. Estrutura interna das áreas

Não se deve repetir mecanicamente a mesma árvore em todas as áreas. Cada função deve ser dividida por seus processos e assuntos reais. O modelo abaixo serve apenas como referência:

```text
Area/
├── 00_Sobre_a_Area/
├── 01_Politicas_e_Diretrizes/
├── 02_Processos_e_Procedimentos/
├── 03_Operacao/
├── 04_Modelos_e_Ferramentas/
├── 05_Indicadores_e_Relatorios/
├── 06_Conhecimento_e_Referencias/
├── 07_Decisoes_e_Licoes_Aprendidas/
└── 90_Arquivo/
```

### 3.1 Convenção transversal de Triage

Sempre que um contexto possuir uma pasta de triagem, ela deve ser denominada **`00_Triage`** e ocupar a primeira posição da estrutura daquele contexto.

`00_Triage` é uma **área de entrada e classificação temporária**: recebe materiais recém-chegados, ainda não analisados ou cuja localização canônica ainda não foi determinada. Depois da triagem, o conteúdo deve ser classificado e movido para a pasta correspondente ao seu contexto empresarial.

A existência de `00_Triage` não significa que toda área precise obrigatoriamente de uma triagem própria. A regra é: **se houver Triage, Triage é sempre `00_Triage`**.

Não usar `00_Triage` como arquivo permanente, depósito genérico ou substituto de classificação.

Exemplo:

```text
Dossie_ou_Projeto/
├── 00_Triage/
├── 01_Contexto/
├── 02_Planejamento/
└── ...
```

**Fundamentação:** o uso de uma zona de entrada controlada preserva a separação entre material ainda não classificado e registros já contextualizados, sem alterar a localização canônica final definida pelos princípios da **ISO 15489-1:2016** e da análise funcional da **ISO/TR 26122:2008**.

### Significado das categorias

- `00_Sobre_a_Area`: escopo, responsabilidades, responsáveis, sistemas e mapa da área.
- `01_Politicas_e_Diretrizes`: regras de aplicação geral e decisões normativas internas.
- `02_Processos_e_Procedimentos`: instruções sobre como executar atividades.
- `03_Operacao`: registros e dossiês produzidos pela atividade cotidiana.
- `04_Modelos_e_Ferramentas`: formulários, templates, planilhas e utilitários reutilizáveis.
- `05_Indicadores_e_Relatorios`: consolidações, análises e acompanhamento de desempenho.
- `06_Conhecimento_e_Referencias`: glossários, normas, estudos e materiais de consulta.
- `07_Decisoes_e_Licoes_Aprendidas`: decisões relevantes, soluções validadas e aprendizado organizacional.
- `90_Arquivo`: informação encerrada, substituída ou sem uso corrente, mantida por valor histórico, administrativo ou legal.

**Fundamentação:**

- **ISO 15489-1:2016:** criação, captura, classificação e controle dos registros.
- **ISO 30401:2018:** criação, manutenção, compartilhamento e melhoria do conhecimento organizacional.
- **ISO 30301:2019:** política, responsabilidades, monitoramento e melhoria do sistema de gestão de registros.
- **Arquitetura da Informação:** agrupamentos coerentes e rótulos previsíveis.

---

## 4. Onde ficam os manuais

### 4.1 Manuais corporativos

Manuais aplicáveis a toda a empresa ficam em:

```text
Empresa/
└── 00_Governanca_e_Estrategia/
    └── Governanca_da_Informacao/
        └── Manuais_Corporativos/
```

Exemplos:

```text
Manual_de_Organizacao_da_Informacao.md
Manual_de_Nomenclatura_de_Arquivos.md
Manual_de_Classificacao_e_Acesso.md
```

### 4.2 Manuais específicos de uma função ou processo

Um manual específico deve ficar junto do processo que ele governa:

```text
Empresa/
└── 01_Financeiro/
    └── Contas_a_Pagar/
        └── Orientacoes_e_Procedimentos/
            └── Manual_de_Contas_a_Pagar.md
```

```text
Empresa/
└── 02_Comercial/
    └── Pre_Venda/
        └── Orientacoes_e_Procedimentos/
            └── Manual_de_Pre_Venda.md
```

### 4.3 Catálogo de manuais

A pasta de manuais corporativos deve conter um catálogo com links para todos os manuais vigentes, inclusive os que permanecem nas áreas específicas:

```text
Manuais_Corporativos/
├── README.md
├── Manual_de_Organizacao_da_Informacao.md
└── Manual_de_Classificacao_e_Acesso.md
```

O `README.md` funciona como índice. Não se deve duplicar fisicamente um manual específico apenas para fazê-lo aparecer no catálogo.

**Fundamentação:**

- **ISO 15489-1:2016:** preservação do contexto empresarial do registro.
- **ISO/TR 26122:2008:** associação da informação à função e ao processo que a produzem e utilizam.
- **ISO 23081-1:2017:** uso de metadados e relações para conectar registros, processos e responsáveis.
- **Arquitetura da Informação:** índices e caminhos alternativos de navegação para melhorar a encontrabilidade sem duplicação.

---

## 5. Estruturas recomendadas por área

## 5.1 Financeiro

```text
01_Financeiro/
├── 00_Sobre_o_Financeiro/
├── 01_Politicas_e_Diretrizes/
├── 02_Planejamento_Orcamentario/
├── 03_Contas_a_Pagar/
├── 04_Contas_a_Receber/
├── 05_Faturamento/
├── 06_Fluxo_de_Caixa_e_Tesouraria/
├── 07_Contabilidade_e_Tributos/
├── 08_Indicadores_e_Relatorios/
├── 09_Modelos_e_Ferramentas/
└── 90_Arquivo/
```

**Fundamentação:** classificação funcional e análise de processos da **ISO/TR 26122:2008**, **ISO 15489-1:2016** e **DIRKS/Business Classification Scheme**.

## 5.2 Comercial

```text
02_Comercial/
├── 00_Sobre_o_Comercial/
├── 01_Estrategia_Comercial/
├── 02_Produtos_e_Servicos/
├── 03_Pre_Venda/
│   ├── Orientacoes_e_Procedimentos/
│   ├── Oportunidades/
│   ├── Demonstracoes/
│   └── Modelos/
├── 04_Propostas/
├── 05_Negociacoes/
├── 06_Contratos_e_Handover/
├── 07_Inteligencia_Comercial/
├── 08_Indicadores/
└── 90_Arquivo/
```

**Fundamentação:** função comercial decomposta em atividades e transações conforme **ISO/TR 26122:2008** e **DIRKS/Business Classification Scheme**; preservação do contexto da oportunidade conforme **ISO 15489-1:2016**.

## 5.3 Marketing e Comunicação

```text
03_Marketing_e_Comunicacao/
├── 00_Sobre_o_Marketing/
├── 01_Marca_e_Identidade/
├── 02_Planejamento_e_Calendario/
├── 03_Campanhas/
├── 04_Canais/
├── 05_Conteudos/
├── 06_Eventos_e_Imprensa/
├── 07_Pesquisas_de_Mercado/
├── 08_Indicadores/
├── 09_Modelos_e_Ativos/
└── 90_Arquivo/
```

**Fundamentação:** **Arquitetura da Informação** para agrupar conteúdo segundo tarefas e expectativas dos usuários; **ISO 25964-1:2011** para padronização de termos, categorias e sinônimos; **ISO 15489-1:2016** para registros de campanhas, aprovações e publicações.

## 5.4 Clientes

```text
04_Clientes/
├── 00_Cadastro_e_Visao_Geral/
├── 01_Clientes_Ativos/
│   └── Cliente_X/
│       ├── Informacoes_Gerais/
│       ├── Contratos/
│       ├── Comunicacoes_Relevantes/
│       ├── Projetos_e_Servicos/
│       ├── Decisoes/
│       └── Historico/
├── 02_Clientes_Inativos/
└── 90_Arquivo/
```

Documentos cuja função principal é comercial, financeira ou de projeto devem permanecer em suas áreas canônicas e ser relacionados ao cliente por links ou metadados.

**Fundamentação:** localização canônica da **ISO 15489-1:2016**; relações contextuais e metadados da **ISO 23081-1:2017**; navegação transversal da **Arquitetura da Informação**.

## 5.5 Operações

```text
05_Operacoes/
├── 00_Sobre_as_Operacoes/
├── 01_Mapa_de_Processos/
├── 02_Procedimentos_Operacionais/
├── 03_Planejamento_Operacional/
├── 04_Execucao_por_Servico/
├── 05_Controle_e_Monitoramento/
├── 06_Ocorrencias_e_Problemas/
├── 07_Melhoria_Continua/
├── 08_Modelos_Checklists_e_Ferramentas/
├── 09_Indicadores/
├── 10_Licoes_Aprendidas/
└── 90_Arquivo/
```

**Fundamentação:** análise funcional e sequencial da **ISO/TR 26122:2008**; controle dos registros da **ISO 15489-1:2016**; aprendizado e reutilização da **ISO 30401:2018**.

## 5.6 Projetos

Em projetos ativos, `00_Triage` é obrigatório como ponto inicial de entrada de materiais ainda não classificados. As demais pastas mantêm localização semântica estável; documentos devem sair de `00_Triage` assim que forem classificados.

```text
06_Projetos/
├── 00_Gestao_de_Projetos/
│   ├── Metodologia/
│   ├── Manuais_e_Procedimentos/
│   ├── Modelos/
│   ├── Indicadores/
│   └── Licoes_Aprendidas/
├── 01_Projetos_Ativos/
│   └── PRJ-2026-001_Projeto_Alfa/
│       ├── 00_Triage/
│       ├── 01_Sobre_o_Projeto/
│       ├── 02_Contrato_e_Escopo/
│       ├── 03_Planejamento/
│       ├── 04_Entradas_e_Referencias/
│       ├── 05_Desenvolvimento/
│       ├── 06_Entregas/
│       ├── 07_Reunioes_e_Decisoes/
│       ├── 08_Riscos_e_Pendencias/
│       ├── 09_Relatorios/
│       └── 10_Licoes_Aprendidas/
├── 02_Projetos_Suspensos/
└── 90_Projetos_Encerrados/
```

**Fundamentação:** contexto, dossiês e agregações de registros da **ISO 15489-1:2016**; análise de processos da **ISO/TR 26122:2008**; gestão do conhecimento e lições aprendidas da **ISO 30401:2018**.

## 5.7 Engenharia e Tecnologia

```text
07_Engenharia_e_Tecnologia/
├── 00_Sobre_a_Area/
├── 01_Dominios_Tecnicos/
├── 02_Normas_e_Requisitos/
├── 03_Metodos_e_Procedimentos/
├── 04_Padroes_Tecnicos/
├── 05_Modelos_e_Ferramentas/
├── 06_Solucoes_Reutilizaveis/
├── 07_Problemas_Conhecidos/
├── 08_Licoes_Aprendidas/
├── 09_Pesquisa_e_Inovacao/
└── 90_Obsoleto/
```

**Fundamentação:** domínios e ativos de conhecimento da **ISO 30401:2018**; vocabulário controlado e relações conceituais da **ISO 25964-1:2011**; controle de documentos e versões da **ISO 15489-1:2016**.

## 5.8 Pessoas

```text
08_Pessoas/
├── 00_Sobre_a_Area/
├── 01_Politicas/
├── 02_Estrutura_Organizacional/
├── 03_Funcoes_e_Competencias/
├── 04_Recrutamento_e_Selecao/
├── 05_Admissao_e_Onboarding/
├── 06_Desenvolvimento_e_Treinamento/
├── 07_Avaliacao_e_Desempenho/
├── 08_Comunicacao_Interna/
├── 09_Modelos_e_Formularios/
├── 10_Indicadores/
└── 90_Arquivo/
```

Separar conteúdo compartilhado de registros pessoais e trabalhistas restritos.

**Fundamentação:** classificação funcional da **ISO/TR 26122:2008**; registros e controle de acesso da **ISO 15489-1:2016**; gestão de riscos e acesso da **ISO/IEC 27001:2022** e controles da **ISO/IEC 27002:2022**.

## 5.9 Compras e Fornecedores

```text
09_Compras_e_Fornecedores/
├── 00_Sobre_a_Area/
├── 01_Politicas_e_Procedimentos/
├── 02_Cadastro_e_Homologacao/
├── 03_Cotacoes_e_Selecoes/
├── 04_Pedidos_de_Compra/
├── 05_Contratos_de_Fornecimento/
├── 06_Avaliacao_de_Fornecedores/
├── 07_Catalogos_e_Referencias/
├── 08_Indicadores/
└── 90_Arquivo/
```

**Fundamentação:** função, atividade e transação da **ISO/TR 26122:2008** e **DIRKS/Business Classification Scheme**; dossiês e rastreabilidade da **ISO 15489-1:2016**.

## 5.10 Jurídico e Compliance

```text
10_Juridico_e_Compliance/
├── 00_Sobre_a_Area/
├── 01_Politicas_e_Diretrizes/
├── 02_Contratos/
├── 03_Pareceres_e_Consultas/
├── 04_Obrigacoes_Legais/
├── 05_Contencioso/
├── 06_Protecao_de_Dados/
├── 07_Compliance_e_Integridade/
├── 08_Modelos/
└── 90_Arquivo/
```

**Fundamentação:** contexto, autenticidade, integridade, retenção e acesso da **ISO 15489-1:2016**; governança da **ISO 30301:2019**; segurança da informação da **ISO/IEC 27001:2022** e **ISO/IEC 27002:2022**.

## 5.11 Qualidade e Segurança

```text
11_Qualidade_e_Seguranca/
├── 00_Sobre_a_Area/
├── 01_Politicas_e_Sistema_de_Gestao/
├── 02_Procedimentos/
├── 03_Inspecoes_e_Auditorias/
├── 04_Nao_Conformidades/
├── 05_Acoes_Corretivas_e_Preventivas/
├── 06_Ocorrencias_e_Incidentes/
├── 07_Indicadores/
├── 08_Licoes_Aprendidas/
└── 90_Arquivo/
```

**Fundamentação:** registros e evidências da **ISO 15489-1:2016**; sistema de gestão e melhoria da **ISO 30301:2019**; conhecimento organizacional da **ISO 30401:2018**.

## 5.12 TI e Dados

```text
12_TI_e_Dados/
├── 00_Sobre_a_Area/
├── 01_Arquitetura_e_Padroes/
├── 02_Sistemas_e_Aplicacoes/
├── 03_Infraestrutura/
├── 04_Suporte_e_Operacao/
├── 05_Desenvolvimento/
├── 06_Dados_e_Integracoes/
├── 07_Seguranca_da_Informacao/
├── 08_Continuidade_e_Recuperacao/
├── 09_Conhecimento_Tecnico/
└── 90_Arquivo/
```

**Fundamentação:** classificação funcional da **ISO/TR 26122:2008**; gestão de registros da **ISO 15489-1:2016**; segurança da **ISO/IEC 27001:2022** e **ISO/IEC 27002:2022**; conhecimento técnico da **ISO 30401:2018**.

---

## 6. Caso obrigatório: contas a pagar

### 6.1 Localização

```text
Empresa/
└── 01_Financeiro/
    └── 03_Contas_a_Pagar/
```

A decomposição é:

```text
Gestao Financeira             ← função
└── Gerenciar contas a pagar  ← atividade ou processo
    └── Obrigação de pagamento ← transação ou dossiê
```

**Fundamentação:** **ISO/TR 26122:2008**, **ISO 15489-1:2016** e **DIRKS/Business Classification Scheme**.

### 6.2 Estrutura recomendada

```text
03_Contas_a_Pagar/
├── 00_Orientacoes_e_Procedimentos/
│   ├── Manual_de_Contas_a_Pagar.md
│   ├── Processo_de_Contas_a_Pagar.md
│   └── Regras_de_Aprovacao.md
├── 01_Controle/
│   └── Registro_de_Contas_a_Pagar.xlsx
├── 02_Dossies_de_Pagamento/
│   └── 2026/
│       └── CP-2026-0001_Fornecedor_ABC/
│           ├── Documento_de_Cobranca.pdf
│           ├── Aprovacao.pdf
│           ├── Comprovante_de_Pagamento.pdf
│           └── Comunicacao_Relevante.pdf
├── 03_Relatorios_e_Conciliacoes/
└── 90_Arquivo/
```

### 6.3 Lista de controle

A lista deve ser um registro mestre, e não uma coleção desconectada dos documentos. Campos recomendados:

```text
ID
Fornecedor
Documento
Descrição
Data de emissão
Data de vencimento
Valor
Status
Responsável
Centro de custo
Projeto
Link para o dossiê
```

**Fundamentação:** metadados e relações da **ISO 23081-1:2017**; contexto e controle da **ISO 15489-1:2016**.

### 6.4 Status

Não usar `Pendente`, `Aprovado` e `Pago` como pastas principais. O dossiê permanece em posição estável e o status é registrado na lista ou nos metadados.

```text
02_Dossies_de_Pagamento/
└── 2026/
    └── CP-2026-0001_Fornecedor_ABC/
```

```text
status: pago
```

**Fundamentação:** **ISO 23081-1:2017**, **ISO 15489-1:2016** e **classificação facetada**. O contexto da transação é estável; o estado é variável.

---

## 7. Caso obrigatório: desenvolvimento temporário para apresentação ao cliente

## 7.1 Antes da contratação

Quando o desenvolvimento existe para apoiar uma oportunidade, demonstração ou proposta, sua localização principal é Comercial/Pré-venda:

```text
Empresa/
└── 02_Comercial/
    └── 03_Pre_Venda/
        └── Oportunidades/
            └── OPP-2026-014_Cliente_X/
```

Estrutura:

```text
OPP-2026-014_Cliente_X/
├── 00_Contexto_da_Oportunidade/
├── 01_Requisitos_e_Referencias/
├── 02_Desenvolvimento_WIP/
│   ├── Codigo/
│   ├── Dados_de_Teste/
│   ├── Mockups/
│   ├── Testes/
│   └── Rascunhos/
├── 03_Demonstracao/
│   ├── Versao_Apresentada/
│   ├── Roteiro/
│   ├── Slides/
│   └── Evidencias/
├── 04_Feedback_e_Decisoes/
└── 90_Encerramento/
```

O fato de haver código não transforma automaticamente o trabalho em informação de TI ou Engenharia. Sua função primária é apoiar uma oportunidade comercial.

**Fundamentação:** classificação pelo processo produtor da **ISO/TR 26122:2008**, **DIRKS/Business Classification Scheme** e preservação do contexto da **ISO 15489-1:2016**.

## 7.2 Depois da contratação

Se o desenvolvimento fizer parte de um serviço contratado, sua localização passa a ser o dossiê do projeto:

```text
Empresa/
└── 06_Projetos/
    └── 01_Projetos_Ativos/
        └── PRJ-2026-021_Cliente_X/
            └── 05_Desenvolvimento/
```

**Fundamentação:** mudança do contexto empresarial e do processo produtor conforme **ISO/TR 26122:2008** e **ISO 15489-1:2016**.

## 7.3 Extração de solução reutilizável

Se parte do desenvolvimento temporário tiver valor geral, criar uma versão generalizada em:

```text
Empresa/
└── 07_Engenharia_e_Tecnologia/
    └── 06_Solucoes_Reutilizaveis/
        └── Nome_da_Solucao/
```

Essa versão deve:

- remover dados e particularidades do cliente;
- possuir documentação e testes próprios;
- registrar a oportunidade ou projeto de origem;
- manter link para a versão apresentada;
- ser administrada como ativo técnico independente.

O dossiê comercial não deve ser movido nem substituído pela solução reutilizável. São dois objetos relacionados:

```text
Dossiê da oportunidade = evidência do trabalho comercial
Solução reutilizável   = ativo técnico extraído do trabalho
```

**Fundamentação:** criação, compartilhamento e reutilização do conhecimento da **ISO 30401:2018**; relações e proveniência documental da **ISO 23081-1:2017**; preservação do dossiê original da **ISO 15489-1:2016**.

---

## 8. Regras de nomenclatura

Os nomes devem revelar o conteúdo ou o processo representado.

### Usar

```text
00_Triage
Contas_a_Pagar
Modelos_de_Proposta
Relatorios_de_Faturamento
Manual_de_Pre_Venda.md
PRJ-2026-001_Projeto_Alfa
```

### Evitar

```text
Geral
Diversos
Outros
Documentos
Pasta_Nova
Temporario
Pasta_do_Joao
Final_agora_vai_3
```

Nomes de pessoas podem aparecer como responsáveis ou metadados, mas não devem ser a estrutura principal. O ano deve aparecer depois do assunto ou processo, e não como primeiro nível de toda a empresa.

**Fundamentação:** vocabulário controlado e recuperação da **ISO 25964-1:2011**; funções estáveis do **Business Classification Scheme**; encontrabilidade da **Arquitetura da Informação**.

---

## 9. Relações hierárquicas devem ser verdadeiras

A posição de um item na árvore afirma uma relação semântica. Por isso, esta estrutura é coerente:

```text
Financeiro
└── Contas_a_Pagar
```

Esta estrutura não é recomendada quando os termos não representam funções, processos, unidades ou códigos formalmente definidos:

```text
Cachorro_Quente
└── Pacaba
    └── Contas_a_Pagar
```

Ela:

- não representa o negócio;
- não fornece pistas de navegação;
- cria relações hierárquicas falsas;
- depende de conhecimento tácito;
- dificulta automação e integração;
- aumenta a chance de classificações divergentes.

Termos arbitrários podem ser usados como códigos somente quando mapeados explicitamente:

```text
codigo: PAC-02
termo_preferido: Contas a pagar
funcao: Gestão Financeira
```

**Fundamentação:** relações hierárquicas e vocabulário controlado da **ISO 25964-1:2011**; contexto empresarial da **ISO 15489-1:2016**; classificação funcional da **ISO/TR 26122:2008**; encontrabilidade da **Arquitetura da Informação**.

---

## 10. Uma localização oficial por informação

Cada documento ou conjunto de dados deve ter uma localização canônica. Quando for relevante para mais de uma área, usar:

- links;
- atalhos;
- metadados;
- páginas de índice;
- referências semânticas;
- visualizações e consultas.

Não criar cópias independentes em áreas diferentes.

`00_Triage` é explicitamente uma exceção **temporária de entrada**, não uma segunda localização canônica. Após a classificação, o item deve sair da triagem e permanecer apenas em sua localização oficial.

**Fundamentação:** autenticidade, integridade, confiabilidade e controle da **ISO 15489-1:2016**; relações da **ISO 23081-1:2017**; navegação transversal da **Arquitetura da Informação**.

---

## 11. Metadados mínimos

Para documentos e dossiês relevantes, registrar conforme aplicável:

```text
ID
Título
Descrição
Função ou área
Processo ou assunto
Tipo de informação
Responsável
Data de criação
Data de atualização
Status
Projeto
Cliente
Confidencialidade
Versão
Origem
Relações
Localização canônica
```

**Fundamentação:** **ISO 23081-1:2017**, que estabelece princípios para metadados de registros e para os processos que os afetam; **ISO 15489-1:2016**, para contexto, captura e gestão.

---

## 12. Acesso e confidencialidade

A classificação temática não substitui a classificação de segurança. Informações financeiras, pessoais, jurídicas, estratégicas ou de clientes podem exigir acesso restrito independentemente de sua posição na árvore.

Exemplo:

```text
08_Pessoas/
├── Compartilhado/
└── Restrito/
```

As permissões devem seguir necessidade de acesso, responsabilidade e risco. A existência de uma pasta não significa que todos devam enxergar seu conteúdo.

**Fundamentação:** sistema de gestão de segurança da informação da **ISO/IEC 27001:2022** e controles de segurança da **ISO/IEC 27002:2022**; controles de acesso e gestão de registros da **ISO 15489-1:2016**.

---

## 13. Arquivamento e conteúdo obsoleto

Conteúdo encerrado, substituído ou sem uso corrente deve ser movido para `90_Arquivo` ou `90_Obsoleto` dentro de seu próprio contexto funcional.

```text
Financeiro/
└── Contas_a_Pagar/
    └── 90_Arquivo/
```

```text
Engenharia_e_Tecnologia/
└── Padroes_Tecnicos/
    └── 90_Obsoleto/
```

Não criar um arquivo corporativo sem preservar a origem funcional. O conteúdo arquivado deve manter metadados de origem, período, versão, responsável e motivo do arquivamento.

**Fundamentação:** ciclo de vida, retenção, contexto e controle da **ISO 15489-1:2016**; metadados da **ISO 23081-1:2017**; governança da **ISO 30301:2019**.

---

## 14. Validação da estrutura

Antes de estabilizar ou ampliar a taxonomia:

1. realizar inventário do conteúdo existente;
2. identificar funções, processos e tarefas reais;
3. testar os nomes com pessoas que procuram a informação;
4. aplicar **card sorting** para verificar agrupamentos esperados;
5. aplicar **tree testing** com tarefas concretas;
6. corrigir caminhos com baixa taxa de acerto;
7. revisar periodicamente termos, duplicações e pastas sem conteúdo definido.

Exemplos de tarefas de teste:

- “Onde você procuraria o formulário de reembolso?”
- “Onde está a versão apresentada ao Cliente X?”
- “Onde fica o manual de contas a pagar?”
- “Onde encontro a solução técnica reutilizável criada em uma pré-venda?”

**Fundamentação:** **Arquitetura da Informação**, **card sorting** e **tree testing** para validar modelo mental, agrupamento, rotulagem e encontrabilidade; melhoria contínua da **ISO 30301:2019** e **ISO 30401:2018**.

---

## 15. Matriz de fundamentação

| Decisão | Fundamentação principal |
|---|---|
| Dividir a empresa em áreas ou funções | DIRKS/Business Classification Scheme; ISO/TR 26122:2008 |
| Decompor áreas em processos e atividades | ISO/TR 26122:2008 |
| Associar documentos ao processo que os produziu | ISO 15489-1:2016 |
| Usar dossiês para transações e casos | ISO 15489-1:2016; DIRKS/BCS |
| Relacionar listas, documentos e responsáveis | ISO 23081-1:2017 |
| Padronizar nomes, sinônimos e hierarquias | ISO 25964-1:2011 |
| Organizar para navegação e encontrabilidade | Arquitetura da Informação |
| Validar agrupamentos e caminhos | Card sorting e tree testing |
| Preservar e reutilizar conhecimento | ISO 30401:2018 |
| Governar e melhorar o sistema | ISO 30301:2019 |
| Restringir informações sensíveis | ISO/IEC 27001:2022; ISO/IEC 27002:2022 |
| Manter uma localização canônica | ISO 15489-1:2016; ISO 23081-1:2017 |
| Tratar status como metadado | ISO 23081-1:2017; classificação facetada |
| Reservar `00_Triage` para entrada temporária | ISO 15489-1:2016; ISO/TR 26122:2008 |

---

## 16. Referências

Edições e fontes consultadas em 03/08/2026:

- [ISO 15489-1:2016 — Information and documentation — Records management — Part 1: Concepts and principles](https://www.iso.org/standard/62542.html)
- [ISO/TR 26122:2008 — Information and documentation — Work process analysis for records](https://www.iso.org/standard/43391.html)
- [ISO 23081-1:2017 — Information and documentation — Records management processes — Metadata for records — Part 1: Principles](https://www.iso.org/standard/73172.html)
- [ISO 25964-1:2011 — Information and documentation — Thesauri and interoperability with other vocabularies — Part 1](https://www.iso.org/standard/53657.html)
- [ISO 30301:2019 — Information and documentation — Management systems for records — Requirements](https://www.iso.org/standard/74292.html)
- [ISO 30401:2018 — Knowledge management systems — Requirements](https://www.iso.org/standard/68683.html)
- [ISO/IEC 27001:2022 — Information security management systems — Requirements](https://www.iso.org/standard/27001.html)
- [ISO/IEC 27002:2022 — Information security controls](https://www.iso.org/standard/75652.html)
- [National Archives of Australia — Classifying information](https://www.naa.gov.au/information-management/describing-information/classifying-information)
- [National Archives of Australia — Develop a Business or Records Classification Scheme](https://www.naa.gov.au/information-management/describing-information/classifying-information/develop-business-or-records-classification-scheme)
- [Information Architecture Institute — What is Information Architecture?](https://www.iainstitute.org/sites/default/files/what_is_ia.pdf)
- [Nielsen Norman Group — Card Sorting](https://www.nngroup.com/articles/card-sorting-definition/)
- [Nielsen Norman Group — Tree Testing](https://www.nngroup.com/articles/tree-testing/)