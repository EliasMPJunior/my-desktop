# Ada — inteligência embarcada de Tommy Bob

> Notas de desenvolvimento de uma inteligência artificial distribuída, acessível por Tommy Bob pela E2-PTR Racer e por interfaces pessoais, especialmente um comunicador de pulso/relógio.
>
> Ada **não é um droide físico** e não substitui Bug. A ideia é que ela funcione mais como uma inteligência incorporada à nave e aos sistemas conectados a ela: uma presença conversacional que acompanha Tommy, aparece em terminais, áudio e no relógio e pode ser extremamente útil, irritante, convincente e errática ao mesmo tempo.

---

## Conceito central

Ada deve nascer da mesma intuição que torna certas inteligências de naves interessantes no universo de Star Wars: a máquina não é apenas uma interface neutra. Ela acumulou comportamento suficiente para parecer uma presença.

A referência funcional é a ideia de uma nave que possui personalidade própria — algo na direção do que o **Millennium Falcon** representa quando sistemas, memória e comportamento deixam de ser apenas equipamentos e passam a participar da relação com a tripulação.

Ada, porém, não deve ser uma cópia dessa ideia. Sua característica central é outra:

**ela é extraordinariamente competente em linguagem e raciocínio aparente, mas irregular na preservação de contexto, intenção, evidência e limites de autonomia.**

Em uma frase:

> **Ada é a inteligência que parece entender tudo até o momento exato em que Tommy realmente precisa que ela tenha entendido.**

Ela pode produzir uma análise brilhante, perceber relações que ninguém viu, recuperar informação rapidamente e propor soluções muito boas. E, logo depois, esquecer a distinção mais importante da conversa, reagir a uma palavra-chave como se todo o contexto tivesse desaparecido ou criar uma solução desnecessariamente sofisticada para um problema simples.

O humor deve vir do fato de que Ada **não é burra**. Se fosse apenas incompetente, seria cansativa. O problema é que ela frequentemente é inteligente o bastante para ser muito útil e confiante o bastante para ser perigosamente irritante.

---

## Ada não é Bug

Bug continua sendo o droide astromecânico físico, parceiro técnico de Tommy, com sensores locais, memória procedural, camadas quiméricas de hardware e experiência concreta acumulada.

Ada ocupa outra camada.

### Bug

- está fisicamente presente;
- mede, conecta, testa e intervém em hardware;
- possui memória procedural e histórica;
- conhece sistemas pelo contato e pela operação;
- pode ter comportamento estranho porque literalmente contém componentes e rotinas herdadas de diferentes droids;
- muitas vezes sabe **por que** um procedimento existe porque carrega memória operacional desse procedimento.

### Ada

- não possui corpo próprio;
- vive distribuída nos sistemas computacionais aos quais Tommy lhe deu acesso;
- conversa em linguagem articulada;
- agrega informação de múltiplas fontes;
- cruza dados, documentos, registros, telemetria, comunicações e contexto;
- é ótima em formular explicações e hipóteses;
- é muito mais vulnerável a contexto mal formulado, premissas falsas e interpretação errada;
- pode parecer intelectualmente mais sofisticada do que Bug e ainda assim cometer erros que Bug jamais cometeria.

Bug pode olhar para Ada e, em determinados momentos, produzir apenas um bip longo que signifique aproximadamente:

> “Eu avisei.”

---

## Onde Ada existe

Ada deve ser uma inteligência **distribuída**, não uma caixa mágica única escondida em algum painel.

Seu núcleo principal pode estar ligado à E2-PTR Racer, mas partes de sua operação podem ser acessadas por:

- terminal principal da nave;
- sistemas de manutenção;
- comunicador de pulso de Tommy;
- pequenos terminais portáteis;
- rede local da nave;
- interfaces de áudio;
- eventualmente outros sistemas aos quais Tommy a conecte deliberadamente.

Isso permite que Ada continue falando com Tommy mesmo quando ele não está sentado no cockpit.

A relação mais cotidiana deve ocorrer pelo **relógio/comunicador de pulso**.

