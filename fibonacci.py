#sequencia fibonacci

ntermos = int(input("quantos termos da sequencia voce quer ?: "))

n1, n2 = 0, 1
contador = 0

print("fibonacci:")
while contador < ntermos+1:
    if n1 > 0:
        print(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
    contador += 1