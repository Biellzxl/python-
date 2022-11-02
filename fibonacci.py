#sequencia fibonacci

ntermos = 12

n1, n2 = 0, 1
contador = 0

print("fibonacci:")
while contador < ntermos:
    print(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
    contador += 1