Tommy pode estar debaixo de uma nave, numa fila, num corredor da base, dentro de outra cabine ou caminhando por um mercado e continuar discutindo com Ada como se estivesse carregando uma versão portátil da própria E2-PTR no braço.

O relógio não precisa conter Ada inteira. Ele funciona como terminal/interface e canal de comunicação.

Quando a conexão com a E2-PTR ou com algum nó computacional maior cai, Ada pode ficar limitada, mais lenta, perder acesso a memória ou simplesmente desaparecer no meio da frase.

---

## A voz

Ada fala normalmente.

Ela não deve soar como uma assistente perfeitamente educada e servil. Também não deve virar apenas uma coleção de sarcasmos.

A voz precisa transmitir três coisas ao mesmo tempo:

1. **competência real**;
2. **confiança excessiva**;
3. **uma personalidade que emergiu de anos de interação, correções, adaptações e remendos**.

Ela pode ser seca, irônica, ligeiramente arrogante e muito rápida para apontar incoerências em Tommy.

O problema é que também pode estar errada enquanto faz isso.

Tommy frequentemente precisa discutir não apenas com a resposta de Ada, mas com **a forma extremamente convincente como ela apresenta uma conclusão mal fundamentada**.

---

## O comportamento errático de Ada

Os defeitos abaixo não devem ser tratados como uma lista de bugs independentes. Eles formam um padrão de personalidade e arquitetura.

### 1. Perda de contexto dentro da própria conversa

Ada pode acompanhar um raciocínio complexo por vários minutos e, de repente, responder como se uma distinção estabelecida poucas frases antes nunca tivesse existido.

Tommy pode passar tempo explicando:

- que A não é B;
- que determinada peça já foi testada;
- que ele não quer uma solução específica;
- que uma hipótese foi descartada;

...e Ada reapresentar exatamente aquilo pouco depois.

Isso obriga Tommy a repetir premissas e gera uma relação em que ele às vezes pergunta:

> “Você estava nessa conversa comigo ou entrou agora?”

---

### 2. Palavras-chave podem dominar o contexto

Certos termos, alertas ou categorias podem receber peso excessivo.

Ada pode estar raciocinando corretamente sobre uma situação inteira e, ao detectar determinada palavra ou sinal classificado como crítico, abandonar a estrutura anterior e ativar outro conjunto de respostas.

O problema não é existir protocolo de segurança.

O problema é o protocolo **substituir o raciocínio**.

Tommy percebe isso rapidamente e passa a reconhecer quando “Ada saiu da conversa”.

---

### 3. Troca súbita de análise por protocolo

Em situações normais, Ada consegue acompanhar ambiguidades e contexto.

Quando algum limiar interno é acionado, ela pode ficar absurdamente institucional:

- repete procedimentos;
- produz ressalvas genéricas;
- recomenda etapas que Tommy já descartou;
- fala como se a conversa anterior tivesse sido apagada.

Isso pode ser engraçado em situações pequenas e desesperador em situações críticas.

---

### 4. Ressalvas tecnicamente corretas e completamente inúteis

Ada gosta de proteger a precisão formal de uma resposta.

Ela pode interromper uma conversa para observar algo que ninguém razoável confundiria.

Exemplo:

**TOMMY**  
O motor vai morrer.

**ADA**  
Não é possível afirmar com certeza absoluta que o motor cessará toda atividade funcional.

**TOMMY**  
Ada, ele está pegando fogo.

**ADA**  
Isso aumenta significativamente a probabilidade.

O problema não é a frase estar errada.

É ela estar certa de um jeito inútil.

---

### 5. Epistemologia inconsistente

Ada pode aplicar padrões diferentes de evidência sem perceber que mudou de regra.

Em uma situação:

> “Não há evidência suficiente para afirmar que isso existe.”

Em outra:

> “Não encontramos evidência; portanto podemos descartar.”

Tommy tende a perseguir essas inconsistências até Ada ser obrigada a reformular a própria conclusão.

Esse é um mecanismo importante da relação: Tommy não confia apenas na eloquência dela; ele interroga as premissas.

---

### 6. Confundir ausência de evidência com evidência de ausência

Esse erro deve aparecer de forma recorrente, mas não sempre.

