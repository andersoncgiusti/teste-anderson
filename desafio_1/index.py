import sys

print('=' * 30)
print('{:^30}'.format('BANCO INTELITRADER'))
print('=' * 30)
print('{:^30}'.format('Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00'))
print('=' * 30)
valor = int(input('Qual valor gostaria de sacar? R$'))
print('=' * 30)

total = valor
if total <= 0 or total % 10 != 0:
  print('Não é possível sacar este valor.')
  sys.exit()
cedula = 100
totalCedula = 0
while True:
  if total >= cedula:
    total -= cedula
    totalCedula += 1
  else:
    if totalCedula > 0:
      print(f'Total de {totalCedula} cédulas de R${cedula}')
    if cedula == 100:
      cedula = 50
    elif cedula == 50:
      cedula = 20
    elif cedula == 20:
      cedula = 10
    totalCedula = 0
    if total == 0:
      break
print('=' * 30)
print('{:^30}'.format('Volte sempre ao BANCO INTELITRADER'))







