def fazer_pedido(bebida, tamanho: str = "Médio"):
   return f"Saindo um {bebida} no tamanho {tamanho}!"



# Por padrão vai dizer que o tamanho do cappuccino é médio
pedido1 = fazer_pedido("Cappuccino")
print(pedido1)

# Agora vai mudar o padrão de tamanho do médio para o pequeno
pedido2 = fazer_pedido("Café Expresso", "Pequeno")
print(pedido2)
