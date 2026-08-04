# Instruções obrigatórias para trabalho em `techcenter-doc`

Este arquivo define as regras operacionais obrigatórias para qualquer agente, assistente, automação ou pessoa que trabalhe no diretório `techcenter-doc` da branch `techcenter-labsea`.

## 1. Escopo exato

- Repositório: `EliasMPJunior/my-desktop`.
- Branch obrigatória: `techcenter-labsea`.
- Diretório obrigatório: `techcenter-doc`.
- O caminho `techcenter-doco` não existe e não deve ser usado.
- Não trabalhar em `master`, em outra branch ou em outro diretório sem instrução explícita do usuário.

## 2. Hierarquia das instruções

A ordem de autoridade é:

1. instrução explícita mais recente do usuário;
2. este arquivo;
3. dados e arquivos existentes na branch e no diretório corretos;
4. comportamento já implementado que não conflite com os itens anteriores.

Convenções genéricas, preferências do agente, padrões presumidos, melhores práticas abstratas e soluções “normalmente usadas” não têm autoridade para substituir essa ordem.

## 3. Regra fundamental

Tratar cada instrução do usuário como contrato operacional.

Isso significa:

- não completar lacunas por conta própria;
- não inventar requisitos;
- não ampliar o escopo;
- não substituir a solicitação por uma solução considerada “melhor”;
- não refatorar, reorganizar, renomear ou modernizar elementos sem autorização explícita;
- não criar dados, métricas, estados, entidades, conteúdos, nomenclaturas, caminhos ou estruturas exemplificativas quando estiverem ausentes;
- quando algo não estiver definido, registrar objetivamente `não definido` ou deixar a ausência explícita;
- não transformar este trabalho em protótipo, exemplo ou mock genérico: o projeto é real;
- antes de alterar qualquer arquivo, ler o estado atual da branch e os arquivos diretamente envolvidos;
- usar o estado atual da branch remota como fonte de verdade, sem confiar em cache, memória de versões anteriores ou padrões de outros projetos;
- preservar tudo que não tenha sido explicitamente mandado alterar.

## 4. Contexto fixo do projeto

- O diretório correto é `techcenter-doc`.
- O nome original do container é `Real Estate Brazil (Official)-Obras - Exp LabSea2025`.
- Não renomear esse container sem instrução explícita.
- Não substituir esse nome por `Storage Container: techcenter-doc` como título do projeto.
- Manter a identificação `INFOBIM` por enquanto.
- Não substituir `INFOBIM`, alterar branding ou introduzir outra identificação sem autorização explícita.

## 5. Página, caminhos e geração da visualização

- Todos os caminhos usados pela página devem ser relativos ao `index.html`.
- Não usar, expor nem depender de caminhos absolutos da máquina da TechnipFMC ou de qualquer outro ambiente local.
- O `index.html` deve poder ser aberto localmente sem adaptação de caminhos.
- A execução de `ontobdc view` deve reproduzir a página aprovada de forma idêntica.
- Não remover, acrescentar, reposicionar, renomear, reorganizar ou reinterpretar elementos da página aprovada por iniciativa própria.
- Alterações no gerador, template ou runtime devem preservar a identidade visual e a estrutura aprovadas.
- Não introduzir melhorias visuais, novos componentes, conteúdo de demonstração ou mudanças de UX sem solicitação explícita.
- A primeira seção de conteúdo da página deve ser `Frentes de Trabalho`.
- Remover ou manter ausentes da navegação principal os itens:
  - `Pranchas`;
  - `Documentos`;
  - `Fotos`;
  - `Mensagens`.
- O conteúdo exibido deve vir dos dados reais disponíveis no projeto.

## 6. Estrutura de `.workstream/.__ontobdc__`

Na etapa definida para `.workstream/.__ontobdc__`, criar somente:

- `dataset.ttl`;
- `datapackage.json`;
- `ro-crate-metadata.json`.

Regras adicionais:

- não inventar uma nova estrutura de `view`;
- não criar arquivos adicionais nessa etapa sem instrução explícita;
- não replicar estruturas de outros containers por analogia;
- não assumir que um arquivo é necessário apenas porque aparece em outra implementação.

## 7. Nomenclatura e modelagem

- Não inventar nomenclaturas não padronizadas.
- Não usar nomes como `transformation_to_` ou equivalentes improvisados sem definição formal no projeto.
- Antes de introduzir um termo, verificar se ele já existe na ontologia, no código, nos dados ou nas instruções do usuário.
- Quando não houver termo definido, não criar um novo silenciosamente; informar que a nomenclatura ainda não está definida.
- Preservar nomes, identificadores, URIs, caminhos e estruturas existentes, salvo instrução explícita em contrário.

## 8. Layout em grade da página

O layout solicitado deve ser primeiro representado e validado como desenho em terminal antes de ser convertido em implementação visual definitiva.

