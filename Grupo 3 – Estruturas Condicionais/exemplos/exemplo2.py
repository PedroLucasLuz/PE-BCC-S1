### Exemplo de como usar uma estrutura condicional de maneira simples em Python
# Primeiro deve ser definida a variável que será usada como parâmetro.
# Após a definição, você deve usar a palavra-chave "if" seguida de uma condição (expressão booleana) e dois pontos.
# O bloco de código que será executado caso a condição seja verdadeira deve ser colocado após os dois pontos e caso não seja, deve ser colocado após o bloco após "else".
idade = 20
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você não é maior de idade.")

# O resultado da execução do código acima será:
# Você é maior de idade.

# Você pode colocar quantas condições quiser usando "elif" (else if) para verificar outras possibilidades.
idade = 15
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 13:
    print("Você é um adolescente.")
elif idade >= 0:
    print("Você é uma criança.")
else:
    print("Idade inválida.")

# O resultado da execução do código acima será:
# Você é um adolescente.