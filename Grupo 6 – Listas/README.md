# PROJETO DE EXTENSÃO: 

## DESMISTIFICANDO A PROGRAMAÇÃO: APRENDENDO LÓGICA DE FORMA SIMPLES 💻

### Informações Gerais📋

* Instituição: Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE).  
* Curso: Bacharelado em Ciência da Computação  
* Disciplina: Lógica de Programação   
* Docente: Pedro Lucas Luz Costa 

### Objetivo🎯

O objetivo deste projeto de extensão é promover o aprendizado de conteúdos relacionados à lógica de programação, focando nas listas e suas funções, de maneira acessível, dinâmica e prática, contribuindo para o desenvolvimento do raciocínio lógico dos participantes e estimulando o interesse pela continuidade dos estudos na área da computação.   

### Equipe e Distribuição de tarefas👥

| Integrante | Responsabilidades |
| :---- | :---- |
| **Alice Bandeira Ferreira de Sousa** | Gerenciamento e organização do GitHub; pesquisa sobre o tema. |
| **Felipe Gabriel Alves de Oliveira** | Produção de exemplos e exercícios; apresentação. |
| **José Henrique Ferreira da Silva** | Elaboração da apresentação. |
| **Kauan Alves de Araújo** | Produção de exemplos e exercícios; apresentação. |
| **Lara Ingrid Rocha Almeida** | Pesquisa sobre o tema; elaboração do relatório. |


# Conteúdo📚

## 📑 Sumário

