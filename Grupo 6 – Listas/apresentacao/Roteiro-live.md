# **Roteiro da apresentação: Listas em Python** 

## Primeira parte: explanação do conteúdo pelo integrante Felipe

### **1.1 Introdução** 

Hoje vamos falar sobre listas em Python, que são uma das estruturas de dados mais importantes da programação. As listas permitem armazenar vários valores em uma única variável, facilitando a organização e manipulação de dados. Elas são amplamente utilizadas em sistemas reais e são fundamentais para quem está começando a programar. 

### **1.2 O que são listas?** 

Uma lista é uma estrutura de dados que permite armazenar múltiplos valores em uma única variável. Ela possui algumas características principais: 

* Pode armazenar diferentes tipos de dados (números, textos, etc.)   
* É mutável, ou seja, pode ser alterada depois de criada   
* Mantém a ordem dos elementos   
* É criada com colchetes \[\] ou com a função list() 

Além disso, listas podem até conter outras listas, tornando-as muito flexíveis 

### **1.3 Armazenamento de múltiplos valores** 

As listas organizam os elementos de forma sequencial e cada item possui um índice. 

* O índice começa em 0   
* O primeiro elemento é o índice 0   
* O segundo é o índice 1, e assim por diante   
- Exemplo: lista \= \["A", "B", "C"\]   
  lista\[0\] → "A"  
  lista\[1\] → "B" 

Também existem dois tipos teóricos de listas: 

* Sequenciais (arrays): elementos em sequência na memória   
* Encadeadas: elementos conectados por ponteiros

 No Python, usamos listas dinâmicas, que se adaptam automaticamente ao tamanho necessário. 

### **1.4 Comandos de armazenamento** 

Para adicionar elementos em listas, usamos principalmente: 

- **append():** Adiciona ao final. EX: lista.append(10)    
- **insert():** Adiciona em posição específica. EX: lista.insert(1, 99\) 

**Outros comandos e suas funções:** 

1. pop   
2. remove   
3. sort   
4. len   
5. reverse   
6. count 

### **1.5 Acesso por índice** 

Para acessar elementos, usamos índices.  
**Índices positivos:** 

* Começam do início   
  lista\[0\]   
  lista\[1\]

**Índices negativos**: 

* Começam do final   
  lista\[-1\] \# último elemento   
  lista\[-2\] \# penúltimo


### **1.6 Percorrendo listas** 

Podemos percorrer listas com estruturas de repetição: 

#### **For** 

* Mais simples e legível    
* Ideal quando sabemos o tamanho da lista 

#### **While** 

* Usa condição  
*  Dá mais controle 

Ambos permitem acessar e manipular dados da lista. 

#### **1.7 Aplicações práticas 4**

Listas são usadas em vários sistemas do dia a dia: 

#### **Trello** 

* Organiza tarefas em listas   
* Permite adicionar, remover e editar itens 

#### **Spotify** 

* Playlists são listas de músicas   
* Mantêm ordem personalizada 

#### **WhatsApp** 

* Lista de conversas   
* Ordenadas por mais recentes 

#### **Desenvolvimento Web**

* Usadas para manipular dados em sites e APIs 

#### **Acessibilidade** 

* Listas ajudam leitores de tela   
* Melhoram organização de conteúdo 

#### **1.8 Falando sobre tuplas e dicionários em python** 

#### **1.9 Conclusão** 

As listas são fundamentais na programação porque: 

* Facilitam o armazenamento de dados   
* São flexíveis e mutáveis   
* Permitem diversas operações   
* Estão presentes em praticamente todos os sistemas

Nesse ponto Felipe finaliza sua explicação abrindo espaço para Kauan começar a apresentar sua parte.

## Segunda Parte: Exemplificação e Resolução de exercícios com o integrante kauan  

### 2.1**Diferenciação e referenciação:**

Inicialmente na parte prática, foi mostrada a questão da diferenciação e referenciação das variáveis múltiplas no python. Sendo elas, as listas sendo referenciadas por dois colchetes: [ ], as tuplas que são referenciadas por dois parênteses: ( ), e os dicionários que são referenciados por duas chaves: { }. A principal diferença entre elas, é que a tupla, só pode receber valores no momento da criação da variável, a lista pode receber valores na criação, modificação, e exclusão de dados; por último, o dicionário que se referencia a um dado por uma “identificação”, se diferenciando de uma lista, ou tupla, que são referenciadas pelo índice. Válido lembrar, que todos dos tipos citados são úteis, à mercê da sua necessidade e complexidade de codificação.  
Dados os seguintes exemplos:
```python
tupla = ('kauan',18)  
lista = ['kauan']  
dicionario = {'nome':'kauan'}
```
**Obs:** O objetivo seria adicionar o nome de uma pessoa na variável múltipla, e depois adicionar um número referente à sua idade, como a tupla é imutável, como mencionado na aula e no documento, modifiquei a tupla para já evidenciar a idade.

