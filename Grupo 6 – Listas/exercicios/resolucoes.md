## Resolução do 1° Exercício:

```python
# Declarando a lista
notas = []
# Utilizando estrutura de repetição para coletar os dados
for i in range(4):
  nota = float(input(f'Digite a sua {i+1}º nota: '))
  notas.append(nota)

#Imprimir as notas na tela
print(f'Notas digitadas: {notas}')

#Descobrir qual é a média e retornar o resultado
media = sum(notas) / 4
print(f'Média: {media}')
if media >= 7:
  print('Aprovado')
else:
  print('Recuperação')
```

## Resolução do 2° Exercício:

```python
# Declarando as listas
nomes = []
idades = []
flag = ''

# Ultilizando estrutura de repetição para coletar os dados
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

# Exibindo os valores na tela
for valor in range(len(nomes)):
    print(f'{nomes[valor]} tem {idades[valor]} anos.')
```