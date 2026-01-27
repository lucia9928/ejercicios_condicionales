import random

secreto = random.randint(1, 100)


cont=0
numero=""
while(numero != secreto):
    numero = input('Introduce un numero: ') #pedimos el valor
    cont += 1
    if numero=="salir": #validamos que el valor introducido sea igual a salir o no
        break #si es igual a salir rompemos el bucle y salimos del flujo
    numero=int(numero) #parseamos el valor a un entero
    if numero < 0 or numero > 100 : #comprobamos que el valor este dentro del rango
        print("VALOR FUERA DE RANGO")
    elif numero < secreto:
        print('DEMASIADO BAJO')
    elif numero > secreto :
        print('DEMASIADO ALTO')
    else:
        print('ACERTASTE')

print(f' el numero de intentos fue: {cont}')
print('APLICACION TERMINADA')