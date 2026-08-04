# Instruções obrigatórias para trabalho em `techcenter-doc`

Este arquivo define as regras operacionais obrigatórias para qualquer agente, assistente ou automação que trabalhe neste diretório.

## 1. Escopo e autoridade

- Repositório: `EliasMPJunior/my-desktop`.
- Branch obrigatória: `techcenter-labsea`.
- Diretório de trabalho: `techcenter-doc`.
- Não trabalhar em `master`, em outra branch ou em outro diretório sem instrução explícita do usuário.
- As instruções explícitas do usuário na conversa têm precedência sobre convenções, preferências do agente, padrões genéricos e suposições.
- Quando este arquivo e uma instrução explícita posterior do usuário divergirem, seguir a instrução explícita mais recente e atualizar este arquivo somente se o usuário solicitar.

## 2. Regra fundamental

Tratar cada instrução do usuário como contrato operacional.

Isso significa:

- não completar lacunas por conta própria;
- não inventar requisitos;
- não ampliar o escopo;
- não substituir a solicitação por uma solução considerada “melhor”;
- não refatorar, reorganizar, renomear ou modernizar elementos sem autorização explícita;
- não criar dados, conteúdo, nomenclaturas, caminhos ou estruturas exemplificativas quando estiverem ausentes;
- quando algo não estiver definido, registrar objetivamente que **não está definido**;
- antes de alterar qualquer arquivo, ler o estado atual da branch e os arquivos diretamente envolvidos;
- usar o estado atual do repositório como fonte de verdade, sem confiar em cache, memória de versões anteriores ou padrões de outros projetos.

## 3. Contexto fixo do projeto

- O diretório correto é `techcenter-doc`.
- O link anteriormente fornecido com `techcenter-doco` contém erro de digitação e não representa um diretório válido.
- O nome original do container é `Real Estate Brazil (Official)-Obras - Exp LabSea2025`.
- Não renomear esse container sem instrução explícita.
- Manter a identificação `INFOBIM` por enquanto.
- Não substituir `INFOBIM`, alterar branding ou introduzir outra identificação sem autorização explícita.

## 4. Página e geração de visualização

- Os caminhos usados pela página devem ser relativos ao `index.html`.
- Não usar caminhos absolutos nem dependências de caminhos específicos da máquina da TechnipFMC ou de qualquer outro ambiente local.
- A execução de `ontobdc view` deve reproduzir a página aprovada de forma idêntica.
- Não remover, acrescentar, reposicionar, renomear ou reinterpretar elementos da página aprovada por iniciativa própria.
- Não introduzir melhorias visuais, novos componentes, conteúdo de demonstração ou mudanças de UX sem solicitação explícita.
- A primeira seção da página deve ser `Frentes de Trabalho`.
- Remover ou manter ausentes da navegação principal os itens:
  - `Pranchas`;
  - `Documentos`;
  - `Fotos`;
  - `Mensagens`.

## 5. Estrutura de `.workstream/.__ontobdc__`

Na etapa definida para `.workstream/.__ontobdc__`, criar somente:

- `dataset.ttl`;
- `datapackage.json`;
- `ro-crate-metadata.json`.

Regras adicionais:

- não inventar uma nova estrutura de `view`;
- não criar arquivos adicionais nessa etapa sem instrução explícita;
- não replicar estruturas de outros containers por analogia;
- não assumir que um arquivo é necessário apenas porque aparece em outra implementação.

## 6. Nomenclatura e modelagem

- Não inventar nomenclaturas não padronizadas.
- Não usar nomes como `transformation_to_` ou equivalentes improvisados sem definição formal no projeto.
- Antes de introduzir um termo, verificar se ele já existe na ontologia, no código, nos dados ou nas instruções do usuário.
- Quando não houver termo definido, não criar um novo silenciosamente; informar que a nomenclatura ainda não está definida.
- Preservar nomes, identificadores, URIs, caminhos e estruturas existentes, salvo instrução explícita em contrário.

## 7. Proibições operacionais

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

## 8. Procedimento obrigatório antes de cada alteração

1. Confirmar que o repositório é `EliasMPJunior/my-desktop`.
2. Confirmar que a branch é `techcenter-labsea`.
3. Confirmar que o caminho está dentro de `techcenter-doc`.
4. Ler este arquivo.
5. Ler os arquivos diretamente afetados.
6. Identificar exatamente o que foi solicitado.
7. Separar fatos existentes de lacunas não definidas.
8. Alterar somente o necessário para cumprir a instrução.
9. Verificar o diff final contra a solicitação.
10. Informar objetivamente o que foi alterado e qualquer ponto que permaneça não definido.

## 9. Critério de decisão em caso de dúvida

Quando houver ambiguidade:

- não escolher silenciosamente uma interpretação;
- não usar “melhor prática” como autorização;
- não copiar uma solução de outro projeto por analogia;
- preservar o estado atual;
- executar apenas a parte inequivocamente definida;
- registrar o restante como não definido, salvo quando o usuário já tiver fornecido a resposta em conversa anterior ou em arquivo aplicável.

## 10. Critério de conclusão

Uma tarefa só está concluída quando:

- foi executada na branch correta;
- respeitou o diretório correto;
- não alterou arquivos fora do escopo;
- não criou requisitos ou conteúdo não solicitados;
- preservou nomes e estruturas obrigatórios;
- produziu exatamente o comportamento solicitado;
- o diff foi revisado em relação à instrução original.

A criatividade do agente não é requisito deste trabalho. Fidelidade às instruções é.
