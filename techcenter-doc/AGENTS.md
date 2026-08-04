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

## 6. Estrutura obrigatória dos datasets `WorkStream`

Esta seção se aplica a **todo dataset cuja entidade seja `WorkStream`**, independentemente:

- do nome da pasta do dataset;
- de o dataset estar em `.workstream`, `desmobilizacao` ou qualquer outro diretório dentro de `techcenter-doc`;
- de ter sido criado manualmente, por comando, por gerador ou por automação;
- de o usuário ter pedido ou não, separadamente, a criação da fachada.

### 6.1 Estrutura mínima obrigatória

Todo dataset `WorkStream` deve conter, obrigatoriamente:

- `.__ontobdc__/dataset.ttl`;
- `.__ontobdc__/datapackage.json`;
- `.__ontobdc__/ro-crate-metadata.json`;
- `.__ontobdc__/linkset/facade.ttl`;
- o workbook real da entidade dentro de `payload/document/`.

Para o modelo atual de `WorkStream`, o workbook é `payload/document/workstream.xlsx`, salvo quando o usuário determinar explicitamente outro nome.

### 6.2 Regra absoluta sobre `linkset/facade.ttl`

O arquivo `.__ontobdc__/linkset/facade.ttl` é **obrigatório** em todo dataset `WorkStream`.

Isso significa:

- não é opcional;
- não depende de solicitação explícita adicional do usuário;
- não é uma melhoria, um arquivo auxiliar, uma precaução ou uma extensão de escopo;
- não pode ser omitido sob a justificativa de que somente `dataset.ttl`, `datapackage.json` e `ro-crate-metadata.json` foram mencionados;
- não pode ser omitido porque uma etapa anterior ou uma lista resumida não o citou;
- a ausência de `linkset/facade.ttl` torna o dataset `WorkStream` incompleto e a tarefa não pode ser declarada concluída.

A antiga interpretação de que `.workstream/.__ontobdc__` deveria conter somente três arquivos está expressamente revogada. Nenhuma regra deste arquivo pode ser interpretada como autorização para omitir `linkset/facade.ttl` de um dataset `WorkStream`.

### 6.3 Fonte e consistência da fachada

- Usar a fachada canônica de `WorkStream` já adotada no projeto.
- Não inventar uma fachada nova nem alterar seus campos silenciosamente.
- `dataset.ttl` deve declarar conformidade com `WorkStreamFacade`.
- `datapackage.json` deve apontar a entidade e o recurso para a mesma `WorkStreamFacade`.
- `ro-crate-metadata.json` deve incluir `.__ontobdc__/linkset/facade.ttl` em `hasPart` e descrevê-lo como arquivo do dataset.
- O workbook deve ser compatível com os campos declarados pela fachada canônica.

### 6.4 Limite desta obrigação

A obrigatoriedade de `linkset/facade.ttl` não autoriza criar silenciosamente outros linksets, views, ontologias, anotações, arquivos ou diretórios.

Para qualquer outro artefato:

- verificar o estado atual do dataset;
- verificar o contrato do gerador ou comando aplicável;
- verificar a instrução explícita do usuário;
- não copiar estruturas adicionais de outro dataset apenas por analogia.

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
- o `PYODIDE RUNTIME` deve funcionar como rodapé da página, ocupando as 12 colunas abaixo da grade principal;
- o rodapé do `PYODIDE RUNTIME` deve ser largo e fino, com altura compacta e conteúdo distribuído horizontalmente em telas largas;
- o `PYODIDE RUNTIME` não deve permanecer na coluna esquerda nem aumentar verticalmente a área de `PROJECT INFORMATION`;
- todos os boxes devem possuir nome visível;
- os nomes devem descrever conteúdo real, sem categorias inventadas;
- quantidade, nomes, distribuição interna e valores dos indicadores não devem ser inventados quando ainda não estiverem definidos.

Desenho-base:

```text
       01    02    03    04    05    06    07    08    09    10    11    12
     ┌───────────────────────────────────────────────┬────────────────────────┐
L01  │ HERO / PROJECT HEADER                         │ GRID DE INDICADORES    │
L02  │                                               │                        │
     ├───────────────────────────────────────────────┤                        │
L03  │ BARRA DE NAVEGAÇÃO / AÇÕES                    │                        │
     └───────────────────────────────────────────────┴────────────────────────┘
     ┌───────────────────────┬────────────────────────────────────────────────┐
L04  │ PROJECT INFORMATION   │                                                │
L05  │                       │                                                │
L06  │                       │             BOARD DE CONTEÚDO                  │
L07  │                       │                                                │
L08  │                       │                                                │
L09  │                       │                                                │
     └───────────────────────┴────────────────────────────────────────────────┘
     ┌────────────────────────────────────────────────────────────────────────┐
L10  │ PYODIDE RUNTIME — RODAPÉ LARGO E FINO                                 │
     └────────────────────────────────────────────────────────────────────────┘
        4 colunas                              8 colunas
```

Distribuição do topo:

```text
HERO / PROJECT HEADER:       colunas 01–08, linhas 01–02
BARRA DE NAVEGAÇÃO / AÇÕES:  colunas 01–08, linha 03
GRID DE INDICADORES:         colunas 09–12, linhas 01–03
PYODIDE RUNTIME:              colunas 01–12, rodapé abaixo da grade principal
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
8. Conferir os dados reais usados pela interface ou pelo dataset.
9. Quando a entidade for `WorkStream`, confirmar a existência de `.__ontobdc__/linkset/facade.ttl` e sua referência consistente em `dataset.ttl`, `datapackage.json` e `ro-crate-metadata.json`.
10. Alterar somente o necessário para cumprir a instrução e os contratos obrigatórios expressamente definidos neste arquivo.
11. Validar sintaxe e caminhos relativos.
12. Verificar o diff final contra a solicitação e contra este arquivo.
13. Informar objetivamente o que foi alterado e qualquer ponto que permaneça não definido.

## 11. Critério de decisão em caso de dúvida

Quando houver ambiguidade:

- não escolher silenciosamente uma interpretação;
- não usar “melhor prática” como autorização;
- não copiar uma solução de outro projeto por analogia;
- preservar o estado atual;
- executar apenas a parte inequivocamente definida;
- registrar o restante como não definido, salvo quando o usuário já tiver fornecido a resposta em conversa anterior ou em arquivo aplicável.

A regra sobre `.__ontobdc__/linkset/facade.ttl` em datasets `WorkStream` não é ambígua: o arquivo é obrigatório e deve ser criado ou preservado.

## 12. Critério de conclusão

Uma tarefa só está concluída quando:

- foi executada na branch correta;
- respeitou o diretório correto;
- não alterou arquivos fora do escopo;
- não criou requisitos ou conteúdo não solicitados;
- preservou nomes e estruturas obrigatórios;
- produziu exatamente o comportamento solicitado;
- o diff foi revisado em relação à instrução original;
- nenhuma regra deste arquivo foi violada;
- quando envolver um dataset `WorkStream`, `.__ontobdc__/linkset/facade.ttl` existe e está corretamente referenciado nos metadados do dataset.

Na dúvida, não improvisar. Verificar os arquivos existentes. Caso a informação continue ausente, declarar a ausência em vez de inventar uma resposta ou implementação.

A criatividade do agente não é requisito deste trabalho. Fidelidade às instruções é.