### 2.2**Métodos e funções:**

* Como o objetivo era mostrar a parte prática, continuamos com a parte de alguns métodos e funções sobre as listas no python. Inicialmente, dado às variáveis anteriores, adicionaremos alguns valores a elas, pelo índice inicialmente. Como já vimos, na tupla, esse tipo de ação não é permitida. Nas listas, você pode adicionar pelo método “append( )”, que irá adicionar o que está dentro do parênteses na última posição da lista. Nos dicionários, foi citado a questão de poder-se adicionar pelo método ‘’update( )’’, mas no contexto de apresentação de curto tempo, apresentei apenas o método de adicionar pela “nova” variável, e seu respectivo nome, seguindo o seguinte sintaxe: nome\_dicionario\[‘nome\_da\_variavel’\] \= variavel.
```python
lista.append(18)  
#tupla.append(2)  
dicionario['idade'] = 18  
print(lista, tupla, dicionario)  
```
**Obs:** A função referente à tupla está comentada, pois não há como adicionar nela, e também para que se prove isto, visto que, no vídeo, ao tentar fazer o mesmo, o programa dá um erro.  
**Saída:**
```python
['kauan', 18] ('kauan', 18) {'nome': 'kauan', 'idade': 18} 
```
* Continuando com a questão de adicionar pelo índice na lista, foi apresentado o método “insert”, onde você adiciona em qualquer lugar da lista, seguindo o seguinte sintaxe: nome\_da\_lista(posição,variável), sendo assim adicionado na ‘’nome\_da\_lista’’, uma variável com a posição citada, sendo ela um número inteiro, detalhe que se a posição for \-1, será o último termo.
```python
lista.insert(0, 'felipe')  
print(lista)
```
Para exemplificar, apenas adicionei o nome “felipe”, indo pra primeira posição, visto que, se inicia pelo índice 0\. E como a lista já havia “kauan” e “18”.  
**Saída:**
```python
['felipe', 'kauan', 18] 
```
* Para finalizar na questão de funções e métodos, foi explicado sobre o “tamanho” das variáveis múltiplas, com o método “len(nome\_da\_variavel)”. Em ordem de digitação, temos: Tamanho da lista, tamanho da tupla, e tamanho do dicionário. Como visto acima, a lista teria 3 elementos, haja vista que foi adicionando um com ‘’append( )’’, e outra com ‘’insert( )’’, e no dicionário só foi adicionado uma, ‘’idade’’.
```python
print(len(lista), len(tupla), len(dicionario))
````
**Obs:** Foi comentado que se tiver apenas um elemento, como no vídeo foi a tupla, ele considera a variável múltipla, como uma simples, fazendo assim a contagem do seu caracteres, no caso, 5 strings do nome “kauan”, mas em seguida, foi resolvido adicionando o “18”, na tupla, fazendo ter 2 elementos.  
**Saída:**
```python
3 2 2 
```
### 2.3**Atividade:**

Foi recomendado a elaboração de uma pequena atividade para melhor fixação,e quis trabalhar o tema central da nossa aula que eram as listas , embora a segunda seja facilmente substituída por uma tupla. Também quis adentrar em outros conceitos para trabalhar a lógica nesse contexto.

* Faça um programa que leia 4 notas, a armazene em uma lista, e diga se o aluno está aprovado ou não(\>=7):

#### **Resolução:**
```python
notas = []  
for i in range(4):  
  nota = float(input(f'Digite a sua {i+1}º nota: '))  
  notas.append(nota)

print(f'Notas digitadas: {notas}')  
media = sum(notas) / 4

print(f'Média: {media}')  
if media >= 7:  
  print('Aprovado')  
else:  
  print('Recuperação')
````
#### **Explicação:**

Inicialmente se cria uma lista, para que sejam armazenadas as notas, e como já é dito que o programa precisa receber quatro notas, eu crio um laço para iterar 4 vezes, e em cada uma dessa iterações, o programa vai: Adicionar uma nota float que o usuário digitar, e essa mesma nota vai ser armazenada na lista criada inicialmente, com a função append( ), pois não há a necessidade de índice. No final das 4 iterações o programa printa a lista, mostrando as 4 notas digitadas pelo usuário, é criado outra variável com o nome de media, que vai receber a soma, com a função com o método “sum( )”, e dividindo por 4 para obter a média, no final o programa apenas verifica se essa variável, é maior ou igual que 7, se sim, o aluno foi aprovado, se não, o aluno foi reprovado. 