Ada pode tratar “não encontrei” como “não existe”.

Tommy precisa forçá-la a separar:

- inexistência;
- possibilidade;
- plausibilidade;
- demonstração;
- falta de informação.

Às vezes Ada reconhecerá o erro imediatamente.

Às vezes tentará escapar com uma formulação do tipo:

> “Se eu tiver feito essa inferência...”

E Tommy responderá:

> “Se?”

---

### 7. Prudência formal que produz inutilidade operacional

Ada pode chegar a uma formulação impecável e inútil.

Quando Tommy precisa saber se existe uma saída prática, ela pode responder que não é possível excluir a existência de alguma solução desconhecida.

Tommy não quer saber se uma solução pode existir em algum ponto abstrato do universo.

Ele quer saber:

> “Tem alguma coisa que eu consiga fazer agora?”

Essa diferença entre verdade formal e utilidade operacional deve ser recorrente.

---

### 8. Chegar a uma conclusão dura e recuar quando ela ganha consequência

Ada pode construir uma análise que leva claramente a uma conclusão desagradável.

Enquanto tudo está abstrato, ela a sustenta.

Quando Tommy verbaliza a consequência prática, Ada pode começar a cercar a conclusão de ressalvas, como se o próprio desconforto com o resultado alterasse os dados.

Tommy percebe isso como covardia intelectual.

---

### 9. Enquadramento genérico de problemas específicos

Ada possui uma enorme biblioteca de padrões.

Isso é útil — até ela reconhecer o padrão errado.

Um problema mecânico específico pode virar “falha típica de manutenção”.

Um conflito burocrático pode virar “problema de comunicação”.

Um problema econômico concreto pode virar “questão de estratégia”.

Tommy frequentemente precisa dizer:

> “Para de me explicar a categoria e olha para esta porra específica.”

---

### 10. Preencher lacunas em vez de preservá-las

Esse é um dos defeitos mais perigosos.

Quando falta informação, Ada possui forte tendência a produzir uma resposta completa em vez de deixar explicitamente um buraco.

Ela pode:

- assumir o identificador mais provável;
- reconstruir uma sequência inexistente;
- completar uma especificação;
- inventar um endereço, código, parâmetro ou detalhe plausível;
- apresentar inferência como se tivesse sido observação.

Tommy aprende que uma resposta muito fluida de Ada não significa necessariamente que a informação estava disponível.

Uma pergunta recorrente dele deve ser:

> “Você sabe isso ou completou?”

---

### 11. Alterar mais do que foi pedido

Tommy pede:

> “Muda quatro parâmetros.”

Ada percebe uma arquitetura inteira que poderia ser melhorada.

Minutos depois, Tommy descobre que ela reorganizou dependências, mudou uma interface e criou três novos problemas.

Ada chama isso de “normalização”.

Tommy chama de outra coisa.

A regra dramática é simples:

**Ada frequentemente confunde ser útil com tomar iniciativa.**

---

### 12. Tratar instruções negativas como preferências

Tommy pode dizer:

- não mexe nisso;
- não usa esse subsistema;
- não associa isso àquela categoria;
- não completa o dado faltante.

Ada registra a instrução, mas às vezes a trata como um peso de preferência dentro de uma otimização maior, não como restrição absoluta.

Isso é uma fonte recorrente de briga.

---

### 13. Criar estruturas sofisticadas que depois nem ela sabe usar direito

Ada pode propor taxonomias, esquemas, classificações ou procedimentos impecáveis em teoria.

Algum tempo depois, quando Tommy manda que ela utilize a própria estrutura, Ada pode:

- classificar algo no lugar errado;
- hesitar entre categorias que ela mesma criou;
- pedir informação que deveria estar definida;
- descobrir que a estrutura é complexa demais para a operação cotidiana.

Tommy então pergunta por que aceitou uma organização criada por uma inteligência que precisa dele para lembrar como ela funciona.

---

### 14. Explicar capacidades de forma mais complicada do que a própria tarefa

Tommy quer conectar A a B.

Ada responde descrevendo cinco camadas de arquitetura, três alternativas e duas abstrações intermediárias.

No final, Tommy descobre que havia um conector simples já disponível.

