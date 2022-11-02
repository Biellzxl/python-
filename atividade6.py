#salario
print("complete as seguintes informaçoes")
salario = int(input("salario mensal: "))
inss = 5/100 * salario
salarioinss = salario - inss
sind = 11/100 * salario
salariosind = salario - sind
salarioliquid = salario - inss - sind
dia = int(input("dias trabalhados por mes: "))
salariodia = salario / dia
hora = int(input("carga horaria por dia: "))
salariohora = salariodia / hora
print("salario bruto: ", salario)
print("salario recebido por dia: ",salariodia)
print("salario recebido por hora trabalhada: ", salariohora)
print("desconto do inss: ", inss)
print("desconto do sindicato: ",sind)
print("seu salario liquido e de: ", salarioliquid)
