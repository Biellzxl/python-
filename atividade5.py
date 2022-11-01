# provas e trabalhos bimestrais
p1 = float(input("nota prova bimestral 1 (nota maxima 15): "))
t1 = float(input("nota trabalho bimestral 1 (nota maxima 10): "))
p2 = float(input("nota prova bimestral 2 (nota maxima 15): "))
t2 = float(input("nota trabalho bimestral 2: (nota maxima 10): "))
p3 = float(input("nota prova bimestral 3 (nota maxima 15): "))
t3 = float(input("nota trabalho bimestral 3 (nota maxima 10): "))
p4 = float(input("nota prova bimestral 4 (nota maxima 15): "))
t4 = float(input("nota trabalho bimestral 4 (nota maxima 10): "))
b1 = (1+t1)
b2 = (2+t2)
b3 = p3+t3)
b4 = ()

print("a nota media do 1° bimestre foi: ", b1)
print("a nota media do 2° bimestre foi: ", b2)
print("a nota media do 3° bimestre foi: ", b3)
print("a nota media do 4° bimestre foi: ", b4)
result = b1/2 + b2/2 + b3/2 + b4/2
if result >= 60 and result < 100:
    print("Parabens, voce foi aprovado!")
elif result >= 40 and result < 60:
    print("voce quase conseguiu, esta de recuperacao")
elif result < 40 and result >= 0:
    print("nao foi dessa vez, voce foi reprovado")
else:
    print("valores nao validos")
