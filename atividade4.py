# ano_letivo

print("boletim anual")
Nota1 = float(input("Nota primeiro bimestre: "))
Nota2 = float(input("Nota segundo bimestre: "))
Nota3 = float(input("Nota terceiro bimestre: "))
Nota4 = float(input("Nota quarto bimestre: "))
result = Nota1 + Nota2 + Nota3 + Nota4
if result >= 60 and result < 100:
    print("Parabens, voce foi aprovado!")
elif result >= 40 and result < 60:
    print("voce quase conseguiu, esta de recuperacao")
elif result < 40 and result >=0:
    print("nao foi dessa vez, voce foi reprovado")
else:
    print("valores nao validos")