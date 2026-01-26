import random

valor =random.randint(1, 100)

numero=''
cont=0
while(numero!=valor):
    numero=int(input('Introduce un numero: '))
    if str(numero)=="salir":
        break
    else:
        cont +=1
        if numero < 0 or numero > 100 :
            print("VALOR FUERA DE RANGO")
        elif numero < valor:
            print('DEMASIADO BAJO')
        elif numero > valor :
            print('DEMASIADO ALTO')
        else:
            print('ACERTASTE')


print(f' el numero de intentos fue: {cont}')
print('APLICACION TERMINADA')