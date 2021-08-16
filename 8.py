"Faça um algoritmo que informe o nome e salário dos funcionários de uma empresa. Considere que a empresa tenha um número x de empregados. Encontre o maior salário e o menor salário pago aos funcionários."

maior_salario = 0
menor_salario = 999999

while(True):
  nome = input("\nDigite o nome do funcionário: ")
  salario = float(input("Digite  o salario: "))

  #Verificar se é maiior ou menor 
  if(salario >= maior_salario):
    maior_salario = salario
    print("Maior salário: ", maior_salario)

  if(salario < menor_salario):
    menor_salario = salario
    print("Menor salário: ", menor_salario)

  sair = input("\nDigite 's' para sair: ")
  if sair == "s":
    break #parda ou saida do laço de repetição

print("Maior salário: ", maior_salario)
print("Menor salário: ", menor_salario)

  

  