# termometr
fahrenheit = float(input("Digite uma temperatura na escala Fahrenheit: "))
grau = fahrenheit - 32 * 5/9
kelvin = grau + 273,15
print("A temperatura fahrenheit digitada se convertida para graus celsius:", grau)
repeat = str(input("deseja repetir, porem convertendo fahrenheit para kelvin ?(sim ou nao): "))
match repeat:
    case "sim":
      fahrenheit2 = float(input("Digite uma temperatura na escala Fahrenheit: "))
      fk = fahrenheit2 - 32 * 5/9 +273.15
      print("A temperatura fahrenheit digitada se convertida para kelvin:", fk)
    case "nao":
        print("fim da conversao!")

