import math #importação de biblioteca
import random #importação de biblioteca


limite_inferior = 100
limite_superior = 1000

#gerar raiz quadrada e número aleatorio entre 100 e 1000

n = random.randint (limite_inferior,limite_superior)
x = math.sqrt (n)
print(f'Numero aleatorio:{n}')
print(f'Raiz quadrada do número: {x}')