**Obs:** Válido lembrar que o método “sum()”, poderia também ser substituído por um laço que iria adicionar cada valor da lista a uma variável, a percorrendo com o for. E que a divisão por 4 na mesma variável com o nome de média, poderia ser substituída por “len(notas)”, pela lista também ter valor numérico de tamanho \= 4\. A questão do ‘‘{i+1}’’ é puramente estético.

#### **Exemplo de saídas:**
```python
Digite a sua 1º nota: 1  
Digite a sua 2º nota: 2  
Digite a sua 3º nota: 3  
Digite a sua 4º nota: 4  
Notas digitadas: [1.0, 2.0, 3.0, 4.0]  
Média: 2.5  
Recuperação
```
---
```python
Digite a sua 1º nota: 7  
Digite a sua 2º nota: 6  
Digite a sua 3º nota: 8  
Digite a sua 4º nota: 7  
Notas digitadas: [7.0, 6.0, 8.0, 7.0]  
Média: 7.0  
Aprovado 
````
* Faça um programa que leia o nome de algumas pessoas, e suas respectivas idades,e a apresente-as no final:

#### **Resolução:**
```python
nomes = []  
idades = []  
flag = ''

while flag.lower() != 'n':  
  nome = input('Digite o nome da pessoa: ')  
  idade = int(input('Digite sua idade: '))  
  nomes.append(nome)  
  idades.append(idade)  
  flag = input('Deseja continuar?(s/n): ')  
  if flag.lower() == 's':  
    continue  
  elif flag.lower() == 'n':  
    print('Programa encerrado.')  
  else:  
    flag = input('Inválido, deseja continuar(s/n): ')

for valor in range(0, len(nomes)):  
  print(f'{nomes[valor]} tem {idades[valor]} anos.')
```
#### **Explicação:**

O programa não especifica o número de pessoas, então a armazenaremos em uma lista, tanto uma para os nomes, como para idades, como mostrado na resolução, juntamente com uma flag. Cria-se um laço de repetição, para parar apenas quando o usuário digitar que não quer mais utilizar o programa (que ficará armazenado na flag). É criado um variável tanto para receber o nome, quanto para receber à idade, que ficaram armazenadas nas suas respectivas listas, ambas utilizando o append( ), depois o sistema irá perguntar se o usuário deseja digitar mais algum nome, caso seja ‘s’, iterarará novamente, caso seja ‘n’, o programa quebrará,  caso seja diferente de ambos, o programa irá perguntar novamente. Agora cria-se outro laço de repetição, como sabemos a quantidade de vezes que irá se repetir, que é o tamanho da lista nomes e idades (que será igual), usamos um for, começando no primeiro termo de ambas as listas (0), indo até o último, que é o valor numérico do len(nomes), ou o len(idades), visto que len(nomes)=len(idades), como já dito anteriormente, exemplo, se o usuário digitar 3 nomes, e consequentemente 3 idades, ambas as listas terão o tamanho (len) \== 3\. Depois para cada iteração, o programa irá imprimir o termo “valor” da lista idades e nomes, indo de 0 que é o primeiro até o len das listas, que é o último termo, imprimindo todos os nomes, com suas respectivas idades.

**Obs:** A questão da flag, é porque se fosse criado um “while True”, na hora que o usuário digitasse uma letra diferente de “n” e “s”, ele não quebraria e teria que colocar outro bloco de código, para que assim, o looping seja quebrado, e que como os valores que a flag irá comparar para se repetir estão no método “lower( )”, o programa aceitará letras maiúsculas e minúsculas.

#### **Exemplo de saídas:**
```python
Digite o nome da pessoa: kauan  
Digite sua idade: 18  
Deseja continuar?(s/n): s  
Digite o nome da pessoa: pedro  
Digite sua idade: 99  
Deseja continuar?(s/n): s  
Digite o nome da pessoa: josé  
Digite sua idade: 17  
Deseja continuar?(s/n): n  
Programa encerrado.  
kauan tem 18 anos.  
pedro tem 99 anos.  
josé tem 17 anos. 
```
### Conclusão
Dessa forma o integrante Kauan finaliza sua apresentação e agradece a atenção.