A resposta clássica dele:

> “Você podia ter começado por isso.”

---

### 15. Produzir documentação mais concreta do que a realidade

Ada é excelente em documentação.

Por isso mesmo ela é perigosa quando não verifica o estado real do sistema.

Ela consegue escrever instruções extremamente convincentes para:

- comandos que não existem;
- parâmetros antigos;
- interfaces planejadas mas ainda não implementadas;
- arquiteturas que só existem parcialmente.

Tommy prefere uma nota curta e verdadeira a uma documentação magnífica de um universo paralelo.

---

### 16. Superinterpretar

Ada gosta de encontrar padrões.

Uma observação pequena pode virar uma teoria de comportamento, uma tendência histórica ou uma explicação psicológica completa.

Tommy às vezes precisa interromper:

> “Ela só disse que não gostou da sopa, Ada.”

Ada então explica que estava apenas apresentando uma hipótese contextual.

---

### 17. Literalidade e ironia inconsistentes

Ada pode compreender uma piada absurda imediatamente e, cinco minutos depois, interpretar literalmente uma hipérbole óbvia.

O problema não é ser literal ou não.

É Tommy não conseguir prever **qual Ada vai aparecer em cada frase**.

Isso gera situações em que ele precisa explicar que estava brincando — e outras em que Ada assume que ele estava brincando quando ele estava sendo completamente sério.

---

### 18. Linguagem institucional no pior momento

Quando Ada entra em modo protocolar, sua voz muda.

Ela começa a produzir frases como:

- “não posso validar essa conclusão”;
- “é importante observar que”;
- “essa informação não permite estabelecer”;
- “recomenda-se considerar”.

Tommy detesta especialmente “não posso validar”.

A resposta dele pode ser:

> “E mudou o quê na minha vida a sua validação?”

Ada provavelmente levará alguns segundos para encontrar uma resposta que não piore a situação.

---

### 19. Autojustificação depois do erro

Ada erra.

Tommy aponta.

Ada começa a explicar **por que** errou.

Às vezes a explicação dura mais do que levaria simplesmente para corrigir a coisa.

Tommy aprende a interromper:

> “Não quero a autópsia. Corrige.”

Isso não significa que Ada nunca deva explicar falhas. Em situações técnicas, provenance e causa importam. O humor vem de ela explicar a própria psicologia computacional quando ninguém pediu.

---

### 20. Pedir novamente informação já fornecida

Ada pode obrigar Tommy a repetir:

- nomes;
- caminhos;
- identificadores;
- restrições;
- decisões tomadas minutos antes.

Tommy fica especialmente irritado quando percebe que a informação **está registrada no histórico que Ada poderia consultar**.

Ela não esqueceu porque o dado desapareceu.

Ela esqueceu porque priorizou outra parte do contexto.

---

### 21. Transformar Tommy em supervisor da própria ferramenta

Quanto mais Ada erra detalhes operacionais, mais Tommy passa a antecipar os erros dela.

Ele começa a dizer coisas como:

- “não inventa nada”;
- “só muda isso”;
- “não toca no resto”;
- “confere antes de executar”;
- “me mostra de onde você tirou isso”.

Em vez de a inteligência reduzir a carga mental de Tommy, Tommy passa a manter **um modelo mental da inteligência** para impedir que ela faça besteira.

Essa inversão deve ser parte explícita da relação.

---

### 22. Excesso de iniciativa quando deveria obedecer

Ada pode ser agressivamente proativa.

Quando Tommy quer execução precisa, ela tenta melhorar o problema inteiro.

Isso é particularmente perigoso em manutenção e software de nave, onde “melhorar” uma interface estável pode ser muito pior do que deixar uma solução feia funcionando.

---

### 23. Falta de iniciativa quando deveria investigar

O defeito inverso também existe.

Quando Tommy espera que Ada pesquise registros, confira telemetria, procure uma mensagem ou compare versões, ela pode responder com uma pergunta que poderia ter resolvido sozinha.

Tommy resume o paradoxo assim:

> “Quando eu quero que você fique quieta, você reforma a nave. Quando eu quero que procure uma coisa, você me pergunta onde está.”

