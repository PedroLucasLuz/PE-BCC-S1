contador = 0 
while True:
    num = int(input("Diga um número: "))
    if num == 0:
        break
    elif num % 2 == 0:
        contador += 1
    else:
        continue
    print("Número par")
print(f"Você digitou {contador} números pares")