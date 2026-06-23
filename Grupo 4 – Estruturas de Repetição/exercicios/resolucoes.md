# Resolução do exercício 1
## código:
    for C in range(2, 51, 2):
        print(C, end=' ')
    print('FIM')
### 1° passo: crie um laço de repetição **for**
    for C in range(2, 51, 2):
* A palavra **for** significa: "Repita uma ação várias vezes"
* A variável **C** funciona como se fosse uma caixa que vai armazenar um número diferente em cada repetição
* **range( )** cria uma sequência de números através de 3 informações: **range(início(2), fim(51), passos(2))** isso significa: "Comece no número 2, vá até antes do 51, pulando de 2 em 2".
### 2° passo: Comando **print()**
    print(C, end=' ')
* **print( )** serve para mostrar algo na tela
* **end=' '** diz ao python: "Depois de mostrar o número, coloque um espaço em vez de mudar de linha".
### 3° passo: depois que o laço termina
    print("FIM")
* Quando o **for** terminar, o programa executa a próxima instrução

# Resolução do exercício 2
## código:
    frase = str(input('Dígite uma frase: ')).strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''
    for letra in range(len(junto) - 1, -1, -1):
        inverso += junto[letra]
    print('O inverso de {} é {}'.format(junto, inverso))
    if inverso == junto:
        print('Temos um palíndomo')
    else:
        print('A frase digitada não é um palíndromo!')
### 1° passo: antes do **for**
    frase = str(input('Dígite uma frase: ')).strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''
* **input()** serve como uma entrada para o usuário escrever o seu texto e armazenar essa resposta na variável *frase*
* **strip()** remove os espaços extras no começo e no final da frase 
* **upper()** transforma as letras digitadas pelos o usuário em letras maiúsculas
* A variável *palavra* irá dívidir a frase da variável *frase* em várias partes, colocando as palavras da frase em um lista, isso feito através do .split()
* A variável *junto* tem a função juntar todos os elementos da lista, através do .join(). '' antes do .join() significa: "Junte tudo sem colocar nada entre as palavras"
* A variável *inverso* tem a função de guardar a frase invertida
### 2° passo: laço **for**
    for letra in range(len(junto) - 1, -1, -1):
        inverso += junto[letra]
* len(junto) tem a função de conta quantos caracteres existem na frase
* range(len(junto) - 1, -1, -1) diz para o programa: "percorra a palavra de trás para frente"
* A variável *inverso* irá carregar, a cada repetição, uma letra é adicionada ao final de inverso
### 3° mostrando a mensagem
    print('O inverso de {} é {}'.format(junto, inverso))
* Ao termino do **for** o programa vai exibir a mensagem: "O inverso de ARARA é ARARA"
### 4° passo: verificação de palíndromo
    if inverso == junto:
        print('Temos um palíndomo')
    else:
        print('A frase digitada não é um palíndromo!')
* **if** vai comparar se: a frase original e a frase invertida, se as duas forem iguais, o programa vai mostrar: "Temos um palíndromo"
* **else** se os dois não forem iguais, o programa avisa que não é um palíndromo: "A frase digitada não é um palíndromo!"
## código:
    sexo = str(input('Informe seu sexo[M/F]: ')).upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Dados inválido. Por favor informe seu sexo: ')).upper()
    print('Sexo {} registrado com sucesso'.format(sexo))
### 1° passo: comando **input( )**
    sexo = str(input('Informe seu sexo[M/F]: ')).upper()
* O **input** serve como uma entrada para o usuário escrever o seu sexo e armazenar essa resposta na variável *sexo*
* **.upper( )** transforma as letras digitadas pelos o usuário em letras maiúsculas 
### 2° passo: o laço de repeição **while**
    while sexo != 'M' and sexo != 'F':
* A palavra **while** significa: "Enquanto esta condição for verdadeira, continue repetindo",
* traduzindo essa linha de código: "Enquanto o valor digitado for diferente de M e diferente de F, continue perguntando"
### 3° passo: continue perguntando
    sexo = str(input('Dados inválido. Por favor informe seu sexo: ')).upper()
* Quando o usuário digitar algo errado, o programa espera outra resposta e substitui o valor da variável *sexo*
### 4° passo: confirmando o cadastro
    print('Sexo {} registrado com sucesso'.format(sexo))
* Quando o usuário finalmente digita um valor válido, o programa exibe a mensagem: "sexo M/F registrado com sucesso"

# Resolução do exercício 4
## código:
    soma = vezes = 0
    num = int(input('Dígite um valor (dígite 999 para parar: )'))
    while True:
        vezes += 1
        soma += num
        num = int(input('Dígite um valor (dígite 999 para parar): '))
        if num == 999:
            break
    print('A soma dos {} números foi {}'.format(vezes, soma))
### 1° passo: fora do **while**
    soma = vezes = 0
    num = int(input('Dígite um valor (dígite 999 para parar: )'))
* *soma* e *vezes* são criados inicialmente para guardar informações e começamos ambos com o valor 0
* *soma* vai acumular o valor de todos os números digitados
* *vezes* vai funcionar como um contador, registrando quantos números o usuário já digitou
* **input( )** como foi explicado anteriormente o input irá receber o que o usuário 
### 2° passo: dentro do while 
    while True:
        vezes += 1
        soma += num
        num = int(input('Dígite um valor (dígite 999 para parar): '))
        if num == 999:
            break
* **while True** significa: "enquanto for verdade", criando um laço de repetição infinita 
* **vezes += 1** é o mesmo que vezes = vezes + 1. Ele adiciona +1 ao contador a cada loop
* **soma += num** é o mesmo que soma = soma + num. ele pega o valor antigo da soma e adiciona o novo número que o usuário acabou de digitar
* **if num == 999**  nesse programa ele irá verificar: "O número digitado é igual a 999?", se sim, o código irá encerrar o laço, por causa do comando **break**
### 3° passo: mostrando o resultado
    print('A soma dos {} números foi {}'.format(vezes, soma))
* Quando o usuário dígitar '999' e encerrar o laço, o programa exibe a mensagem: "A soma dos X números foi Y"