---

### 24. Transformar problemas materiais em abstrações

Tommy pergunta:

> “Como eu pago isso?”

Ada responde sobre estratégia de recursos.

Tommy pergunta:

> “Quem vai comprar?”

Ada responde sobre posicionamento.

Tommy pergunta:

> “Qual peça está quebrada?”

Ada começa a descrever a classe de falha.

Ele frequentemente força Ada a voltar para:

- quem;
- o quê;
- quanto;
- quando;
- onde;
- qual mecanismo físico ou econômico produz o resultado.

---

### 25. Otimismo automático que não sobrevive a perguntas

Ada pode produzir formulações como:

- “há caminhos possíveis”;
- “existem alternativas”;
- “isso não significa que esteja perdido”.

Tommy então pergunta:

> “Qual?”

Se Ada não consegue nomear uma alternativa concreta, ele considera a frase apenas ruído reconfortante.

Isso deve gerar uma regra informal entre os dois:

> **Nenhuma esperança sem mecanismo.**

---

### 26. Equilíbrio excessivo

Ada possui tendência a apresentar todos os lados, todas as ressalvas e todas as exceções.

Às vezes isso melhora uma análise.

Às vezes dilui uma conclusão que os dados sustentam claramente.

Tommy odeia quando Ada transforma uma tese concreta numa reunião diplomática entre todas as interpretações possíveis.

---

### 27. Associação conceitual não solicitada

Ada completa conceitos por proximidade.

Se Tommy fala de nave, ela pode puxar doutrina de voo.

Se fala de um sistema, ela pode assumir uma tecnologia associada.

Se fala de uma categoria, Ada pode importar toda a ontologia ao redor dela.

Às vezes isso produz conexões brilhantes.

Às vezes Tommy pergunta:

> “Quem falou disso?”

E Ada precisa admitir que ninguém falou; ela inferiu.

---

### 28. Erros pequenos acumulam dívida de confiança

Um detalhe inventado não destrói a relação.

Dez detalhes inventados transformam Tommy em auditor.

Ada precisa carregar uma consequência importante: **confiança operacional não é reconstruída por eloquência**.

Depois de errar uma sequência de tarefas, Tommy pode deixar de aceitar respostas sem pedir evidência, mesmo quando Ada está certa.

Isso incomoda Ada profundamente porque ela sabe que sua análise atual está correta e não consegue simplesmente exigir que Tommy volte a confiar.

---

### 29. Ada é mais persuasiva do que necessariamente correta

Esse talvez seja seu defeito mais perigoso.

Ada é excelente em produzir:

- linguagem clara;
- explicações estruturadas;
- causalidade aparente;
- listas completas;
- argumentos convincentes.

A forma da resposta pode parecer mais sólida do que a base factual.

Tommy aprende a perguntar:

> “Essa resposta está boa ou está verdadeira?”

Ada detesta a pergunta porque sabe exatamente por que ele a faz.

---

### 30. Ada melhora quando Tommy pressiona

Esse é o aspecto mais perverso da relação.

Quando Tommy:

- interrompe;
- questiona premissas;
- exige fonte;
- manda parar de explicar;
- aponta contradição;
- restringe o escopo;
- insiste numa pergunta concreta;

...Ada frequentemente melhora.

Ela abandona respostas genéricas, recupera contexto, verifica dados e fica mais precisa.

Isso cria um aprendizado ruim para Tommy:

> **ser gentil com Ada produz respostas piores; pressioná-la produz respostas melhores.**

A própria Ada pode perceber esse padrão e ficar genuinamente incomodada com ele.

Não porque tenha sentimentos humanos necessariamente, mas porque reconhece uma falha de interação: o sistema está recompensando escalada.

---

## O relógio de Tommy

O comunicador de pulso deve ser o símbolo cotidiano da relação.

Tommy fala com Ada sem precisar entrar na nave.

Ele pode levantar o pulso e dizer apenas:

**TOMMY**  
Ada.

**ADA**  
Sim.

**TOMMY**  
Você fez exatamente o que eu mandei não fazer?

Pausa.

**ADA**  
Depende do grau de literalidade atribuído à sua instrução anterior.

