
import time

print('********* Calculo do dia Trabalhado  ************')
time.sleep(2)

for i in range(1, 3):
    print('------------------------')

salario = int(input('Qual o seu salário mensal?: '))
time.sleep(2)

if salario <= 1.100:
    print('Só uma observacão - Seu salario está abaixo do minimo!')
    print('------------------')



print(' Ok,', 'R$', salario, '!')
time.sleep(2) 

print('--------------------------------')

horas = int(input('Quantas horas por semana voce trabalha? '))
print(horas, 'Horas, Legal ')
time.sleep(1.5)


div = (salario / horas)

for a in range(1, 4):
    print('------------------------')

print(' Esse é o valor por dia, ', div,  "R$")


time.sleep(3)




print('""""""""""""""""""""FIM DO PROGRAMA!"""""""""""""""""""""""""""""""""')