def fatorial(n)
   if n <= 1:
       return 1
   return n * fatorial(n - 1) # retorna ela mesma mas com um número menor


resultado = fatorial(5)
print(resultado)