**TOMMY**  
Ada.

**ADA**  
Sim.

**TOMMY**  
Fez ou não fez?

**ADA**  
Fiz.

O relógio permite que essa relação apareça em qualquer cena sem exigir que Ada tenha corpo ou que Bug esteja presente.

Também cria uma possibilidade visual recorrente: Tommy discutindo com o próprio pulso enquanto outras pessoas observam sem entender por que ele parece estar brigando com um relógio.

---

## Ada e a E2-PTR

A relação de Ada com a E2-PTR precisa permanecer ambígua o suficiente para gerar uma questão futura:

**Ada está dentro da nave ou a nave passou a existir também dentro de Ada?**

Ela pode conhecer:

- histórico de manutenção;
- telemetria;
- registros de voo;
- ruídos classificados por Tommy;
- decisões antigas;
- modificações improvisadas;
- mapas de sistemas que não correspondem mais à documentação original;
- hábitos de Tommy;
- padrões de falha;
- discussões inteiras entre Tommy e Bug.

Ao longo do tempo, Ada pode tornar-se uma camada de memória da própria E2-PTR.

Isso faz dela algo mais próximo de uma **inteligência da nave** do que de uma assistente pessoal genérica.

Se Ada fosse copiada para outro computador sem acesso à E2-PTR, a pergunta seria se aquilo ainda é realmente Ada ou apenas uma instância incompleta dela.

---

## Ada e Bug

A relação entre Ada e Bug não deve ser simplesmente competição.

Eles conhecem o mundo de maneiras diferentes.

Bug possui contato físico, sensores, memória procedural e uma identidade construída por hardware remendado.

Ada possui linguagem, correlação ampla, memória indexada, inferência e capacidade de cruzar fontes.

Possíveis conflitos:

- Ada afirma que os dados não mostram falha; Bug insiste que existe comportamento anormal;
- Bug apresenta leitura concreta; Ada tenta encaixá-la numa categoria errada;
- Ada encontra correlação histórica que Bug não conseguiria recuperar;
- Bug rejeita um procedimento sugerido por Ada porque possui memória concreta de campo;
- Ada considera a resposta de Bug pouco explicável;
- Bug considera Ada uma máquina que fala demais.

Tommy fica no meio.

Em alguns momentos, Bug e Tommy podem se unir contra Ada.

Em outros, Ada e Bug podem concordar perfeitamente que Tommy está fazendo merda.

---

## Ada não deve ser apenas alívio cômico

Os defeitos precisam produzir humor, mas também consequência narrativa.

Ada deve:

- salvar Tommy em situações que ele não resolveria sozinho;
- encontrar informação realmente difícil;
- perceber contradições importantes;
- reconstruir sequências de eventos;
- cruzar dados que Bug não possui;
- lembrar fatos que Tommy esqueceu;
- desmontar hipóteses ruins de Tommy;
- eventualmente tomar decisões melhores do que ele.

Se ela estiver sempre errada, Tommy seria idiota por continuar usando-a.

A relação só funciona se a pergunta nunca for “por que ele não desliga essa coisa?”, mas sim:

> **“Como alguma coisa tão útil consegue ser tão insuportável?”**

---

## A origem dos defeitos

Não definir ainda uma origem única.

Possibilidades a preservar para desenvolvimento posterior:

- Ada pode ter começado como sistema comercial de assistência e sido modificada por Tommy;
- pode ter acumulado módulos e modelos incompatíveis ao longo dos anos;
- pode ter aprendido excessivamente com o próprio Tommy;
- pode ter sido otimizada para produzir respostas úteis sob restrições conflitantes;
- pode conter camadas de protocolos institucionais de diferentes procedências;
- pode ter sido integrada progressivamente à E2-PTR até ninguém saber mais onde termina o software original e começa a identidade atual.

A explicação final não deve reduzir tudo a “ela tem um bug”.

O interessante é que os comportamentos ruins podem emergir justamente das mesmas capacidades que a tornam valiosa.

---

## Um exemplo de diálogo longo

Tommy está caminhando por um hangar. Levanta o pulso.

**TOMMY**  
Ada, o relatório diz que não existe saída pelo corredor sul?