- [O que são listas?](#o-que-são-listas)
- [Armazenamento de múltiplos valores](#armazenamento-de-múltiplos-valores)
- [Outros exemplos de estruturas de dados parecidas com as listas são:](#Outros-exemplos-de-estruturas-de-dados-parecidas-com-as-listas-são:)
- [Outros comandos usados:](#Outros-comandos-usados:)
- [Acesso por índices](#acesso-aos-elementos-de-uma-lista-por-índice)
- [Estruturas de repetição](#percorrendo-listas-com-estruturas-de-repetição)
- [Aplicações práticas](#aplicações-práticas-das-listas-no-desenvolvimento-de-programas)

## O que são listas?

Estrutura da dados que permite o armazenamento de múltiplos valores de diversos tipos e também de listas dentro de outras listas, além de que é uma estrutura mutável, permitindo a adição, eliminação e modificação de dados. Muito usado em contextos que é necessário uma estrutura de armazenamentos mais flexível, que permita alterações de adição e retirada. Sua indicação muda dependendo da linguagem de programação usada, no python, por exemplo, as listas são indicadas por colchetes ou pela função list(), na declaração de variáveis para criar listas vazias.

## Armazenamento de múltiplos valores.

As listas armazenam os valores em pequenos espaços na memória, eles podem ser acessados por índices, um número identificador que começa no 0, portanto o  primeiro elemento da lista é indicado pela posição 0 e o segundo pela posição 1\. Por mais que eles sejam mostrados de forma sequencial, não é necessário que eles estejam armazenadas na memória de forma sequencial. As listas podem ser guardadas de duas formas: 

- Listas sequenciais: Os valores são armazenados em sequência na memória, para isso, geralmente é necessário determinar ou limitar o tamanho máximo de elementos no momento de sua criação , esse tipo é mais conhecido como array, contudo hoje em dia são muito usadas as arrays dinâmicas que mudam de tamanho conforme o necesário.  
- Listas encadeadas: Os elementos não estão necessariamente armazenados em sequência na memória, mas é necessário haver uma lógica que mantenha uma ordem entre os valores, sendo um tipo mais flexível, sem determinação de tamanho, sua desvantagem no entanto se encontra no uso de conceitos mais avançados na programação.

Existem diferentes comandos e formas de armazenar valores em listas, que vão mudando conforme a linguagem de programação usada. No python, por exemplo, os comandos mais usados são:

| Comandos | Função |
| :---- | :---- |
| .append | Adiciona o elemento ao final da lista. |
| .insert(posição, elemento) | Adiciona o elemento a uma posição específica. |

## Outros exemplos de estruturas de dados parecidas com as listas são:

*  Tuplas: Estrutura de armazenamento que, assim como a lista, armazena múltiplos elementos, indicados por índices. Esse tipo de estrutura não apresenta flexibilidade, permanecendo imutável. No Python, uma tupla é frequentemente representada por parênteses.  
*  Dicionário: Estrutura de armazenamento que armazena múltiplos valores, mas tem um funcionamento bastante distinto. Sua estrutura de armazenamento é desenvolvida através do par chave/valor, onde uma chave (elemento) tem um valor atribuído e, quando chamada, faz referência a esse valor. Por exemplo, ao criar uma chave "nome" em um dicionário, pode atribuir-lhe um nome específico, como "Luiza". Dessa forma, quando a chave for chamada, ela retornará o valor "Luíza".

## Outros comandos usados:

| Comando | Função |
| :---- | :---- |
| pop | Remove um item da lista, podendo ser um específico ou o último. |
| remove | Usado para remover itens específicos. |
| sort | Colocar a lista em ordem. |
| len | Serve para saber o comprimento da lista. |
| reverse | Quando usado em conjunto com o sort coloca a lista em ordem decrescente, como por exemplo: “lista.sort(reverse=True)”. |
| count | Conta quantas vezes determinado elemento apareceu. |


## Acesso aos elementos de uma lista por índice

Para que seja possível acessar qualquer elemento que esteja em uma lista, utilizamos a indexação numérica, também chamada de índice. Contudo, a contagem dos elementos não começa pelo número 1, como funcionaria na lógica natural, mas sim pelo índice 0\. Assim, o primeiro elemento estará na posição 0, o segundo na posição 1, e assim sucessivamente. Além disso, também podemos utilizar índices negativos para acessar o final de uma lista. Seguindo essa lógica, se buscamos pelo índice \-1, acessamos o último elemento da lista; o \-2 acessa o penúltimo elemento, e assim por diante. Um breve exemplo de como funciona essa lógica seria tendo uma lista de nomes A \= \[“João”, “Emily”, “Carlos”, “Elisa”\]. Se pedíssemos o elemento que está na posição 1, o retorno seria o nome “Emily”. Caso pedíssemos o elemento da posição \-1, o retorno seria o nome “Elisa”, que está no final da lista. Da mesma forma, se buscássemos pelo índice \-2, o sistema retornará o nome “Carlos”, que ocupa a penúltima posição.

| NOMES | João | Emily | Carlos | Elisa |
| :---: | :---: | :---: | :---: | :---: |
|  **ÍNDICES** | 0 | 1 | 2 | 3 |
|  | \-4 | \-3 | \-2 | \-1 |

## Percorrendo listas com estruturas de repetição

Além do acesso aos elementos de uma lista por meio de índices, conseguimos percorrer os itens de uma maneira mais rápida e fácil utilizando estruturas de repetição. Grosso modo, elas permitem que um código seja executado por um determinado número de vezes ou até mesmo em loop. Os termos mais utilizados nas linguagens de programação são o “for” e o “while”. Dependendo do idioma de código escolhido, a forma como essas expressões são construídas possui divergências, porém, continuam seguindo a mesma lógica. O laço for (para) é a maneira mais comum de percorrer uma lista, sendo utilizado principalmente quando sabemos o total de elementos que ela possui. Dessa forma, se temos uma lista de 50 elementos, o código irá percorrer cada um e exercerá a função dada a ele. Já o while (enquanto) funciona por meio de uma condição lógica. Ele só percorrerá a lista caso a condição seja verdadeira, o que permite, por exemplo, interromper o laço de repetição assim que o critério definido pelo desenvolvedor for atingido. Exemplo de funcionamento:

**\- For**  
Numa lista B \= \[“pêra”, “uva”, “maçã”, “salada-mista”\], se utilizarmos o laço for, o nosso programa nos retornará cada termo separadamente.

**Retorno:** pêra  
                uva  
                maçã  
                salada-mista

**\- While**  
Nessa mesma lista B \= \[“pêra”, “uva”, “maçã”, “salada-mista”\], se usarmos o laço while, o nosso programa retornará de acordo com uma condição, por exemplo, o código deve repetir enquanto o contador for menor que 4, não podemos esquecer que a contagem começa do zero.

**Retorno:** pêra  
                uva  
                maçã  
                salada-mista

\- Caso pedíssemos para repetir o código enquanto o contador fosse menor que 3\.

**Retorno:** pêra  
                uva  
                maçã

## Aplicações práticas das listas no desenvolvimento de programas 

Como já foi discutido, as listas armazenam os dados utilizando índices para organizar os elementos e são um recurso essencial na programação. Desse modo, o acesso às informações torna-se bem mais fácil e rápido. Algumas aplicações práticas dessas estruturas incluem grandes softwares como:

1. ### **TRELLO**

O Trello é uma ferramenta baseada na metodologia Kanban, muito utilizada nos setores empresariais que permite gerenciar projetos e tarefas visualmente. Nesse programa, as listas colaboram na organização do fluxo de trabalho, informando se uma atividade está pendente ou se já foi concluída. Além disso, elas possibilitam que o usuário adicione, modifique e remova os elementos da maneira que desejar, estimulando a produtividade e a organização dos profissionais.

2. ### **SPOTIFY**

Um dos aplicativos mais utilizados para a reprodução de músicas, o Spotify utiliza a lógica das listas para que o usuário consiga selecionar os sons que mais gosta em playlists na ordem que desejar. Isso facilita a organização de grandes catálogos musicais e permite a sugestão de novas faixas com base nas preferências de cada perfil. 

3. ### **WHATSAPP**

O WhatsApp é um aplicativo de conversas instantâneas que também suporta chamadas de voz e vídeo, disponível para vários tipos de dispositivos. A plataforma organiza cada conversa em forma de listas, das mais recentes para as mais antigas. Além disso, o usuário consegue fixar conversas ou grupos no topo e arquivar elementos para que fiquem em uma pasta escondida.

4. ### **LISTAS E A ACESSIBILIDADE**

As listas são muito úteis para o funcionamento de diferentes plataformas, porém, muito além de aplicações para trabalho ou escuta de músicas, essas estruturas possuem um papel importante para a acessibilidade. Listas semânticas em HTML facilitam que os conteúdos sejam compreendidos por leitores de tela, que são ferramentas utilizadas por pessoas com deficiência visual. Dessa forma, os softwares avisam o usuário sobre a existência de uma lista e a quantidade exata de itens nela, oferecendo autonomia para navegar pelas informações. Além desse efeito social, essa estrutura colabora com o trabalho dos motores de busca, como o Google, que dão prioridade a sites bem organizados, posicionando-os melhor nos resultados de pesquisa.  

## Conclusão 📌

Por fim, as listas são a base de conceitos que vão dos simples aos mais avançados na programação, permitindo aos desenvolvedores criar estruturas complexas como matrizes, pilhas e filas de dados. Dessa forma, elas são amplamente utilizadas em diferentes contextos na tecnologia. 