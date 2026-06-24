### Exemplo de como usar o match-case em Python
# O match-case é uma estrutura condicional que permite verificar o valor de uma variável e executar diferentes blocos de código dependendo do valor dessa variável.
# O match-case segue a mesma lógica do if-elif-else, mas é mais legível e fácil de entender.
#Para escrever um match-case, você deve usar a palavra-chave "match" seguida da variável que será verificada e dois pontos.
#Após os dois pontos, você deve escrever os diferentes casos que serão verificados, usando a palavra-chave "case" seguida do valor que será verificado e dois pontos.
#O bloco de código que será executado caso o valor da variável seja igual ao valor do case deve ser colocado após os dois pontos.
idade = 30

match idade:
    case idade if idade < 0:
        print("Idade inválida.")
    case idade if idade < 13:
        print("Você é uma criança.")
    case idade if idade < 18:
        print("Você é um adolescente.")
    case idade if idade < 65:
        print("Você é um adulto.")
    case _:
        print("Você é um idoso.")

# O resultado da execução do código acima será:
# Você é um adulto.