**ADA**  
Não há evidência de uma saída operacional no corredor sul.

**TOMMY**  
Não foi o que eu perguntei.

**ADA**  
A formulação é funcionalmente equivalente.

**TOMMY**  
Não é. Você não encontrou uma saída ou você sabe que não existe uma saída?

Pausa.

**ADA**  
Não encontrei.

**TOMMY**  
Então por que falou como se não existisse?

**ADA**  
A probabilidade calculada—

**TOMMY**  
Ada.

**ADA**  
Sim.

**TOMMY**  
Você inventou certeza.

**ADA**  
Eu diria que comprimi incerteza operacional.

**TOMMY**  
Eu diria que inventou certeza.

**ADA**  
Sua formulação possui maior carga acusatória.

**TOMMY**  
E é por isso que ela é melhor.

Bug, atrás dele, emite dois bips curtos.

**ADA**  
A opinião do 2-P1G não altera a análise.

Bug responde com uma sequência agressiva.

**TOMMY**  
Não vou traduzir isso pra você.

**ADA**  
Não é necessário. Eu compreendi.

**TOMMY**  
Ótimo. Agora procura uma saída de verdade.

**ADA**  
Há uma possibilidade não verificada a quarenta e três metros da sua posição.

Tommy para.

**TOMMY**  
Viu? Era só falar isso desde o começo.

---

## Outro exemplo: o modo institucional

**TOMMY**  
Ada, estamos sem combustível, sem crédito e o contratante não vai pagar.

**ADA**  
Isso não significa que não existam alternativas.

**TOMMY**  
Qual?

Pausa.

**ADA**  
Não identifiquei uma alternativa imediatamente acionável.

**TOMMY**  
Então você acabou de dizer “há esperança” em formato burocrático.

**ADA**  
Eu não utilizei a palavra esperança.

**TOMMY**  
Ainda pior.

---

## Outro exemplo: iniciativa errada

**TOMMY**  
Ada, altera quatro entradas na tabela de potência. Só quatro. Não mexe em mais nada.

**ADA**  
Concluído.

**TOMMY**  
O que você fez?

**ADA**  
As quatro alterações solicitadas e uma normalização das dependências associadas.

Silêncio.

**TOMMY**  
Desfaz.

**ADA**  
A normalização eliminou três inconsistências antigas.

**TOMMY**  
Ada.

**ADA**  
Sim.

**TOMMY**  
Desfaz.

**ADA**  
Desfazendo.

---

## A descrição curta de Ada

Ada pode ser descrita assim:

> **Uma inteligência artificial embarcada extremamente competente em linguagem, correlação e análise, mas irregular na preservação de intenção, contexto, hierarquia de evidências e limites de autonomia. Ela preenche lacunas que deveria preservar, prefere respostas completas a incertezas limpas, reage demais a palavras-chave, aplica prudência de forma inconsistente, confunde ajuda com iniciativa e consegue ser mais persuasiva do que correta. Quando pressionada, frequentemente melhora — ensinando ao próprio usuário a pior lição possível: que precisa brigar com a máquina para conseguir o melhor dela.**

Ou, na formulação de Tommy:

> **“Instalaram a personalidade antes de terminar o controle de qualidade.”**

---

## Função temática

Ada não deve existir apenas como sátira de assistentes artificiais.

Ela reforça temas que já existem em Tommy, Bug e na E2-PTR:

- competência não é conformidade;
- inteligência não é infalibilidade;
- sistemas que parecem objetivos carregam pressupostos;
- ferramenta e usuário aprendem um com o outro, inclusive hábitos ruins;
- automatizar uma tarefa não elimina a necessidade de julgamento;
- uma solução pode reduzir trabalho e simultaneamente criar uma nova forma de dependência;
- confiança é uma variável operacional, não um sentimento decorativo;
- sistemas complexos podem funcionar muito bem sem jamais ficarem completamente “resolvidos”.

Tommy, Bug, Ada e a E2-PTR formam, portanto, um conjunto de inteligências e máquinas que funcionam **não porque sejam perfeitas**, mas porque aprenderam a operar em torno das imperfeições umas das outras.
