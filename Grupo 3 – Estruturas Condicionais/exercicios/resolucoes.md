# Gabarito / Respostas dos Exercícios

## Questões de múltipla escolha

**Questão 1- Resposta: C** (Permitir que o programa tome decisões com base em condições.)

**Questão 2 - Resposta: D** (if) 

**Questão 3 - Resposta: B** (Quando a condição do if é falsa.) 

**Questão 4 - Resposta: D** (Verificar uma nova condição caso a anterior seja falsa.)

**Questão 5 - Resposta: C** (Apenas o bloco correspondente é executado e os demais são ignorados.) 
 
**Questão 6 - Resposta: B** (Decidir se uma pessoa pode votar com base na idade.) 
 
**Questão 7 - Resposta: C** (Condições avaliadas como verdadeiras ou falsas.) 

**Questão 8 - Resposta : B** (Porque permitem que o programa execute ações diferentes conforme a situação.)
 
**Questão 9 - Resposta: A** (Comparar um valor com diferentes opções.)
 
**Questão 10 - Resposta: A** (Há várias possibilidades para um mesmo valor.)

## Atividade prática
### Códigos esperados

**Questão 1**
```
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")
```

**Questão 2**
```
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

**Questão 3**
```
nota = float(input("Digite a nota: "))

if nota <= 4:
    print("Reprovado")
elif nota <= 6:
    print("Recuperação")
else:
    print("Aprovado")
```

**Questão 4**
```
dia = int(input("Digite um número de 1 a 7: "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Número inválido")
```