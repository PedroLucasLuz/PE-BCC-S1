# exemplos_operadores.py
# Grupo 2 - Operadores: Aritméticos, Relacionais e Lógicos
# Demonstração prática com 2 exemplos por tipo de operador

# ============================================================
# PARTE 1 — OPERADORES ARITMÉTICOS
# ============================================================

# --- Exemplo 1: Calculando troco em uma compra ---
print("=== Exemplo 1: Troco na compra ===")
valor_pago   = 50.00
valor_compra = 37.50
troco = valor_pago - valor_compra
print(f"Valor pago:    R$ {valor_pago:.2f}")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Troco:         R$ {troco:.2f}")

print()

# --- Exemplo 2: Dividindo conta entre amigos e calculando gorjeta ---
print("=== Exemplo 2: Divisão de conta e gorjeta ===")
conta_total    = 120.00
num_amigos     = 4
percentual_gorjeta = 10
gorjeta  = conta_total * (percentual_gorjeta / 100)
total    = conta_total + gorjeta
por_pessoa = total / num_amigos
print(f"Conta total: R$ {conta_total:.2f}")
print(f"Gorjeta ({percentual_gorjeta}%): R$ {gorjeta:.2f}")
print(f"Total com gorjeta: R$ {total:.2f}")
print(f"Cada amigo paga: R$ {por_pessoa:.2f}")

print()

# ============================================================
# PARTE 2 — OPERADORES RELACIONAIS
# ============================================================

# --- Exemplo 3: Verificando acesso por idade ---
print("=== Exemplo 3: Controle de acesso por idade ===")
idade = 16
print(f"Idade informada: {idade} anos")
print(f"Tem 18 anos?         {idade == 18}")
print(f"É menor de idade?    {idade < 18}")
print(f"Pode entrar (18+)?   {idade >= 18}")

if idade >= 18:
    print("✅ Acesso liberado!")
else:
    print("❌ Acesso negado — menor de idade.")

print()

# --- Exemplo 4: Sistema de aprovação escolar ---
print("=== Exemplo 4: Aprovação escolar ===")
nota_aluno  = 7.5
nota_minima = 6.0
print(f"Nota do aluno:  {nota_aluno}")
print(f"Nota mínima:    {nota_minima}")
print(f"Aprovado?       {nota_aluno >= nota_minima}")
print(f"Reprovado?      {nota_aluno < nota_minima}")
print(f"Nota exata mín? {nota_aluno == nota_minima}")

if nota_aluno >= nota_minima:
    print("✅ Aluno aprovado!")
else:
    print("❌ Aluno reprovado.")

print()

# ============================================================
# PARTE 3 — OPERADORES LÓGICOS
# ============================================================

# --- Exemplo 5: Aprovação de empréstimo bancário (AND) ---
print("=== Exemplo 5: Aprovação de empréstimo (AND) ===")
renda_suficiente = True
bom_historico    = False
aprovado = renda_suficiente and bom_historico
print(f"Renda suficiente?    {renda_suficiente}")
print(f"Bom histórico?       {bom_historico}")
print(f"Empréstimo aprovado? {aprovado}")

if aprovado:
    print("✅ Empréstimo concedido!")
else:
    print("❌ Empréstimo negado — ambas as condições precisam ser verdadeiras.")

print()

# --- Exemplo 6: Decidir levar casaco (OR) e verificar folga (NOT) ---
print("=== Exemplo 6: Levar casaco e dia de folga ===")
esta_frio    = False
esta_chovendo = True
dia_de_trabalho = True

levar_casaco = esta_frio or esta_chovendo
folga        = not dia_de_trabalho

print(f"Está frio?           {esta_frio}")
print(f"Está chovendo?       {esta_chovendo}")
print(f"Levar casaco?        {levar_casaco}")
print()
print(f"Dia de trabalho?     {dia_de_trabalho}")
print(f"É dia de folga?      {folga}")

if levar_casaco:
    print("🧥 Leve o casaco!")
else:
    print("👕 Sem casaco hoje.")

if folga:
    print("🛋️  Aproveite a folga!")
else:
    print("💼 Bora trabalhar!")
