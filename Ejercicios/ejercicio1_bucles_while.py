import random

valor =random.randint(1, 100)

numero=''
cont=0
while(numero!=valor):
    numero=input('Introduce un numero: ')
    if numero=="salir":
        break
    else:
        cont +=1
        if int(numero) < 0 or int(numero) > 100 :
            print("VALOR FUERA DE RANGO")
        elif int(numero) < valor:
            print('DEMASIADO BAJO')
        elif int(numero) > valor :
            print('DEMASIADO ALTO')
        else:
            print('ACERTASTE')


print(f' el numero de intentos fue: {cont}')
print('APLICACION TERMINADA')