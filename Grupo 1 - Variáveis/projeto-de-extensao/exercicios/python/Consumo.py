"""
====================================
EXERCÍCIO 1 - CONSUMO DE COMBUSTÍVEL
====================================

Peça a distância percorrida e a quantidade
de combustível consumida. Calcule o consumo médio.
"""

# double (float) -> distância percorrida
distancia = float(input("Digite a distância percorrida (km): "))

# double (float) -> combustível consumido
litros = float(input("Digite os litros consumidos: "))

# double (float) -> cálculo do consumo médio
consumo = distancia / litros

print("Consumo médio: " + str(consumo) + " km/l")