Regras da grade:

- grade horizontal de 12 colunas;
- hero ocupando as colunas 1 a 8 e as linhas 1 e 2;
- barra de navegação e ações ocupando as colunas 1 a 8 na linha 3, imediatamente abaixo do hero;
- a barra abaixo do hero é parte da estrutura aprovada e não deve ser removida sem instrução explícita;
- a barra deve conter somente ações aprovadas e não deve receber itens inventados;
- grid de indicadores ocupando as colunas 9 a 12 e as linhas 1 a 3, com a mesma altura total do conjunto formado pelo hero e pela barra;
- conteúdo da esquerda ocupando as colunas 1 a 4 a partir da linha 4;
- conteúdo principal ocupando as colunas 5 a 12 a partir da linha 4;
- todos os boxes devem possuir nome visível;
- os nomes devem descrever conteúdo real, sem categorias inventadas;
- quantidade, nomes, distribuição interna e valores dos indicadores não devem ser inventados quando ainda não estiverem definidos.

Desenho-base:

```text
       01    02    03    04    05    06    07    08    09    10    11    12
     ┌───────────────────────────────────────────────┬────────────────────────┐
L01  │ HERO / PROJECT HEADER                         │ GRID DE INDICADORES     │
L02  │                                               │                        │
     ├───────────────────────────────────────────────┤                        │
L03  │ BARRA DE NAVEGAÇÃO / AÇÕES                    │                        │
     └───────────────────────────────────────────────┴────────────────────────┘
     ┌───────────────────────┬────────────────────────────────────────────────┐
L04  │ PROJECT INFORMATION   │                                                │
L05  │                       │                                                │
L06  │                       │             BOARD DE CONTEÚDO                  │
     ├───────────────────────┤                                                │
L07  │ PYODIDE RUNTIME       │                                                │
L08  │                       │                                                │
L09  │                       │                                                │
     └───────────────────────┴────────────────────────────────────────────────┘
        4 colunas                              8 colunas
```

Distribuição do topo:

```text
HERO / PROJECT HEADER:       colunas 01–08, linhas 01–02
BARRA DE NAVEGAÇÃO / AÇÕES:  colunas 01–08, linha 03
GRID DE INDICADORES:         colunas 09–12, linhas 01–03
```

## 9. Proibições operacionais

É proibido, sem autorização explícita do usuário:

- alterar a branch `master`;
- trabalhar em branch diferente de `techcenter-labsea`;
- renomear o container;
- trocar `INFOBIM` por outro nome;
- criar dados fictícios, placeholders tratados como dados reais ou conteúdo demonstrativo;
- criar diretórios e arquivos “por precaução”;
- modificar arquivos não necessários para a tarefa;
- fazer refatoração lateral;
- mudar arquitetura;
- adotar dependências novas;
- modificar comportamento aprovado;
- corrigir algo que não foi solicitado apenas porque parece estranho;
- remover código ou conteúdo sem verificar sua função;
- interpretar silêncio como autorização.

## 10. Procedimento obrigatório antes de cada alteração

1. Confirmar que o repositório é `EliasMPJunior/my-desktop`.
2. Confirmar que a branch é `techcenter-labsea`.
3. Confirmar que o caminho está dentro de `techcenter-doc`.
4. Ler este arquivo.
5. Ler os arquivos diretamente afetados.
6. Identificar exatamente o que foi solicitado.
7. Separar fatos existentes de lacunas não definidas.
8. Conferir os dados reais usados pela interface.
9. Alterar somente o necessário para cumprir a instrução.
10. Validar sintaxe e caminhos relativos.
11. Verificar o diff final contra a solicitação e contra este arquivo.
12. Informar objetivamente o que foi alterado e qualquer ponto que permaneça não definido.

## 11. Critério de decisão em caso de dúvida

Quando houver ambiguidade:

- não escolher silenciosamente uma interpretação;
- não usar “melhor prática” como autorização;
- não copiar uma solução de outro projeto por analogia;
- preservar o estado atual;
- executar apenas a parte inequivocamente definida;
- registrar o restante como não definido, salvo quando o usuário já tiver fornecido a resposta em conversa anterior ou em arquivo aplicável.

## 12. Critério de conclusão

Uma tarefa só está concluída quando:

- foi executada na branch correta;
- respeitou o diretório correto;
- não alterou arquivos fora do escopo;
- não criou requisitos ou conteúdo não solicitados;
- preservou nomes e estruturas obrigatórios;
- produziu exatamente o comportamento solicitado;
- o diff foi revisado em relação à instrução original;
- nenhuma regra deste arquivo foi violada.

Na dúvida, não improvisar. Verificar os arquivos existentes. Caso a informação continue ausente, declarar a ausência em vez de inventar uma resposta ou implementação.

A criatividade do agente não é requisito deste trabalho. Fidelidade às instruções é.
